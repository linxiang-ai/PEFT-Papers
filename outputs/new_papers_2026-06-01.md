# New arXiv PEFT papers — 2026-06-01

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **35**.

## Candidates

### Balanced LoRA: Removing Parameter Invariance to Accelerate Convergence
- **Authors**: Valérie Castin, Kimia Nadjahi, Pierre Ablin, Gabriel Peyré
- **arXiv**: [2605.31484](http://arxiv.org/abs/2605.31484v1)
- **Published**: 2026-05-29
- **Categories**: cs.LG

> Low-Rank Adaptation (LoRA) is the most widely adopted method for fine-tuning large language models. Notably, LoRA is inherently overparameterized: multiple pairs of low-rank factors can yield the same adapted weight matrix. We show--both theoretically and empirically--that these pairs exhibit signif...

### TRACE: Discovering Task-Specific Parameter via Adaptation-Aware Probing for Continual Fine-Tuning
- **Authors**: Xiaosong Han, Ke Chen, Xindi Dai, Di Liang, Minlong Peng, Wei Pang, Fausto Giunchiglia, Xiaoyue Feng, Yonghao Liu, Renchu Guan
- **arXiv**: [2605.31025](http://arxiv.org/abs/2605.31025v1)
- **Published**: 2026-05-29
- **Categories**: cs.CL

> In real-world deployment, LLMs are often adapted continually across tasks to keep LLMs up-to-date in production, where new fine-tuning should preserve previously learned skills. However, indiscriminately mixing tasks can dilute task specialization, while sequential fine-tuning (full-parameter or low...

### CSULoRA: Closest Safe Update Low-Rank Adaptation
- **Authors**: Oleksandr Marchenko Breneur, Adelaide Danilov, Aria Nourbakhsh, Salima Lamsiyah
- **arXiv**: [2605.30640](http://arxiv.org/abs/2605.30640v1)
- **Published**: 2026-05-28
- **Categories**: cs.LG, cs.CL

> Low-rank adaptation has become a standard method for parameter-efficient fine-tuning of large language models, but even small amounts of unsafe or adversarial fine-tuning data can substantially weaken the safety behavior of aligned models. Existing safety-preserving LoRA methods often rely on hard i...

### PInVerify: An Offline Embodied Benchmark for Active Instance Verification
- **Authors**: Yuhang Jiang
- **arXiv**: [2605.30639](http://arxiv.org/abs/2605.30639v1)
- **Published**: 2026-05-28
- **Categories**: cs.CV, cs.AI, cs.RO

> Embodied agents have made strong progress in navigating to target objects, but reaching the goal vicinity does not guarantee that the agent has found the correct instance: subtle attribute differences (e.g., "white floral" vs. "white striped") often require close-range, multi-view inspection. We add...

### Improving Small Language Models for Code Generation with Reinforcement Learning from Verification Feedback
- **Authors**: Egor Skopin, Evgeny Kotelnikov
- **arXiv**: [2605.30478](http://arxiv.org/abs/2605.30478v1)
- **Published**: 2026-05-28
- **Categories**: cs.SE, cs.CL

> Reinforcement learning with verifiable rewards (RLVR) trains language models using programmatically checkable signals such as unit-test outcomes, enabling direct optimization for functional correctness in code generation. We conduct an empirical study of RLVR for Python code generation on the MBPP b...

### How LoRA Remembers? A Parametric Memory Law for LLM Finetuning
- **Authors**: Ziwen Xu, Haiwen Hong, Linsong Yu, Benglei Cui, Longtao Huang, Hui Xue, Ningyu Zhang
- **arXiv**: [2605.30260](http://arxiv.org/abs/2605.30260v1)
- **Published**: 2026-05-28
- **Categories**: cs.CL, cs.AI, cs.CV, cs.LG

> Large Language Models (LLMs) must continuously learn and update knowledge to remain effective in dynamic real-world environments. While Low-Rank Adaptation (LoRA) is widely used for such memory updates, existing studies mainly rely on qualitative downstream evaluations, leaving the quantitative capa...

### iLoRA: Bayesian Low-Rank Adaptation with Latent Interaction Graphs for Microbiome Diagnosis
- **Authors**: Yang Song, Yixuan Zhang, Lingfa Meng, Tongyuan Hu, Haizhou Shi, Hao Wang, Samir Bhatt, Hengguan Huang
- **arXiv**: [2605.30179](http://arxiv.org/abs/2605.30179v1)
- **Published**: 2026-05-28
- **Categories**: cs.LG, cs.AI

> Parameter-efficient adaptation has made LLMs practical for domain prediction, but standard LoRA still relies on a static low-rank update and does not expose the latent interactions that often drive scientific labels. We introduce iLoRA. To our knowledge, it is the first Bayesian graph-conditioned Lo...

### Alignment-Guided Score Matching for Text-to-Image Alignment in Diffusion Models
- **Authors**: Jaa-Yeon Lee, Yeobin Hong, Taesung Kwon, Jong Chul Ye
- **arXiv**: [2605.30038](http://arxiv.org/abs/2605.30038v1)
- **Published**: 2026-05-28
- **Categories**: cs.LG, cs.AI, cs.CV

> Diffusion models generate highly realistic images but often struggle with precise text-image alignment. While recent post-training methods improve alignment using external rewards or human preference signals, their performance heavily depends on reward quality and does not directly address alignment...

### SLAD : Shared LoRA Adapters for Task Specific Distillation
- **Authors**: Reda Bensaid, Yassir Bendou, Vincent Gripon, François Leduc-Primeau
- **arXiv**: [2605.29726](http://arxiv.org/abs/2605.29726v1)
- **Published**: 2026-05-28
- **Categories**: cs.CV

> In the context of resource-constrained environments such as embedded systems, adapting reduced-size foundation models to downstream tasks has become increasingly popular. This has recently motivated the emerging setting of task-specific distillation, where a larger and a smaller version of the same ...

### NaRA: Noise-Aware LoRA for Parameter-Efficient Fine-Tuning of Diffusion LLMs
- **Authors**: Shuaidi Wang, Zhan Zhuang, Ruping Huang, Yu Zhang
- **arXiv**: [2605.29716](http://arxiv.org/abs/2605.29716v1)
- **Published**: 2026-05-28
- **Categories**: cs.AI

> Diffusion Large Language Models (dLLMs) have emerged as a promising non-autoregressive generative paradigm. Given the prohibitive computational cost of full fine-tuning, Parameter-Efficient Fine-Tuning (PEFT) has become the standard approach. However, existing PEFT methods (e.g., LoRA), originally t...

### On the Construction and Implications of Low-Loss Valleys in LoRA-based Bayesian Inference
- **Authors**: Daniel Dold, Emanuel Sommer, Julius Kobialka, Oliver Dürr, David Rügamer
- **arXiv**: [2605.29580](http://arxiv.org/abs/2605.29580v1)
- **Published**: 2026-05-28
- **Categories**: cs.LG, stat.ML

> While parameter-efficient fine-tuning methods like low-rank adaptation (LoRA) are standard for large language models, principled estimation of epistemic uncertainty remains challenging. Recent results in the LoRA regime suggest that discrete multi-mode approaches such as deep ensembles offer little ...

### Mask the Target: A Plug-and-Play Regularizer Against LoRA Forgetting
- **Authors**: Runze Xu, Arpit Garg, Hemanth Saratchandran, Simon Lucey
- **arXiv**: [2605.29498](http://arxiv.org/abs/2605.29498v1)
- **Published**: 2026-05-28
- **Categories**: cs.CL, cs.CV

> Low-Rank Adaptation (LoRA) has become one of the most widely used fine-tuning mechanisms for adapting large language models to new domains, tasks, and users. Yet adaptation performance alone can obscure an important failure mode: LoRA updates may improve performance on the target distribution while ...

### FedSmoothLoRA: Toward Smoother and Faster Convergence in Federated Low-Rank Adaptation
- **Authors**: Zehao Wang, Guanglei Yang, Yihan Zeng, Hang Xu, Hongzhi Zhang, Wangmeng Zuo, Chun-Mei Feng
- **arXiv**: [2605.29460](http://arxiv.org/abs/2605.29460v1)
- **Published**: 2026-05-28
- **Categories**: cs.CV

> Federated fine-tuning of foundation models with Low-Rank Adaptation (LoRA) provides an efficient solution for reducing communication and computation costs while preserving data locality. However, the direct combination of FedAvg and LoRA suffers from three key issues: limited update space, which res...

### FoRA: Fisher-orthogonal Rank Adaptation for Parameter-Efficient Fine-Tuning
- **Authors**: Juneyoung Park, Seongbae Lee, Han-Sang Lee, Kyuho Lee, Minjae Kim, Seungheon Hyeon, Kiduk Kwon, Seongwan Kim, Jaeho Lee
- **arXiv**: [2605.29317](http://arxiv.org/abs/2605.29317v2)
- **Published**: 2026-05-28
- **Categories**: cs.CL

> Parameter-efficient fine-tuning(PEFT) has largely focused on LoRA and its accuracy-oriented variants, leaving the original goal of reducing trainable parameters has receivedcomparatively little attention. We introduce FoRA, which revisits this goal by reducing the number of adapted layers rather tha...

### OpenClawBench: Benchmarking Process-side Anomalies in Real-world Agent Execution Trajectories
- **Authors**: Yibing Liu, Yangze Liu, Xiaolong Yin, Bin Wang, Chong Zhang, Hao Yin, Zhongyi Han
- **arXiv**: [2605.29253](http://arxiv.org/abs/2605.29253v1)
- **Published**: 2026-05-28
- **Categories**: cs.AI

> Task success can hide process anomalies in real-world agent executions. An agent may pass the final task oracle while still accumulating unresolved ambiguity, unsafe external writes, ignored errors, weakly grounded commitments, or capability-boundary overcommitment. We study this mismatch as the Out...

### Janus-LoRA: A Balanced Low-Rank Adaptation for Continual Learning
- **Authors**: Cheng Chen, Pengpeng Zeng, Yuyu Guo, Lianli Gao, Hengtao Shen, Jingkuan Song
- **arXiv**: [2605.28495](http://arxiv.org/abs/2605.28495v1)
- **Published**: 2026-05-27
- **Categories**: cs.CV

> Low-Rank Adaptation (LoRA) has emerged as a promising paradigm for Continual Learning. It independently updates its low-rank factors ($A$ and $B$), creating a composite update to the full weight matrix through their interaction. To prevent catastrophic forgetting, this update should remain orthogona...

### Feature Geometry of LoRA Adapters: A Sparse Autoencoder Analysis of Representational Divergence in Fine-Tuned Language Models
- **Authors**: Prasanth K K
- **arXiv**: [2605.28896](http://arxiv.org/abs/2605.28896v1)
- **Published**: 2026-05-27
- **Categories**: cs.LG

> Low-Rank Adaptation (LoRA) has emerged as a widely adopted approach for adapting large language models, yet the internal representational changes induced by LoRA fine-tuning remain insufficiently understood. In this work, we investigate the geometry of LoRA-induced representations using Sparse Autoe...

### Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation
- **Authors**: Evgenii Palnikov, Elizaveta Gavrilova
- **arXiv**: [2605.28222](http://arxiv.org/abs/2605.28222v1)
- **Published**: 2026-05-27
- **Categories**: cs.CL, cs.IR, cs.LG

> We study quality-latency-resource trade-offs in a documentation-grounded retrieval-augmented generation (RAG) system that uses Low-Rank Adaptation (LoRA) of the generator. We build a manually verified benchmark of 5,144 question-answer pairs over the official Kubernetes documentation and combine it ...

### Adapting Automotive Aerodynamics Surrogates to New Vehicle Families via Transfer Learning
- **Authors**: Seunghwan Keum, Alok Warey
- **arXiv**: [2605.27968](http://arxiv.org/abs/2605.27968v1)
- **Published**: 2026-05-27
- **Categories**: cs.CE, cs.LG, physics.comp-ph

> Deploying Scientific Machine Learning surrogates in industrial CFD workflows requires adapting pretrained models to new vehicle families without large datasets; yet whether geometric representations learned by a geometry encoder transfer to topologically distinct shapes remains unvalidated. We addre...

### SIGMA: Bridging Structural and Distributional Gaps for Vision Foundation Model Adaptation
- **Authors**: Lingyu Xiong, Jinjin Shi, Xuran Xu, Cong Luo, Runyu Shi, Ying Huang
- **arXiv**: [2605.27893](http://arxiv.org/abs/2605.27893v1)
- **Published**: 2026-05-27
- **Categories**: cs.CV

> Vision Foundation Models (VFMs) have demonstrated impressive representational capabilities. However, adapting them to downstream tasks via full fine-tuning incurs prohibitive computational and storage overhead. Parameter-Efficient Fine-Tuning (PEFT) has emerged as a compelling alternative, aiming to...

### GRADE: Generalizable Reasoning-Aware Dialogue Evaluation for AI Tutors
- **Authors**: Parth Bhalerao, Jeromy Chang, David Chou, Oana Ignat
- **arXiv**: [2605.27866](http://arxiv.org/abs/2605.27866v1)
- **Published**: 2026-05-27
- **Categories**: cs.CL

> Evaluating AI tutor responses requires more than factual correctness: tutors must identify mistakes, locate errors, provide guidance, and offer actionable next steps. We present GRADE, a systematic study of open-source models for pedagogical ability assessment in student-tutor dialogues. Building on...

### CAREF: Calibration-Aware Regularization for Explanation Faithfulness Without Rationale Supervision
- **Authors**: Naphat Nithisopa, Teerapong Panboonyuen
- **arXiv**: [2605.27835](http://arxiv.org/abs/2605.27835v1)
- **Published**: 2026-05-27
- **Categories**: cs.LG, cs.CL

> We introduce CAREF, a parameter-efficient fine-tuning framework that jointly optimizes predictive accuracy and explanation faithfulness via calibration-aware regularization. At its core, CAREF couples entropy-based calibration with token-level sparsity control through a single unified loss, the Cali...

### Unsupervised Identification and Removal of Spurious Correlations During Fine-Tuning
- **Authors**: Ciarán M. Gilligan-Lee, Joseph Egan, Yuchen Zhu, Michael O'Riordan
- **arXiv**: [2605.27676](http://arxiv.org/abs/2605.27676v1)
- **Published**: 2026-05-26
- **Categories**: stat.ML, cs.LG

> Fine-tuning a pretrained language model on a curated dataset can produce spurious correlations between the fine-tuning task and unintended latent factors -- such as misaligned personas or political slant -- that the curation procedure has entangled with the task. The model can latch onto these spuri...

### BhashaSetu: A Data-Centric Approach to Low-Resource Machine Translation
- **Authors**: Param Thakkar, Anushka Yadav, Michael Tiemann, Abhi Mehta, Akshita Bhasin, Shrinivas Khedkar
- **arXiv**: [2605.27050](http://arxiv.org/abs/2605.27050v1)
- **Published**: 2026-05-26
- **Categories**: cs.CL, cs.LG

> We present BhashaSetu, a linguistically enriched English--Marathi parallel dataset addressing persistent data limitations in low-resource neural machine translation (NMT). Marathi, spoken by over 95 million people, remains underrepresented in high-quality parallel corpora across diverse domains. Our...

### Energy-Structured Low-Rank Adaptation for Continual Learning
- **Authors**: Longhua Li, Lei Qi, Qi Tian, Xin Geng
- **arXiv**: [2605.27482](http://arxiv.org/abs/2605.27482v1)
- **Published**: 2026-05-26
- **Categories**: cs.LG, cs.AI

> While orthogonal subspace methods try to mitigate task interference in Continual Learning (CL), they often suffer from energy diffusion across the basis, hindering knowledge compaction and exhausting capacity for future tasks. We observe that output feature drift induced by parameter updates is inhe...

### EmoDistill: Offline Emotion Skill Distillation for Language Model Agents in Adversarial Negotiation
- **Authors**: Yunbo Long, Haolang Zhao, Lukas Beckenbauer, Liming Xu, Alexandra Brintrup
- **arXiv**: [2605.26785](http://arxiv.org/abs/2605.26785v1)
- **Published**: 2026-05-26
- **Categories**: cs.CL, cs.AI

> Post-trained LLMs are often optimized to align responses with human preferences, making them safe, polite, and conversationally appropriate. In adversarial negotiation, however, this alignment can become a vulnerability: emotionally framed language may steer agents toward the counterparty's interest...

### Reliable Extraction of Clinical Follow-Up Instructions: A Hybrid Neural-Symbolic Pipeline
- **Authors**: Michal Laufer, Yehudit Aperstein, Alexander Apartsin
- **arXiv**: [2605.26560](http://arxiv.org/abs/2605.26560v1)
- **Published**: 2026-05-26
- **Categories**: cs.CL, cs.AI

> Objective. Outpatient notes carry follow-up instructions pairing actions with future times ("MRI brain in two weeks"). Extracting (action, date) pairs supports scheduling and audit, but generative extractors miss the date because linking and arithmetic are implicit in decoding. We test a hybrid neur...

### A Hybrid Vision-Language Architecture for Automated Defect Reasoning and Report Generation in Industrial Inspection
- **Authors**:  Malikussaid, Imad Gohar
- **arXiv**: [2605.26533](http://arxiv.org/abs/2605.26533v1)
- **Published**: 2026-05-26
- **Categories**: cs.CV, cs.AI, cs.CL, cs.LG

> Automated industrial inspection requires both precise defect localization and structured maintenance report generation; in current practice these tasks are handled separately, with linguistic interpretation left to human experts. This paper describes a decoupled, edge-deployable pipeline for wind tu...

### Vectors Are Not Neutral: Sensitive-Information Inference from Exported LLM Representations in Summarization
- **Authors**: Weixin Liu, Bowen Qu, Juming Xiong, Congning Ni, Bradley A. Malin, Zhijun Yin
- **arXiv**: [2605.26433](http://arxiv.org/abs/2605.26433v1)
- **Published**: 2026-05-26
- **Categories**: cs.CL

> Large language model (LLM) summarization systems may pass compact vector representations of private inputs to downstream retrieval, monitoring, audit, or analytic workflows. Even when source documents remain access-restricted, derived vectors may be handled under different access controls and still ...

### Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning
- **Authors**: Taha Koleilat, Hassan Rivaz, Yiming Xiao
- **arXiv**: [2605.26292](http://arxiv.org/abs/2605.26292v1)
- **Published**: 2026-05-25
- **Categories**: cs.CV, cs.CL

> Parameter-efficient adaptation of vision-language foundation models is crucial for precise multimodal understanding of biomedical images, yet existing methods remain deterministic and often struggle under domain shift or ambiguous image-text alignment. This limitation is particularly critical in the...

### UAV-OVO: Out-of-Viewpoint Generalization in UAV Action Recognition
- **Authors**: Yu Xia, Zhengbo Zhang, Shuaihu Zhang, Zhigang Tu
- **arXiv**: [2605.25615](http://arxiv.org/abs/2605.25615v1)
- **Published**: 2026-05-25
- **Categories**: cs.CV

> UAV action recognition faces a deployment shift that standard benchmarks often obscure: a model trained on UAV footage captured from low-depression viewpoints may be required to recognize the same action classes from high-depression viewpoints. While the action labels remain unchanged, this shift al...

### RotMoLE: Enhancing Mixture of Low-Rank Experts through Rotational Gating Mechanism
- **Authors**: Mengyang Sun, Maochuan Dou, Tao Feng, Dan Zhang, Yihao Wang, Junpeng Liu, Yifan Zhu, Jie Tang
- **arXiv**: [2605.25565](http://arxiv.org/abs/2605.25565v1)
- **Published**: 2026-05-25
- **Categories**: cs.LG, cs.CL

> While Large Language Models (LLMs) are commonly fine-tuned to handle domain-specific tasks before being applied to vertical applications, adapting them to complex scenarios with diverse specialized knowledge remains challenging. Meanwhile, Mixture-of-Experts (MoE) architecture has risen as a crucial...

### RepSAM: Bridging Foundation Models to Robotic Vision via Representation-Guided Adaptation
- **Authors**: Wenhui Chu
- **arXiv**: [2605.25495](http://arxiv.org/abs/2605.25495v1)
- **Published**: 2026-05-25
- **Categories**: cs.RO, cs.CV

> Robotic perception in unstructured environments remains challenging despite the zero-shot capabilities of foundation models such as SAM. This work attributes performance degradation to non-uniform representation shifts across transformer layers: shallow layers exhibit substantial domain gaps (CKA < ...

### MAIL++: Multi-Modal Bi-directional Agent Layer for Vision-Language Models
- **Authors**: Kaixiang Chen, Pengfei Fang, Hui Xue
- **arXiv**: [2605.25479](http://arxiv.org/abs/2605.25479v1)
- **Published**: 2026-05-25
- **Categories**: cs.CV

> Adapting large vision-language models (VLMs) such as CLIP to downstream tasks remains challenging, as full fine-tuning is computationally prohibitive and prone to overfitting in low-data regimes. Parameter-efficient fine-tuning (PEFT) alleviates these issues with lightweight prompt- or adapter-based...

### CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation
- **Authors**: Fangtai Wu, Hailong Guo, Shijie Huang, Jiayi Song, Yubo Huang, Mushui Liu, Zhao Wang, Yunlong Yu, Jiaming Liu, Ruihua Huang
- **arXiv**: [2605.25378](http://arxiv.org/abs/2605.25378v2)
- **Published**: 2026-05-25
- **Categories**: cs.CV, cs.AI

> Customized image editing aims to equip pre-trained diffusion models with specific visual effects using limited paired data, typically via Low-Rank Adaptation (LoRA). As the number of desired effects grows, storing and dynamically loading numerous these effect LoRAs significantly increases deployment...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "castin-2026",
    "title": "Balanced LoRA: Removing Parameter Invariance to Accelerate Convergence",
    "authors": [
      "Valérie Castin",
      "Kimia Nadjahi",
      "Pierre Ablin",
      "Gabriel Peyré"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.31484",
    "paper_url": "https://arxiv.org/abs/2605.31484",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "han-2026",
    "title": "TRACE: Discovering Task-Specific Parameter via Adaptation-Aware Probing for Continual Fine-Tuning",
    "authors": [
      "Xiaosong Han",
      "Ke Chen",
      "Xindi Dai",
      "Di Liang",
      "Minlong Peng",
      "Wei Pang",
      "Fausto Giunchiglia",
      "Xiaoyue Feng",
      "Yonghao Liu",
      "Renchu Guan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.31025",
    "paper_url": "https://arxiv.org/abs/2605.31025",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "breneur-2026",
    "title": "CSULoRA: Closest Safe Update Low-Rank Adaptation",
    "authors": [
      "Oleksandr Marchenko Breneur",
      "Adelaide Danilov",
      "Aria Nourbakhsh",
      "Salima Lamsiyah"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.30640",
    "paper_url": "https://arxiv.org/abs/2605.30640",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "jiang-2026",
    "title": "PInVerify: An Offline Embodied Benchmark for Active Instance Verification",
    "authors": [
      "Yuhang Jiang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.30639",
    "paper_url": "https://arxiv.org/abs/2605.30639",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "skopin-2026",
    "title": "Improving Small Language Models for Code Generation with Reinforcement Learning from Verification Feedback",
    "authors": [
      "Egor Skopin",
      "Evgeny Kotelnikov"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.30478",
    "paper_url": "https://arxiv.org/abs/2605.30478",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "xu-2026",
    "title": "How LoRA Remembers? A Parametric Memory Law for LLM Finetuning",
    "authors": [
      "Ziwen Xu",
      "Haiwen Hong",
      "Linsong Yu",
      "Benglei Cui",
      "Longtao Huang",
      "Hui Xue",
      "Ningyu Zhang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.30260",
    "paper_url": "https://arxiv.org/abs/2605.30260",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "song-2026",
    "title": "iLoRA: Bayesian Low-Rank Adaptation with Latent Interaction Graphs for Microbiome Diagnosis",
    "authors": [
      "Yang Song",
      "Yixuan Zhang",
      "Lingfa Meng",
      "Tongyuan Hu",
      "Haizhou Shi",
      "Hao Wang",
      "Samir Bhatt",
      "Hengguan Huang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.30179",
    "paper_url": "https://arxiv.org/abs/2605.30179",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "lee-2026",
    "title": "Alignment-Guided Score Matching for Text-to-Image Alignment in Diffusion Models",
    "authors": [
      "Jaa-Yeon Lee",
      "Yeobin Hong",
      "Taesung Kwon",
      "Jong Chul Ye"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.30038",
    "paper_url": "https://arxiv.org/abs/2605.30038",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "bensaid-2026",
    "title": "SLAD : Shared LoRA Adapters for Task Specific Distillation",
    "authors": [
      "Reda Bensaid",
      "Yassir Bendou",
      "Vincent Gripon",
      "François Leduc-Primeau"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.29726",
    "paper_url": "https://arxiv.org/abs/2605.29726",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "wang-2026",
    "title": "NaRA: Noise-Aware LoRA for Parameter-Efficient Fine-Tuning of Diffusion LLMs",
    "authors": [
      "Shuaidi Wang",
      "Zhan Zhuang",
      "Ruping Huang",
      "Yu Zhang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.29716",
    "paper_url": "https://arxiv.org/abs/2605.29716",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "dold-2026",
    "title": "On the Construction and Implications of Low-Loss Valleys in LoRA-based Bayesian Inference",
    "authors": [
      "Daniel Dold",
      "Emanuel Sommer",
      "Julius Kobialka",
      "Oliver Dürr",
      "David Rügamer"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.29580",
    "paper_url": "https://arxiv.org/abs/2605.29580",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "xu-2026",
    "title": "Mask the Target: A Plug-and-Play Regularizer Against LoRA Forgetting",
    "authors": [
      "Runze Xu",
      "Arpit Garg",
      "Hemanth Saratchandran",
      "Simon Lucey"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.29498",
    "paper_url": "https://arxiv.org/abs/2605.29498",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "wang-2026",
    "title": "FedSmoothLoRA: Toward Smoother and Faster Convergence in Federated Low-Rank Adaptation",
    "authors": [
      "Zehao Wang",
      "Guanglei Yang",
      "Yihan Zeng",
      "Hang Xu",
      "Hongzhi Zhang",
      "Wangmeng Zuo",
      "Chun-Mei Feng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.29460",
    "paper_url": "https://arxiv.org/abs/2605.29460",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "park-2026",
    "title": "FoRA: Fisher-orthogonal Rank Adaptation for Parameter-Efficient Fine-Tuning",
    "authors": [
      "Juneyoung Park",
      "Seongbae Lee",
      "Han-Sang Lee",
      "Kyuho Lee",
      "Minjae Kim",
      "Seungheon Hyeon",
      "Kiduk Kwon",
      "Seongwan Kim",
      "Jaeho Lee"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.29317",
    "paper_url": "https://arxiv.org/abs/2605.29317",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "liu-2026",
    "title": "OpenClawBench: Benchmarking Process-side Anomalies in Real-world Agent Execution Trajectories",
    "authors": [
      "Yibing Liu",
      "Yangze Liu",
      "Xiaolong Yin",
      "Bin Wang",
      "Chong Zhang",
      "Hao Yin",
      "Zhongyi Han"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.29253",
    "paper_url": "https://arxiv.org/abs/2605.29253",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "chen-2026",
    "title": "Janus-LoRA: A Balanced Low-Rank Adaptation for Continual Learning",
    "authors": [
      "Cheng Chen",
      "Pengpeng Zeng",
      "Yuyu Guo",
      "Lianli Gao",
      "Hengtao Shen",
      "Jingkuan Song"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.28495",
    "paper_url": "https://arxiv.org/abs/2605.28495",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "k-2026",
    "title": "Feature Geometry of LoRA Adapters: A Sparse Autoencoder Analysis of Representational Divergence in Fine-Tuned Language Models",
    "authors": [
      "Prasanth K K"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.28896",
    "paper_url": "https://arxiv.org/abs/2605.28896",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "palnikov-2026",
    "title": "Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation",
    "authors": [
      "Evgenii Palnikov",
      "Elizaveta Gavrilova"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.28222",
    "paper_url": "https://arxiv.org/abs/2605.28222",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "keum-2026",
    "title": "Adapting Automotive Aerodynamics Surrogates to New Vehicle Families via Transfer Learning",
    "authors": [
      "Seunghwan Keum",
      "Alok Warey"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.27968",
    "paper_url": "https://arxiv.org/abs/2605.27968",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "xiong-2026",
    "title": "SIGMA: Bridging Structural and Distributional Gaps for Vision Foundation Model Adaptation",
    "authors": [
      "Lingyu Xiong",
      "Jinjin Shi",
      "Xuran Xu",
      "Cong Luo",
      "Runyu Shi",
      "Ying Huang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.27893",
    "paper_url": "https://arxiv.org/abs/2605.27893",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "bhalerao-2026",
    "title": "GRADE: Generalizable Reasoning-Aware Dialogue Evaluation for AI Tutors",
    "authors": [
      "Parth Bhalerao",
      "Jeromy Chang",
      "David Chou",
      "Oana Ignat"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.27866",
    "paper_url": "https://arxiv.org/abs/2605.27866",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "nithisopa-2026",
    "title": "CAREF: Calibration-Aware Regularization for Explanation Faithfulness Without Rationale Supervision",
    "authors": [
      "Naphat Nithisopa",
      "Teerapong Panboonyuen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.27835",
    "paper_url": "https://arxiv.org/abs/2605.27835",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "gilligan-lee-2026",
    "title": "Unsupervised Identification and Removal of Spurious Correlations During Fine-Tuning",
    "authors": [
      "Ciarán M. Gilligan-Lee",
      "Joseph Egan",
      "Yuchen Zhu",
      "Michael O'Riordan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.27676",
    "paper_url": "https://arxiv.org/abs/2605.27676",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "thakkar-2026",
    "title": "BhashaSetu: A Data-Centric Approach to Low-Resource Machine Translation",
    "authors": [
      "Param Thakkar",
      "Anushka Yadav",
      "Michael Tiemann",
      "Abhi Mehta",
      "Akshita Bhasin",
      "Shrinivas Khedkar"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.27050",
    "paper_url": "https://arxiv.org/abs/2605.27050",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "li-2026",
    "title": "Energy-Structured Low-Rank Adaptation for Continual Learning",
    "authors": [
      "Longhua Li",
      "Lei Qi",
      "Qi Tian",
      "Xin Geng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.27482",
    "paper_url": "https://arxiv.org/abs/2605.27482",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "long-2026",
    "title": "EmoDistill: Offline Emotion Skill Distillation for Language Model Agents in Adversarial Negotiation",
    "authors": [
      "Yunbo Long",
      "Haolang Zhao",
      "Lukas Beckenbauer",
      "Liming Xu",
      "Alexandra Brintrup"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.26785",
    "paper_url": "https://arxiv.org/abs/2605.26785",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "laufer-2026",
    "title": "Reliable Extraction of Clinical Follow-Up Instructions: A Hybrid Neural-Symbolic Pipeline",
    "authors": [
      "Michal Laufer",
      "Yehudit Aperstein",
      "Alexander Apartsin"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.26560",
    "paper_url": "https://arxiv.org/abs/2605.26560",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "malikussaid-2026",
    "title": "A Hybrid Vision-Language Architecture for Automated Defect Reasoning and Report Generation in Industrial Inspection",
    "authors": [
      " Malikussaid",
      "Imad Gohar"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.26533",
    "paper_url": "https://arxiv.org/abs/2605.26533",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "liu-2026",
    "title": "Vectors Are Not Neutral: Sensitive-Information Inference from Exported LLM Representations in Summarization",
    "authors": [
      "Weixin Liu",
      "Bowen Qu",
      "Juming Xiong",
      "Congning Ni",
      "Bradley A. Malin",
      "Zhijun Yin"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.26433",
    "paper_url": "https://arxiv.org/abs/2605.26433",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "koleilat-2026",
    "title": "Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning",
    "authors": [
      "Taha Koleilat",
      "Hassan Rivaz",
      "Yiming Xiao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.26292",
    "paper_url": "https://arxiv.org/abs/2605.26292",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "xia-2026",
    "title": "UAV-OVO: Out-of-Viewpoint Generalization in UAV Action Recognition",
    "authors": [
      "Yu Xia",
      "Zhengbo Zhang",
      "Shuaihu Zhang",
      "Zhigang Tu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.25615",
    "paper_url": "https://arxiv.org/abs/2605.25615",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "sun-2026",
    "title": "RotMoLE: Enhancing Mixture of Low-Rank Experts through Rotational Gating Mechanism",
    "authors": [
      "Mengyang Sun",
      "Maochuan Dou",
      "Tao Feng",
      "Dan Zhang",
      "Yihao Wang",
      "Junpeng Liu",
      "Yifan Zhu",
      "Jie Tang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.25565",
    "paper_url": "https://arxiv.org/abs/2605.25565",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "chu-2026",
    "title": "RepSAM: Bridging Foundation Models to Robotic Vision via Representation-Guided Adaptation",
    "authors": [
      "Wenhui Chu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.25495",
    "paper_url": "https://arxiv.org/abs/2605.25495",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "chen-2026",
    "title": "MAIL++: Multi-Modal Bi-directional Agent Layer for Vision-Language Models",
    "authors": [
      "Kaixiang Chen",
      "Pengfei Fang",
      "Hui Xue"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.25479",
    "paper_url": "https://arxiv.org/abs/2605.25479",
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
    "added_date": "2026-06-01"
  },
  {
    "id": "wu-2026",
    "title": "CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation",
    "authors": [
      "Fangtai Wu",
      "Hailong Guo",
      "Shijie Huang",
      "Jiayi Song",
      "Yubo Huang",
      "Mushui Liu",
      "Zhao Wang",
      "Yunlong Yu",
      "Jiaming Liu",
      "Ruihua Huang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2605.25378",
    "paper_url": "https://arxiv.org/abs/2605.25378",
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
    "added_date": "2026-06-01"
  }
]
```
