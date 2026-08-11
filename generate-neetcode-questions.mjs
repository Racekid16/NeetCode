#!/usr/bin/env node
// generate-neetcode-questions.mjs
//
// Pulls problem metadata from NeetCode's API for a list of problems, PARSES
// each one into a plain data object, then RENDERS that object through a
// template — like React: parse() builds the data, render() is a pure
// function from data -> markdown string.
//
// Auth: reads your token from a file named token.txt in the current
// directory (just the raw token, no quotes, trailing newline is fine).
//
// Questions file format: one problem per line, "<filename>,<url>" —
//   - <filename> is the name of the file to write for this problem
//     (written to the current directory).
//   - <url> is the problem's NeetCode question-page URL, e.g.
//     https://neetcode.io/problems/car-fleet/question?list=neetcode150
//     The problemId used to call the API is parsed out of this URL
//     (the path segment right after "/problems/").
// Blank lines are ignored. Example line:
//   019.car_fleet_question.md,https://neetcode.io/problems/car-fleet/question?list=neetcode150
//
// Usage:
//   node generate-neetcode-questions.mjs questions.txt
//
// Requires Node 18+ (built-in fetch).

import fs from "node:fs";

const TOKEN = fs.readFileSync("token.txt", "utf8").trim();
if (!TOKEN) {
  console.error("token.txt is empty. Put your auth token in it and try again.");
  process.exit(1);
}

const inputFile = process.argv[2];
if (!inputFile) {
  console.error("Usage: node generate-neetcode-questions.mjs <questions-file>");
  process.exit(1);
}
const DELAY_MS = 1000; // be polite to the API

function problemIdFromUrl(url) {
  const match = url.match(/\/problems\/([^/]+)\//);
  if (!match) throw new Error(`Could not parse problemId from ${url}`);
  return match[1];
}

async function fetchProblem(problemId) {
  const res = await fetch("https://neetcode.io/api/getProblemMetadataFunctionHttp", {
    method: "POST",
    headers: {
      authorization: TOKEN,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ data: { problemId } }),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status} fetching ${problemId}`);
  const json = await res.json();
  return json.data;
}

// ===========================================================================
// STEP 1: low-level text cleanup (string-level fixes, order-sensitive)
// ===========================================================================

// "1,000,000" -> "1000000" (thousands separators, not array/list separators).
// Repeats to collapse multi-group numbers.
function stripThousandsSeparators(text) {
  let prev;
  do {
    prev = text;
    text = text.replace(/(\d),(\d{3})(?!\d)/g, "$1$2");
  } while (text !== prev);
  return text;
}

// "[-1,0,1]" -> "[-1, 0, 1]" (any comma not already followed by whitespace).
function spaceAfterCommas(text) {
  return text.replace(/,(?!\s)/g, ", ");
}

// Drop the language tag after ``` and remove blank lines inside code fences
// (e.g. the empty line between "Input:" and "Output:").
function cleanCodeFences(text) {
  return text.replace(/```[a-zA-Z]*\n([\s\S]*?)```/g, (_, body) => {
    const cleaned = body
      .split("\n")
      .filter((line) => line.trim() !== "")
      .join("\n");
    return "```\n" + cleaned + "\n```";
  });
}

// `word` -> ``word``, but only outside code fences.
function doubleBackticks(text) {
  const parts = text.split(/(```[\s\S]*?```)/g);
  return parts
    .map((part, i) => (i % 2 === 1 ? part : part.replace(/`([^`\n]+)`/g, "``$1``")))
    .join("");
}

// A trailing period just inside a closing ``code`` span moves outside it:
// "``...= 0.``" -> "``...= 0``."
function moveTrailingPeriodOutsideBackticks(text) {
  return text.replace(/\.``/g, "``.");
}

function stripBrTags(text) {
  return text.replace(/<br\s*\/?>/g, "");
}

// "* foo" -> "- foo" (line-leading single asterisk; won't touch "**bold**",
// since that has no space after the opening "**").
function bulletsToDashes(text) {
  return text.replace(/^\*\s+/gm, "- ");
}

function cleanupText(raw) {
  let text = raw;
  text = stripThousandsSeparators(text);
  text = spaceAfterCommas(text);
  text = cleanCodeFences(text);
  text = doubleBackticks(text);
  text = moveTrailingPeriodOutsideBackticks(text);
  text = stripBrTags(text);
  text = bulletsToDashes(text);
  return text;
}

// Collapse 3+ blank lines down to 1 (leftover from stripped <br> tags etc.)
// without forcing everything onto single lines.
function tidyBlankLines(text) {
  return text.replace(/\n{3,}/g, "\n\n").trim();
}

// ===========================================================================
// STEP 2: parse the cleaned text into a plain data object
// ===========================================================================

function parseBody(body) {
  const constraintsMatch = body.match(/\*\*Constraints:?\*\*([\s\S]*)$/);
  const examplesBlock = (constraintsMatch ? body.slice(0, constraintsMatch.index) : body).trim();
  const constraintsBlock = constraintsMatch ? constraintsMatch[1].trim() : "";

  const constraints = constraintsBlock
    ? constraintsBlock
      .split("\n")
      .map((l) => l.trim())
      .filter(Boolean)
      .map((l) => l.replace(/^[*-]\s*/, ""))
    : [];

  const firstExampleMatch = examplesBlock.match(/\*\*Example \d+:?\*\*/);
  const intro = (firstExampleMatch ? examplesBlock.slice(0, firstExampleMatch.index) : examplesBlock).trim();

  const examples = [];
  const exampleRe =
    /\*\*Example \d+:?\*\*\s*```\s*Input:\s*([\s\S]*?)\n\s*Output:\s*([\s\S]*?)\s*```\s*([\s\S]*?)(?=\*\*Example \d+:?\*\*|$)/g;
  let m;
  while ((m = exampleRe.exec(examplesBlock))) {
    examples.push({
      input: m[1].trim(),
      output: m[2].trim(),
      explanation: tidyBlankLines(m[3]),
    });
  }

  return { intro: tidyBlankLines(intro), examples, constraints };
}

function parseDetails(detailsSection) {
  const text = detailsSection.replace(/<details class="company-tags-accordion">[\s\S]*?<\/details>/g, "");

  const blockRe = /<details class="hint-accordion">\s*<summary>([^<]+)<\/summary>([\s\S]*?)<\/details>/g;
  let topics = [];
  let recommendedComplexity = "";
  const hints = [];
  let m;
  while ((m = blockRe.exec(text))) {
    const title = m[1].trim();
    const inner = m[2];

    if (title === "Topics") {
      topics = [...inner.matchAll(/<a[^>]*>([^<]+)<\/a>/g)].map((a) => a[1].trim());
    } else if (title === "Recommended Time & Space Complexity") {
      recommendedComplexity = tidyBlankLines(inner.replace(/<\/?p>/g, ""));
    } else {
      // Hint 1, Hint 2, ... — keep in source order regardless of exact title.
      hints.push(tidyBlankLines(inner.replace(/<\/?p>/g, "")));
    }
  }

  return { topics, recommendedComplexity, hints };
}

function parseProblem({ url, name, difficulty, description }) {
  const text = cleanupText(description);

  const detailsStart = text.indexOf("<details");
  const body = detailsStart === -1 ? text : text.slice(0, detailsStart);
  const detailsSection = detailsStart === -1 ? "" : text.slice(detailsStart);

  const { intro, examples, constraints } = parseBody(body);
  const { topics, recommendedComplexity, hints } = parseDetails(detailsSection);

  return { url, name, difficulty, intro, examples, constraints, topics, recommendedComplexity, hints };
}

// ===========================================================================
// STEP 3: render the data object through the template
// ===========================================================================

function render({ url, name, difficulty, intro, examples, constraints, topics, recommendedComplexity, hints }) {
  const examplesSection = examples
    .map((ex, i) => {
      const fence = `**Example ${i + 1}**\n\`\`\`\nInput: ${ex.input}\nOutput: ${ex.output}\n\`\`\``;
      return ex.explanation ? `${fence}\n\n${ex.explanation}` : fence;
    })
    .join("\n\n");

  const constraintsSection = ["**Constraints**", ...constraints.map((c) => `- ${c}`)].join("\n");

  const topicsSection = `<details>\n  <summary>Topics</summary>\n  ${topics.join(", ")}\n</details>`;

  const complexitySection = `<details>\n  <summary>Recommended Time & Space Complexity</summary>\n  ${recommendedComplexity}\n</details>`;

  const hintsSection = hints
    .map((h, i) => `<details>\n  <summary>Hint ${i + 1}</summary>\n  ${h}\n</details>`)
    .join("\n\n");

  return (
    [url, `# ${name}`, `*${difficulty}*`, intro, examplesSection, constraintsSection, topicsSection, complexitySection, hintsSection]
      .filter(Boolean)
      .join("\n\n") + "\n\n"
  );
}

// ===========================================================================
// main
// ===========================================================================

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function main() {
  const lines = fs
    .readFileSync(inputFile, "utf8")
    .split("\n")
    .map((l) => l.trim())
    .filter(Boolean);

  for (const line of lines) {
    const commaIndex = line.indexOf(",");
    const filename = line.slice(0, commaIndex);
    const url = line.slice(commaIndex + 1);
    const problemId = problemIdFromUrl(url);

    console.log(`Fetching ${problemId} -> ${filename}`);
    try {
      const data = await fetchProblem(problemId);
      const parsed = parseProblem({ url, name: data.name, difficulty: data.difficulty, description: data.description });
      fs.writeFileSync(filename, render(parsed), "utf8");
    } catch (err) {
      console.error(`Failed on ${problemId}: ${err.message}`);
    }
    await sleep(DELAY_MS);
  }
}

main();
