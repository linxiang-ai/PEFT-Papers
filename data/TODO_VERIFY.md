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

### pissa-2024 · venue
- Current value: `NeurIPS` 2024
- Why uncertain: Recalled as accepted at NeurIPS 2024, not freshly verified.
- Action needed: Confirm venue/year; downgrade to `arXiv` if not accepted.
- Status: open

### rslora-2023 · venue, code_url
- Current value: `arXiv` / `null`
- Why uncertain: No formal venue claimed; could not confirm an official repo (rsLoRA scaling is integrated into HF PEFT).
- Action needed: Check whether the paper was later accepted somewhere and whether the author released code.
- Status: open

### lora-fa-2023 · venue, code_url
- Current value: `arXiv` / `null`
- Why uncertain: No formal venue claimed; could not locate an official repo for Zhang et al.
- Action needed: Confirm venue/code; otherwise leave as community implementation.
- Status: open

### dylora-2023 · code_url
- Current value: `https://github.com/huawei-noah/KD-NLP`
- Why uncertain: Linked to Huawei Noah's umbrella repo, but DyLoRA's actual sub-path / dedicated repo was not verified.
- Action needed: Replace with the exact DyLoRA sub-path or canonical repo.
- Status: open

### clip-adapter-2024 · year
- Current value: 2024 (venue `IJCV`)
- Why uncertain: arXiv preprint is from 2021; IJCV publication year could be 2023 or 2024.
- Action needed: Confirm exact IJCV publication year and adjust.
- Status: open

### svdiff-2023 · code_url
- Current value: `null` (open_source: `community`)
- Why uncertain: Original Han et al. paper did not advertise official code; community reproductions exist.
- Action needed: Check whether an official Google Research repo was eventually released.
- Status: open

### qa-lora-2024 · venue
- Current value: `ICLR` 2024
- Why uncertain: Recalled as ICLR 2024 but not freshly verified.
- Action needed: Confirm acceptance venue.
- Status: open

### peqa-2023 · code_url
- Current value: `null`
- Why uncertain: Could not confirm an official Samsung/NAVER repo for PEQA.
- Action needed: Verify whether official code is released.
- Status: open

### mole-2024 · venue, code_url
- Current value: `ICLR` 2024 / `null`
- Why uncertain: Wu et al. arXiv 2404.13628 — venue unclear; multiple papers use the "MoLE" name.
- Action needed: Confirm this is the canonical MoLE paper, its venue, and whether code is released.
- Status: open

### mola-2024 · venue
- Current value: `arXiv` 2024
- Why uncertain: Could not confirm a formal venue acceptance.
- Action needed: Check for ACL/EMNLP/NAACL acceptance and update.
- Status: open

### x-lora-2024 · venue
- Current value: `arXiv` 2024
- Why uncertain: May have been published in APL Machine Learning; not verified.
- Action needed: Confirm formal venue and update.
- Status: open

### mora-2024 · venue
- Current value: `arXiv` 2024
- Why uncertain: No formal venue verified.
- Action needed: Check for NeurIPS/ICLR/ACL acceptance and update.
- Status: open

---

## Archive

(empty)
