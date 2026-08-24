# New arXiv PEFT papers — 2026-08-24

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **9**.

## Candidates

### CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment
- **Authors**: Chengxiao Wang, Enyi Jiang, Xiaojing Liao, Sanmi Koyejo
- **arXiv**: [2608.21278](http://arxiv.org/abs/2608.21278v1)
- **Published**: 2026-08-21
- **Categories**: cs.AI

> Improving the safety of large language models (LLMs) often comes at the expense of utility, as globally applied safety tuning may affect model responses to both harmful and benign inputs. We propose \textbf{C}ontinuous \textbf{L}at\textbf{E}nt \textbf{A}dapter \textbf{R}outing (CLEAR), a conditional...

### Thermo-FL: Thermal-Aware Robust Federated Fine-Tuning of Large Language Models for Edge AI
- **Authors**: Shiva Shrestha, Kazi Shaharair Sharif, Zongxing Xie, Jiajing Huang, Anhao Xiang, Honghui Xu
- **arXiv**: [2608.21172](http://arxiv.org/abs/2608.21172v1)
- **Published**: 2026-08-21
- **Categories**: cs.LG, cs.DC

> Federated fine-tuning enables large language models to adapt on edge devices without centralizing private data, but practical deployments must address hardware instability and adversarial update corruption together. Thermally constrained clients may throttle, slow local training, or delay synchronou...

### What You Can't See Is What You Learn: Restricted Evidence Visibility Favors Compositional Generalization in Shared-Genome Language-Model Societies
- **Authors**: Narcis Marincat
- **arXiv**: [2608.20054](http://arxiv.org/abs/2608.20054v1)
- **Published**: 2026-08-20
- **Categories**: cs.AI, cs.LG, cs.MA

> Multi-module systems often expose every module to the full input. We test whether restricting evidence visibility changes which solutions gradient-based training discovers. Four-cell societies share one frozen pretrained language model and one low-rank adapter, communicating only through two model-w...

### LoRA-GA$^2$: Low Rank Adaptation with Multi-step Gradient Adaptive Alignment
- **Authors**: Haonan He, Xinyue Fan
- **arXiv**: [2608.19800](http://arxiv.org/abs/2608.19800v1)
- **Published**: 2026-08-20
- **Categories**: cs.CL, cs.AI

> Low-Rank Adaptation (LoRA) is a prominent fine-tuning method for large models, achieving competitive performance with reduced memory overhead. However, a persistent performance gap remains between LoRA and full fine-tuning. Recent studies have sought to narrow this gap by employing one-step gradient...

### Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation
- **Authors**: Tatsuya Amano, Hirozumi Yamaguchi
- **arXiv**: [2608.19778](http://arxiv.org/abs/2608.19778v1)
- **Published**: 2026-08-20
- **Categories**: cs.MA, cs.AI

> Pedestrian simulators need a behaviour rule for every agent, but privacy usually limits the data for setting one to aggregate statistics, namely zone-level device counts and origin-to-destination (OD) flows, with no individual trajectories. Such aggregates under-determine individual behaviour, becau...

### Frequency-Aware Continual Learning for Smart Contract Vulnerability Detection with Large Language Models
- **Authors**: Tenghui Huang, Jiawen Kang, Dongning Liu, Changyan Yi, Chengjun Cai, Anjia Yang, Li Li, Dong In Kim
- **arXiv**: [2608.19680](http://arxiv.org/abs/2608.19680v1)
- **Published**: 2026-08-20
- **Categories**: cs.AI

> Smart contract vulnerability detection with Large Language Models (LLMs) faces three causally linked challenges. First, new vulnerability categories demand parameter-efficient adaptation, since full retraining is prohibitive for sequentially arriving tasks. Second, training per-task adapters on a sh...

### A Few Cases Are All You Need: An Empirical Study of Annotation-Efficient LoRA Fine-Tuning of MedSAM3
- **Authors**: Sachin Dudda Nagaraju, Bendik Skarre Abrahamsen, Ashkan Moradi, Mattijs Elschot
- **arXiv**: [2608.18731](http://arxiv.org/abs/2608.18731v1)
- **Published**: 2026-08-19
- **Categories**: cs.CV, cs.AI

> Medical image segmentation is essential for clinical workflows such as treatment planning and disease assessment. While specialist tools like TotalSegmentator and MRSegmentator achieve strong performance, they require large annotated datasets for training. Medical foundation models offer a promising...

### Vision-Language Models for Analog Gauge Reading: An Empirical Study of Specialization, Transfer and Reliability
- **Authors**: Abdul Mueez, Aaditya Baranwal, Junior Chaj-Mejia, Guneet Bhatia, Jason T. Voelker, Shruti Vyas
- **arXiv**: [2608.17723](http://arxiv.org/abs/2608.17723v1)
- **Published**: 2026-08-18
- **Categories**: cs.CV

> Analog gauges remain common in industrial environments where manual inspection is costly or hazardous. The engineering application addressed here is direct numerical reading of single-target analog-gauge images, while the artificial-intelligence contribution is a systematic evaluation of specializat...

### Self-Routed Tensor Adapters for Parameter-Efficient Universal Visual Adaptation
- **Authors**: Suraj Yadav
- **arXiv**: [2608.16384](http://arxiv.org/abs/2608.16384v1)
- **Published**: 2026-08-17
- **Categories**: cs.CV, cs.LG

> Universal visual representations require adaptation mechanisms that adapt across heterogeneous domains without fragmenting knowledge into domain-specific modules. Parameter-efficient fine-tuning adapts frozen visual foundation models efficiently, but standard low-rank adapters use a fixed subspace f...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "wang-2026",
    "title": "CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment",
    "authors": [
      "Chengxiao Wang",
      "Enyi Jiang",
      "Xiaojing Liao",
      "Sanmi Koyejo"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.21278",
    "paper_url": "https://arxiv.org/abs/2608.21278",
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
    "added_date": "2026-08-24"
  },
  {
    "id": "shrestha-2026",
    "title": "Thermo-FL: Thermal-Aware Robust Federated Fine-Tuning of Large Language Models for Edge AI",
    "authors": [
      "Shiva Shrestha",
      "Kazi Shaharair Sharif",
      "Zongxing Xie",
      "Jiajing Huang",
      "Anhao Xiang",
      "Honghui Xu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.21172",
    "paper_url": "https://arxiv.org/abs/2608.21172",
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
    "added_date": "2026-08-24"
  },
  {
    "id": "marincat-2026",
    "title": "What You Can't See Is What You Learn: Restricted Evidence Visibility Favors Compositional Generalization in Shared-Genome Language-Model Societies",
    "authors": [
      "Narcis Marincat"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.20054",
    "paper_url": "https://arxiv.org/abs/2608.20054",
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
    "added_date": "2026-08-24"
  },
  {
    "id": "he-2026",
    "title": "LoRA-GA$^2$: Low Rank Adaptation with Multi-step Gradient Adaptive Alignment",
    "authors": [
      "Haonan He",
      "Xinyue Fan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.19800",
    "paper_url": "https://arxiv.org/abs/2608.19800",
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
    "added_date": "2026-08-24"
  },
  {
    "id": "amano-2026",
    "title": "Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation",
    "authors": [
      "Tatsuya Amano",
      "Hirozumi Yamaguchi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.19778",
    "paper_url": "https://arxiv.org/abs/2608.19778",
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
    "added_date": "2026-08-24"
  },
  {
    "id": "huang-2026",
    "title": "Frequency-Aware Continual Learning for Smart Contract Vulnerability Detection with Large Language Models",
    "authors": [
      "Tenghui Huang",
      "Jiawen Kang",
      "Dongning Liu",
      "Changyan Yi",
      "Chengjun Cai",
      "Anjia Yang",
      "Li Li",
      "Dong In Kim"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.19680",
    "paper_url": "https://arxiv.org/abs/2608.19680",
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
    "added_date": "2026-08-24"
  },
  {
    "id": "nagaraju-2026",
    "title": "A Few Cases Are All You Need: An Empirical Study of Annotation-Efficient LoRA Fine-Tuning of MedSAM3",
    "authors": [
      "Sachin Dudda Nagaraju",
      "Bendik Skarre Abrahamsen",
      "Ashkan Moradi",
      "Mattijs Elschot"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.18731",
    "paper_url": "https://arxiv.org/abs/2608.18731",
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
    "added_date": "2026-08-24"
  },
  {
    "id": "mueez-2026",
    "title": "Vision-Language Models for Analog Gauge Reading: An Empirical Study of Specialization, Transfer and Reliability",
    "authors": [
      "Abdul Mueez",
      "Aaditya Baranwal",
      "Junior Chaj-Mejia",
      "Guneet Bhatia",
      "Jason T. Voelker",
      "Shruti Vyas"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.17723",
    "paper_url": "https://arxiv.org/abs/2608.17723",
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
    "added_date": "2026-08-24"
  },
  {
    "id": "yadav-2026",
    "title": "Self-Routed Tensor Adapters for Parameter-Efficient Universal Visual Adaptation",
    "authors": [
      "Suraj Yadav"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.16384",
    "paper_url": "https://arxiv.org/abs/2608.16384",
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
    "added_date": "2026-08-24"
  }
]
```
