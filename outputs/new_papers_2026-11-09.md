# New arXiv PEFT papers — 2026-11-09

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **29**.

## Candidates

### Breaking the Privacy Promise: Gradient Inversion Attacks on Federated Low-Rank Adapted Vision Transformers
- **Authors**: Ritik K. Badiya, Siladittya Manna, Ashmit Sinha, M Yashwanth, Anirban Chakraborty
- **arXiv**: [2611.09652](http://arxiv.org/abs/2611.09652v1)
- **Published**: 2026-11-06
- **Categories**: cs.CV, cs.AI, cs.CR, cs.DC, cs.LG

> Parameter-efficient fine-tuning (PEFT) has been increasingly adopted to fine-tune pretrained models with low computational cost and is therefore also preferred in the federated learning paradigm to reduce computational and communication overhead. In this work, we investigate the sparsely explored pr...

### Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters
- **Authors**: Constantinos Karouzos, Nikolaos Aletras
- **arXiv**: [2611.09634](http://arxiv.org/abs/2611.09634v1)
- **Published**: 2026-11-06
- **Categories**: cs.CL, cs.AI, cs.LG

> Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a prefere...

### From LoRA to Language: Recovering Skill Documents from Adapters
- **Authors**: Saranya Dintakurthy Swadha, Pavan C Shekar, Arpit Jain, Aswanth Krishnan
- **arXiv**: [2611.09454](http://arxiv.org/abs/2611.09454v1)
- **Published**: 2026-11-06
- **Categories**: cs.LG, cs.AI, cs.CL

> Agent skills are short documents that teach a language model how to handle a class of tasks. To save context, these documents are increasingly compiled into low-rank adapters (LoRA), which keep the behaviour but lose the text: an adapter is hard to read, edit, audit or move to another model. We ask ...

### Turkish Multimodal Video Fact-Checking: A New Dataset and a Comparison of Zero-Shot Agentic and Fine-Tuned Systems
- **Authors**: Azra Açıl
- **arXiv**: [2611.08651](http://arxiv.org/abs/2611.08651v1)
- **Published**: 2026-11-05
- **Categories**: cs.CV, cs.CL

> Video-based misinformation spreads rapidly on social media, but almost all existing fact-checking systems focus exclusively on English text. Tools for low-resource languages such as Turkish are severely limited. In this work, we present TeViD (Turkish Video Fact-checking Dataset), to the best of our...

### Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning
- **Authors**: Chenruo Liu, Zihan Wang, Yijun Dong, Qi Lei
- **arXiv**: [2611.08414](http://arxiv.org/abs/2611.08414v1)
- **Published**: 2026-11-05
- **Categories**: cs.LG, stat.ML

> Low-rank adaptation (LoRA) is commonly used in both supervised fine-tuning (SFT) and reinforcement learning (RL), often under similar optimizer settings. Yet, how the different dynamics of the two stages manifest in the low-rank increment that LoRA optimizes remains unclear. Tracking the singular sp...

### Towards Label-Efficient Geospatial Foundation Model Adaptation via Positive-Unlabeled Learning for Building Damage Mapping
- **Authors**: Hengwei Zhao, Qirui Wang, Zhuo Zheng, Xiaoyan Lu, Rusty Feagin, Wenzhe Jiao
- **arXiv**: [2611.08561](http://arxiv.org/abs/2611.08561v1)
- **Published**: 2026-11-05
- **Categories**: cs.CV, cs.AI

> Geospatial foundation models (GFMs) are reshaping remote sensing by shifting the field from task-specific modeling toward general-purpose geospatial intelligence. Mapping the damage to buildings stands to benefit substantially from this shift, as GFMs pretrained on large-scale Earth observation data...

### Automated Video-to-QA Pipeline: End-to-End Question Generation and Verification Using Large Language Models
- **Authors**: Jaival Chauhan, Vikram Singh, Pruthwik Mishra
- **arXiv**: [2611.07755](http://arxiv.org/abs/2611.07755v1)
- **Published**: 2026-11-05
- **Categories**: cs.CL

> The exponential growth of educational and informational video content on platforms like YouTube presents a challenge for efficient knowledge retrieval and assessment. This paper proposes an end-to-end automated pipeline for extracting structured summaries and generating high-fidelity Question-Answer...

### Embedding-Space Fingerprinting of LoRA Fine-Tunes: Recovering the Training-Data Domain from the Model Artifact Alone
- **Authors**: Shivesh Rane
- **arXiv**: [2611.07610](http://arxiv.org/abs/2611.07610v1)
- **Published**: 2026-11-05
- **Categories**: cs.AI, cs.CL, cs.LG

> When a base language model is fine-tuned with Low-Rank Adaptation (LoRA), how much of the training data domain leaks into the resulting artifact? This paper studies whether a simple classifier can recover the domain of a fine-tune given only the model artifact (weight deltas, internal activations on...

### Align Before Aggregation: Basis-Consistent Federated LoRA under Heterogeneous Ranks
- **Authors**: Pengpeng Qiao, Yang Cao, Lingling Zhang, Guo Cheng, Junwei Chen, Manjiang Yu, Wei Yang Bryan Lim, Masatoshi Yoshikawa
- **arXiv**: [2611.07598](http://arxiv.org/abs/2611.07598v1)
- **Published**: 2026-11-05
- **Categories**: cs.AI

> Federated fine-tuning of large language models (LLMs) under heterogeneous client capacities is increasingly important, and low-rank adaptation (LoRA) with heterogeneous ranks makes it practical. Existing server-side aggregators compose local matrix updates $ΔW_i$ from client-specific LoRA factors $(...

### From What Is Used to What Is Missing: Rethinking Dynamic Rank in LoRA
- **Authors**: Peng Xue, Guodong Fan, Guang-Yong Chen, Xing Chen
- **arXiv**: [2611.07349](http://arxiv.org/abs/2611.07349v1)
- **Published**: 2026-11-05
- **Categories**: math.OC, cs.LG

> Parameter-efficient fine-tuning with LoRA is governed by rank, which controls parameter budget and locally accessible task updates. Existing dynamic-rank methods mainly focus on capacity allocation, leaving unresolved whether the current adaptation space is sufficient for the task. We characterize t...

### The Behavioral Rate of Fine-Tuning: Compression as a Measure of Useful Information
- **Authors**: Joey David, Paul Caillon, Alexandre Allauzen
- **arXiv**: [2611.06598](http://arxiv.org/abs/2611.06598v1)
- **Published**: 2026-11-04
- **Categories**: cs.LG

> Low-Rank Adaptation (LoRA) adapts a frozen language model through a compact learned update, making it a natural setting for asking how much information fine-tuning needs to write. Yet adapter rank, parameter count, or numerical reconstruction error do not directly tell us how many bits are required ...

### Zuse: A Decision Model for European Languages
- **Authors**: Umair Mehmood Imam
- **arXiv**: [2611.06238](http://arxiv.org/abs/2611.06238v1)
- **Published**: 2026-11-04
- **Categories**: cs.CL, cs.LG

> Decision models read a document and return a probability for each of a fixed set of options instead of generating text. Several appeared in 2026, but none has published results outside English. We describe Zuse, three decision models (4B, 9B and 27B) that train a low-rank adapter and a pointer head ...

### ReTailor: A Residual Feature Tailoring Framework for Real-Time Cross-Sensor Pansharpening Adaptation
- **Authors**: Jing-Ze Liang, Wei-Jie Xiao, Zi-Han Cao, Yang-Dong Li, Tian-Yi Hu, Liang-Jian Deng
- **arXiv**: [2611.05811](http://arxiv.org/abs/2611.05811v1)
- **Published**: 2026-11-04
- **Categories**: cs.CV

> Recent pansharpening models achieve strong fusion performance on trained sensors, yet often generalize poorly to unseen sensors. Existing cross-sensor adaptation is limited by target-sensor retraining, which requires target-sensor training pairs and a dedicated training stage, and by per-image zero-...

### Distinguishing Initial-Condition and Model Error Using Machine-Learning Weather Models
- **Authors**: P. Trent Vonich, Gregory J. Hakim
- **arXiv**: [2611.05592](http://arxiv.org/abs/2611.05592v2)
- **Published**: 2026-11-03
- **Categories**: physics.ao-ph, cs.LG

> Differentiable weather models allow atmospheric initial conditions to be directly optimized to shadow a known trajectory, which we take from a reanalysis dataset. Here, we extend this optimization to include the forecast model, GraphCast, using low-rank adaptation (LoRA). We compare model optimizati...

### Modulating Merging Strengths via Joint Loss Estimation for LoRA-based Continual Learning
- **Authors**: Kun Gu, De Cheng, Zhipeng Xu, Lingfeng He, Di Xu, Nannan Wang
- **arXiv**: [2611.04931](http://arxiv.org/abs/2611.04931v1)
- **Published**: 2026-11-03
- **Categories**: cs.LG

> Continual learning (CL) aims to adapt models to new tasks while preserving previously learned knowledge. Recently, Low-Rank Adaptation (LoRA), a representative Parameter-Efficient Fine-Tuning (PEFT) method, has gained increasing attention in CL due to its efficiency and scalability. Several LoRA-bas...

### SaMA: Morpho Adaptation via Asymmetric Expansion of Kronecker Product
- **Authors**: An Nguyen, Anh Tong
- **arXiv**: [2611.04462](http://arxiv.org/abs/2611.04462v1)
- **Published**: 2026-11-03
- **Categories**: cs.LG, cs.AI

> Low-rank adaptation (LoRA) has attracted significant attention in the parameter-efficient fine-tuning (PEFT) landscape. However, its design suffers from two fundamental limitations. First, its invariance manifold induces flat directions in the loss landscape, creating an optimization bottleneck for ...

### Sketchpad: certified exact arithmetic with a small vision-language model
- **Authors**: Mostafa 'Neo' Mohsenvand
- **arXiv**: [2611.04434](http://arxiv.org/abs/2611.04434v1)
- **Published**: 2026-11-03
- **Categories**: cs.LG, cs.CL, cs.LO

> Language models are accurate on most long-arithmetic problems, but their accuracy is estimated on samples and carries no guarantee for an unseen input; tool use is exact but moves the computation outside the network. We show that exactness at all input lengths becomes a finite, checkable property of...

### RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training
- **Authors**: Shresth Grover, Andrey Kolobov, Dhruv Shah
- **arXiv**: [2611.04368](http://arxiv.org/abs/2611.04368v1)
- **Published**: 2026-11-03
- **Categories**: cs.RO, cs.CV

> Adapting a generalist vision-language-action (VLA) policy to a target task with limited demonstrations can improve nominal task success while reducing robustness to variations in appearance, objects, and instructions. We introduce reasoning-aligned fine-tuning (RAFT), a two-stage post-training proce...

### Beyond Fine-Tuning: Evaluating Prompt Engineering and Prompt Tuning for Roman Urdu Hate Speech Detection
- **Authors**: Toneema Zubair, Muhammad Junaid Asif, Faisal Kamiran, Hafiz Hassan Saeed, Rana Fayyaz Ahmad
- **arXiv**: [2611.04342](http://arxiv.org/abs/2611.04342v1)
- **Published**: 2026-11-03
- **Categories**: cs.AI

> Low Resource Languages (LRLs) pose significant challenges for hate speech detection because of a scarcity of readily available annotated data, language variation, non-standard spelling, and context-dependent ambiguity. Beyond the problem of informal conventions of writing in Roman Urdu, there is als...

### LIRA: A More Interpretable Dynamic Loss-Informed Rank Allocation for Low-Rank Adaptation
- **Authors**: Sihao Wang, Bozheng Li, Xuemiao Xu, Haoxin Yang, Yujie Xu, Jie Tang
- **arXiv**: [2611.04239](http://arxiv.org/abs/2611.04239v1)
- **Published**: 2026-11-03
- **Categories**: cs.LG, cs.AI

> Low-rank adaptation (LoRA) has become a widely used parameter-efficient fine-tuning method for large pretrained models. However, standard LoRA typically assigns a fixed rank profile despite layer- and stage-dependent adaptation needs, while recent adaptive-rank variants often rely on heuristic or fi...

### EpiLoRA: Fusing Many LoRA Adapters into Low-Precision GEMMs for Serving and RL
- **Authors**: Hieu Tran, Hong Yu
- **arXiv**: [2611.03899](http://arxiv.org/abs/2611.03899v1)
- **Published**: 2026-11-02
- **Categories**: cs.DC, cs.CL, cs.LG

> Low-rank adapters (LoRA) let one base model serve many fine-tuned variants: multi-tenant engines keep a single copy of the base and batch the requests of many tenants, each with its own adapter. As base models move to 8-bit (FP8) and 4-bit formats, their general matrix multiplications (GEMMs) become...

### BISECT: Bilevel Spectral Decomposition for Low-Rank Continual Learning
- **Authors**: Tom Saliencro, Wen-Hsuan Liu, Rohan Desai, Amara Okonkwo, Maya Lindqvist
- **arXiv**: [2611.03574](http://arxiv.org/abs/2611.03574v1)
- **Published**: 2026-11-02
- **Categories**: cs.LG

> Exemplar-free continual learning on pre-trained Vision Transformers increasingly relies on Low-Rank Adaptation (LoRA), yet prevailing methods govern the low-rank update space through strict subspace isolation. By projecting each incoming task into the approximate null space of historical token activ...

### ArabGeoText: Tool-Augmented Vision-Language Models for Arabic Geospatial Text Spotting
- **Authors**: Yakoub Bazi, Sarah Alsaleh, Mohamad M. Al Rahhal, Mohamed A. Mekhtiche, Mansour Zuair
- **arXiv**: [2611.03339](http://arxiv.org/abs/2611.03339v1)
- **Published**: 2026-11-02
- **Categories**: cs.CV

> Geospatial text spotting involves locating and transcribing geographic labels, such as road names, district names, and landmarks, in raster maps. These labels are often small, densely arranged, and arbitrarily oriented. Although Arabic text recognition has been studied extensively in documents and n...

### Comparative study of global pooling for pre-departure ship fuel consumption prediction: Advantages over per-ship and adaptation-based approaches
- **Authors**: Heungjun Im, Bongmin Cha, Agung Nugraha, Donghyun Kim, Seongphil Kang, Minwook Choi, Jeongmin Park, Jihwan Lee
- **arXiv**: [2611.03015](http://arxiv.org/abs/2611.03015v1)
- **Published**: 2026-11-02
- **Categories**: cs.LG, cs.AI

> Most fuel oil consumption (FOC) models for voyage planning are per-ship models and thus generalize poorly beyond each vessel's records. Transfer and federated learning have been reported to perform better, but under different protocols that often use inputs unavailable before departure or random dat...

### One Image Is Enough: Self-Generated Supervision for Personalizing Human Video Diffusion at Test Time
- **Authors**: Sadman Rakib Pinon, Adamo Orsini, Yanis Falaki, Linlian Jiang, Jacob Kingi, Yang Wang, Xinxin Zuo
- **arXiv**: [2611.02964](http://arxiv.org/abs/2611.02964v1)
- **Published**: 2026-11-02
- **Categories**: cs.CV, cs.GR, cs.LG

> Pose-driven human video diffusion animates a person from a single reference image and a target pose sequence, yet it struggles to preserve identity, rendering the face and garments unfaithfully as the pose departs from it. Personalization is the standard remedy, but its supervision is missing: one i...

### Unlocking the Potential of Vision Foundation Models for Multi-Task Dense Prediction via Mixture of Task Adapters
- **Authors**: Yunzhi Zhuge, Xinzhuo Yu, Sitong Gong, Lu Zhang, Pingping Zhang, Huchuan Lu
- **arXiv**: [2611.02769](http://arxiv.org/abs/2611.02769v1)
- **Published**: 2026-11-02
- **Categories**: cs.CV

> Multi-task dense prediction seeks a single, coherent representation that supports simultaneously discriminative semantic recognition and regularized geometric/structural inference. For vision foundation models, pretrained semantic invariances conflict with the frequency and smoothness biases of dens...

### DINOFAS: Bonafide-Centric Representation Learning for Face Anti-Spoofing
- **Authors**: Shakeel Muhammad Ibrahim, Muhammad Sohail Ibrahim, Muhammad Shahid Jabbar, Shujaat Khan
- **arXiv**: [2611.02756](http://arxiv.org/abs/2611.02756v1)
- **Published**: 2026-11-02
- **Categories**: cs.CV, cs.AI, eess.IV

> Face anti-spoofing (FAS) models often learn attack- and dataset-specific cues that degrade performance under unseen acquisition conditions and presentation attacks. We present DINOFAS, a DINOv3-based framework that formulates FAS as bonafide-centric representation learning. The proposed framework co...

### Train the Sampler You Run: Few-Step Masked Diffusion Language Models via Mixture-Likelihood Fine-Tuning
- **Authors**: Amin Najafgholizadeh
- **arXiv**: [2611.02666](http://arxiv.org/abs/2611.02666v1)
- **Published**: 2026-11-02
- **Categories**: cs.LG, cs.CL

> When a masked diffusion language model is sampled in a few parallel steps in a random order, the model actually run is a mixture over reveal plans, while cross-entropy training fits token conditionals rather than this mixture. We introduce mixture-likelihood fine-tuning (Mix-FT), which fine-tunes a ...

### Blueprint2CAD: Benchmarking Foundation Models on Engineering Drawing-to-CAD Render Correspondence
- **Authors**: Alexander Valverde, Danny Xie-Li, Zhichao Wang, Marcos V. Conde
- **arXiv**: [2611.02433](http://arxiv.org/abs/2611.02433v2)
- **Published**: 2026-11-02
- **Categories**: cs.CV

> Engineering drawings specify mechanical parts through orthographic projections. Recognizing which part a drawing depicts underlies part search, design reuse, and digitization, yet no public benchmark measures whether vision models can do it. We introduce Blueprint2CAD, a benchmark for drawing-to-ren...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "badiya-2026",
    "title": "Breaking the Privacy Promise: Gradient Inversion Attacks on Federated Low-Rank Adapted Vision Transformers",
    "authors": [
      "Ritik K. Badiya",
      "Siladittya Manna",
      "Ashmit Sinha",
      "M Yashwanth",
      "Anirban Chakraborty"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.09652",
    "paper_url": "https://arxiv.org/abs/2611.09652",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "karouzos-2026",
    "title": "Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters",
    "authors": [
      "Constantinos Karouzos",
      "Nikolaos Aletras"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.09634",
    "paper_url": "https://arxiv.org/abs/2611.09634",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "swadha-2026",
    "title": "From LoRA to Language: Recovering Skill Documents from Adapters",
    "authors": [
      "Saranya Dintakurthy Swadha",
      "Pavan C Shekar",
      "Arpit Jain",
      "Aswanth Krishnan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.09454",
    "paper_url": "https://arxiv.org/abs/2611.09454",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "a-l-2026",
    "title": "Turkish Multimodal Video Fact-Checking: A New Dataset and a Comparison of Zero-Shot Agentic and Fine-Tuned Systems",
    "authors": [
      "Azra Açıl"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.08651",
    "paper_url": "https://arxiv.org/abs/2611.08651",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "liu-2026",
    "title": "Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning",
    "authors": [
      "Chenruo Liu",
      "Zihan Wang",
      "Yijun Dong",
      "Qi Lei"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.08414",
    "paper_url": "https://arxiv.org/abs/2611.08414",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "zhao-2026",
    "title": "Towards Label-Efficient Geospatial Foundation Model Adaptation via Positive-Unlabeled Learning for Building Damage Mapping",
    "authors": [
      "Hengwei Zhao",
      "Qirui Wang",
      "Zhuo Zheng",
      "Xiaoyan Lu",
      "Rusty Feagin",
      "Wenzhe Jiao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.08561",
    "paper_url": "https://arxiv.org/abs/2611.08561",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "chauhan-2026",
    "title": "Automated Video-to-QA Pipeline: End-to-End Question Generation and Verification Using Large Language Models",
    "authors": [
      "Jaival Chauhan",
      "Vikram Singh",
      "Pruthwik Mishra"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.07755",
    "paper_url": "https://arxiv.org/abs/2611.07755",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "rane-2026",
    "title": "Embedding-Space Fingerprinting of LoRA Fine-Tunes: Recovering the Training-Data Domain from the Model Artifact Alone",
    "authors": [
      "Shivesh Rane"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.07610",
    "paper_url": "https://arxiv.org/abs/2611.07610",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "qiao-2026",
    "title": "Align Before Aggregation: Basis-Consistent Federated LoRA under Heterogeneous Ranks",
    "authors": [
      "Pengpeng Qiao",
      "Yang Cao",
      "Lingling Zhang",
      "Guo Cheng",
      "Junwei Chen",
      "Manjiang Yu",
      "Wei Yang Bryan Lim",
      "Masatoshi Yoshikawa"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.07598",
    "paper_url": "https://arxiv.org/abs/2611.07598",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "xue-2026",
    "title": "From What Is Used to What Is Missing: Rethinking Dynamic Rank in LoRA",
    "authors": [
      "Peng Xue",
      "Guodong Fan",
      "Guang-Yong Chen",
      "Xing Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.07349",
    "paper_url": "https://arxiv.org/abs/2611.07349",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "david-2026",
    "title": "The Behavioral Rate of Fine-Tuning: Compression as a Measure of Useful Information",
    "authors": [
      "Joey David",
      "Paul Caillon",
      "Alexandre Allauzen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.06598",
    "paper_url": "https://arxiv.org/abs/2611.06598",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "imam-2026",
    "title": "Zuse: A Decision Model for European Languages",
    "authors": [
      "Umair Mehmood Imam"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.06238",
    "paper_url": "https://arxiv.org/abs/2611.06238",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "liang-2026",
    "title": "ReTailor: A Residual Feature Tailoring Framework for Real-Time Cross-Sensor Pansharpening Adaptation",
    "authors": [
      "Jing-Ze Liang",
      "Wei-Jie Xiao",
      "Zi-Han Cao",
      "Yang-Dong Li",
      "Tian-Yi Hu",
      "Liang-Jian Deng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.05811",
    "paper_url": "https://arxiv.org/abs/2611.05811",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "vonich-2026",
    "title": "Distinguishing Initial-Condition and Model Error Using Machine-Learning Weather Models",
    "authors": [
      "P. Trent Vonich",
      "Gregory J. Hakim"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.05592",
    "paper_url": "https://arxiv.org/abs/2611.05592",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "gu-2026",
    "title": "Modulating Merging Strengths via Joint Loss Estimation for LoRA-based Continual Learning",
    "authors": [
      "Kun Gu",
      "De Cheng",
      "Zhipeng Xu",
      "Lingfeng He",
      "Di Xu",
      "Nannan Wang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.04931",
    "paper_url": "https://arxiv.org/abs/2611.04931",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "nguyen-2026",
    "title": "SaMA: Morpho Adaptation via Asymmetric Expansion of Kronecker Product",
    "authors": [
      "An Nguyen",
      "Anh Tong"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.04462",
    "paper_url": "https://arxiv.org/abs/2611.04462",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "mohsenvand-2026",
    "title": "Sketchpad: certified exact arithmetic with a small vision-language model",
    "authors": [
      "Mostafa 'Neo' Mohsenvand"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.04434",
    "paper_url": "https://arxiv.org/abs/2611.04434",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "grover-2026",
    "title": "RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training",
    "authors": [
      "Shresth Grover",
      "Andrey Kolobov",
      "Dhruv Shah"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.04368",
    "paper_url": "https://arxiv.org/abs/2611.04368",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "zubair-2026",
    "title": "Beyond Fine-Tuning: Evaluating Prompt Engineering and Prompt Tuning for Roman Urdu Hate Speech Detection",
    "authors": [
      "Toneema Zubair",
      "Muhammad Junaid Asif",
      "Faisal Kamiran",
      "Hafiz Hassan Saeed",
      "Rana Fayyaz Ahmad"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.04342",
    "paper_url": "https://arxiv.org/abs/2611.04342",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "wang-2026",
    "title": "LIRA: A More Interpretable Dynamic Loss-Informed Rank Allocation for Low-Rank Adaptation",
    "authors": [
      "Sihao Wang",
      "Bozheng Li",
      "Xuemiao Xu",
      "Haoxin Yang",
      "Yujie Xu",
      "Jie Tang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.04239",
    "paper_url": "https://arxiv.org/abs/2611.04239",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "tran-2026",
    "title": "EpiLoRA: Fusing Many LoRA Adapters into Low-Precision GEMMs for Serving and RL",
    "authors": [
      "Hieu Tran",
      "Hong Yu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.03899",
    "paper_url": "https://arxiv.org/abs/2611.03899",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "saliencro-2026",
    "title": "BISECT: Bilevel Spectral Decomposition for Low-Rank Continual Learning",
    "authors": [
      "Tom Saliencro",
      "Wen-Hsuan Liu",
      "Rohan Desai",
      "Amara Okonkwo",
      "Maya Lindqvist"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.03574",
    "paper_url": "https://arxiv.org/abs/2611.03574",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "bazi-2026",
    "title": "ArabGeoText: Tool-Augmented Vision-Language Models for Arabic Geospatial Text Spotting",
    "authors": [
      "Yakoub Bazi",
      "Sarah Alsaleh",
      "Mohamad M. Al Rahhal",
      "Mohamed A. Mekhtiche",
      "Mansour Zuair"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.03339",
    "paper_url": "https://arxiv.org/abs/2611.03339",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "im-2026",
    "title": "Comparative study of global pooling for pre-departure ship fuel consumption prediction: Advantages over per-ship and adaptation-based approaches",
    "authors": [
      "Heungjun Im",
      "Bongmin Cha",
      "Agung Nugraha",
      "Donghyun Kim",
      "Seongphil Kang",
      "Minwook Choi",
      "Jeongmin Park",
      "Jihwan Lee"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.03015",
    "paper_url": "https://arxiv.org/abs/2611.03015",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "pinon-2026",
    "title": "One Image Is Enough: Self-Generated Supervision for Personalizing Human Video Diffusion at Test Time",
    "authors": [
      "Sadman Rakib Pinon",
      "Adamo Orsini",
      "Yanis Falaki",
      "Linlian Jiang",
      "Jacob Kingi",
      "Yang Wang",
      "Xinxin Zuo"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.02964",
    "paper_url": "https://arxiv.org/abs/2611.02964",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "zhuge-2026",
    "title": "Unlocking the Potential of Vision Foundation Models for Multi-Task Dense Prediction via Mixture of Task Adapters",
    "authors": [
      "Yunzhi Zhuge",
      "Xinzhuo Yu",
      "Sitong Gong",
      "Lu Zhang",
      "Pingping Zhang",
      "Huchuan Lu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.02769",
    "paper_url": "https://arxiv.org/abs/2611.02769",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "ibrahim-2026",
    "title": "DINOFAS: Bonafide-Centric Representation Learning for Face Anti-Spoofing",
    "authors": [
      "Shakeel Muhammad Ibrahim",
      "Muhammad Sohail Ibrahim",
      "Muhammad Shahid Jabbar",
      "Shujaat Khan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.02756",
    "paper_url": "https://arxiv.org/abs/2611.02756",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "najafgholizadeh-2026",
    "title": "Train the Sampler You Run: Few-Step Masked Diffusion Language Models via Mixture-Likelihood Fine-Tuning",
    "authors": [
      "Amin Najafgholizadeh"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.02666",
    "paper_url": "https://arxiv.org/abs/2611.02666",
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
    "added_date": "2026-11-09"
  },
  {
    "id": "valverde-2026",
    "title": "Blueprint2CAD: Benchmarking Foundation Models on Engineering Drawing-to-CAD Render Correspondence",
    "authors": [
      "Alexander Valverde",
      "Danny Xie-Li",
      "Zhichao Wang",
      "Marcos V. Conde"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.02433",
    "paper_url": "https://arxiv.org/abs/2611.02433",
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
    "added_date": "2026-11-09"
  }
]
```
