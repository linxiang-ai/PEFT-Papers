# Selective Methods

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_3 papers, sorted by year (desc)._

### Multi-Concept Customization of Text-to-Image Diffusion
- **Authors**: Nupur Kumari et al.
- **Venue**: CVPR 2023
- **Paper**: [arXiv:2212.04488](https://arxiv.org/abs/2212.04488)
- **Code**: [adobe-research/custom-diffusion](https://github.com/adobe-research/custom-diffusion)
- **Idea**: Customize text-to-image diffusion by fine-tuning only cross-attention key/value projections, enabling multi-concept composition.
- **Params**: ~3% | **Open-source**: official

### Memory-Efficient Fine-Tuning of Compressed Large Language Models via sub-4-bit Integer Quantization
- **Authors**: Jeonghoon Kim et al.
- **Venue**: NeurIPS 2023
- **Paper**: [arXiv:2305.14152](https://arxiv.org/abs/2305.14152)
- **Idea**: Fine-tune only quantization scales of a sub-4-bit integer model, enabling memory-efficient adaptation without LoRA-style add-on weights.
- **Params**: <0.5% | **Open-source**: community

### BitFit: Simple Parameter-efficient Fine-tuning for Transformer-based Masked Language-models
- **Authors**: Elad Ben Zaken et al.
- **Venue**: ACL 2022
- **Paper**: [arXiv:2106.10199](https://arxiv.org/abs/2106.10199)
- **Code**: [benzakenelad/BitFit](https://github.com/benzakenelad/BitFit)
- **Idea**: Fine-tune only the bias terms of a pretrained Transformer, matching full fine-tuning on small-to-medium tasks.
- **Params**: 0.08%-0.1% | **Open-source**: official
