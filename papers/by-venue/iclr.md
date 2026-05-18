# ICLR papers

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_10 papers, sorted by year (desc)._

### LLaMA-Adapter: Efficient Fine-tuning of Language Models with Zero-init Attention
- **Authors**: Renrui Zhang et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2303.16199](https://arxiv.org/abs/2303.16199)
- **Code**: [OpenGVLab/LLaMA-Adapter](https://github.com/OpenGVLab/LLaMA-Adapter)
- **Idea**: Inject learnable prompt tokens with zero-initialized gated attention, enabling efficient instruction tuning and multimodal extension.
- **Params**: ~0.02% | **Open-source**: official

### LoftQ: LoRA-Fine-Tuning-Aware Quantization for Large Language Models
- **Authors**: Yixiao Li et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2310.08659](https://arxiv.org/abs/2310.08659)
- **Code**: [yxli2123/LoftQ](https://github.com/yxli2123/LoftQ)
- **Idea**: Jointly initialize quantized weights and LoRA factors via alternating optimization to narrow the gap with full-precision fine-tuning.
- **Params**: 0.1%-1% | **Open-source**: official

### LQ-LoRA: Low-rank Plus Quantized Matrix Decomposition for Efficient Language Model Finetuning
- **Authors**: Han Guo et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2311.12023](https://arxiv.org/abs/2311.12023)
- **Code**: [HanGuo97/lq-lora](https://github.com/HanGuo97/lq-lora)
- **Idea**: Decompose pretrained weights into a quantized base plus a low-rank residual via iterative SVD, improving QLoRA accuracy at extreme bit-widths.
- **Params**: 0.1%-0.5% | **Open-source**: official

### Mixture of LoRA Experts
- **Authors**: Xun Wu et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2404.13628](https://arxiv.org/abs/2404.13628)
- **Idea**: Hierarchically compose multiple trained LoRA experts via a learnable gating function, enabling flexible specialization without retraining.
- **Params**: varies | **Open-source**: community

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

### AdaLoRA: Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning
- **Authors**: Qingru Zhang et al.
- **Venue**: ICLR 2023
- **Paper**: [arXiv:2303.10512](https://arxiv.org/abs/2303.10512)
- **Code**: [QingruZhang/AdaLoRA](https://github.com/QingruZhang/AdaLoRA)
- **Idea**: Parameterize LoRA updates as SVD-style decompositions and adaptively prune unimportant singular values to allocate rank budgets per layer.
- **Params**: varies | **Open-source**: official

### An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion
- **Authors**: Rinon Gal et al.
- **Venue**: ICLR 2023
- **Paper**: [arXiv:2208.01618](https://arxiv.org/abs/2208.01618)
- **Code**: [rinongal/textual_inversion](https://github.com/rinongal/textual_inversion)
- **Idea**: Learn a new pseudo-word embedding in the text encoder to capture a visual concept from a few images without retraining the diffusion model.
- **Params**: <0.001% | **Open-source**: official

### LoRA: Low-Rank Adaptation of Large Language Models
- **Authors**: Edward J. Hu et al.
- **Venue**: ICLR 2022
- **Paper**: [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
- **Code**: [microsoft/LoRA](https://github.com/microsoft/LoRA)
- **Idea**: Inject trainable low-rank decomposition matrices into frozen weight matrices to approximate full fine-tuning updates.
- **Params**: 0.01%-0.1% | **Open-source**: official

### Towards a Unified View of Parameter-Efficient Transfer Learning
- **Authors**: Junxian He et al.
- **Venue**: ICLR 2022
- **Paper**: [arXiv:2110.04366](https://arxiv.org/abs/2110.04366)
- **Code**: [jxhe/unify-parameter-efficient-tuning](https://github.com/jxhe/unify-parameter-efficient-tuning)
- **Idea**: Cast adapters, prefix tuning, and LoRA as instances of one design space, yielding the MAM Adapter hybrid.
- **Params**: varies | **Open-source**: official
