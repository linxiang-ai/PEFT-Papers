# Other venues

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_8 papers, sorted by year (desc)._

### CLIP-Adapter: Better Vision-Language Models with Feature Adapters
- **Authors**: Peng Gao et al.
- **Venue**: IJCV 2024
- **Paper**: [arXiv:2110.04544](https://arxiv.org/abs/2110.04544)
- **Code**: [gaopengcuhk/CLIP-Adapter](https://github.com/gaopengcuhk/CLIP-Adapter)
- **Idea**: Add a small bottleneck adapter on top of CLIP's frozen visual or text encoder with residual blending for few-shot classification.
- **Params**: <1% | **Open-source**: official

### Concept Sliders: LoRA Adaptors for Precise Control in Diffusion Models
- **Authors**: Rohit Gandikota et al.
- **Venue**: ECCV 2024
- **Paper**: [arXiv:2311.12092](https://arxiv.org/abs/2311.12092)
- **Code**: [rohitgandikota/sliders](https://github.com/rohitgandikota/sliders)
- **Idea**: Train low-rank LoRA adaptors as semantic sliders, enabling continuous control over specific image attributes in diffusion models.
- **Params**: <1% | **Open-source**: official

### Parameter-efficient fine-tuning of large-scale pre-trained language models
- **Authors**: Ning Ding et al.
- **Venue**: Nature Machine Intelligence 2023
- **Paper**: [arXiv:2203.06904](https://arxiv.org/abs/2203.06904)
- **Code**: [thunlp/OpenDelta](https://github.com/thunlp/OpenDelta)
- **Idea**: Comprehensive empirical study and taxonomy of delta tuning methods, with theoretical analyses linking them to optimization and optimal control.
- **Params**: varies | **Open-source**: official

### DyLoRA: Parameter Efficient Tuning of Pre-trained Models using Dynamic Search-Free Low-Rank Adaptation
- **Authors**: Mojtaba Valipour et al.
- **Venue**: EACL 2023
- **Paper**: [arXiv:2210.07558](https://arxiv.org/abs/2210.07558)
- **Code**: [huawei-noah/KD-NLP](https://github.com/huawei-noah/KD-NLP)
- **Idea**: Train LoRA at multiple ranks simultaneously via nested dropout, eliminating the need to search for an optimal rank per task.
- **Params**: varies | **Open-source**: official

### SVDiff: Compact Parameter Space for Diffusion Fine-Tuning
- **Authors**: Ligong Han et al.
- **Venue**: ICCV 2023
- **Paper**: [arXiv:2303.11305](https://arxiv.org/abs/2303.11305)
- **Idea**: Fine-tune only singular values of pretrained weight matrices via SVD, yielding compact and composable diffusion personalizations.
- **Params**: ~0.05% | **Open-source**: community

### Learning to Prompt for Vision-Language Models
- **Authors**: Kaiyang Zhou et al.
- **Venue**: IJCV 2022
- **Paper**: [arXiv:2109.01134](https://arxiv.org/abs/2109.01134)
- **Code**: [KaiyangZhou/CoOp](https://github.com/KaiyangZhou/CoOp)
- **Idea**: Replace CLIP's hand-crafted text prompts with learnable continuous context vectors for few-shot vision-language classification.
- **Params**: <0.01% | **Open-source**: official

### Visual Prompt Tuning
- **Authors**: Menglin Jia et al.
- **Venue**: ECCV 2022
- **Paper**: [arXiv:2203.12119](https://arxiv.org/abs/2203.12119)
- **Code**: [kmnp/vpt](https://github.com/kmnp/vpt)
- **Idea**: Insert learnable visual prompt tokens at the input or every layer of a frozen ViT to adapt to downstream vision tasks.
- **Params**: <1% | **Open-source**: official

### AdapterFusion: Non-Destructive Task Composition for Transfer Learning
- **Authors**: Jonas Pfeiffer et al.
- **Venue**: EACL 2021
- **Paper**: [arXiv:2005.00247](https://arxiv.org/abs/2005.00247)
- **Code**: [adapter-hub/adapters](https://github.com/adapter-hub/adapters)
- **Idea**: Two-stage scheme that first trains task-specific adapters, then composes them through an attention-based fusion layer.
- **Params**: varies | **Open-source**: official
