# LoRA Family

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_19 papers, sorted by year (desc)._

### Concept Sliders: LoRA Adaptors for Precise Control in Diffusion Models
- **Authors**: Rohit Gandikota et al.
- **Venue**: ECCV 2024
- **Paper**: [arXiv:2311.12092](https://arxiv.org/abs/2311.12092)
- **Code**: [rohitgandikota/sliders](https://github.com/rohitgandikota/sliders)
- **Idea**: Train low-rank LoRA adaptors as semantic sliders, enabling continuous control over specific image attributes in diffusion models.
- **Params**: <1% | **Open-source**: official

### DoRA: Weight-Decomposed Low-Rank Adaptation
- **Authors**: Shih-Yang Liu et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2402.09353](https://arxiv.org/abs/2402.09353)
- **Code**: [NVlabs/DoRA](https://github.com/NVlabs/DoRA)
- **Idea**: Decompose pretrained weights into magnitude and direction, applying LoRA only to direction to close the gap to full fine-tuning.
- **Params**: <0.1% | **Open-source**: official

### Accurate LoRA-Finetuning Quantization of LLMs via Information Retention
- **Authors**: Haotong Qin et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2402.05445](https://arxiv.org/abs/2402.05445)
- **Code**: [htqin/ir-qlora](https://github.com/htqin/ir-qlora)
- **Idea**: Preserve information during LoRA-finetuned LLM quantization via calibration on quantization parameters and elastic LoRA initialization.
- **Params**: 0.1%-0.5% | **Open-source**: official

### LoftQ: LoRA-Fine-Tuning-Aware Quantization for Large Language Models
- **Authors**: Yixiao Li et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2310.08659](https://arxiv.org/abs/2310.08659)
- **Code**: [yxli2123/LoftQ](https://github.com/yxli2123/LoftQ)
- **Idea**: Jointly initialize quantized weights and LoRA factors via alternating optimization to narrow the gap with full-precision fine-tuning.
- **Params**: 0.1%-1% | **Open-source**: official

### LoRA+: Efficient Low Rank Adaptation of Large Models
- **Authors**: Soufiane Hayou et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2402.12354](https://arxiv.org/abs/2402.12354)
- **Code**: [nikhil-ghosh-berkeley/loraplus](https://github.com/nikhil-ghosh-berkeley/loraplus)
- **Idea**: Use different learning rates for the LoRA A and B matrices to fix feature-learning inefficiency at large model widths.
- **Params**: same as LoRA | **Open-source**: official

### LoRAMoE: Alleviating World Knowledge Forgetting in Large Language Models via MoE-Style Plugin
- **Authors**: Shihan Dou et al.
- **Venue**: ACL 2024
- **Paper**: [arXiv:2312.09979](https://arxiv.org/abs/2312.09979)
- **Code**: [Ablustrund/LoRAMoE](https://github.com/Ablustrund/LoRAMoE)
- **Idea**: Combine multiple LoRA experts with a router and localized balancing loss to prevent world-knowledge forgetting during instruction tuning.
- **Params**: varies | **Open-source**: official

### LQ-LoRA: Low-rank Plus Quantized Matrix Decomposition for Efficient Language Model Finetuning
- **Authors**: Han Guo et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2311.12023](https://arxiv.org/abs/2311.12023)
- **Code**: [HanGuo97/lq-lora](https://github.com/HanGuo97/lq-lora)
- **Idea**: Decompose pretrained weights into a quantized base plus a low-rank residual via iterative SVD, improving QLoRA accuracy at extreme bit-widths.
- **Params**: 0.1%-0.5% | **Open-source**: official

### Higher Layers Need More LoRA Experts
- **Authors**: Chongyang Gao et al.
- **Venue**: arXiv 2024
- **Paper**: [arXiv:2402.08562](https://arxiv.org/abs/2402.08562)
- **Code**: [GCYZSL/MoLA](https://github.com/GCYZSL/MoLA)
- **Idea**: Allocate more LoRA experts to higher Transformer layers where representations specialize, improving layer-aware MoE-LoRA performance.
- **Params**: varies | **Open-source**: official

### Mixture of LoRA Experts
- **Authors**: Xun Wu et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2404.13628](https://arxiv.org/abs/2404.13628)
- **Idea**: Hierarchically compose multiple trained LoRA experts via a learnable gating function, enabling flexible specialization without retraining.
- **Params**: varies | **Open-source**: community

### PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models
- **Authors**: Fanxu Meng et al.
- **Venue**: NeurIPS 2024
- **Paper**: [arXiv:2404.02948](https://arxiv.org/abs/2404.02948)
- **Code**: [GraphPKU/PiSSA](https://github.com/GraphPKU/PiSSA)
- **Idea**: Initialize LoRA matrices with the principal singular components of pretrained weights for faster convergence and stronger results.
- **Params**: same as LoRA | **Open-source**: official

### QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models
- **Authors**: Yuhui Xu et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2309.14717](https://arxiv.org/abs/2309.14717)
- **Code**: [yuhuixu1993/qa-lora](https://github.com/yuhuixu1993/qa-lora)
- **Idea**: Use group-wise operators to balance quantization and LoRA fine-tuning so the merged model stays quantized without dequantization.
- **Params**: 0.1%-0.5% | **Open-source**: official

### VeRA: Vector-based Random Matrix Adaptation
- **Authors**: Dawid Jan Kopiczko et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2310.11454](https://arxiv.org/abs/2310.11454)
- **Idea**: Share a single pair of frozen random low-rank matrices across layers and train only tiny per-layer scaling vectors.
- **Params**: ~10x smaller than LoRA | **Open-source**: community

### X-LoRA: Mixture of Low-Rank Adapter Experts, a Flexible Framework for Large Language Models with Applications in Protein Mechanics and Molecular Design
- **Authors**: Eric L. Buehler et al.
- **Venue**: arXiv 2024
- **Paper**: [arXiv:2402.07148](https://arxiv.org/abs/2402.07148)
- **Code**: [EricLBuehler/xlora](https://github.com/EricLBuehler/xlora)
- **Idea**: Dynamically mix pretrained LoRA adapters per token and layer via a learned gating network, adding no parameters per expert.
- **Params**: varies | **Open-source**: official

### AdaLoRA: Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning
- **Authors**: Qingru Zhang et al.
- **Venue**: ICLR 2023
- **Paper**: [arXiv:2303.10512](https://arxiv.org/abs/2303.10512)
- **Code**: [QingruZhang/AdaLoRA](https://github.com/QingruZhang/AdaLoRA)
- **Idea**: Parameterize LoRA updates as SVD-style decompositions and adaptively prune unimportant singular values to allocate rank budgets per layer.
- **Params**: varies | **Open-source**: official

### DyLoRA: Parameter Efficient Tuning of Pre-trained Models using Dynamic Search-Free Low-Rank Adaptation
- **Authors**: Mojtaba Valipour et al.
- **Venue**: EACL 2023
- **Paper**: [arXiv:2210.07558](https://arxiv.org/abs/2210.07558)
- **Code**: [huawei-noah/KD-NLP](https://github.com/huawei-noah/KD-NLP)
- **Idea**: Train LoRA at multiple ranks simultaneously via nested dropout, eliminating the need to search for an optimal rank per task.
- **Params**: varies | **Open-source**: official

### LoRA-FA: Memory-efficient Low-rank Adaptation for Large Language Models Fine-tuning
- **Authors**: Longteng Zhang et al.
- **Venue**: arXiv 2023
- **Paper**: [arXiv:2308.03303](https://arxiv.org/abs/2308.03303)
- **Idea**: Freeze LoRA's down-projection matrix A and train only B, halving activation memory while matching standard LoRA quality.
- **Params**: ~0.5x of LoRA | **Open-source**: community

### QLoRA: Efficient Finetuning of Quantized LLMs
- **Authors**: Tim Dettmers et al.
- **Venue**: NeurIPS 2023
- **Paper**: [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)
- **Code**: [artidoro/qlora](https://github.com/artidoro/qlora)
- **Idea**: Combine 4-bit NF4 quantization, double quantization, and paged optimizers with LoRA to fine-tune 65B models on a single GPU.
- **Params**: 0.1%-0.5% | **Open-source**: official

### A Rank Stabilization Scaling Factor for Fine-Tuning with LoRA
- **Authors**: Damjan Kalajdzievski
- **Venue**: arXiv 2023
- **Paper**: [arXiv:2312.03732](https://arxiv.org/abs/2312.03732)
- **Idea**: Replace LoRA's 1/r scaling with 1/sqrt(r) to stabilize gradients and unlock effective fine-tuning at higher ranks.
- **Params**: same as LoRA | **Open-source**: community

### LoRA: Low-Rank Adaptation of Large Language Models
- **Authors**: Edward J. Hu et al.
- **Venue**: ICLR 2022
- **Paper**: [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
- **Code**: [microsoft/LoRA](https://github.com/microsoft/LoRA)
- **Idea**: Inject trainable low-rank decomposition matrices into frozen weight matrices to approximate full fine-tuning updates.
- **Params**: 0.01%-0.1% | **Open-source**: official
