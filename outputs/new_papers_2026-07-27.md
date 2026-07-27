# New arXiv PEFT papers — 2026-07-27

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **9**.

## Candidates

### IFCLoRA: Topology-Aware Rank Allocation for Parameter-Efficient Fine-Tuning
- **Authors**: Wei Zhang, Xinwu Liu, Yihang Cheng
- **arXiv**: [2607.22251](http://arxiv.org/abs/2607.22251v1)
- **Published**: 2026-07-24
- **Categories**: cs.LG, cs.AI

> Low-Rank Adaptation (LoRA) is a widely used parameter-efficient fine-tuning method for large language models, but its performance depends strongly on how a fixed rank budget is distributed across Transformer modules. Existing adaptive-rank methods usually rely on local gradient statistics collected ...

### MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation
- **Authors**: Qingyu Yang, Haonan He, Minglei Li, Jingqi Ye, Tao Chen, Lei Bai, Peng Ye
- **arXiv**: [2607.21978](http://arxiv.org/abs/2607.21978v1)
- **Published**: 2026-07-24
- **Categories**: cs.CL

> Mixture-of-Experts (MoE) architectures have been widely adopted in large language models, yet parameter-efficient fine-tuning (PEFT) for MoE models remains underexplored. Existing PEFT methods for MoE either ignore router priors with uniform adapters, reducing efficiency and risking forgetting, or r...

### How Many Bits Can an Adapter Write? Measuring the Capacity and Memorization of Parameter-Efficient Fine-Tuning
- **Authors**: Kaizhen Tan, Heqing Du, Yang Feng
- **arXiv**: [2607.21351](http://arxiv.org/abs/2607.21351v1)
- **Published**: 2026-07-23
- **Categories**: cs.LG

> A LoRA adapter is a few megabytes that almost everyone treats as a skill rather than a record of the data behind it. We put that assumption on a scale. Extending compression-based memorization analysis to the frozen-base setting, we measure directly, in bits, how much a low-rank adapter writes into ...

### Three-Pronged Spectral Control for Federated Parameter Efficient Fine Tuning
- **Authors**: Shiva Raj Pokhrel, Dipsan Bhattarai, Anwar Walid
- **arXiv**: [2607.20914](http://arxiv.org/abs/2607.20914v1)
- **Published**: 2026-07-23
- **Categories**: cs.LG, cs.NI

> Federated parameter-efficient fine-tuning (PEFT) enables communication-efficient adaptation of large pretrained models on decentralized edge data, but it remains fragile under non-IID client heterogeneity. In low-rank adaptation (LoRA), different clients may learn locally useful but spectrally misal...

### Source-Prior-Driven Selective Adaptation for Efficient Diffusion Model Finetuning
- **Authors**: Yi Xiong, Yuan-Yuan Cheng, Xiao-Ming Fu
- **arXiv**: [2607.20913](http://arxiv.org/abs/2607.20913v1)
- **Published**: 2026-07-23
- **Categories**: cs.AI

> Fine-tuning large diffusion models for new domains or styles involves a trade-off: improving target-specific generation often degrades the pretrained model's broad generative capability. Existing full and parameter-efficient fine-tuning methods typically handle this trade-off only implicitly. In thi...

### The Blessing of Dimensionality: How Near-Orthogonality in High-Dimensional Spaces Explains Temporal Portability
- **Authors**: Abigail Woodring, Adrian Chan, Rana Muhammad Shahroz Khan, Sukwon Yun, Chau-Wai Wong, Tianlong Chen
- **arXiv**: [2607.20301](http://arxiv.org/abs/2607.20301v1)
- **Published**: 2026-07-22
- **Categories**: cs.LG, cs.CL

> Fine-tuning has been widely used to adapt large language models (LLMs) for domain-specific tasks. Parameter efficient fine-tuning (PEFT) methods such as low-rank adaptation (LoRA) are frequently used to reduce computational costs. PortLLM is a training-free and data-free scheme used to adapt LLMs af...

### Statistical Inference for Rank Allocation in Low-Rank Adaptation
- **Authors**: Yihang Gao, Vincent Y. F. Tan
- **arXiv**: [2607.20205](http://arxiv.org/abs/2607.20205v1)
- **Published**: 2026-07-22
- **Categories**: stat.ML, cs.LG, math.ST

> Low-rank adaptation (LoRA) has become a widely used parameter-efficient fine-tuning method for large language models. Since different modules and layers may contribute unequally to downstream adaptation, allocating rank resources under a fixed parameter budget is an important problem for balancing e...

### A Dual-Hypothesis Reasoning Framework for LLM Guardrails
- **Authors**: Md Asiful Islam, Mihai Surdeanu
- **arXiv**: [2607.17575](http://arxiv.org/abs/2607.17575v1)
- **Published**: 2026-07-20
- **Categories**: cs.AI

> We propose ARBITER, a novel LLM guardrail framework that introduces two key ideas: (i) dual-hypothesis reasoning, a reasoning method for LLM guardrails that explicitly considers both safe and unsafe interpretations of a prompt before making a safety decision, and (ii) multi-component supervised fine...

### Opto-ViT-v2: Noise-Resilient On-Chip Fine-Tuning for Photonic Near-Sensor Vision Transformer Accelerators
- **Authors**: Xuming Chen, Deniz Najafi, Mehrdad Morsali, Chengwei Zhou, Zahra Ghanaatianjobzari, Mahdi Nikdast, Shaahin Angizi, Gourav Datta
- **arXiv**: [2607.19421](http://arxiv.org/abs/2607.19421v1)
- **Published**: 2026-07-20
- **Categories**: cs.AR, cs.AI

> Silicon-photonic (SiPh) accelerators have emerged as a promising platform for Vision Transformer (ViT) inference by performing matrix multiplications on microring-resonator (MRR) banks with high throughput and energy efficiency. Extending these platforms to support on-chip fine-tuning remains challe...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "zhang-2026",
    "title": "IFCLoRA: Topology-Aware Rank Allocation for Parameter-Efficient Fine-Tuning",
    "authors": [
      "Wei Zhang",
      "Xinwu Liu",
      "Yihang Cheng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.22251",
    "paper_url": "https://arxiv.org/abs/2607.22251",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-07-27"
  },
  {
    "id": "yang-2026",
    "title": "MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation",
    "authors": [
      "Qingyu Yang",
      "Haonan He",
      "Minglei Li",
      "Jingqi Ye",
      "Tao Chen",
      "Lei Bai",
      "Peng Ye"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.21978",
    "paper_url": "https://arxiv.org/abs/2607.21978",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-07-27"
  },
  {
    "id": "tan-2026",
    "title": "How Many Bits Can an Adapter Write? Measuring the Capacity and Memorization of Parameter-Efficient Fine-Tuning",
    "authors": [
      "Kaizhen Tan",
      "Heqing Du",
      "Yang Feng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.21351",
    "paper_url": "https://arxiv.org/abs/2607.21351",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-07-27"
  },
  {
    "id": "pokhrel-2026",
    "title": "Three-Pronged Spectral Control for Federated Parameter Efficient Fine Tuning",
    "authors": [
      "Shiva Raj Pokhrel",
      "Dipsan Bhattarai",
      "Anwar Walid"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.20914",
    "paper_url": "https://arxiv.org/abs/2607.20914",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-07-27"
  },
  {
    "id": "xiong-2026",
    "title": "Source-Prior-Driven Selective Adaptation for Efficient Diffusion Model Finetuning",
    "authors": [
      "Yi Xiong",
      "Yuan-Yuan Cheng",
      "Xiao-Ming Fu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.20913",
    "paper_url": "https://arxiv.org/abs/2607.20913",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-07-27"
  },
  {
    "id": "woodring-2026",
    "title": "The Blessing of Dimensionality: How Near-Orthogonality in High-Dimensional Spaces Explains Temporal Portability",
    "authors": [
      "Abigail Woodring",
      "Adrian Chan",
      "Rana Muhammad Shahroz Khan",
      "Sukwon Yun",
      "Chau-Wai Wong",
      "Tianlong Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.20301",
    "paper_url": "https://arxiv.org/abs/2607.20301",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-07-27"
  },
  {
    "id": "gao-2026",
    "title": "Statistical Inference for Rank Allocation in Low-Rank Adaptation",
    "authors": [
      "Yihang Gao",
      "Vincent Y. F. Tan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.20205",
    "paper_url": "https://arxiv.org/abs/2607.20205",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-07-27"
  },
  {
    "id": "islam-2026",
    "title": "A Dual-Hypothesis Reasoning Framework for LLM Guardrails",
    "authors": [
      "Md Asiful Islam",
      "Mihai Surdeanu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.17575",
    "paper_url": "https://arxiv.org/abs/2607.17575",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-07-27"
  },
  {
    "id": "chen-2026",
    "title": "Opto-ViT-v2: Noise-Resilient On-Chip Fine-Tuning for Photonic Near-Sensor Vision Transformer Accelerators",
    "authors": [
      "Xuming Chen",
      "Deniz Najafi",
      "Mehrdad Morsali",
      "Chengwei Zhou",
      "Zahra Ghanaatianjobzari",
      "Mahdi Nikdast",
      "Shaahin Angizi",
      "Gourav Datta"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.19421",
    "paper_url": "https://arxiv.org/abs/2607.19421",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-07-27"
  }
]
```
