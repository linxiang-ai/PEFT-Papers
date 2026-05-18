# NeurIPS papers

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_7 papers, sorted by year (desc)._

### PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models
- **Authors**: Fanxu Meng et al.
- **Venue**: NeurIPS 2024
- **Paper**: [arXiv:2404.02948](https://arxiv.org/abs/2404.02948)
- **Code**: [GraphPKU/PiSSA](https://github.com/GraphPKU/PiSSA)
- **Idea**: Initialize LoRA matrices with the principal singular components of pretrained weights for faster convergence and stronger results.
- **Params**: same as LoRA | **Open-source**: official

### ReFT: Representation Finetuning for Language Models
- **Authors**: Zhengxuan Wu et al.
- **Venue**: NeurIPS 2024
- **Paper**: [arXiv:2404.03592](https://arxiv.org/abs/2404.03592)
- **Code**: [stanfordnlp/pyreft](https://github.com/stanfordnlp/pyreft)
- **Idea**: Edit a sparse set of hidden representations via learned low-rank interventions, parameter-efficient yet stronger than LoRA on instruction tuning.
- **Params**: <0.03% | **Open-source**: official

### Controlling Text-to-Image Diffusion by Orthogonal Finetuning
- **Authors**: Zeju Qiu et al.
- **Venue**: NeurIPS 2023
- **Paper**: [arXiv:2306.07280](https://arxiv.org/abs/2306.07280)
- **Code**: [Zeju1997/oft](https://github.com/Zeju1997/oft)
- **Idea**: Reparameterize fine-tuning as a learned orthogonal transformation of pretrained weights, preserving hyperspherical energy during adaptation.
- **Params**: varies | **Open-source**: official

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

### AdaptFormer: Adapting Vision Transformers for Scalable Visual Recognition
- **Authors**: Shoufa Chen et al.
- **Venue**: NeurIPS 2022
- **Paper**: [arXiv:2205.13535](https://arxiv.org/abs/2205.13535)
- **Code**: [ShoufaChen/AdaptFormer](https://github.com/ShoufaChen/AdaptFormer)
- **Idea**: Add a parallel scaled adapter alongside frozen ViT MLP blocks to transfer image pretrained models to video and dense tasks.
- **Params**: <2% | **Open-source**: official

### Compacter: Efficient Low-Rank Hypercomplex Adapter Layers
- **Authors**: Rabeeh Karimi Mahabadi et al.
- **Venue**: NeurIPS 2021
- **Paper**: [arXiv:2106.04647](https://arxiv.org/abs/2106.04647)
- **Code**: [rabeehk/compacter](https://github.com/rabeehk/compacter)
- **Idea**: Use Kronecker-product hypercomplex low-rank parameterization to shrink adapter parameters by orders of magnitude.
- **Params**: ~0.05% | **Open-source**: official
