# New arXiv PEFT papers — 2026-07-20

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **11**.

## Candidates

### Model Merging for Medical LVLMs: A Benchmark and a Winner-Take-All Approach
- **Authors**: Lichao Mou, Shilan Zhang, Chunlei Li, Bingcong Yan, Jingliang Hu, Yilei Shi, Shengwu Xiong, Xiao Xiang Zhu, Lei Li, Yaxiong Chen
- **arXiv**: [2607.15661](http://arxiv.org/abs/2607.15661v1)
- **Published**: 2026-07-17
- **Categories**: cs.CV

> Large vision-language models (LVLMs) can be adapted to specialized medical imaging tasks via parameter-efficient fine-tuning approaches such as low-rank adaptation (LoRA), leading to a growing ecosystem of expert models tailored to specific imaging modalities and clinical scenarios. However, deployi...

### Long-Context Fine-Tuning with Limited VRAM
- **Authors**: Vladimir Fedosov, Aleksandr Sazhin, Artemiy Grinenko, Frank Woernle
- **arXiv**: [2607.15105](http://arxiv.org/abs/2607.15105v2)
- **Published**: 2026-07-16
- **Categories**: cs.AI

> Parameter-efficient fine-tuning reduces model and optimizer memory, but dense attention still makes long training sequences expensive. We combine Hierarchical Global Attention (HGA) with segment-wise backpropagation and tiered KV storage. Only the active segment remains differentiable in VRAM; older...

### MagicPrompt: Ultra-Lightweight Prompt Tuning for Video Generation
- **Authors**: Yinhan Zhang, Dinwei Tan, Xianghao Kong, Yue Ma, Yeying Jin, Anyi Rao
- **arXiv**: [2607.14595](http://arxiv.org/abs/2607.14595v1)
- **Published**: 2026-07-16
- **Categories**: cs.CV

> Large-scale video diffusion models (VDMs) deliver strong generation performance, but full fine-tuning for downstream tasks incurs prohibitive computational costs. Existing parameter-efficient fine-tuning (PEFT) methods have two critical flaws on billion-scale models: they still require substantial t...

### Non-vacuous Generalization Bounds for Reinforcement Learning with Verifiable Rewards
- **Authors**: Yuxuan Zhu, Rohan Alur, Daniel Kang
- **arXiv**: [2607.14506](http://arxiv.org/abs/2607.14506v1)
- **Published**: 2026-07-16
- **Categories**: cs.LG, cs.AI

> While reinforcement learning with verifiable rewards (RLVR) is widely used to improve the reasoning capabilities of large language models (LLMs), the generalizability of the resulting models remains poorly understood. In this work, we establish the first non-vacuous generalization bounds for paramet...

### Dysco: Dynamic Subspace Boosting to Mitigate LoRA Interference in Federated Learning
- **Authors**: Haobo Zhang, Jiankun Wang, Suraj Rajendran, Weishen Pan, Lam Tsoi, Yong Chen, Fei Wang, Jiayu Zhou
- **arXiv**: [2607.14367](http://arxiv.org/abs/2607.14367v1)
- **Published**: 2026-07-15
- **Categories**: cs.LG

> Federated fine-tuning of large pre-trained models increasingly relies on Low-Rank Adaptation (LoRA) to reduce communication and computation, but heterogeneous clients can make adapter aggregation unstable. We identify the data-parameter interference as a geometric source of this instability. This in...

### Constraint-Driven Model Optimization: An Industry Framework for Selecting Compression and Acceleration Techniques in Modern Machine Learning Systems
- **Authors**: Dhruv Shivkant, Saket Mohanty, Somya Rai, Utkarsh Wadhwa
- **arXiv**: [2607.13735](http://arxiv.org/abs/2607.13735v2)
- **Published**: 2026-07-15
- **Categories**: cs.LG

> The rapid deployment of machine learning systems across cloud, edge, and enterprise environments has brought model optimization to the forefront of systems-engineering. Despite a rich literature spanning quantization, pruning, knowledge distillation, parameter-efficient fine-tuning (PEFT), and infer...

### Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model
- **Authors**: Harsha Vardhan Khurdula, Abhinav Kumar Singh, Yoeven D Khemlani, Vineet Agarwal
- **arXiv**: [2607.13013](http://arxiv.org/abs/2607.13013v1)
- **Published**: 2026-07-14
- **Categories**: cs.AI, cs.SD

> Automatic speech recognition is dominated by autoregressive decoders that emit one token at a time. We ask whether a discrete diffusion language model can transcribe speech instead, refining a whole transcript in parallel over a small number of denoising steps. We train an audio-native interface for...

### MBTI: A Multi-Branch Efficient Fine-Tuning Framework for Hyperspectral Image Classification with Foundation Models
- **Authors**: Mingzhen Xu, Haonan Guo, Di Wang, Yinghua Qu, Zhiliang Zhou, Lei Zhang, Huiwen Yao, Rui Zhao, Fengxiang Wang, Gang Wan, Bo Du, Liangpei Zhang
- **arXiv**: [2607.12782](http://arxiv.org/abs/2607.12782v1)
- **Published**: 2026-07-14
- **Categories**: cs.CV

> Hyperspectral foundation models learn transferable spectral-spatial representations from large-scale unlabeled data. They provide an effective paradigm for adapting to downstream hyperspectral image (HSI) classification tasks with limited labeled samples. However, spectral band configurations vary s...

### An Empirical Analysis of Continual Learning for Heterogeneous Medical Visual Question Answering
- **Authors**: Mai A. Shaaban, Tausifa Jan Saleem, Alaa Mohamed, Dilnaz Utemissova, Ufaq Khan, Mohammad Yaqub
- **arXiv**: [2607.12048](http://arxiv.org/abs/2607.12048v1)
- **Published**: 2026-07-13
- **Categories**: cs.CV, cs.AI, cs.CL

> Deploying medical visual question answering (MedVQA) systems in real-world clinical settings requires models that adapt to new clinical tasks without forgetting previously acquired knowledge. Continual learning (CL) provides a practical framework for this setting. Despite rapid progress in medical v...

### LoRA-Based Cascaded Multimodal Fusion for Action Recognition in Medical Training Environments
- **Authors**: Divya Mereddy, Jeevan Beedareddy
- **arXiv**: [2607.11839](http://arxiv.org/abs/2607.11839v1)
- **Published**: 2026-07-13
- **Categories**: cs.CV, cs.AI

> This paper presents a cascaded Low-Rank Adaptation (LoRA)-based multimodal fusion framework for action and activity recognition in healthcare-oriented training environments. The proposed architecture combines parameter-efficient modality-specific adaptation with sequential fusion, enabling modalitie...

### Higher-Order Cell Tracking Transformer
- **Authors**: Jordão Bragantini, Ilan Theodoro, Loïc A. Royer
- **arXiv**: [2607.11754](http://arxiv.org/abs/2607.11754v1)
- **Published**: 2026-07-13
- **Categories**: cs.CV

> Reconstructing lineages from live-imaging microscopy requires linking cell detections across time, including through cell divisions. A common approach is to construct a candidate graph and associate cell segmentations (nodes) across frames. However, these and other existing methods overlook two stru...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "mou-2026",
    "title": "Model Merging for Medical LVLMs: A Benchmark and a Winner-Take-All Approach",
    "authors": [
      "Lichao Mou",
      "Shilan Zhang",
      "Chunlei Li",
      "Bingcong Yan",
      "Jingliang Hu",
      "Yilei Shi",
      "Shengwu Xiong",
      "Xiao Xiang Zhu",
      "Lei Li",
      "Yaxiong Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.15661",
    "paper_url": "https://arxiv.org/abs/2607.15661",
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
    "added_date": "2026-07-20"
  },
  {
    "id": "fedosov-2026",
    "title": "Long-Context Fine-Tuning with Limited VRAM",
    "authors": [
      "Vladimir Fedosov",
      "Aleksandr Sazhin",
      "Artemiy Grinenko",
      "Frank Woernle"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.15105",
    "paper_url": "https://arxiv.org/abs/2607.15105",
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
    "added_date": "2026-07-20"
  },
  {
    "id": "zhang-2026",
    "title": "MagicPrompt: Ultra-Lightweight Prompt Tuning for Video Generation",
    "authors": [
      "Yinhan Zhang",
      "Dinwei Tan",
      "Xianghao Kong",
      "Yue Ma",
      "Yeying Jin",
      "Anyi Rao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.14595",
    "paper_url": "https://arxiv.org/abs/2607.14595",
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
    "added_date": "2026-07-20"
  },
  {
    "id": "zhu-2026",
    "title": "Non-vacuous Generalization Bounds for Reinforcement Learning with Verifiable Rewards",
    "authors": [
      "Yuxuan Zhu",
      "Rohan Alur",
      "Daniel Kang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.14506",
    "paper_url": "https://arxiv.org/abs/2607.14506",
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
    "added_date": "2026-07-20"
  },
  {
    "id": "zhang-2026",
    "title": "Dysco: Dynamic Subspace Boosting to Mitigate LoRA Interference in Federated Learning",
    "authors": [
      "Haobo Zhang",
      "Jiankun Wang",
      "Suraj Rajendran",
      "Weishen Pan",
      "Lam Tsoi",
      "Yong Chen",
      "Fei Wang",
      "Jiayu Zhou"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.14367",
    "paper_url": "https://arxiv.org/abs/2607.14367",
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
    "added_date": "2026-07-20"
  },
  {
    "id": "shivkant-2026",
    "title": "Constraint-Driven Model Optimization: An Industry Framework for Selecting Compression and Acceleration Techniques in Modern Machine Learning Systems",
    "authors": [
      "Dhruv Shivkant",
      "Saket Mohanty",
      "Somya Rai",
      "Utkarsh Wadhwa"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.13735",
    "paper_url": "https://arxiv.org/abs/2607.13735",
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
    "added_date": "2026-07-20"
  },
  {
    "id": "khurdula-2026",
    "title": "Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model",
    "authors": [
      "Harsha Vardhan Khurdula",
      "Abhinav Kumar Singh",
      "Yoeven D Khemlani",
      "Vineet Agarwal"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.13013",
    "paper_url": "https://arxiv.org/abs/2607.13013",
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
    "added_date": "2026-07-20"
  },
  {
    "id": "xu-2026",
    "title": "MBTI: A Multi-Branch Efficient Fine-Tuning Framework for Hyperspectral Image Classification with Foundation Models",
    "authors": [
      "Mingzhen Xu",
      "Haonan Guo",
      "Di Wang",
      "Yinghua Qu",
      "Zhiliang Zhou",
      "Lei Zhang",
      "Huiwen Yao",
      "Rui Zhao",
      "Fengxiang Wang",
      "Gang Wan",
      "Bo Du",
      "Liangpei Zhang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.12782",
    "paper_url": "https://arxiv.org/abs/2607.12782",
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
    "added_date": "2026-07-20"
  },
  {
    "id": "shaaban-2026",
    "title": "An Empirical Analysis of Continual Learning for Heterogeneous Medical Visual Question Answering",
    "authors": [
      "Mai A. Shaaban",
      "Tausifa Jan Saleem",
      "Alaa Mohamed",
      "Dilnaz Utemissova",
      "Ufaq Khan",
      "Mohammad Yaqub"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.12048",
    "paper_url": "https://arxiv.org/abs/2607.12048",
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
    "added_date": "2026-07-20"
  },
  {
    "id": "mereddy-2026",
    "title": "LoRA-Based Cascaded Multimodal Fusion for Action Recognition in Medical Training Environments",
    "authors": [
      "Divya Mereddy",
      "Jeevan Beedareddy"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.11839",
    "paper_url": "https://arxiv.org/abs/2607.11839",
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
    "added_date": "2026-07-20"
  },
  {
    "id": "bragantini-2026",
    "title": "Higher-Order Cell Tracking Transformer",
    "authors": [
      "Jordão Bragantini",
      "Ilan Theodoro",
      "Loïc A. Royer"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.11754",
    "paper_url": "https://arxiv.org/abs/2607.11754",
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
    "added_date": "2026-07-20"
  }
]
```
