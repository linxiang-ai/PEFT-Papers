# ACL papers

> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually.

_4 papers, sorted by year (desc)._

### LoRAMoE: Alleviating World Knowledge Forgetting in Large Language Models via MoE-Style Plugin
- **Authors**: Shihan Dou et al.
- **Venue**: ACL 2024
- **Paper**: [arXiv:2312.09979](https://arxiv.org/abs/2312.09979)
- **Code**: [Ablustrund/LoRAMoE](https://github.com/Ablustrund/LoRAMoE)
- **Idea**: Combine multiple LoRA experts with a router and localized balancing loss to prevent world-knowledge forgetting during instruction tuning.
- **Params**: varies | **Open-source**: official

### BitFit: Simple Parameter-efficient Fine-tuning for Transformer-based Masked Language-models
- **Authors**: Elad Ben Zaken et al.
- **Venue**: ACL 2022
- **Paper**: [arXiv:2106.10199](https://arxiv.org/abs/2106.10199)
- **Code**: [benzakenelad/BitFit](https://github.com/benzakenelad/BitFit)
- **Idea**: Fine-tune only the bias terms of a pretrained Transformer, matching full fine-tuning on small-to-medium tasks.
- **Params**: 0.08%-0.1% | **Open-source**: official

### P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks
- **Authors**: Xiao Liu et al.
- **Venue**: ACL 2022
- **Paper**: [arXiv:2110.07602](https://arxiv.org/abs/2110.07602)
- **Code**: [THUDM/P-tuning-v2](https://github.com/THUDM/P-tuning-v2)
- **Idea**: Apply deep prompt tuning at every layer so prompt tuning stays competitive across model scales and sequence labelling tasks.
- **Params**: 0.1%-3% | **Open-source**: official

### Prefix-Tuning: Optimizing Continuous Prompts for Generation
- **Authors**: Xiang Lisa Li et al.
- **Venue**: ACL 2021
- **Paper**: [arXiv:2101.00190](https://arxiv.org/abs/2101.00190)
- **Code**: [XiangLi1999/PrefixTuning](https://github.com/XiangLi1999/PrefixTuning)
- **Idea**: Prepend trainable continuous prefix vectors to every Transformer layer while keeping the language model frozen.
- **Params**: 0.1% | **Open-source**: official
