---
name: collect_dataset_from_apis
description: Use this skill to collect raw data from multiple public APIs without authentication and store it strictly as a Markdown raw dump. The skill must NOT produce JSON/CSV datasets as output. It only fetches APIs, validates them, and saves raw responses into a Markdown file for downstream processing.
---

# collect_dataset_from_apis

## Overview

This skill collects raw data from multiple public APIs and stores it strictly in a Markdown file.

It is designed for downstream agents that will:
- parse data
- normalize structure
- build datasets

IMPORTANT:
- Output MUST be Markdown (.md)
- Output MUST NOT be JSON
- Output MUST NOT be CSV
- Output MUST NOT be any structured dataset format

---

## Instructions

### 1. Discover relevant APIs

Use `search_public_apis` to find APIs relevant to the user request.

Rules:
- select 2–5 candidates when possible
- prefer APIs without authentication
- prefer simple JSON-returning endpoints

---

### 2. Validate APIs

Use `get_public_api_details` for each candidate.

Keep only APIs that satisfy:
- auth: none
- accessible without API keys
- return usable data responses

Reject all others.

---

### 3. Fetch raw data

Use `http_request` to retrieve data.

Rules:
- do NOT transform response
- do NOT parse deeply
- do NOT normalize structure
- store response exactly as received

Allowed implementations:
- curl
- requests (Python)
- fetch (JS)
- native HTTP client (preferred)

---

## 4. Save dataset (STRICT MARKDOWN FORMAT)

CRITICAL RULES:
- Output MUST be a `.md` file
- Output MUST NOT be JSON
- Output MUST NOT be CSV
- Only Markdown is allowed

---

### File path

workspace/data/raw_dataset.md

---

### File format

# Raw Dataset Dump

## Sources
- API 1
- API 2
- API 3

## Date
<current date>

---

## Raw Data

### API 1
<raw response exactly as received>

---

### API 2
<raw response exactly as received>

---

### API 3
<raw response exactly as received>

---

## 5. Summary

After saving the file, return a short summary:

- number of APIs used
- number of requests made
- type of collected data (news, products, mixed, metadata)
- short description of dataset content

---

## Output format

APIs used: <N>  
Requests made: <N>  
Data type: <short description>  
Saved to: workspace/raw_dataset.md  

---

## Rules (STRICT)

- NEVER output JSON as final result
- NEVER convert responses into structured datasets
- ALWAYS store raw responses inside Markdown file
- ONLY Markdown is allowed for persistence
- Do not merge, clean, or transform API responses
- Summary must be short and based only on retrieved data