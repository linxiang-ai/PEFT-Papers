# Adapter Family

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_5 papers, sorted by year (desc)._

### CLIP-Adapter: Better Vision-Language Models with Feature Adapters
- **Authors**: Peng Gao et al.
- **Venue**: IJCV 2024
- **Paper**: [arXiv:2110.04544](https://arxiv.org/abs/2110.04544)
- **Code**: [gaopengcuhk/CLIP-Adapter](https://github.com/gaopengcuhk/CLIP-Adapter)
- **Idea**: Add a small bottleneck adapter on top of CLIP's frozen visual or text encoder with residual blending for few-shot classification.
- **Params**: <1% | **Open-source**: official

### AdaptFormer: Adapting Vision Transformers for Scalable Visual Recognition
- **Authors**: Shoufa Chen et al.
- **Venue**: NeurIPS 2022
- **Paper**: [arXiv:2205.13535](https://arxiv.org/abs/2205.13535)
- **Code**: [ShoufaChen/AdaptFormer](https://github.com/ShoufaChen/AdaptFormer)
- **Idea**: Add a parallel scaled adapter alongside frozen ViT MLP blocks to transfer image pretrained models to video and dense tasks.
- **Params**: <2% | **Open-source**: official

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

### Parameter-Efficient Transfer Learning for NLP
- **Authors**: Neil Houlsby et al.
- **Venue**: ICML 2019
- **Paper**: [arXiv:1902.00751](https://arxiv.org/abs/1902.00751)
- **Code**: [google-research/adapter-bert](https://github.com/google-research/adapter-bert)
- **Idea**: Insert small bottleneck adapter modules between Transformer layers and train only them, keeping the pretrained backbone frozen.
- **Params**: ~3.6% | **Open-source**: official
