# ICML papers

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_6 papers, sorted by year (desc)._

### DoRA: Weight-Decomposed Low-Rank Adaptation
- **Authors**: Shih-Yang Liu et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2402.09353](https://arxiv.org/abs/2402.09353)
- **Code**: [NVlabs/DoRA](https://github.com/NVlabs/DoRA)
- **Idea**: Decompose pretrained weights into magnitude and direction, applying LoRA only to direction to close the gap to full fine-tuning.
- **Params**: <0.1% | **Open-source**: official

### Parameter-Efficient Fine-Tuning with Discrete Fourier Transform
- **Authors**: Ziqi Gao et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2405.03003](https://arxiv.org/abs/2405.03003)
- **Code**: [Chaos96/fourierft](https://github.com/Chaos96/fourierft)
- **Idea**: Learn a sparse set of Fourier spectral coefficients to represent weight updates, achieving higher compression than LoRA.
- **Params**: ~6x smaller than LoRA | **Open-source**: official

### GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection
- **Authors**: Jiawei Zhao et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2403.03507](https://arxiv.org/abs/2403.03507)
- **Code**: [jiaweizzhao/GaLore](https://github.com/jiaweizzhao/GaLore)
- **Idea**: Project gradients into a low-rank subspace before optimizer updates, enabling full-parameter LLM training with LoRA-level memory.
- **Params**: 100% (low-rank gradient) | **Open-source**: official

### Accurate LoRA-Finetuning Quantization of LLMs via Information Retention
- **Authors**: Haotong Qin et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2402.05445](https://arxiv.org/abs/2402.05445)
- **Code**: [htqin/ir-qlora](https://github.com/htqin/ir-qlora)
- **Idea**: Preserve information during LoRA-finetuned LLM quantization via calibration on quantization parameters and elastic LoRA initialization.
- **Params**: 0.1%-0.5% | **Open-source**: official

### LoRA+: Efficient Low Rank Adaptation of Large Models
- **Authors**: Soufiane Hayou et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2402.12354](https://arxiv.org/abs/2402.12354)
- **Code**: [nikhil-ghosh-berkeley/loraplus](https://github.com/nikhil-ghosh-berkeley/loraplus)
- **Idea**: Use different learning rates for the LoRA A and B matrices to fix feature-learning inefficiency at large model widths.
- **Params**: same as LoRA | **Open-source**: official

### Parameter-Efficient Transfer Learning for NLP
- **Authors**: Neil Houlsby et al.
- **Venue**: ICML 2019
- **Paper**: [arXiv:1902.00751](https://arxiv.org/abs/1902.00751)
- **Code**: [google-research/adapter-bert](https://github.com/google-research/adapter-bert)
- **Idea**: Insert small bottleneck adapter modules between Transformer layers and train only them, keeping the pretrained backbone frozen.
- **Params**: ~3.6% | **Open-source**: official
