---
name: comparison_analysis
description: Compare items from dataset and rank them based on key attributes such as price, rating, or relevance.
---

# comparison-analysis

## Purpose

This skill compares items in a dataset and produces a ranked or sorted result.

It works only on already loaded data. No external fetching.

---

## When to use

- comparing products
- ranking options
- selecting best items
- sorting by criteria

---

## Input

Dataset from:
workspace/data/raw_dataset.md

---

## Process

1. Identify comparable fields (price, rating, value, etc.)
2. Choose primary sorting key based on user request
3. Rank items accordingly
4. Return ordered list

---

## Rules

- do not modify original dataset
- do not fetch external data
- do not invent missing fields
- preserve source references