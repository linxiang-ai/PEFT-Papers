# Prompt Tuning

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_7 papers, sorted by year (desc)._

### LLaMA-Adapter: Efficient Fine-tuning of Language Models with Zero-init Attention
- **Authors**: Renrui Zhang et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2303.16199](https://arxiv.org/abs/2303.16199)
- **Code**: [OpenGVLab/LLaMA-Adapter](https://github.com/OpenGVLab/LLaMA-Adapter)
- **Idea**: Inject learnable prompt tokens with zero-initialized gated attention, enabling efficient instruction tuning and multimodal extension.
- **Params**: ~0.02% | **Open-source**: official

### An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion
- **Authors**: Rinon Gal et al.
- **Venue**: ICLR 2023
- **Paper**: [arXiv:2208.01618](https://arxiv.org/abs/2208.01618)
- **Code**: [rinongal/textual_inversion](https://github.com/rinongal/textual_inversion)
- **Idea**: Learn a new pseudo-word embedding in the text encoder to capture a visual concept from a few images without retraining the diffusion model.
- **Params**: <0.001% | **Open-source**: official

### Learning to Prompt for Vision-Language Models
- **Authors**: Kaiyang Zhou et al.
- **Venue**: IJCV 2022
- **Paper**: [arXiv:2109.01134](https://arxiv.org/abs/2109.01134)
- **Code**: [KaiyangZhou/CoOp](https://github.com/KaiyangZhou/CoOp)
- **Idea**: Replace CLIP's hand-crafted text prompts with learnable continuous context vectors for few-shot vision-language classification.
- **Params**: <0.01% | **Open-source**: official

### P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks
- **Authors**: Xiao Liu et al.
- **Venue**: ACL 2022
- **Paper**: [arXiv:2110.07602](https://arxiv.org/abs/2110.07602)
- **Code**: [THUDM/P-tuning-v2](https://github.com/THUDM/P-tuning-v2)
- **Idea**: Apply deep prompt tuning at every layer so prompt tuning stays competitive across model scales and sequence labelling tasks.
- **Params**: 0.1%-3% | **Open-source**: official

### Visual Prompt Tuning
- **Authors**: Menglin Jia et al.
- **Venue**: ECCV 2022
- **Paper**: [arXiv:2203.12119](https://arxiv.org/abs/2203.12119)
- **Code**: [kmnp/vpt](https://github.com/kmnp/vpt)
- **Idea**: Insert learnable visual prompt tokens at the input or every layer of a frozen ViT to adapt to downstream vision tasks.
- **Params**: <1% | **Open-source**: official

### Prefix-Tuning: Optimizing Continuous Prompts for Generation
- **Authors**: Xiang Lisa Li et al.
- **Venue**: ACL 2021
- **Paper**: [arXiv:2101.00190](https://arxiv.org/abs/2101.00190)
- **Code**: [XiangLi1999/PrefixTuning](https://github.com/XiangLi1999/PrefixTuning)
- **Idea**: Prepend trainable continuous prefix vectors to every Transformer layer while keeping the language model frozen.
- **Params**: 0.1% | **Open-source**: official

### The Power of Scale for Parameter-Efficient Prompt Tuning
- **Authors**: Brian Lester et al.
- **Venue**: EMNLP 2021
- **Paper**: [arXiv:2104.08691](https://arxiv.org/abs/2104.08691)
- **Code**: [google-research/prompt-tuning](https://github.com/google-research/prompt-tuning)
- **Idea**: Learn a small soft prompt prepended to the input; matches full fine-tuning once model scale is sufficiently large.
- **Params**: <0.01% | **Open-source**: official
