# Unverified Fields — pending manual review

Tracks `papers.json` fields where the value could not be verified at entry time.
The author (you) clears items here by either confirming the value, replacing it,
or marking it permanently unknown.

## Format

```
### <paper id> · <field>
- Current value: <what's in papers.json now>
- Why uncertain: <one line>
- Action needed: <what to verify>
- Status: open | verified | replaced
```

When resolved: update `papers.json`, change Status to `verified` / `replaced`, and keep the row for audit (or move to an Archive section).

---

## Open items

### vera-2024 · code_url
- Current value: `null` (open_source: `community`)
- Why uncertain: VeRA paper does not point to an official repo; HuggingFace PEFT integrates it as a community implementation.
- Action needed: Confirm whether Kopiczko et al. released an official repo. If not, decide whether to link the HF PEFT VeRA module page instead.
- Status: open

### bitfit-2022 · code_url
- Current value: `https://github.com/benzakenelad/BitFit`
- Why uncertain: URL recalled from memory, not freshly verified that the repo still exists / is the canonical mirror.
- Action needed: Open the link; if dead, replace with current canonical repo or set `null`.
- Status: open

### delta-tuning-2023 · title
- Current value: `Parameter-efficient fine-tuning of large-scale pre-trained language models` (Nature MI published title)
- Why uncertain: arXiv version uses a different title — `Delta Tuning: A Comprehensive Study of Parameter Efficient Methods for Pre-trained Language Models`. Project policy on which version to record is undefined.
- Action needed: Decide on a policy (prefer published venue title vs. arXiv title) and apply consistently.
- Status: open

### delta-tuning-2023 · category
- Current value: `["other"]`
- Why uncertain: Paper is a survey/taxonomy, not a single method. Forced into `other` because the schema enum has no `survey` category.
- Action needed: Either (a) extend the category enum with `survey`, or (b) confirm `other` is the right home for survey entries.
- Status: open

---

## Archive

(empty)
