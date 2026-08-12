#!/usr/bin/env node
/*
Fetches problem metadata from NeetCode's API, and for each problem writes the
code of the last "Accepted" submission (if any) to a .py file. Output
filenames are derived, not read from the links file. Files are written to
the current directory.

Usage: generate-neetcode-submissions.mjs <links.txt>
  <links.txt> format: one NeetCode question-page URL per line, e.g. https://neetcode.io/problems/car-fleet/question?list=neetcode150

Note: requires an auth token, which the script reads from a file named token.txt in the current directory.

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
  console.error("Usage: node generate-neetcode-submissions.mjs <links-file>");
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

// Find the last submission in the array with statusDescription == "Accepted".
function lastAcceptedSubmission(submissionHistory) {
  if (!Array.isArray(submissionHistory)) return null;
  for (let i = submissionHistory.length - 1; i >= 0; i--) {
    if (submissionHistory[i].statusDescription === "Accepted") return submissionHistory[i];
  }
  return null;
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
      console.log(data);
      const submission = lastAcceptedSubmission(data.submissionHistory);
      if (!submission) {
        console.log(`  No accepted submission for ${problemId}, skipping.`);
      } else {
        const filename = `${number}.${processName(data.name)}_submission.py`;
        fs.writeFileSync(filename, submission.code, "utf8");
      }
    } catch (err) {
      console.error(`Failed on ${problemId}: ${err.message}`);
    }
    await sleep(DELAY_MS);
  }
}

main();
