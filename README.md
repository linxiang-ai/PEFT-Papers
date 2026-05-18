# PEFT-Papers: A Structured Collection of Parameter-Efficient Fine-Tuning Research

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Last Update](https://img.shields.io/github/last-commit/linxiang-ai/PEFT-Papers)](https://github.com/linxiang-ai/PEFT-Papers/commits/main)
[![Papers](https://img.shields.io/badge/papers-42-green.svg)]()

> A curated, structured database of papers on **Parameter-Efficient Fine-Tuning (PEFT)** for large pre-trained models. Designed for researchers who need to navigate the rapidly evolving PEFT landscape.

📊 **Current stats**: 42 papers · 6 method families · 4 application domains · Updated weekly via CI

---

## 🎯 What makes this repo different?

Unlike typical awesome lists, this repository:

- 📐 **Structured metadata for every paper** — venue, backbone model, trainable params ratio, open-source status
- 🌳 **Multi-dimensional indexing** — browse by method / year / domain / venue
- 🗺️ **Method taxonomy with evolution diagrams** — understand how the field developed
- 🔄 **Auto-updated weekly** via GitHub Actions scraping arXiv
- 📊 **Benchmark comparison tables** for standard tasks

---

## 🚀 Quick Start for Researchers

**Looking for a specific paper?** → Browse:
- [By Method](papers/by-method/) — LoRA family, Adapter, Prompt Tuning, Selective, Hybrid, Quantization-aware
- [By Year](papers/by-year/) — Chronological view of the field
- [By Domain](papers/by-domain/) — NLP, Vision, Multimodal, Diffusion
- [By Venue](papers/by-venue/) — Top conference papers
- [Must-Read](papers/must-read.md) — Foundational + must-read entries

**Need quick context?** → See [Method Taxonomy](#-method-taxonomy) below.

> 📝 Planned: `SURVEY.md` (method evolution narrative), `benchmarks.md` (cross-method comparison), `implementations.md` (full library catalog).

---

## 📚 Method Taxonomy

_(Taxonomy diagram TBD — will live at `figures/taxonomy.png`.)_

PEFT methods can be grouped into four main paradigms:

| Paradigm | Key Idea | Representative Methods |
|----------|----------|------------------------|
| **Additive** | Insert new trainable modules | Adapter, Prefix-Tuning, Prompt Tuning |
| **Reparameterization** | Low-rank decomposition of updates | LoRA, DoRA, AdaLoRA, VeRA |
| **Selective** | Update a subset of original params | BitFit, DiffPruning |
| **Hybrid** | Combine multiple paradigms | MAM Adapter, UniPELT |

---

## ⭐ Must-Read Papers

If you're starting out, read these in order:

1. **Houlsby et al.** "Parameter-Efficient Transfer Learning for NLP" (ICML 2019) — [`paper`](https://arxiv.org/abs/1902.00751)
2. **Li & Liang** "Prefix-Tuning: Optimizing Continuous Prompts for Generation" (ACL 2021) — [`paper`](https://arxiv.org/abs/2101.00190)
3. **Hu et al.** "LoRA: Low-Rank Adaptation of Large Language Models" (ICLR 2022) — [`paper`](https://arxiv.org/abs/2106.09685)
4. **He et al.** "Towards a Unified View of Parameter-Efficient Transfer Learning" (ICLR 2022) — [`paper`](https://arxiv.org/abs/2110.04366)
5. **Dettmers et al.** "QLoRA: Efficient Finetuning of Quantized LLMs" (NeurIPS 2023) — [`paper`](https://arxiv.org/abs/2305.14314)

[See more must-read papers →](papers/must-read.md)

---

## 🆕 Recent Additions

A weekly arXiv scan is scheduled in [`.github/workflows/weekly-update.yml`](.github/workflows/weekly-update.yml). Every Monday it opens a PR with a curated review queue of new PEFT papers — see [open PRs](https://github.com/linxiang-ai/PEFT-Papers/pulls).

---

## 📖 Surveys & Reviews

- **Han et al.** "Parameter-Efficient Fine-Tuning for Large Models: A Comprehensive Survey" (2024) — [`paper`](https://arxiv.org/abs/2403.14608)
- **Lialin et al.** "Scaling Down to Scale Up: A Guide to PEFT" (2023) — [`paper`](https://arxiv.org/abs/2303.15647)
- **Ding et al.** "Parameter-efficient fine-tuning of large-scale pre-trained language models" (Nature MI 2023) — [`paper`](https://www.nature.com/articles/s42256-023-00626-4)

---

## 🛠️ Implementations

The most-used PEFT libraries:

| Library | Maintainer | Coverage |
|---------|-----------|----------|
| [PEFT](https://github.com/huggingface/peft) | Hugging Face | LoRA, Prefix-Tuning, P-Tuning, Prompt Tuning, Adapter |
| [AdapterHub](https://github.com/adapter-hub/adapters) | Adapter-Hub | Adapter family, AdapterFusion |
| [LoRA](https://github.com/microsoft/LoRA) | Microsoft | Original LoRA |

[See full list →](implementations.md)

---

## 🤝 Contributing

We welcome contributions! See [`CONTRIBUTING.md`](CONTRIBUTING.md) for:
- How to submit a new paper
- Metadata format requirements
- Review process

To suggest a paper: [open an issue](https://github.com/linxiang-ai/PEFT-Papers/issues/new?template=add-paper.md) using the template.

---

## 📊 Statistics

- Total papers: **42**
- Top-venue papers (NeurIPS / ICML / ICLR / ACL / EMNLP / CVPR): **29**
- Papers with official open-source code: **36**
- Last updated: see commit log

---

## 📄 Citation

If this repository helps your research, please consider citing:

```bibtex
@misc{peft-papers,
  author = {Lin Xiang},
  title = {PEFT-Papers: A Structured Collection of Parameter-Efficient Fine-Tuning Research},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/linxiang-ai/PEFT-Papers}
}
```

---

## 📬 Contact

- Issues & PRs: welcome — file at [github.com/linxiang-ai/PEFT-Papers/issues](https://github.com/linxiang-ai/PEFT-Papers/issues)

---

## ⚖️ License

MIT License. See [`LICENSE`](LICENSE) for details.
