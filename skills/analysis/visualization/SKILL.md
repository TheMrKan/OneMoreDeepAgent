---
name: visualization
description: Build simple charts from dataset using Python libraries (matplotlib). Used for trends, comparisons and distributions.
---

# visualization

## Purpose

Create visual representations of dataset:
- bar charts
- line charts
- simple distributions

---

Dataset must be preloaded and parsed by analysis agent.

---

## Libraries used

- pandas
- matplotlib
- seaborn

---

## Process

1. Load dataset into pandas DataFrame
2. Identify numeric fields for visualization
3. Choose chart type based on request:
   - comparison → bar chart
   - trends → line chart
   - distribution → histogram
4. Generate plot using matplotlib
5. Save image to workspace

---

## Output file

workspace/analysis_plot.png

---

## Rules

- do not modify raw dataset
- do not fetch external data
- only use local dataset
- keep charts simple and readable