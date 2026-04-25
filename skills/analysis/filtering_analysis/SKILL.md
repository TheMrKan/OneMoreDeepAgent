---
name: filtering_analysis
description: Filter dataset items based on conditions such as category, price range, or attributes.
---

# filtering-analysis

## Purpose

Filters dataset based on user-defined constraints.

---

## When to use

- search within dataset
- parameter-based selection
- narrowing results

---


## Process

1. Read dataset
2. Extract items
3. Apply filters:
   - equality conditions
   - numeric ranges
   - category matching
4. Return filtered subset

---

## Examples of filters

- category = "electronics"
- price <= 1000
- rating >= 4

---

## Rules

- no data modification
- no external requests
- no schema transformation
- preserve raw structure