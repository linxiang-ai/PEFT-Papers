# Vision PEFT

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_3 papers, sorted by year (desc)._

### Parameter-Efficient Fine-Tuning with Discrete Fourier Transform
- **Authors**: Ziqi Gao et al.
- **Venue**: ICML 2024
- **Paper**: [arXiv:2405.03003](https://arxiv.org/abs/2405.03003)
- **Code**: [Chaos96/fourierft](https://github.com/Chaos96/fourierft)
- **Idea**: Learn a sparse set of Fourier spectral coefficients to represent weight updates, achieving higher compression than LoRA.
- **Params**: ~6x smaller than LoRA | **Open-source**: official

### AdaptFormer: Adapting Vision Transformers for Scalable Visual Recognition
- **Authors**: Shoufa Chen et al.
- **Venue**: NeurIPS 2022
- **Paper**: [arXiv:2205.13535](https://arxiv.org/abs/2205.13535)
- **Code**: [ShoufaChen/AdaptFormer](https://github.com/ShoufaChen/AdaptFormer)
- **Idea**: Add a parallel scaled adapter alongside frozen ViT MLP blocks to transfer image pretrained models to video and dense tasks.
- **Params**: <2% | **Open-source**: official

### Visual Prompt Tuning
- **Authors**: Menglin Jia et al.
- **Venue**: ECCV 2022
- **Paper**: [arXiv:2203.12119](https://arxiv.org/abs/2203.12119)
- **Code**: [kmnp/vpt](https://github.com/kmnp/vpt)
- **Idea**: Insert learnable visual prompt tokens at the input or every layer of a frozen ViT to adapt to downstream vision tasks.
- **Params**: <1% | **Open-source**: official
