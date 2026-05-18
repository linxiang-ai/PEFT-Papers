# arXiv papers

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_5 papers, sorted by year (desc)._

### Higher Layers Need More LoRA Experts
- **Authors**: Chongyang Gao et al.
- **Venue**: arXiv 2024
- **Paper**: [arXiv:2402.08562](https://arxiv.org/abs/2402.08562)
- **Code**: [GCYZSL/MoLA](https://github.com/GCYZSL/MoLA)
- **Idea**: Allocate more LoRA experts to higher Transformer layers where representations specialize, improving layer-aware MoE-LoRA performance.
- **Params**: varies | **Open-source**: official

### MoRA: High-Rank Updating for Parameter-Efficient Fine-Tuning
- **Authors**: Ting Jiang et al.
- **Venue**: arXiv 2024
- **Paper**: [arXiv:2405.12130](https://arxiv.org/abs/2405.12130)
- **Code**: [kongds/MoRA](https://github.com/kongds/MoRA)
- **Idea**: Replace LoRA's low-rank product with a single square matrix plus compress/decompress operators, getting higher-rank updates at equal parameters.
- **Params**: same as LoRA | **Open-source**: official

### X-LoRA: Mixture of Low-Rank Adapter Experts, a Flexible Framework for Large Language Models with Applications in Protein Mechanics and Molecular Design
- **Authors**: Eric L. Buehler et al.
- **Venue**: arXiv 2024
- **Paper**: [arXiv:2402.07148](https://arxiv.org/abs/2402.07148)
- **Code**: [EricLBuehler/xlora](https://github.com/EricLBuehler/xlora)
- **Idea**: Dynamically mix pretrained LoRA adapters per token and layer via a learned gating network, adding no parameters per expert.
- **Params**: varies | **Open-source**: official

### LoRA-FA: Memory-efficient Low-rank Adaptation for Large Language Models Fine-tuning
- **Authors**: Longteng Zhang et al.
- **Venue**: arXiv 2023
- **Paper**: [arXiv:2308.03303](https://arxiv.org/abs/2308.03303)
- **Idea**: Freeze LoRA's down-projection matrix A and train only B, halving activation memory while matching standard LoRA quality.
- **Params**: ~0.5x of LoRA | **Open-source**: community

### A Rank Stabilization Scaling Factor for Fine-Tuning with LoRA
- **Authors**: Damjan Kalajdzievski
- **Venue**: arXiv 2023
- **Paper**: [arXiv:2312.03732](https://arxiv.org/abs/2312.03732)
- **Idea**: Replace LoRA's 1/r scaling with 1/sqrt(r) to stabilize gradients and unlock effective fine-tuning at higher ranks.
- **Params**: same as LoRA | **Open-source**: community
