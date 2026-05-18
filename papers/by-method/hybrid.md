# Hybrid Methods

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_5 papers, sorted by year (desc)._

### LoRAMoE: Alleviating World Knowledge Forgetting in Large Language Models via MoE-Style Plugin
- **Authors**: Shihan Dou et al.
- **Venue**: ACL 2024
- **Paper**: [arXiv:2312.09979](https://arxiv.org/abs/2312.09979)
- **Code**: [Ablustrund/LoRAMoE](https://github.com/Ablustrund/LoRAMoE)
- **Idea**: Combine multiple LoRA experts with a router and localized balancing loss to prevent world-knowledge forgetting during instruction tuning.
- **Params**: varies | **Open-source**: official

### Higher Layers Need More LoRA Experts
- **Authors**: Chongyang Gao et al.
- **Venue**: arXiv 2024
- **Paper**: [arXiv:2402.08562](https://arxiv.org/abs/2402.08562)
- **Code**: [GCYZSL/MoLA](https://github.com/GCYZSL/MoLA)
- **Idea**: Allocate more LoRA experts to higher Transformer layers where representations specialize, improving layer-aware MoE-LoRA performance.
- **Params**: varies | **Open-source**: official

### Mixture of LoRA Experts
- **Authors**: Xun Wu et al.
- **Venue**: ICLR 2024
- **Paper**: [arXiv:2404.13628](https://arxiv.org/abs/2404.13628)
- **Idea**: Hierarchically compose multiple trained LoRA experts via a learnable gating function, enabling flexible specialization without retraining.
- **Params**: varies | **Open-source**: community

### X-LoRA: Mixture of Low-Rank Adapter Experts, a Flexible Framework for Large Language Models with Applications in Protein Mechanics and Molecular Design
- **Authors**: Eric L. Buehler et al.
- **Venue**: arXiv 2024
- **Paper**: [arXiv:2402.07148](https://arxiv.org/abs/2402.07148)
- **Code**: [EricLBuehler/xlora](https://github.com/EricLBuehler/xlora)
- **Idea**: Dynamically mix pretrained LoRA adapters per token and layer via a learned gating network, adding no parameters per expert.
- **Params**: varies | **Open-source**: official

### Towards a Unified View of Parameter-Efficient Transfer Learning
- **Authors**: Junxian He et al.
- **Venue**: ICLR 2022
- **Paper**: [arXiv:2110.04366](https://arxiv.org/abs/2110.04366)
- **Code**: [jxhe/unify-parameter-efficient-tuning](https://github.com/jxhe/unify-parameter-efficient-tuning)
- **Idea**: Cast adapters, prefix tuning, and LoRA as instances of one design space, yielding the MAM Adapter hybrid.
- **Params**: varies | **Open-source**: official
