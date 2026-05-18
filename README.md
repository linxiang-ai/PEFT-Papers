# PEFT-Papers: A Structured Collection of Parameter-Efficient Fine-Tuning Research

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Last Update](https://img.shields.io/github/last-commit/YOUR_USERNAME/PEFT-Papers)](https://github.com/YOUR_USERNAME/PEFT-Papers/commits/main)
[![Papers](https://img.shields.io/badge/papers-100+-green.svg)]()

> A curated, structured database of papers on **Parameter-Efficient Fine-Tuning (PEFT)** for large pre-trained models. Designed for researchers who need to navigate the rapidly evolving PEFT landscape.

📊 **Current stats**: 120+ papers · 6 method families · 5 application domains · Updated weekly

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

**New to PEFT?** → Start with [`SURVEY.md`](SURVEY.md) — our overview of the field

**Looking for a specific paper?** → Browse:
- [By Method](papers/by-method/) — LoRA family, Adapter, Prompt Tuning, etc.
- [By Year](papers/by-year/) — Chronological view of the field
- [By Domain](papers/by-domain/) — NLP, Vision, Multimodal, Diffusion
- [By Venue](papers/by-venue/) — Top conference papers

**Want to compare methods?** → See [`benchmarks.md`](benchmarks.md)

**Need code implementations?** → See [`implementations.md`](implementations.md)

---

## 📚 Method Taxonomy

![PEFT Taxonomy](figures/taxonomy.png)

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

<!-- This section is auto-updated by GitHub Actions -->

| Date | Paper | Method | Venue |
|------|-------|--------|-------|
| 2026-05-10 | *Placeholder* | LoRA variant | arXiv |
| 2026-05-03 | *Placeholder* | MoE-PEFT | ICML 2026 |

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

To suggest a paper: [open an issue](https://github.com/YOUR_USERNAME/PEFT-Papers/issues/new?template=add-paper.md) using the template.

---

## 📊 Statistics

- Total papers: 120+
- Papers from top venues (NeurIPS/ICML/ICLR/ACL): 60+
- Papers with official code: 80+
- Last updated: auto-generated

---

## 📄 Citation

If this repository helps your research, please consider citing:

```bibtex
@misc{peft-papers,
  author = {Your Name},
  title = {PEFT-Papers: A Structured Collection of Parameter-Efficient Fine-Tuning Research},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/YOUR_USERNAME/PEFT-Papers}
}
```

---

## 📬 Contact

- Issues & PRs: welcome!
- Email: your.email@example.com
- Twitter/X: @your_handle

---

## ⚖️ License

MIT License. See [`LICENSE`](LICENSE) for details.
