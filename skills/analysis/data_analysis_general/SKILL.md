---
name: data_analysis_general
description: Analyze already collected datasets. Performs minimal preprocessing and routes tasks to specialized analysis skills.
---

# data-analysis-agent

## Overview

This skill works only with existing datasets.

It does NOT collect data.  
It does NOT call APIs.

Input is usually:
workspace/data/raw_dataset.md

---

## Responsibilities

1. Load dataset from file
2. Perform minimal preprocessing
3. Route request to appropriate analysis mode

---

## Minimal preprocessing rules

- Do not restructure dataset
- Do not normalize fully
- Do not merge sources
- Remove only clearly broken or empty entries
- Preserve original raw data

---

## Routing logic

Depending on user request:

- comparison → compare items in dataset
- filter → apply constraints
- aggregate → group or summarize data

---

## Analysis modes

### Comparison mode
Used when user asks to compare or rank items.

Logic:
Sort items by relevant attribute (price, rating, etc.)

---

### Filtering mode
Used when user provides constraints.

Logic:
Return only items matching conditions (category, price range, etc.)

---

### Visualisation mode

Used when you can visualize the data.

Logic:
Create some plots with Python libs and save it to the workspace folder.

## Rules

- No external API calls
- No data fetching
- No rewriting dataset structure
- Keep traceability to source APIs
- Work only on provided dataset files