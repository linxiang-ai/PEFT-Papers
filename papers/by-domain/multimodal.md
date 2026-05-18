# Multimodal PEFT

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_5 papers, sorted by year (desc)._

### CLIP-Adapter: Better Vision-Language Models with Feature Adapters
- **Authors**: Peng Gao et al.
- **Venue**: IJCV 2024
- **Paper**: [arXiv:2110.04544](https://arxiv.org/abs/2110.04544)
- **Code**: [gaopengcuhk/CLIP-Adapter](https://github.com/gaopengcuhk/CLIP-Adapter)
- **Idea**: Add a small bottleneck adapter on top of CLIP's frozen visual or text encoder with residual blending for few-shot classification.
- **Params**: <1% | **Open-source**: official

### DoRA: Weight-Decomposed Low-Rank Adaptation
- **Authors**: Shih-Yang Liu et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2402.09353](https://arxiv.org/abs/2402.09353)
- **Code**: [NVlabs/DoRA](https://github.com/NVlabs/DoRA)
- **Idea**: Decompose pretrained weights into magnitude and direction, applying LoRA only to direction to close the gap to full fine-tuning.
- **Params**: <0.1% | **Open-source**: official

### LLaMA-Adapter: Efficient Fine-tuning of Language Models with Zero-init Attention
- **Authors**: Renrui Zhang et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2303.16199](https://arxiv.org/abs/2303.16199)
- **Code**: [OpenGVLab/LLaMA-Adapter](https://github.com/OpenGVLab/LLaMA-Adapter)
- **Idea**: Inject learnable prompt tokens with zero-initialized gated attention, enabling efficient instruction tuning and multimodal extension.
- **Params**: ~0.02% | **Open-source**: official

### Mixture of LoRA Experts
- **Authors**: Xun Wu et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2404.13628](https://arxiv.org/abs/2404.13628)
- **Idea**: Hierarchically compose multiple trained LoRA experts via a learnable gating function, enabling flexible specialization without retraining.
- **Params**: varies | **Open-source**: community

### Learning to Prompt for Vision-Language Models
- **Authors**: Kaiyang Zhou et al.
- **Venue**: IJCV 2022
- **Paper**: [arXiv:2109.01134](https://arxiv.org/abs/2109.01134)
- **Code**: [KaiyangZhou/CoOp](https://github.com/KaiyangZhou/CoOp)
- **Idea**: Replace CLIP's hand-crafted text prompts with learnable continuous context vectors for few-shot vision-language classification.
- **Params**: <0.01% | **Open-source**: official
