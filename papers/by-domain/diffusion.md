# Diffusion PEFT

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_5 papers, sorted by year (desc)._

### Concept Sliders: LoRA Adaptors for Precise Control in Diffusion Models
- **Authors**: Rohit Gandikota et al.
- **Venue**: ECCV 2024
- **Paper**: [arXiv:2311.12092](https://arxiv.org/abs/2311.12092)
- **Code**: [rohitgandikota/sliders](https://github.com/rohitgandikota/sliders)
- **Idea**: Train low-rank LoRA adaptors as semantic sliders, enabling continuous control over specific image attributes in diffusion models.
- **Params**: <1% | **Open-source**: official

### Multi-Concept Customization of Text-to-Image Diffusion
- **Authors**: Nupur Kumari et al.
- **Venue**: CVPR 2023
- **Paper**: [arXiv:2212.04488](https://arxiv.org/abs/2212.04488)
- **Code**: [adobe-research/custom-diffusion](https://github.com/adobe-research/custom-diffusion)
- **Idea**: Customize text-to-image diffusion by fine-tuning only cross-attention key/value projections, enabling multi-concept composition.
- **Params**: ~3% | **Open-source**: official

### Controlling Text-to-Image Diffusion by Orthogonal Finetuning
- **Authors**: Zeju Qiu et al.
- **Venue**: NeurIPS 2023
- **Paper**: [arXiv:2306.07280](https://arxiv.org/abs/2306.07280)
- **Code**: [Zeju1997/oft](https://github.com/Zeju1997/oft)
- **Idea**: Reparameterize fine-tuning as a learned orthogonal transformation of pretrained weights, preserving hyperspherical energy during adaptation.
- **Params**: varies | **Open-source**: official

### SVDiff: Compact Parameter Space for Diffusion Fine-Tuning
- **Authors**: Ligong Han et al.
- **Venue**: ICCV 2023
- **Paper**: [arXiv:2303.11305](https://arxiv.org/abs/2303.11305)
- **Idea**: Fine-tune only singular values of pretrained weight matrices via SVD, yielding compact and composable diffusion personalizations.
- **Params**: ~0.05% | **Open-source**: community

### An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion
- **Authors**: Rinon Gal et al.
- **Venue**: ICLR 2023
- **Paper**: [arXiv:2208.01618](https://arxiv.org/abs/2208.01618)
- **Code**: [rinongal/textual_inversion](https://github.com/rinongal/textual_inversion)
- **Idea**: Learn a new pseudo-word embedding in the text encoder to capture a visual concept from a few images without retraining the diffusion model.
- **Params**: <0.001% | **Open-source**: official
