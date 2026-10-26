# New arXiv PEFT papers — 2026-10-26

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **24**.

## Candidates

### Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery
- **Authors**: Marek Masiak, Andrzej Szablewski, Nicola Cancedda, Constantin Venhoff
- **arXiv**: [2610.32866](http://arxiv.org/abs/2610.32866v1)
- **Published**: 2026-10-23
- **Categories**: cs.LG, cs.AI, cs.CL

> Fine-tuning on datasets of unknown origin can create a backdoor in the trained model when the data includes poisoned examples. Difficult to localise and remove, backdoors can persist through safety training. While parameter-efficient fine-tuning methods capture the full parameter changes introduced ...

### Singular Geometry of Low-Rank Adaptation
- **Authors**: Kamillo Ferry, Anthea Monod, Keisuke Yano
- **arXiv**: [2610.32854](http://arxiv.org/abs/2610.32854v1)
- **Published**: 2026-10-23
- **Categories**: stat.ML, cs.LG

> Low-rank adaptation (LoRA) is now a standard approach to parameter-efficient fine-tuning of large neural networks. Its low-rank factorization is inherently non-identifiable, making LoRA a singular statistical model whose learning complexity cannot be described by parameter dimension alone. We study ...

### When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning
- **Authors**: Zongyao Zhao, Cheng-Jie Zhao, Ruihang Jiang, Bing Zheng, Zhaolin Wang, Yuanwei Liu
- **arXiv**: [2610.32431](http://arxiv.org/abs/2610.32431v1)
- **Published**: 2026-10-23
- **Categories**: cs.AI

> A failed vision-language-action (VLA) rollout does not imply that every action contributed to failure. Yet in group-relative policy optimization (GRPO), a single trajectory-level advantage is assigned to all actions in a rollout. Potentially useful recovery attempts can thus be penalized alongside t...

### Rethinking LoRA Initialization for Robust Asymmetric Learning Rates
- **Authors**: Disen Liao, Yaoliang Yu
- **arXiv**: [2610.32142](http://arxiv.org/abs/2610.32142v1)
- **Published**: 2026-10-23
- **Categories**: cs.LG, cs.AI

> Low-Rank Adaptation (LoRA) is often highly sensitive to learning-rate (LR) choices. Recent empirical studies suggest that, once LRs are carefully tuned, vanilla LoRA can remain competitive with many proposed LoRA variants. This shifts the central practical question from designing ever more variants ...

### FSVL: Taxonomic Fast-Slow Vision-to-Language Collaborative Framework for Interpretable Confusable Fish Species Identification and Knowledge Generation in the Middle Yangtze River
- **Authors**: Meng Liang, Fucheng Wang, Lang Zhao, Jun Chen, Ziying Li, Yuxiang Zhao, Haozhuang Chi, Wenkai Fang, Qiong Zhou, Junlin Yang, Jinming Wu
- **arXiv**: [2610.31880](http://arxiv.org/abs/2610.31880v1)
- **Published**: 2026-10-22
- **Categories**: cs.CV, cs.AI

> The Yangtze River Basin is a critical region for freshwater biodiversity conservation. The implementation of the Yangtze River Ten-Year Fishing Ban has increased the importance of effective aquatic biodiversity monitoring and species-level identification. However, fine-grained identification of clos...

### Forecasting Associations, Not Interventions: A Preregistered Causal Audit of Covariate-Aware Time Series Foundation Models
- **Authors**: Zong-Han Bai
- **arXiv**: [2610.31869](http://arxiv.org/abs/2610.31869v1)
- **Published**: 2026-10-22
- **Categories**: cs.LG

> Covariate-aware time series foundation models (TSFMs) accept a future path for a control variable and return a forecast, inviting what-if queries. The query is interventional; the models are trained on observational data. We determine whether their answers are the conditional slope $\partial E[Y|X]$...

### Don't Forget What You Just Learned: Self-Directed Repair Turns Agent Mistakes Into Lasting Lessons
- **Authors**: Yuval Kansal, Karen Ullrich, Polina Kirichenko, Ilia Kulikov, Niraj K. Jha, Mohammad Pezeshki, Mark Ibrahim
- **arXiv**: [2610.31846](http://arxiv.org/abs/2610.31846v1)
- **Published**: 2026-10-22
- **Categories**: cs.AI, cs.LG

> Intelligent agents should learn from their mistakes so that experience leads to continuous improvement. Yet today's agents recover from a mistake only temporarily: in-context reflections are easily forgotten across sessions and compete for limited context, while full-parameter fine-tuning is expensi...

### AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark
- **Authors**: Ruicong Liu, Liangyang Ouyang, Fengbo Lan, Zhixiang Wang, Kaipeng Zhang
- **arXiv**: [2610.31466](http://arxiv.org/abs/2610.31466v1)
- **Published**: 2026-10-22
- **Categories**: cs.CV

> AI coding agents can now build small playable games in minutes, but the results usually look like programmer art: gray blockouts, colored geometric primitives, and flat semantic blobs. We present AnyGameRenderer, a video-to-video generative renderer that turns such footage into high-quality visuals ...

### LoRA Superposition across Pretrained Models
- **Authors**: Keigo Watanabe, Hiroshi Kera, Kazuhiko Kawamoto
- **arXiv**: [2610.30691](http://arxiv.org/abs/2610.30691v1)
- **Published**: 2026-10-22
- **Categories**: cs.CV, cs.AI

> Low-rank adaptation (LoRA) is usually tied to the pretrained backbone on which it is learned. We ask whether LoRAs trained independently for the same task on different pretrained backbones can be summed and applied unchanged to all contributing backbones. We call this construction LoRA superposition...

### NormTune: Norm-Guided Parameter-Efficient Fine-Tuning for Reasoning-Intensive Tasks
- **Authors**: Zhangming Li, Qinghao Hu, Weifan Guan, Yifan Zhang, Peisong Wang, Jian Cheng
- **arXiv**: [2610.29134](http://arxiv.org/abs/2610.29134v1)
- **Published**: 2026-10-21
- **Categories**: cs.AI

> Full fine-tuning has achieved remarkable success on reasoning-intensive tasks, but it often requires substantial GPU resource consumption. Parameter-efficient fine-tuning (PEFT) provides a promising alternative for reducing this cost, yet we observe a substantial performance gap on reasoning-intensi...

### Complexity-Aware Surgical Video Reasoning Segmentation with Digital Twin and Context Memory
- **Authors**: Yiqing Shen, Mathias Unberath
- **arXiv**: [2610.28776](http://arxiv.org/abs/2610.28776v1)
- **Published**: 2026-10-20
- **Categories**: cs.CV

> Conventional surgical segmentation relies on closed-set categories or explicit text queries, which cannot resolve implicit queries that require reasoning about workflows, instrument functions, and temporal relationships. To address these limitations, we propose SurgReasonSeg, a complexity-aware meth...

### Parameter-Efficient Adaptation of Time Series Foundation Models for Electrical Load Forecasting
- **Authors**:  Aliullah, Julian Oelhaf, Edouard Fouché, Jessica Deuschel, Christian Bergler, Andreas Maier, Siming Bayer
- **arXiv**: [2610.28200](http://arxiv.org/abs/2610.28200v1)
- **Published**: 2026-10-20
- **Categories**: cs.LG, cs.AI

> Accurate electrical load forecasting supports power-system operation across countries, regions, cities, and buildings, but repeated development of target-specific models is costly. Time series foundation models (TSFMs) provide reusable pretrained backbones, although multi-domain pretraining may not ...

### Temporal Evidence-Parameter Co-Alignment for LLM Reasoning over Temporal Knowledge Graphs
- **Authors**: Jiapu Wang
- **arXiv**: [2610.28176](http://arxiv.org/abs/2610.28176v1)
- **Published**: 2026-10-20
- **Categories**: cs.CL, cs.AI

> Large Language Models (LLMs) often struggle with temporally grounded reasoning because their static parametric memory is misaligned with the dynamic evolution of real-world knowledge. Although RAG and Parameter-Efficient Fine-Tuning (PEFT) provide practical ways to enhance LLMs, they remain insuffic...

### MuPACE: Learning to Pace Muon for LoRA Fine-Tuning
- **Authors**: Jan Kobiolka, Christian Frey, Josif Grabocka
- **arXiv**: [2610.28072](http://arxiv.org/abs/2610.28072v1)
- **Published**: 2026-10-20
- **Categories**: cs.LG

> Learning rate schedules are typically fixed before training begins, yet when fine-tuning large language models with low-rank adapters (LoRA), the appropriate scale varies substantially with the model, task, and adapter configuration. Practitioners re-tune a schedule for every new problem, yet a tune...

### From Tokens to Files: Multi-Granularity Detection and Localization of AI-Involved Code
- **Authors**: Yue Xu, Xiyang Wang, Hui Liu, Bolei He
- **arXiv**: [2610.27863](http://arxiv.org/abs/2610.27863v1)
- **Published**: 2026-10-20
- **Categories**: cs.SE, cs.CL, cs.LG

> The increasing use of large language models for code generation calls for methods that distinguish purely human-written code from AI-involved code: files in which any part, however small, was generated or substantially modified by a model. Beyond flagging such files, we aim to localize the lines or ...

### LoRASpace: A Pool-Wide Shared Substrate for Static and Dynamic Multi-LoRA Composition
- **Authors**: Thamirawaran Sathiyalogeswaran, Navindu De Silva, Chamikara Siriwardane, W. K. Alwis, Jason Mars, Udaya Sampath K. Perera Miriya Thanthrige, Ranga Rodrigo
- **arXiv**: [2610.27444](http://arxiv.org/abs/2610.27444v1)
- **Published**: 2026-10-20
- **Categories**: cs.CV, cs.LG

> Low-rank adaptation (LoRA) attaches small low-rank matrices to a frozen backbone, and public repositories host many LoRAs per backbone, each for a different concept or task. Combining several LoRAs in one generation forces a trade-off. Merging their weights into one update needs a single forward pas...

### LSA-PAST: Layer-Specific Adaptation and Prototype Transport for Compositional Incremental Learning
- **Authors**: Kyle Stein, Andrew Arash Mahyari, Guillermo Francia, Eman El-Sheikh, Jiangpeng He
- **arXiv**: [2610.27203](http://arxiv.org/abs/2610.27203v1)
- **Published**: 2026-10-19
- **Categories**: cs.AI

> Class-Incremental Learning (CIL) enables models to recognize new classes over time while retaining prior knowledge, but many real-world problems are compositional, where visual concepts arise from combinations of primitives such as states (i.e., red, shiny) and objects (i.e., shoe, car). Standard CI...

### Scaling Parameter-Efficient Fine-Tuning for Brain Encoding
- **Authors**: Zhuofan Josh Ying, Guanglong Sun, Nolan Ho, Kieran Liu, Rui Yang, Andrew Chen, Nikolaus Kriegeskorte, Pony Ma, Hossein Adeli
- **arXiv**: [2610.26802](http://arxiv.org/abs/2610.26802v1)
- **Published**: 2026-10-19
- **Categories**: cs.LG

> Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or fully fine-tune them after task-pretraining has proven difficult because neural data is costly and l...

### TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning
- **Authors**: Liana Patel, Rishabh Ranjan, Ion Stoica, Matei Zaharia, Carlos Guestrin
- **arXiv**: [2610.26754](http://arxiv.org/abs/2610.26754v1)
- **Published**: 2026-10-19
- **Categories**: cs.CL, cs.AI

> Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters. On the other hand, language models process all input tokens through each model layer, resulting in significant processing costs for long-context inputs. We introduce ...

### An Empirical Study of Parameter-Efficient Fine-Tuning for Mixture-of-Experts LLMs
- **Authors**: Minglei Li, Peng Ye, Haonan He, Jingqi Ye, Qingyu Yang, Tao Chen
- **arXiv**: [2610.26370](http://arxiv.org/abs/2610.26370v1)
- **Published**: 2026-10-19
- **Categories**: cs.LG, cs.CL

> Parameter-efficient fine-tuning (PEFT) methods are critical for adapting large models under resource-constrained settings. However, as mixture-of-experts (MoE) architectures, which offer efficient inference at massive parameter scales, gain increasing prevalence in the community, a critical gap aris...

### TaQFormer: A Treatment-as-Query Transformer with Data-Fusion for Multidimensional Treatment Modeling in Coupon Allocation
- **Authors**: Jiahong Li, Zeqin Yang, Yu Xiang, Zhifan Jiang, Jingqi Ma, Enzheng Hua, Jixing Xu, Jun Wu, Fei Wang, Enyun Yu, Jiecheng Guo
- **arXiv**: [2610.26199](http://arxiv.org/abs/2610.26199v1)
- **Published**: 2026-10-19
- **Categories**: cs.LG

> We study coupon allocation on an online marketplace offering multiple service categories. Issuing coupons requires choosing a vector of category-specific discounts, accounting for both their direct effects and cross-category demand shifts. We present TaQFormer, a treatment-as-query Transformer for t...

### Residual-Guided Adaptive Tucker Rank Allocation for Parameter-Efficient MCI Conversion Prediction
- **Authors**: Guanghua He, Hancan Zhu, Gaohang Yu, An Zhang
- **arXiv**: [2610.25873](http://arxiv.org/abs/2610.25873v1)
- **Published**: 2026-10-19
- **Categories**: cs.LG

> Allocating limited trainable capacity across convolutional layers is a central challenge in parameter-efficient fine-tuning (PEFT) of pretrained three-dimensional (3D) networks. We propose Residual-Guided Adaptive Tucker Rank Allocation, which jointly selects input- and output-channel ranks under a ...

### Communication-Efficient Federated Domain Generalization in Edge Networks via Dynamic Prototype Regulation
- **Authors**: Yuankun Xia, Hui Wang, Ling Yuan, Ziyu Hong, Di Yin, Yufeng Zhou
- **arXiv**: [2610.25810](http://arxiv.org/abs/2610.25810v1)
- **Published**: 2026-10-19
- **Categories**: cs.LG

> Federated learning (FL) is a distributed paradigm for Internet of Things (IoT) edge networks. However, deploying Vision-Language Models (VLMs) over wireless edge networks presents distinct challenges: large model parameters increase uplink transmission latency over bandwidth-constrained fading chann...

### PFedQFT: Personalized Federated Quantum-Inspired Fine-Tuning for Medical Large Language Models
- **Authors**: Qihan Huang, Lingxia Zhang, Guye Zhang, Zizhu Wang, Xiaowei Mao
- **arXiv**: [2610.25712](http://arxiv.org/abs/2610.25712v1)
- **Published**: 2026-10-19
- **Categories**: cs.AI

> Medical data remain fragmented across institutional silos because of privacy, governance, and ownership constraints. Federated learning enables medical institutions to adapt large language models (LLMs) collaboratively without transferring raw records. However, independently parameterized low-rank a...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "masiak-2026",
    "title": "Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery",
    "authors": [
      "Marek Masiak",
      "Andrzej Szablewski",
      "Nicola Cancedda",
      "Constantin Venhoff"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.32866",
    "paper_url": "https://arxiv.org/abs/2610.32866",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "ferry-2026",
    "title": "Singular Geometry of Low-Rank Adaptation",
    "authors": [
      "Kamillo Ferry",
      "Anthea Monod",
      "Keisuke Yano"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.32854",
    "paper_url": "https://arxiv.org/abs/2610.32854",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "zhao-2026",
    "title": "When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning",
    "authors": [
      "Zongyao Zhao",
      "Cheng-Jie Zhao",
      "Ruihang Jiang",
      "Bing Zheng",
      "Zhaolin Wang",
      "Yuanwei Liu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.32431",
    "paper_url": "https://arxiv.org/abs/2610.32431",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "liao-2026",
    "title": "Rethinking LoRA Initialization for Robust Asymmetric Learning Rates",
    "authors": [
      "Disen Liao",
      "Yaoliang Yu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.32142",
    "paper_url": "https://arxiv.org/abs/2610.32142",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "liang-2026",
    "title": "FSVL: Taxonomic Fast-Slow Vision-to-Language Collaborative Framework for Interpretable Confusable Fish Species Identification and Knowledge Generation in the Middle Yangtze River",
    "authors": [
      "Meng Liang",
      "Fucheng Wang",
      "Lang Zhao",
      "Jun Chen",
      "Ziying Li",
      "Yuxiang Zhao",
      "Haozhuang Chi",
      "Wenkai Fang",
      "Qiong Zhou",
      "Junlin Yang",
      "Jinming Wu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.31880",
    "paper_url": "https://arxiv.org/abs/2610.31880",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "bai-2026",
    "title": "Forecasting Associations, Not Interventions: A Preregistered Causal Audit of Covariate-Aware Time Series Foundation Models",
    "authors": [
      "Zong-Han Bai"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.31869",
    "paper_url": "https://arxiv.org/abs/2610.31869",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "kansal-2026",
    "title": "Don't Forget What You Just Learned: Self-Directed Repair Turns Agent Mistakes Into Lasting Lessons",
    "authors": [
      "Yuval Kansal",
      "Karen Ullrich",
      "Polina Kirichenko",
      "Ilia Kulikov",
      "Niraj K. Jha",
      "Mohammad Pezeshki",
      "Mark Ibrahim"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.31846",
    "paper_url": "https://arxiv.org/abs/2610.31846",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "liu-2026",
    "title": "AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark",
    "authors": [
      "Ruicong Liu",
      "Liangyang Ouyang",
      "Fengbo Lan",
      "Zhixiang Wang",
      "Kaipeng Zhang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.31466",
    "paper_url": "https://arxiv.org/abs/2610.31466",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "watanabe-2026",
    "title": "LoRA Superposition across Pretrained Models",
    "authors": [
      "Keigo Watanabe",
      "Hiroshi Kera",
      "Kazuhiko Kawamoto"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.30691",
    "paper_url": "https://arxiv.org/abs/2610.30691",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "li-2026",
    "title": "NormTune: Norm-Guided Parameter-Efficient Fine-Tuning for Reasoning-Intensive Tasks",
    "authors": [
      "Zhangming Li",
      "Qinghao Hu",
      "Weifan Guan",
      "Yifan Zhang",
      "Peisong Wang",
      "Jian Cheng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.29134",
    "paper_url": "https://arxiv.org/abs/2610.29134",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "shen-2026",
    "title": "Complexity-Aware Surgical Video Reasoning Segmentation with Digital Twin and Context Memory",
    "authors": [
      "Yiqing Shen",
      "Mathias Unberath"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.28776",
    "paper_url": "https://arxiv.org/abs/2610.28776",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "aliullah-2026",
    "title": "Parameter-Efficient Adaptation of Time Series Foundation Models for Electrical Load Forecasting",
    "authors": [
      " Aliullah",
      "Julian Oelhaf",
      "Edouard Fouché",
      "Jessica Deuschel",
      "Christian Bergler",
      "Andreas Maier",
      "Siming Bayer"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.28200",
    "paper_url": "https://arxiv.org/abs/2610.28200",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "wang-2026",
    "title": "Temporal Evidence-Parameter Co-Alignment for LLM Reasoning over Temporal Knowledge Graphs",
    "authors": [
      "Jiapu Wang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.28176",
    "paper_url": "https://arxiv.org/abs/2610.28176",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "kobiolka-2026",
    "title": "MuPACE: Learning to Pace Muon for LoRA Fine-Tuning",
    "authors": [
      "Jan Kobiolka",
      "Christian Frey",
      "Josif Grabocka"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.28072",
    "paper_url": "https://arxiv.org/abs/2610.28072",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "xu-2026",
    "title": "From Tokens to Files: Multi-Granularity Detection and Localization of AI-Involved Code",
    "authors": [
      "Yue Xu",
      "Xiyang Wang",
      "Hui Liu",
      "Bolei He"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.27863",
    "paper_url": "https://arxiv.org/abs/2610.27863",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "sathiyalogeswaran-2026",
    "title": "LoRASpace: A Pool-Wide Shared Substrate for Static and Dynamic Multi-LoRA Composition",
    "authors": [
      "Thamirawaran Sathiyalogeswaran",
      "Navindu De Silva",
      "Chamikara Siriwardane",
      "W. K. Alwis",
      "Jason Mars",
      "Udaya Sampath K. Perera Miriya Thanthrige",
      "Ranga Rodrigo"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.27444",
    "paper_url": "https://arxiv.org/abs/2610.27444",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "stein-2026",
    "title": "LSA-PAST: Layer-Specific Adaptation and Prototype Transport for Compositional Incremental Learning",
    "authors": [
      "Kyle Stein",
      "Andrew Arash Mahyari",
      "Guillermo Francia",
      "Eman El-Sheikh",
      "Jiangpeng He"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.27203",
    "paper_url": "https://arxiv.org/abs/2610.27203",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "ying-2026",
    "title": "Scaling Parameter-Efficient Fine-Tuning for Brain Encoding",
    "authors": [
      "Zhuofan Josh Ying",
      "Guanglong Sun",
      "Nolan Ho",
      "Kieran Liu",
      "Rui Yang",
      "Andrew Chen",
      "Nikolaus Kriegeskorte",
      "Pony Ma",
      "Hossein Adeli"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.26802",
    "paper_url": "https://arxiv.org/abs/2610.26802",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "patel-2026",
    "title": "TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning",
    "authors": [
      "Liana Patel",
      "Rishabh Ranjan",
      "Ion Stoica",
      "Matei Zaharia",
      "Carlos Guestrin"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.26754",
    "paper_url": "https://arxiv.org/abs/2610.26754",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "li-2026",
    "title": "An Empirical Study of Parameter-Efficient Fine-Tuning for Mixture-of-Experts LLMs",
    "authors": [
      "Minglei Li",
      "Peng Ye",
      "Haonan He",
      "Jingqi Ye",
      "Qingyu Yang",
      "Tao Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.26370",
    "paper_url": "https://arxiv.org/abs/2610.26370",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "li-2026",
    "title": "TaQFormer: A Treatment-as-Query Transformer with Data-Fusion for Multidimensional Treatment Modeling in Coupon Allocation",
    "authors": [
      "Jiahong Li",
      "Zeqin Yang",
      "Yu Xiang",
      "Zhifan Jiang",
      "Jingqi Ma",
      "Enzheng Hua",
      "Jixing Xu",
      "Jun Wu",
      "Fei Wang",
      "Enyun Yu",
      "Jiecheng Guo"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.26199",
    "paper_url": "https://arxiv.org/abs/2610.26199",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "he-2026",
    "title": "Residual-Guided Adaptive Tucker Rank Allocation for Parameter-Efficient MCI Conversion Prediction",
    "authors": [
      "Guanghua He",
      "Hancan Zhu",
      "Gaohang Yu",
      "An Zhang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.25873",
    "paper_url": "https://arxiv.org/abs/2610.25873",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "xia-2026",
    "title": "Communication-Efficient Federated Domain Generalization in Edge Networks via Dynamic Prototype Regulation",
    "authors": [
      "Yuankun Xia",
      "Hui Wang",
      "Ling Yuan",
      "Ziyu Hong",
      "Di Yin",
      "Yufeng Zhou"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.25810",
    "paper_url": "https://arxiv.org/abs/2610.25810",
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
    "added_date": "2026-10-26"
  },
  {
    "id": "huang-2026",
    "title": "PFedQFT: Personalized Federated Quantum-Inspired Fine-Tuning for Medical Large Language Models",
    "authors": [
      "Qihan Huang",
      "Lingxia Zhang",
      "Guye Zhang",
      "Zizhu Wang",
      "Xiaowei Mao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.25712",
    "paper_url": "https://arxiv.org/abs/2610.25712",
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
    "added_date": "2026-10-26"
  }
]
```
