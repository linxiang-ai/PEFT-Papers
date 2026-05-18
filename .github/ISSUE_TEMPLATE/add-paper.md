---
name: Add a paper
about: Suggest a new PEFT paper to include in papers.json
title: "[paper] <paper title>"
labels: new-paper
assignees: ""
---

<!--
Fill in every field you can. If unsure (especially for arxiv / paper_url), leave it blank rather than guess.
Final entry will be inserted into data/papers.json and must validate against data/papers.schema.json.
-->

## Paper metadata

- **id** (kebab-case, unique, e.g. `lora-2022`):
- **title**:
- **authors** (comma-separated):
- **venue** (ICLR / NeurIPS / arXiv / ...):
- **year**:
- **arxiv** (ID only, e.g. `2106.09685`):
- **paper_url**:
- **code_url** (or `null`):

## Classification

- **category** (one or more of: `additive`, `adapter-family`, `soft-prompt`, `reparameterization`, `lora-family`, `selective`, `hybrid`, `other`):
- **domain** (one or more of: `nlp`, `vision`, `multimodal`, `diffusion`, `speech`):
- **backbone** (models tested on, e.g. `GPT-3`, `RoBERTa`):

## Summary

- **key_idea** (one English sentence):
- **trainable_params_ratio** (e.g. `0.01%-0.1%` or `varies`):
- **open_source** (`official` / `community` / `none`):
- **tags** (any of: `foundational`, `must-read`, `new`, `survey`, `benchmark`):

## Proposed JSON entry

```json
{
  "id": "",
  "title": "",
  "authors": [],
  "venue": "",
  "year": 0,
  "arxiv": null,
  "paper_url": "",
  "code_url": null,
  "category": [],
  "domain": [],
  "backbone": [],
  "key_idea": "",
  "trainable_params_ratio": "",
  "open_source": "none",
  "tags": [],
  "added_date": "YYYY-MM-DD"
}
```

## Checklist

- [ ] I verified the arXiv ID and `paper_url` (did not fabricate)
- [ ] `id` does not collide with an existing entry
- [ ] `category` and `domain` values are from the controlled vocabulary
