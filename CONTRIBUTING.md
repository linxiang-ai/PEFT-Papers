# Contributing to PEFT-Papers

Thanks for considering a contribution. This repository tracks Parameter-Efficient Fine-Tuning (PEFT) papers and projects. All paper data lives in a single source of truth: [`data/papers.json`](data/papers.json).

## Ways to contribute

- **Add a new paper** — submit an issue using the [Add Paper template](.github/ISSUE_TEMPLATE/add-paper.md), or open a PR directly.
- **Fix metadata** — correct authors, venue, arXiv ID, or links.
- **Improve scripts** — generators, validators, or the weekly arXiv fetcher under [`scripts/`](scripts/).
- **Survey work** — extend `SURVEY.md` with a method group or empirical comparison.

## Adding a paper (PR workflow)

1. Fork the repo and create a branch: `git checkout -b add-paper/<paper-id>`.
2. Append a new entry to `data/papers.json`. Validate against [`data/papers.schema.json`](data/papers.schema.json).
3. Run the generator so category `.md` files stay in sync:
   ```bash
   python scripts/generate_md.py
   ```
4. Run validation:
   ```bash
   python scripts/validate_schema.py
   python scripts/check_links.py
   ```
5. Commit with a conventional message:
   ```
   feat(paper): add LoRA (ICLR 2022)
   ```
6. Open a PR. Fill in the checklist:
   - [ ] Entry validates against `papers.schema.json`
   - [ ] arXiv ID and `paper_url` verified (not fabricated)
   - [ ] Category and domain values match the controlled vocabulary
   - [ ] Category `.md` files regenerated

## Schema rules

Every entry in `papers.json` MUST conform to `data/papers.schema.json`. Key rules:

| Field                    | Rule                                                                 |
| ------------------------ | -------------------------------------------------------------------- |
| `id`                     | kebab-case, unique across the file (e.g. `lora-2022`)                |
| `arxiv`                  | arXiv ID only, no URL prefix (e.g. `2106.09685`)                     |
| `paper_url`              | Full URL                                                             |
| `category`               | Controlled vocabulary — see schema `enum`                            |
| `domain`                 | One or more of: `nlp`, `vision`, `multimodal`, `diffusion`, `speech` |
| `open_source`            | `official` / `community` / `none`                                    |
| `key_idea`               | One sentence, English                                                |
| `added_date`             | `YYYY-MM-DD`                                                         |

If you are unsure about a field (especially `arxiv` or `paper_url`), leave it `null` rather than guess.

## Method taxonomy

Based on He et al. (ICLR 2022) unified view:

1. **Additive** — Adapter family, soft prompts
2. **Reparameterization** — LoRA family, low-rank methods
3. **Selective** — BitFit, DiffPruning
4. **Hybrid** — MAM Adapter, UniPELT, S4

Use the matching `category` enum value in `papers.json`.

## Editing rules

- **Do not hand-edit** files under `papers/by-method/`, `papers/by-year/`, `papers/by-domain/`, or `papers/by-venue/`. They are regenerated from `papers.json` by `scripts/generate_md.py`.
- **Do** hand-edit `README.md`, `SURVEY.md`, `benchmarks.md`, `implementations.md`, and `papers/must-read.md`.

## Commit style

Conventional Commits:

- `feat: ...` — new paper, new feature
- `fix: ...` — metadata correction, bug fix
- `docs: ...` — README / SURVEY edits
- `chore: ...` — tooling, CI, repo housekeeping

## Code style

- Python: PEP 8.
- Markdown: clear heading hierarchy, minimal emoji, English primary.

## Questions

Open an issue with the `question` label.
