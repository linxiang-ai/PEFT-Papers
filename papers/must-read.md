# Must-read PEFT papers

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_23 papers, sorted by year (desc)._

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

### GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection
- **Authors**: Jiawei Zhao et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2403.03507](https://arxiv.org/abs/2403.03507)
- **Code**: [jiaweizzhao/GaLore](https://github.com/jiaweizzhao/GaLore)
- **Idea**: Project gradients into a low-rank subspace before optimizer updates, enabling full-parameter LLM training with LoRA-level memory.
- **Params**: 100% (low-rank gradient) | **Open-source**: official

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

### ReFT: Representation Finetuning for Language Models
- **Authors**: Zhengxuan Wu et al.
- **Venue**: NeurIPS 2024
- **Paper**: [arXiv:2404.03592](https://arxiv.org/abs/2404.03592)
- **Code**: [stanfordnlp/pyreft](https://github.com/stanfordnlp/pyreft)
- **Idea**: Edit a sparse set of hidden representations via learned low-rank interventions, parameter-efficient yet stronger than LoRA on instruction tuning.
- **Params**: <0.03% | **Open-source**: official

### AdaLoRA: Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning
- **Authors**: Qingru Zhang et al.
- **Venue**: ICLR 2023
- **Paper**: [arXiv:2303.10512](https://arxiv.org/abs/2303.10512)
- **Code**: [QingruZhang/AdaLoRA](https://github.com/QingruZhang/AdaLoRA)
- **Idea**: Parameterize LoRA updates as SVD-style decompositions and adaptively prune unimportant singular values to allocate rank budgets per layer.
- **Params**: varies | **Open-source**: official

### Multi-Concept Customization of Text-to-Image Diffusion
- **Authors**: Nupur Kumari et al.
- **Venue**: CVPR 2023
- **Paper**: [arXiv:2212.04488](https://arxiv.org/abs/2212.04488)
- **Code**: [adobe-research/custom-diffusion](https://github.com/adobe-research/custom-diffusion)
- **Idea**: Customize text-to-image diffusion by fine-tuning only cross-attention key/value projections, enabling multi-concept composition.
- **Params**: ~3% | **Open-source**: official

### Parameter-efficient fine-tuning of large-scale pre-trained language models
- **Authors**: Ning Ding et al.
- **Venue**: Nature Machine Intelligence 2023
- **Paper**: [arXiv:2203.06904](https://arxiv.org/abs/2203.06904)
- **Code**: [thunlp/OpenDelta](https://github.com/thunlp/OpenDelta)
- **Idea**: Comprehensive empirical study and taxonomy of delta tuning methods, with theoretical analyses linking them to optimization and optimal control.
- **Params**: varies | **Open-source**: official

### QLoRA: Efficient Finetuning of Quantized LLMs
- **Authors**: Tim Dettmers et al.
- **Venue**: NeurIPS 2023
- **Paper**: [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)
- **Code**: [artidoro/qlora](https://github.com/artidoro/qlora)
- **Idea**: Combine 4-bit NF4 quantization, double quantization, and paged optimizers with LoRA to fine-tune 65B models on a single GPU.
- **Params**: 0.1%-0.5% | **Open-source**: official

### An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion
- **Authors**: Rinon Gal et al.
- **Venue**: ICLR 2023
- **Paper**: [arXiv:2208.01618](https://arxiv.org/abs/2208.01618)
- **Code**: [rinongal/textual_inversion](https://github.com/rinongal/textual_inversion)
- **Idea**: Learn a new pseudo-word embedding in the text encoder to capture a visual concept from a few images without retraining the diffusion model.
- **Params**: <0.001% | **Open-source**: official

### AdaptFormer: Adapting Vision Transformers for Scalable Visual Recognition
- **Authors**: Shoufa Chen et al.
- **Venue**: NeurIPS 2022
- **Paper**: [arXiv:2205.13535](https://arxiv.org/abs/2205.13535)
- **Code**: [ShoufaChen/AdaptFormer](https://github.com/ShoufaChen/AdaptFormer)
- **Idea**: Add a parallel scaled adapter alongside frozen ViT MLP blocks to transfer image pretrained models to video and dense tasks.
- **Params**: <2% | **Open-source**: official

### BitFit: Simple Parameter-efficient Fine-tuning for Transformer-based Masked Language-models
- **Authors**: Elad Ben Zaken et al.
- **Venue**: ACL 2022
- **Paper**: [arXiv:2106.10199](https://arxiv.org/abs/2106.10199)
- **Code**: [benzakenelad/BitFit](https://github.com/benzakenelad/BitFit)
- **Idea**: Fine-tune only the bias terms of a pretrained Transformer, matching full fine-tuning on small-to-medium tasks.
- **Params**: 0.08%-0.1% | **Open-source**: official

### Learning to Prompt for Vision-Language Models
- **Authors**: Kaiyang Zhou et al.
- **Venue**: IJCV 2022
- **Paper**: [arXiv:2109.01134](https://arxiv.org/abs/2109.01134)
- **Code**: [KaiyangZhou/CoOp](https://github.com/KaiyangZhou/CoOp)
- **Idea**: Replace CLIP's hand-crafted text prompts with learnable continuous context vectors for few-shot vision-language classification.
- **Params**: <0.01% | **Open-source**: official

### LoRA: Low-Rank Adaptation of Large Language Models
- **Authors**: Edward J. Hu et al.
- **Venue**: ICLR 2022
- **Paper**: [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
- **Code**: [microsoft/LoRA](https://github.com/microsoft/LoRA)
- **Idea**: Inject trainable low-rank decomposition matrices into frozen weight matrices to approximate full fine-tuning updates.
- **Params**: 0.01%-0.1% | **Open-source**: official

### P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks
- **Authors**: Xiao Liu et al.
- **Venue**: ACL 2022
- **Paper**: [arXiv:2110.07602](https://arxiv.org/abs/2110.07602)
- **Code**: [THUDM/P-tuning-v2](https://github.com/THUDM/P-tuning-v2)
- **Idea**: Apply deep prompt tuning at every layer so prompt tuning stays competitive across model scales and sequence labelling tasks.
- **Params**: 0.1%-3% | **Open-source**: official

### Towards a Unified View of Parameter-Efficient Transfer Learning
- **Authors**: Junxian He et al.
- **Venue**: ICLR 2022
- **Paper**: [arXiv:2110.04366](https://arxiv.org/abs/2110.04366)
- **Code**: [jxhe/unify-parameter-efficient-tuning](https://github.com/jxhe/unify-parameter-efficient-tuning)
- **Idea**: Cast adapters, prefix tuning, and LoRA as instances of one design space, yielding the MAM Adapter hybrid.
- **Params**: varies | **Open-source**: official

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

### Compacter: Efficient Low-Rank Hypercomplex Adapter Layers
- **Authors**: Rabeeh Karimi Mahabadi et al.
- **Venue**: NeurIPS 2021
- **Paper**: [arXiv:2106.04647](https://arxiv.org/abs/2106.04647)
- **Code**: [rabeehk/compacter](https://github.com/rabeehk/compacter)
- **Idea**: Use Kronecker-product hypercomplex low-rank parameterization to shrink adapter parameters by orders of magnitude.
- **Params**: ~0.05% | **Open-source**: official

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

### Parameter-Efficient Transfer Learning for NLP
- **Authors**: Neil Houlsby et al.
- **Venue**: ICML 2019
- **Paper**: [arXiv:1902.00751](https://arxiv.org/abs/1902.00751)
- **Code**: [google-research/adapter-bert](https://github.com/google-research/adapter-bert)
- **Idea**: Insert small bottleneck adapter modules between Transformer layers and train only them, keeping the pretrained backbone frozen.
- **Params**: ~3.6% | **Open-source**: official
