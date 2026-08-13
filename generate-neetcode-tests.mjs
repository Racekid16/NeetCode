#!/usr/bin/env node
/*
Usage: generate-neetcode-tests.mjs <links.txt>
  <links.txt> format: one NeetCode question-page URL per line, e.g. https://neetcode.io/problems/car-fleet/question?list=neetcode150

Note: requires an auth token, which the script reads from a file named token.txt in
the current directory (same as generate-neetcode-questions.mjs).

Limitations: values are parsed as plain JSON-ish literals (numbers, strings, bools,
None/null, nested arrays). Problems whose examples encode trees/linked lists as
nested arrays (e.g. "root = [3,9,20,null,null,15,7]") come through as a plain array
too -- turning that into an actual tree/list is left to the runner, per problem type.
Design/class-type problems (e.g. MinStack) don't give "key = value" pairs at all --
just one flat array of constructor/method calls -- so for those, "input" is that raw
array rather than a named-parameter object; see parseInput.

Written with the help of Claude.
*/

import fs from "node:fs";

const TOKEN = fs.readFileSync("token.txt", "utf8").trim();
if (!TOKEN) {
  console.error("token.txt is empty. Put your auth token in it and try again.");
  process.exit(1);
}

const inputFile = process.argv[2];
if (!inputFile) {
  console.error("Usage: node generate-neetcode-tests.mjs <links-file>");
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
// STEP 1: minimal text cleanup, just enough to make Example blocks regular
// (same idea as generate-neetcode-questions.mjs's cleanupText, trimmed down to
// what test extraction needs).
// ===========================================================================

// "1,000,000" -> "1000000" (thousands separators, not array/list separators).
function stripThousandsSeparators(text) {
  let prev;
  do {
    prev = text;
    text = text.replace(/(\d),(\d{3})(?!\d)/g, "$1$2");
  } while (text !== prev);
  return text;
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

// ===========================================================================
// STEP 2: split a NeetCode literal string into top-level comma-separated parts,
// respecting nesting ([], (), {}) and quotes so we don't split inside them.
// ===========================================================================

function splitTopLevel(str) {
  const parts = [];
  let depth = 0;
  let inQuote = null;
  let current = "";

  for (let i = 0; i < str.length; i++) {
    const c = str[i];
    if (inQuote) {
      current += c;
      if (c === inQuote && str[i - 1] !== "\\") inQuote = null;
      continue;
    }
    if (c === '"' || c === "'") {
      inQuote = c;
      current += c;
      continue;
    }
    if ("[({".includes(c)) depth++;
    if ("])}".includes(c)) depth--;
    if ((c === "," || c === "\n") && depth === 0) {
      parts.push(current);
      current = "";
      continue;
    }
    current += c;
  }
  if (current.trim() !== "") parts.push(current);
  return parts.map((p) => p.trim());
}

// ===========================================================================
// STEP 3: parse a single literal (Python-flavored) into a JS value.
// ===========================================================================

function parseValue(raw) {
  const str = raw.trim();
  if (str === "True" || str === "true") return true;
  if (str === "False" || str === "false") return false;
  if (str === "None" || str === "null") return null;
  if (/^-?\d+$/.test(str)) return parseInt(str, 10);
  if (/^-?\d*\.\d+$/.test(str)) return parseFloat(str);
  if ((str.startsWith('"') && str.endsWith('"')) || (str.startsWith("'") && str.endsWith("'"))) {
    return str.slice(1, -1);
  }
  if (str.startsWith("[") && str.endsWith("]")) {
    const inner = str.slice(1, -1).trim();
    return inner === "" ? [] : splitTopLevel(inner).map(parseValue);
  }
  // Fallback: unrecognized token (e.g. "inf") -- keep as a raw string rather than
  // guessing, so it's obvious in the output that it needs a manual look.
  return str;
}

// "nums = [1, 2, 3, 3], target = 9" -> { nums: [1,2,3,3], target: 9 }
function parseAssignments(inputStr) {
  const result = {};
  for (const part of splitTopLevel(inputStr)) {
    const eqIdx = part.indexOf("=");
    if (eqIdx === -1) continue;
    const key = part.slice(0, eqIdx).trim();
    result[key] = parseValue(part.slice(eqIdx + 1));
  }
  return result;
}

// Most problems give "key = value" pairs, which parseAssignments turns into a
// named-parameter object. Design/class-type problems (e.g. MinStack) instead give
// one flat array of constructor/method calls with no "=" anywhere -- for those,
// fall back to the raw parsed literal rather than an empty object.
function parseInput(inputStr) {
  const assignments = parseAssignments(inputStr);
  return Object.keys(assignments).length > 0 ? assignments : parseValue(inputStr);
}

// ===========================================================================
// STEP 4: pull every "**Example N:** ... ```Input:/Output:``` " block out of the
// API's raw `description` field.
// ===========================================================================

const exampleRe =
  /\*\*Example \d+:?\*\*\s*(?:!\[[^\]]*\]\([^)]*\)\s*)?```\s*Input:\s*([\s\S]*?)\n\s*Output:\s*([\s\S]*?)(?=\n\s*Explanation:|\n?\s*```)/g;

function extractExamples(description) {
  const cleaned = cleanCodeFences(stripThousandsSeparators(description));
  const examples = [];
  let m;
  exampleRe.lastIndex = 0;
  while ((m = exampleRe.exec(cleaned))) {
    examples.push({ inputStr: m[1].trim(), outputStr: m[2].trim() });
  }
  return examples;
}

// Combine description examples (input + output) with custom_test_cases (input
// only, but the cleaner source) when their counts line up 1:1.
function buildTests(data) {
  const examples = extractExamples(data.description || "");
  const customCases = Array.isArray(data.custom_test_cases) ? data.custom_test_cases : [];
  const useCustomInputs = customCases.length === examples.length && examples.length > 0;

  return examples.map((ex, i) => ({
    input: parseInput(useCustomInputs ? customCases[i] : ex.inputStr),
    output: parseValue(ex.outputStr),
  }));
}

// resJSON.data.name, lowercased/underscored/stripped for use as a filename.
// e.g. "Pow(x, n)" -> "powx_n"
function processName(name) {
  return name
    .toLowerCase()
    .trim()
    .replace(/\s+/g, "_")
    .replace(/[^a-z0-9_]/g, "");
}

// ===========================================================================
// Pretty-printer: objects get one key per line (like JSON.stringify(v, null, 2)),
// but arrays stay on a single line -- "nums": [1, 2, 3, 3], not one element per
// line -- since that's how NeetCode itself displays them.
// ===========================================================================

function inlineValue(value) {
  if (Array.isArray(value)) return "[" + value.map(inlineValue).join(", ") + "]";
  if (value !== null && typeof value === "object") {
    const body = Object.entries(value)
      .map(([k, v]) => `${JSON.stringify(k)}: ${inlineValue(v)}`)
      .join(", ");
    return `{${body}}`;
  }
  return JSON.stringify(value);
}

function prettyStringify(value, indent) {
  if (Array.isArray(value)) return inlineValue(value);
  if (value !== null && typeof value === "object") {
    const keys = Object.keys(value);
    if (keys.length === 0) return "{}";
    const pad = "  ".repeat(indent);
    const childPad = "  ".repeat(indent + 1);
    const body = keys.map((k) => `${childPad}${JSON.stringify(k)}: ${prettyStringify(value[k], indent + 1)}`).join(",\n");
    return `{\n${body}\n${pad}}`;
  }
  return JSON.stringify(value);
}

function formatTests(tests) {
  const items = tests.map((t) => "  " + prettyStringify(t, 1));
  return "[\n" + items.join(",\n") + "\n]\n";
}

// ===========================================================================
// main
// ===========================================================================

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function main() {
  const urls = fs
    .readFileSync(inputFile, "utf8")
    .split("\n")
    .map((l) => l.trim())
    .filter(Boolean);

  for (let i = 0; i < urls.length; i++) {
    const url = urls[i];
    const number = String(i + 1).padStart(3, "0");
    const problemId = problemIdFromUrl(url);

    console.log(`Fetching ${problemId} (${number})`);
    try {
      const data = await fetchProblem(problemId);
      const tests = buildTests(data);

      if (tests.length === 0) {
        console.warn(`No examples found for ${problemId}, skipping`);
      } else {
        const filename = `${number}.${processName(data.name)}_tests.txt`;
        fs.writeFileSync(filename, formatTests(tests), "utf8");
      }
    } catch (err) {
      console.error(`Failed on ${problemId}: ${err.message}`);
    }
    await sleep(DELAY_MS);
  }
}

main();
