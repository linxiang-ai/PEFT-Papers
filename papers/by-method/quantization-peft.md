# Quantization-aware PEFT

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_6 papers, sorted by year (desc)._

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

### LQ-LoRA: Low-rank Plus Quantized Matrix Decomposition for Efficient Language Model Finetuning
- **Authors**: Han Guo et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2311.12023](https://arxiv.org/abs/2311.12023)
- **Code**: [HanGuo97/lq-lora](https://github.com/HanGuo97/lq-lora)
- **Idea**: Decompose pretrained weights into a quantized base plus a low-rank residual via iterative SVD, improving QLoRA accuracy at extreme bit-widths.
- **Params**: 0.1%-0.5% | **Open-source**: official

### QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models
- **Authors**: Yuhui Xu et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2309.14717](https://arxiv.org/abs/2309.14717)
- **Code**: [yuhuixu1993/qa-lora](https://github.com/yuhuixu1993/qa-lora)
- **Idea**: Use group-wise operators to balance quantization and LoRA fine-tuning so the merged model stays quantized without dequantization.
- **Params**: 0.1%-0.5% | **Open-source**: official

### Memory-Efficient Fine-Tuning of Compressed Large Language Models via sub-4-bit Integer Quantization
- **Authors**: Jeonghoon Kim et al.
- **Venue**: NeurIPS 2023
- **Paper**: [arXiv:2305.14152](https://arxiv.org/abs/2305.14152)
- **Idea**: Fine-tune only quantization scales of a sub-4-bit integer model, enabling memory-efficient adaptation without LoRA-style add-on weights.
- **Params**: <0.5% | **Open-source**: community

### QLoRA: Efficient Finetuning of Quantized LLMs
- **Authors**: Tim Dettmers et al.
- **Venue**: NeurIPS 2023
- **Paper**: [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)
- **Code**: [artidoro/qlora](https://github.com/artidoro/qlora)
- **Idea**: Combine 4-bit NF4 quantization, double quantization, and paged optimizers with LoRA to fine-tune 65B models on a single GPU.
- **Params**: 0.1%-0.5% | **Open-source**: official
