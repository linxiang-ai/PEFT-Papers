# New arXiv PEFT papers — 2026-06-08

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **30**.

## Candidates

### Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling
- **Authors**: Rohan Shravan
- **arXiv**: [2606.07404](http://arxiv.org/abs/2606.07404v1)
- **Published**: 2026-06-05
- **Categories**: cs.LG

> This paper reports on training a hundred-billion-parameter sparse mixture of experts on a single eight-GPU node, end to end. LightningLM 0.1V is a recurrence-backbone language model family grown in four stages from a small dense seed, through a 5B and a 9B mixture of experts, to a 120B model with 46...

### Entropy as a Structural Prior: How a Log-Barrier on DiT Belief Space Drives Musical Diversity and Development
- **Authors**: Zixi Li, Youzhen Li
- **arXiv**: [2606.07207](http://arxiv.org/abs/2606.07207v1)
- **Published**: 2026-06-05
- **Categories**: cs.SD, cs.LG, eess.AS

> Confidence-based loss weighting is usually avoided in generative models because it accelerates errors when the model is confidently wrong, but this intuition breaks down in supervised diffusion training. We introduce the Eisbach log-barrier, a parameter-free weight derived from the entropy of the Di...

### TraRA: Trajectory-level Recognition Aggregation for Video Text Spotting in Urban Surveillance
- **Authors**: Duc Tri Tran, Trung Thanh Nguyen, Vijay John, Phi Le Nguyen, Yasutomo Kawanishi
- **arXiv**: [2606.07161](http://arxiv.org/abs/2606.07161v1)
- **Published**: 2026-06-05
- **Categories**: cs.CV

> Video Text Spotting (VTS) is essential for urban surveillance and intelligent transportation systems, enabling automated reading of street signs, vehicle markings, and scene text in video streams. However, reliable recognition remains challenging due to dynamic video factors common in surveillance s...

### Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition
- **Authors**: Tung X. Nguyen, Hieu Minh Truong, Giang-Son Nguyen, Nhu Vo, Wray Buntine, Dung D. Le
- **arXiv**: [2606.06985](http://arxiv.org/abs/2606.06985v1)
- **Published**: 2026-06-05
- **Categories**: cs.CL, eess.AS

> Code-switching (CS), the alternation between multiple languages within a single utterance, remains challenging for Automatic Speech Recognition (ASR). To address this issue, we propose a Point-of-Interest (POI)-aware contrastive training framework that improves recognition at CS-critical regions. We...

### Auditing Training Data in Domain-adapted LLMs: LoRA-MINT
- **Authors**: Gonzalo Mancera, Daniel DeAlcala, Aythami Morales, Julian Fierrez, Ruben Tolosana, Francisco Jurado
- **arXiv**: [2606.06946](http://arxiv.org/abs/2606.06946v1)
- **Published**: 2026-06-05
- **Categories**: cs.CL, cs.AI

> We present LoRA-MINT, a new methodology for Membership Inference Test (MINT) applied to recent Large Language Models (LLMs) fine-tuned for specific Natural Language Processing (NLP) tasks through Low-Rank Adaptation (LoRA). The primary goal is to assess whether individual samples were part of the tr...

### The Fine-Tuning Trap: Evaluating Negative Transfer and the Role of PEFT in Sub-1B Mathematical Reasoning
- **Authors**: Rahul Nair, Chun Tao
- **arXiv**: [2606.06920](http://arxiv.org/abs/2606.06920v1)
- **Published**: 2026-06-05
- **Categories**: cs.LG, cs.AI

> Deploying Small Language Models (SLMs) on edge devices requires efficient fine-tuning strategies that adapt models to new tasks without degrading their general capabilities. In this study, we benchmark five sub-1B models (135M-1B) on mathematical reasoning tasks and uncover a critical vulnerability:...

### TALAN: Task-Aligned Latent Adaptation Networks for Targeted Post-Training of Large Language Models
- **Authors**: Chengkai Zhang, Ziteng Liu, Junpu Wang, Zeyi Tao, Yang Wang, Sagar Chordia, Qin Huang
- **arXiv**: [2606.06902](http://arxiv.org/abs/2606.06902v1)
- **Published**: 2026-06-05
- **Categories**: cs.LG

> Targeted post-training aims to improve reasoning, math, and code without degrading strengths. Low-rank adapters are efficient but task-global; activation interventions are input-aware but often require separate probes, vectors, or inference-time steering. We introduce TALAN (Task-Aligned Latent Adap...

### Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution
- **Authors**: Liliana Hotsko, Yinxi Li, Yuntian Deng, Pengyu Nie
- **arXiv**: [2606.06492](http://arxiv.org/abs/2606.06492v1)
- **Published**: 2026-06-04
- **Categories**: cs.SE, cs.AI, cs.CL

> Code language models need repository-level context to resolve imports, APIs, and project conventions. Existing methods inject this knowledge as long inputs (retrieved through RAG or dependency analysis) or through per-repository fine-tuning and LoRA -- costly at repository scale and brittle to evolv...

### FiLM-Based Speaker Conditioning of a SpeechLLM for Pathological Speech Recognition
- **Authors**: Fernando López, Santosh Kesiraju, Jordi Luque
- **arXiv**: [2606.06211](http://arxiv.org/abs/2606.06211v1)
- **Published**: 2026-06-04
- **Categories**: cs.CL, cs.SD, eess.AS

> Automatic speech recognition (ASR) has advanced remarkably for standard speech; however, pathological speech from neurological conditions remains a significant challenge. We investigate speaker conditioning via Feature-wise Linear Modulation (FiLM), injecting x-vector-derived information into each t...

### Amortizing Federated Adaptation: Hypernetwork Driven LoRA for Personalized Foundation Models
- **Authors**: Sunny Gupta, Shambhavi Shanker, Amit Sethi
- **arXiv**: [2606.06154](http://arxiv.org/abs/2606.06154v1)
- **Published**: 2026-06-04
- **Categories**: cs.AI

> Federated fine-tuning of foundation models using Low-Rank Adaptation (LoRA) offers a communication efficient solution for distributed learning. However, existing federated LoRA methods suffer from two fundamental limitations: (1) structural aggregation bias, where independently averaging low rank fa...

### TLA-Prover: Verifiable TLA+ Specification Synthesis via Preference-Optimized Low-Rank Adaptation
- **Authors**: Eric Spencer, Arslan Bisharat, Brian Ortiz, Khushboo Bhadauria, TaiNing Wang, George K. Thiruvathukal, Konstantin Laufer, Mohammed Abuhamad
- **arXiv**: [2606.06133](http://arxiv.org/abs/2606.06133v1)
- **Published**: 2026-06-04
- **Categories**: cs.SE, cs.AI, cs.LG, cs.LO

> TLA+ is a formal specification language for verifying distributed systems and safety-critical protocols. Large language models (LLMs) frequently produce TLA+ specifications that fail the TLC model checker for semantic reasons. Across 25 LLMs, the best public baseline is 26.6% syntactic parse and 8.6...

### HyperVis: Continuous Latent Visual Relational Graphs on the Lorentz Hyperboloid for Compositional Reasoning
- **Authors**: Moshiur Farazi, Sameera Ramasinghe, Mahbub Ahmed Turza, Shafin Rahman
- **arXiv**: [2606.06100](http://arxiv.org/abs/2606.06100v1)
- **Published**: 2026-06-04
- **Categories**: cs.CV

> Vision-Language Models (VLMs) struggle with compositional reasoning that requires understanding inter-object relationships. A natural remedy is to inject explicit scene graph triplets $\langle s, p, o \rangle$ from an off-the-shelf scene graph generator (SGG), but we show this backfires: discrete te...

### High-Dimensional Theory of LoRA Fine-Tuning in a Solvable Attention Model
- **Authors**: O. Duranthon, F. Boncoraglio, L. Zdeborová
- **arXiv**: [2606.05899](http://arxiv.org/abs/2606.05899v1)
- **Published**: 2026-06-04
- **Categories**: cs.LG, cond-mat.dis-nn

> We develop a high-dimensional statistical theory of low-rank adaptation (LoRA) in attention models, capturing the interplay between pre-training and fine-tuning. We introduce a solvable framework in which a single-head attention layer is first pre-trained on a data-abundant task and subsequently ada...

### Emotion-Aware Image Generation from Korean Diary Text via LLM-based Prompt Translation and LoRA Fine-Tuning
- **Authors**: Jihun Cho, Soo-Yeon Jeong, Sun-Young Ihm
- **arXiv**: [2606.05816](http://arxiv.org/abs/2606.05816v1)
- **Published**: 2026-06-04
- **Categories**: cs.CV, cs.AI

> T2I models cannot effectively capture sentiment from various types of text, including diaries, as they primarily focus on visual object-related patterns rather than contextual emotional understanding. This paper proposes an emotion-aware text-to-image pipeline that generates children's hand drawing ...

### Domain-Adapted Small Language Models with Hybrid Post-Processing: Achieving Cost-Efficient, Low-Latency Multi-Label Structured Prediction via LoRA Fine-Tuning on Scarce Data
- **Authors**: Srinivasan Manoharan, Dilipkumar Nallusamy, Sachin Kumar, Haifeng Wu
- **arXiv**: [2606.05781](http://arxiv.org/abs/2606.05781v1)
- **Published**: 2026-06-04
- **Categories**: cs.LG

> Deploying frontier large language models (LLMs) for domain-specific structured evaluation tasks often incurs substantial latency, cost, and data privacy overhead. We present a hybrid framework that combines a fine-tuned small language model (LLaMA 3.1 8B, with only 2.05% trainable parameters via LoR...

### Noise-Aware Visual Representation Learning for Medical Visual Question Answering
- **Authors**: I Putu Adi Pratama, Bahadorreza Ofoghi, Atul Sajjanhar, Shang Gao
- **arXiv**: [2606.05535](http://arxiv.org/abs/2606.05535v1)
- **Published**: 2026-06-04
- **Categories**: cs.CV, cs.AI

> Medical visual question answering (Med-VQA) has strong potential for clinical decision support by enabling AI models to interpret medical images and answer clinically relevant queries. Recent approaches typically connect off-the-shelf vision encoders with large language models (LLMs) through lightwe...

### Video2LoRA: Parametric Video Internalization for Vision-Language Models
- **Authors**: Manan Suri, Sarvesh Baskar, Dinesh Manocha
- **arXiv**: [2606.04351](http://arxiv.org/abs/2606.04351v1)
- **Published**: 2026-06-03
- **Categories**: cs.CV, cs.CL

> Processing video in vision-language models is expensive: each frame occupies hundreds of tokens, and inference cost scales with every frame and every repeated query. We introduce Video2LoRA, a method for parametric video internalization. A perceiver hypernetwork reads the intermediate representation...

### Parameter-Efficient Fine-Tuning with Learnable Rank
- **Authors**: Arpit Garg, Simon Lucey, Hemanth Saratchandran
- **arXiv**: [2606.04325](http://arxiv.org/abs/2606.04325v1)
- **Published**: 2026-06-03
- **Categories**: cs.CL

> Low-Rank Adaptation (LoRA) is a popular parameter-efficient fine-tuning (PEFT) method that restricts weight updates to low-rank adapters, introducing a fixed low-rank inductive bias by optimizing in a low-dimensional subspace. In this work, we question whether a fixed-rank constraint is the most eff...

### Recover-LoRA for Aggressive Quantization: Reclaiming Accuracy in 2-Bit Language Models via Low-Rank Adaptation with Knowledge Distillation on Synthetic Data
- **Authors**: Devleena Das, Rajeev Patwari, Elliott Delaye, Ashish Sirasao
- **arXiv**: [2606.04238](http://arxiv.org/abs/2606.04238v1)
- **Published**: 2026-06-02
- **Categories**: cs.LG, cs.AI

> Aggressive weight quantization to 2-bit precision offers substantial throughput and memory gains for large language model (LLM) inference, but typically incurs severe accuracy degradation. These gains are particularly relevant for edge and on-device deployment, where memory capacity and bandwidth ar...

### Where Do We (Not) Need Temporal Context in Low-Resource Video Task Adaptation?
- **Authors**: Luc P. J. Sträter, Hazel Doughty
- **arXiv**: [2606.03837](http://arxiv.org/abs/2606.03837v1)
- **Published**: 2026-06-02
- **Categories**: cs.CV

> Parameter-efficient fine-tuning (PEFT) and probing enable adaptation of foundation models using only a small number of trainable parameters, making it attractive for video understanding where annotation and computation are expensive. However, video PEFT has focused on adapting image-pretrained model...

### Training-Free Multi-Concept LoRA Composition with Prompt-Aware Weighting
- **Authors**: Georgios Tsoumplekas, Stella Bounareli, Vasileios Argyriou
- **arXiv**: [2606.03792](http://arxiv.org/abs/2606.03792v1)
- **Published**: 2026-06-02
- **Categories**: cs.CV, cs.LG

> Low-Rank Adaptation (LoRA) successfully enables personalization in text-to-image generation by adapting pre-trained diffusion models to specific visual concepts and styles. However, extending such models to multi-concept customization remains challenging. Naively combining multiple LoRA weights or t...

### Compress then Merge: From Multiple LoRAs into One Low-Rank Adapter
- **Authors**: Zhengbao He, Ruiqi Ding, Zhehao Huang, Ruikai Yang, Tao Li, Xiaolin Huang
- **arXiv**: [2606.03723](http://arxiv.org/abs/2606.03723v1)
- **Published**: 2026-06-02
- **Categories**: cs.LG

> Low-rank adaptation (LoRA) enables parameter-efficient specialization of foundation models, but the proliferation of task-specific adapters fragments capabilities across many adapters, complicating reuse and deployment. We study the problem of merging $T$ LoRAs into a single rank-$r$ LoRA, thereby p...

### Decoupled Smart Contract Audits: Lightweight LLM Framework via Distillation and Aggregation
- **Authors**: Bagus Rakadyanto Oktavianto Putra, Muhamad Risqi Utama Saputra,  Widyawan, Guntur Dharma Putra
- **arXiv**: [2606.03128](http://arxiv.org/abs/2606.03128v1)
- **Published**: 2026-06-02
- **Categories**: cs.CR, cs.AI, cs.CL, cs.LG

> Smart contracts face critical security challenges that require thorough auditing in decentralized web services. While Large Language Models (LLMs) have shown promise in automated vulnerability detection, existing approaches lack severity evaluations with actionable remediation and demand unnecessari...

### ProtoAda: Prototype-Guided Adaptive Adapter Expansion and Geometric Consolidation for Multimodal Continual Instruction Tuning
- **Authors**: Yu-Cheng Shi, Zhen-Hao Xie, Jun-Tao Tang, Da-Wei Zhou
- **arXiv**: [2606.02576](http://arxiv.org/abs/2606.02576v2)
- **Published**: 2026-06-01
- **Categories**: cs.CV, cs.LG

> Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, but real-world deployment requires them to continually acquire new vision-language capabilities, making Multimodal Continual Instruction Tuning (MCIT) essential. To reduce inter-task interference and prom...

### On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters
- **Authors**: Mind Lab,  :, Vin Bo, Song Cao, Vic Cao, Andrew Chen, Kaijie Chen, Cleon Cheng, Steven Chiang, Kaixuan Fan, Hera Feng, Huan Feng, Arthur Fu, Jun Gao, Hongquan Gu, Aaron Guan, Nolan Ho, Mutian Hong, Hailee Hou, Peixuan Hua, Charles Huang, Miles Jiang, Nora Jiang, Yuyi Jiang, Qiuyu Jin, Fancy Kong, Andrew Lei, Kyrie Lei, Alexy Li, Lucian Li, Ray Li, Theo Li, Wenhao Li, Zhihui Li, Allen Lin, Jiayi Lin, Kairus Liu, Kieran Liu, Logan Liu, Xiang Liu, Irvine Lu, Maeve Luo, Runze Lv, Pony Ma, Verity Niu, Anson Qiu, Vincent Wang, Rio Yang, Maxwell Yao, Carrie Ye, Regis Ye, Wenlin Ye, Josh Ying, Danney Zeng, Yuhan Zhan, Anya Zhang, Di Zhang, Ruijia Zhang, Shiyang Zhang, Sueky Zhang, Ya Zhang, Wei Zhao, Ada Zhou, Adrian Zhou, Yuhua Zhou, Xinyue Zhu, Murphy Zhuang
- **arXiv**: [2606.02437](http://arxiv.org/abs/2606.02437v2)
- **Published**: 2026-06-01
- **Categories**: cs.LG, cs.CL

> Parameter-efficient fine-tuning (PEFT) is usually treated as a cheaper alternative to full fine-tuning. We study a broader role: small trainable adapters as persistent local state on top of strong shared foundation models. In this framing, the base model provides shared competence while adapters car...

### Parameter-efficient Dual-encoder Architecture with Differentiable Choquet Integral Fusion for Underwater Acoustic Classification
- **Authors**: Amirmohammad Mohammadi, Joshua Peeples, Alexandra Van Dine
- **arXiv**: [2606.02341](http://arxiv.org/abs/2606.02341v1)
- **Published**: 2026-06-01
- **Categories**: cs.SD, cs.LG

> Underwater acoustic classification has a wide array of oceanic applications, but faces challenges due to an increasingly complex acoustic environment. Waveform and spectrogram representations have been primarily used as acoustic data features for classification tasks in this domain. Spectrograms mod...

### Normality-Preserving Continual Industrial Anomaly Detection via Orthogonal LoRA Banks
- **Authors**: Weibai Fang, Haijun Che, Feiyang Ren, Qiancheng Lao
- **arXiv**: [2606.02042](http://arxiv.org/abs/2606.02042v1)
- **Published**: 2026-06-01
- **Categories**: cs.CV

> Continual industrial anomaly detection with diffusion models suffers from historical normality prior drift and catastrophic forgetting. Existing continual diffusion methods preserve previous knowledge through replay or constrained optimization, but they lack an explicit mechanism for isolating and p...

### Parameter-Efficient Fine-Tuning of Large Pretrained Models for Instance Segmentation Tasks
- **Authors**: Nermeen Abou Baker, David Rohrschneider, Uwe Handmann
- **arXiv**: [2606.01947](http://arxiv.org/abs/2606.01947v1)
- **Published**: 2026-06-01
- **Categories**: cs.CV, cs.AI

> Research and applications in artificial intelligence have recently shifted with the rise of large pretrained models, which deliver state-of-the-art results across numerous tasks. However, the substantial increase in parameters introduces a need for parameter-efficient training strategies. Despite si...

### G2LoRA: Gradient Orthogonal Low-Rank Adaptation Framework for Graph Continual Learning on Text-Attributed Graphs
- **Authors**: Yuhan Wang, Yibo Ding, Yutong Ye, Mufan Zhao, Wenbo Zhang, Ruijie Wang, Jianxin Li
- **arXiv**: [2606.01873](http://arxiv.org/abs/2606.01873v1)
- **Published**: 2026-06-01
- **Categories**: cs.LG

> LLM-as-Aligner has emerged as a prevalent pre-training paradigm for Text-Attributed Graphs(TAGS), aligning graph and text modalities into a shared embedding space via CLIP-style contrastive learning. While effective on individual downstream tasks, we observe severe catastrophic forgetting when such ...

### LayerRoute: Input-Conditioned Adaptive Layer Skipping via LoRA Fine-Tuning for Agentic Language Models
- **Authors**: Prateek Kumar Sikdar
- **arXiv**: [2606.01838](http://arxiv.org/abs/2606.01838v1)
- **Published**: 2026-06-01
- **Categories**: cs.CL, cs.AI, cs.LG

> Agentic language model systems alternate between two structurally distinct step types: structured tool calls (short, deterministic, low perplexity) and open-ended planning/reasoning steps (long, complex, high perplexity). Despite this heterogeneity, current inference systems apply identical compute ...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "shravan-2026",
    "title": "Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling",
    "authors": [
      "Rohan Shravan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.07404",
    "paper_url": "https://arxiv.org/abs/2606.07404",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "li-2026",
    "title": "Entropy as a Structural Prior: How a Log-Barrier on DiT Belief Space Drives Musical Diversity and Development",
    "authors": [
      "Zixi Li",
      "Youzhen Li"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.07207",
    "paper_url": "https://arxiv.org/abs/2606.07207",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "tran-2026",
    "title": "TraRA: Trajectory-level Recognition Aggregation for Video Text Spotting in Urban Surveillance",
    "authors": [
      "Duc Tri Tran",
      "Trung Thanh Nguyen",
      "Vijay John",
      "Phi Le Nguyen",
      "Yasutomo Kawanishi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.07161",
    "paper_url": "https://arxiv.org/abs/2606.07161",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "nguyen-2026",
    "title": "Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition",
    "authors": [
      "Tung X. Nguyen",
      "Hieu Minh Truong",
      "Giang-Son Nguyen",
      "Nhu Vo",
      "Wray Buntine",
      "Dung D. Le"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.06985",
    "paper_url": "https://arxiv.org/abs/2606.06985",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "mancera-2026",
    "title": "Auditing Training Data in Domain-adapted LLMs: LoRA-MINT",
    "authors": [
      "Gonzalo Mancera",
      "Daniel DeAlcala",
      "Aythami Morales",
      "Julian Fierrez",
      "Ruben Tolosana",
      "Francisco Jurado"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.06946",
    "paper_url": "https://arxiv.org/abs/2606.06946",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "nair-2026",
    "title": "The Fine-Tuning Trap: Evaluating Negative Transfer and the Role of PEFT in Sub-1B Mathematical Reasoning",
    "authors": [
      "Rahul Nair",
      "Chun Tao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.06920",
    "paper_url": "https://arxiv.org/abs/2606.06920",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "zhang-2026",
    "title": "TALAN: Task-Aligned Latent Adaptation Networks for Targeted Post-Training of Large Language Models",
    "authors": [
      "Chengkai Zhang",
      "Ziteng Liu",
      "Junpu Wang",
      "Zeyi Tao",
      "Yang Wang",
      "Sagar Chordia",
      "Qin Huang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.06902",
    "paper_url": "https://arxiv.org/abs/2606.06902",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "hotsko-2026",
    "title": "Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution",
    "authors": [
      "Liliana Hotsko",
      "Yinxi Li",
      "Yuntian Deng",
      "Pengyu Nie"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.06492",
    "paper_url": "https://arxiv.org/abs/2606.06492",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "l-pez-2026",
    "title": "FiLM-Based Speaker Conditioning of a SpeechLLM for Pathological Speech Recognition",
    "authors": [
      "Fernando López",
      "Santosh Kesiraju",
      "Jordi Luque"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.06211",
    "paper_url": "https://arxiv.org/abs/2606.06211",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "gupta-2026",
    "title": "Amortizing Federated Adaptation: Hypernetwork Driven LoRA for Personalized Foundation Models",
    "authors": [
      "Sunny Gupta",
      "Shambhavi Shanker",
      "Amit Sethi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.06154",
    "paper_url": "https://arxiv.org/abs/2606.06154",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "spencer-2026",
    "title": "TLA-Prover: Verifiable TLA+ Specification Synthesis via Preference-Optimized Low-Rank Adaptation",
    "authors": [
      "Eric Spencer",
      "Arslan Bisharat",
      "Brian Ortiz",
      "Khushboo Bhadauria",
      "TaiNing Wang",
      "George K. Thiruvathukal",
      "Konstantin Laufer",
      "Mohammed Abuhamad"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.06133",
    "paper_url": "https://arxiv.org/abs/2606.06133",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "farazi-2026",
    "title": "HyperVis: Continuous Latent Visual Relational Graphs on the Lorentz Hyperboloid for Compositional Reasoning",
    "authors": [
      "Moshiur Farazi",
      "Sameera Ramasinghe",
      "Mahbub Ahmed Turza",
      "Shafin Rahman"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.06100",
    "paper_url": "https://arxiv.org/abs/2606.06100",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "duranthon-2026",
    "title": "High-Dimensional Theory of LoRA Fine-Tuning in a Solvable Attention Model",
    "authors": [
      "O. Duranthon",
      "F. Boncoraglio",
      "L. Zdeborová"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.05899",
    "paper_url": "https://arxiv.org/abs/2606.05899",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "cho-2026",
    "title": "Emotion-Aware Image Generation from Korean Diary Text via LLM-based Prompt Translation and LoRA Fine-Tuning",
    "authors": [
      "Jihun Cho",
      "Soo-Yeon Jeong",
      "Sun-Young Ihm"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.05816",
    "paper_url": "https://arxiv.org/abs/2606.05816",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "manoharan-2026",
    "title": "Domain-Adapted Small Language Models with Hybrid Post-Processing: Achieving Cost-Efficient, Low-Latency Multi-Label Structured Prediction via LoRA Fine-Tuning on Scarce Data",
    "authors": [
      "Srinivasan Manoharan",
      "Dilipkumar Nallusamy",
      "Sachin Kumar",
      "Haifeng Wu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.05781",
    "paper_url": "https://arxiv.org/abs/2606.05781",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "pratama-2026",
    "title": "Noise-Aware Visual Representation Learning for Medical Visual Question Answering",
    "authors": [
      "I Putu Adi Pratama",
      "Bahadorreza Ofoghi",
      "Atul Sajjanhar",
      "Shang Gao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.05535",
    "paper_url": "https://arxiv.org/abs/2606.05535",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "suri-2026",
    "title": "Video2LoRA: Parametric Video Internalization for Vision-Language Models",
    "authors": [
      "Manan Suri",
      "Sarvesh Baskar",
      "Dinesh Manocha"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.04351",
    "paper_url": "https://arxiv.org/abs/2606.04351",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "garg-2026",
    "title": "Parameter-Efficient Fine-Tuning with Learnable Rank",
    "authors": [
      "Arpit Garg",
      "Simon Lucey",
      "Hemanth Saratchandran"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.04325",
    "paper_url": "https://arxiv.org/abs/2606.04325",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "das-2026",
    "title": "Recover-LoRA for Aggressive Quantization: Reclaiming Accuracy in 2-Bit Language Models via Low-Rank Adaptation with Knowledge Distillation on Synthetic Data",
    "authors": [
      "Devleena Das",
      "Rajeev Patwari",
      "Elliott Delaye",
      "Ashish Sirasao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.04238",
    "paper_url": "https://arxiv.org/abs/2606.04238",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "str-ter-2026",
    "title": "Where Do We (Not) Need Temporal Context in Low-Resource Video Task Adaptation?",
    "authors": [
      "Luc P. J. Sträter",
      "Hazel Doughty"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.03837",
    "paper_url": "https://arxiv.org/abs/2606.03837",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "tsoumplekas-2026",
    "title": "Training-Free Multi-Concept LoRA Composition with Prompt-Aware Weighting",
    "authors": [
      "Georgios Tsoumplekas",
      "Stella Bounareli",
      "Vasileios Argyriou"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.03792",
    "paper_url": "https://arxiv.org/abs/2606.03792",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "he-2026",
    "title": "Compress then Merge: From Multiple LoRAs into One Low-Rank Adapter",
    "authors": [
      "Zhengbao He",
      "Ruiqi Ding",
      "Zhehao Huang",
      "Ruikai Yang",
      "Tao Li",
      "Xiaolin Huang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.03723",
    "paper_url": "https://arxiv.org/abs/2606.03723",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "putra-2026",
    "title": "Decoupled Smart Contract Audits: Lightweight LLM Framework via Distillation and Aggregation",
    "authors": [
      "Bagus Rakadyanto Oktavianto Putra",
      "Muhamad Risqi Utama Saputra",
      " Widyawan",
      "Guntur Dharma Putra"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.03128",
    "paper_url": "https://arxiv.org/abs/2606.03128",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "shi-2026",
    "title": "ProtoAda: Prototype-Guided Adaptive Adapter Expansion and Geometric Consolidation for Multimodal Continual Instruction Tuning",
    "authors": [
      "Yu-Cheng Shi",
      "Zhen-Hao Xie",
      "Jun-Tao Tang",
      "Da-Wei Zhou"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.02576",
    "paper_url": "https://arxiv.org/abs/2606.02576",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "lab-2026",
    "title": "On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters",
    "authors": [
      "Mind Lab",
      " :",
      "Vin Bo",
      "Song Cao",
      "Vic Cao",
      "Andrew Chen",
      "Kaijie Chen",
      "Cleon Cheng",
      "Steven Chiang",
      "Kaixuan Fan",
      "Hera Feng",
      "Huan Feng",
      "Arthur Fu",
      "Jun Gao",
      "Hongquan Gu",
      "Aaron Guan",
      "Nolan Ho",
      "Mutian Hong",
      "Hailee Hou",
      "Peixuan Hua",
      "Charles Huang",
      "Miles Jiang",
      "Nora Jiang",
      "Yuyi Jiang",
      "Qiuyu Jin",
      "Fancy Kong",
      "Andrew Lei",
      "Kyrie Lei",
      "Alexy Li",
      "Lucian Li",
      "Ray Li",
      "Theo Li",
      "Wenhao Li",
      "Zhihui Li",
      "Allen Lin",
      "Jiayi Lin",
      "Kairus Liu",
      "Kieran Liu",
      "Logan Liu",
      "Xiang Liu",
      "Irvine Lu",
      "Maeve Luo",
      "Runze Lv",
      "Pony Ma",
      "Verity Niu",
      "Anson Qiu",
      "Vincent Wang",
      "Rio Yang",
      "Maxwell Yao",
      "Carrie Ye",
      "Regis Ye",
      "Wenlin Ye",
      "Josh Ying",
      "Danney Zeng",
      "Yuhan Zhan",
      "Anya Zhang",
      "Di Zhang",
      "Ruijia Zhang",
      "Shiyang Zhang",
      "Sueky Zhang",
      "Ya Zhang",
      "Wei Zhao",
      "Ada Zhou",
      "Adrian Zhou",
      "Yuhua Zhou",
      "Xinyue Zhu",
      "Murphy Zhuang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.02437",
    "paper_url": "https://arxiv.org/abs/2606.02437",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "mohammadi-2026",
    "title": "Parameter-efficient Dual-encoder Architecture with Differentiable Choquet Integral Fusion for Underwater Acoustic Classification",
    "authors": [
      "Amirmohammad Mohammadi",
      "Joshua Peeples",
      "Alexandra Van Dine"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.02341",
    "paper_url": "https://arxiv.org/abs/2606.02341",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "fang-2026",
    "title": "Normality-Preserving Continual Industrial Anomaly Detection via Orthogonal LoRA Banks",
    "authors": [
      "Weibai Fang",
      "Haijun Che",
      "Feiyang Ren",
      "Qiancheng Lao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.02042",
    "paper_url": "https://arxiv.org/abs/2606.02042",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "baker-2026",
    "title": "Parameter-Efficient Fine-Tuning of Large Pretrained Models for Instance Segmentation Tasks",
    "authors": [
      "Nermeen Abou Baker",
      "David Rohrschneider",
      "Uwe Handmann"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.01947",
    "paper_url": "https://arxiv.org/abs/2606.01947",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "wang-2026",
    "title": "G2LoRA: Gradient Orthogonal Low-Rank Adaptation Framework for Graph Continual Learning on Text-Attributed Graphs",
    "authors": [
      "Yuhan Wang",
      "Yibo Ding",
      "Yutong Ye",
      "Mufan Zhao",
      "Wenbo Zhang",
      "Ruijie Wang",
      "Jianxin Li"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.01873",
    "paper_url": "https://arxiv.org/abs/2606.01873",
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
    "added_date": "2026-06-08"
  },
  {
    "id": "sikdar-2026",
    "title": "LayerRoute: Input-Conditioned Adaptive Layer Skipping via LoRA Fine-Tuning for Agentic Language Models",
    "authors": [
      "Prateek Kumar Sikdar"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.01838",
    "paper_url": "https://arxiv.org/abs/2606.01838",
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
    "added_date": "2026-06-08"
  }
]
```
