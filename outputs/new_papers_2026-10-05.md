# New arXiv PEFT papers — 2026-10-05

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **47**.

## Candidates

### Query-aware routing for Cross-lingual performance gains in Encoders
- **Authors**: Akshay Jain, Edward Kim
- **arXiv**: [2610.02875](http://arxiv.org/abs/2610.02875v1)
- **Published**: 2026-10-02
- **Categories**: cs.CL, cs.AI, cs.IR

> Multilingual encoders can exhibit reduced retrieval effectiveness when queries and relevant documents differ in language, despite strong same-language performance. We investigate whether Finnish and Swedish cross-lingual retrieval can improve while preserving an encoder's existing same-language perf...

### Learn the Directions, Normalize the Gains: Post-Training Normalization for LoRA
- **Authors**: Zailong Tian, Yanzhe Chen, Zhuoheng Han, Houfeng Wang, Lizi Liao
- **arXiv**: [2610.02067](http://arxiv.org/abs/2610.02067v1)
- **Published**: 2026-10-01
- **Categories**: cs.LG

> While Low-Rank Adaptation (LoRA) enables efficient task specialization, its learned updates can compromise capabilities beyond the target task. We identify \textbf{adaptation imbalance}: a few singular directions dominate the trained update, leaving its performance sensitive to how gains are allocat...

### Task-Oriented Rank Adaptation for Continual Learning in Text Classification
- **Authors**: Rey Sanchez Lopez, Eduardo Morales Manzanares, Hugo Jair Escalante
- **arXiv**: [2610.01702](http://arxiv.org/abs/2610.01702v1)
- **Published**: 2026-10-01
- **Categories**: cs.CL

> Continual learning (CL) in text classification faces two critical challenges: catastrophic forgetting and negative transfer across sequential tasks. Parameter-Efficient Fine-Tuning (PEFT) methods such as LoRA enable efficient adaptation by learning low-rank updates of the model parameters. However, ...

### MuLoRA: Spectrally Balanced Low-Rank Adaptation for Continual Learning
- **Authors**: Junkang Liu
- **arXiv**: [2610.02283](http://arxiv.org/abs/2610.02283v1)
- **Published**: 2026-10-01
- **Categories**: cs.LG

> Low-rank adaptation (LoRA) provides a parameter-efficient approach to continual learning, but its nominal rank can conceal a loss of effective adaptation capacity. We identify \emph{spectral plasticity collapse}: during sequential adaptation, update energy becomes concentrated in a small subset of s...

### Beyond Domain-Level Adaptation: Margin-Oriented Semantic-Appearance Interaction Correction for Personalized Federated Vision-Language Models
- **Authors**: Wentao Yue, Qingyu Mao, Tianyou Lai, Ahmed M. Abdelmoniem, Qilei Li
- **arXiv**: [2610.01625](http://arxiv.org/abs/2610.01625v1)
- **Published**: 2026-10-01
- **Categories**: cs.CV

> Federated parameter-efficient fine-tuning enables distributed clients to adapt pretrained vision-language models without sharing raw data or updating the full backbone. Its effectiveness, however, is limited by domain heterogeneity across clients. Existing personalized methods separate globally shar...

### FedLore: Communication and Memory Efficient Federated Learning via Shared Gradient Low-Rank Projection
- **Authors**: Junkang Liu
- **arXiv**: [2610.01620](http://arxiv.org/abs/2610.01620v1)
- **Published**: 2026-10-01
- **Categories**: cs.AI

> Federated training of foundation models is constrained by client memory and communication costs. LoRA-based methods reduce these costs through low-rank adapters, but their fixed rank budget can limit adaptation. Gradient low-rank optimization offers greater flexibility, yet independently chosen clie...

### FedFit: Federated Fine-Tuning of LLMs via Vector-Bank Parameterization and Quantization
- **Authors**: Hang Zou, Chao Zhang, Yuzhi Yang, Yu Tian, Samson Lasaulce, Mérouane Debbah
- **arXiv**: [2610.01537](http://arxiv.org/abs/2610.01537v1)
- **Published**: 2026-10-01
- **Categories**: cs.LG

> Federated Learning (FL) enables privacy-preserving fine-tuning of Large Language Models (LLMs), yet the massive communication overhead remains a critical bottleneck. Furthermore, applying Low-Rank Adaptation (LoRA) in FL faces a fundamental "aggregation dilemma" between the accurate Sum-of-Products ...

### CLASP: Continual Low-rank Adapters for Spatially Placed Concepts from One Hypernetwork
- **Authors**: Wojciech Gromski, Patryk Krukowski, Jan Miksa, Maciej Zieba, Przemysław Spurek
- **arXiv**: [2610.01331](http://arxiv.org/abs/2610.01331v1)
- **Published**: 2026-10-01
- **Categories**: cs.CV

> Continual personalization of text-to-image diffusion models requires sequentially acquiring new concepts while retaining previously learned ones. However, existing methods either suffer from catastrophic forgetting or rely on storing additional concept-specific parameters and spatial components, cau...

### Platonic Task Arithmetic
- **Authors**: Junghwan Park, Woojin Cho
- **arXiv**: [2610.00929](http://arxiv.org/abs/2610.00929v2)
- **Published**: 2026-10-01
- **Categories**: cs.LG, cs.CV, stat.ML

> Distinct pre-trained models specialized for the same task converge to closely similar behavior, yet the parameter updates that produce it share no common coordinate system. Weight-space task arithmetic is therefore confined to a single model, and transporting an update between models requires a stru...

### Efficient Task Adaptation in Large Language Models: A Survey of Weight-Based, Prompt-Based, and Embedding-Based Adaptations
- **Authors**: Jungwon Park, Changin Choi, Jimyeong Kim, Nojun Kwak, Wonjong Rhee
- **arXiv**: [2610.00928](http://arxiv.org/abs/2610.00928v1)
- **Published**: 2026-10-01
- **Categories**: cs.CL

> As large language models are increasingly deployed across diverse downstream tasks, efficient task adaptation has emerged as a central challenge. In response, a wide range of task adaptation methods have been proposed, spanning parameter-efficient fine-tuning, in-context learning, and embedding-inje...

### Towards Robust Numerical Claim Verification
- **Authors**: Peter Røysland Aarnes, Vinay Setty
- **arXiv**: [2610.00689](http://arxiv.org/abs/2610.00689v1)
- **Published**: 2026-09-30
- **Categories**: cs.CL

> Large language models (LLMs) are widely used for claim verification, yet remain brittle for numerical reasoning: even small changes in value can sharply degrade accuracy. We show that this brittleness persists in frontier LLMs, but can be mitigated through adversarial fine-tuning on numerically pert...

### Backdoor Purification for LoRA-Tuned LLMs via Null-Space Projection
- **Authors**: Jianwei Li, Jung-Eun Kim
- **arXiv**: [2610.00685](http://arxiv.org/abs/2610.00685v1)
- **Published**: 2026-09-30
- **Categories**: cs.AI, cs.CR, cs.LG

> With the rapid adoption of large language models (LLMs) and parameter-efficient fine-tuning (PEFT) methods, the risk of backdoor attacks has become more severe. Existing backdoor purification methods typically rely on at least one of the strong assumptions, such as prior knowledge of triggers, acces...

### Analysis of Quantized and Efficiently Adapted Protein Language Models
- **Authors**: Ilan Yaniv Zeisler, Sebastian Clancy, Pouriya Bayat, Saaim Raad, Ivan Kraskov, Matthew Xie, Vivian White, Spencer Perkins, Serena Singh, Sepehr Bayat, Keith Pardee
- **arXiv**: [2610.00665](http://arxiv.org/abs/2610.00665v1)
- **Published**: 2026-09-30
- **Categories**: cs.LG, q-bio.QM

> Background: Protein language models (PLMs) are increasingly used for sequence generation and property prediction, but their size makes fine-tuning and deployment expensive. The effects of quantization and parameter efficient fine-tuning on performance, representations and generation remain insuffici...

### PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation
- **Authors**: Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi
- **arXiv**: [2610.00664](http://arxiv.org/abs/2610.00664v1)
- **Published**: 2026-09-30
- **Categories**: cs.CL

> Bengali secondary education lacks curriculum-grounded benchmarks for STEM question-solving, and general-purpose language models struggle with the precise terminology, unit conventions, and derivations that physics problems demand. We introduce PhysicsMate, a benchmark of 1834 question-answer pairs b...

### Explainable Suicide Risk Assessment on Social Media with Multi-Task QLoRA
- **Authors**: Xuan Zhong Feng, Geoffrey Martin, Hexin Dong, Yifan Peng
- **arXiv**: [2610.00610](http://arxiv.org/abs/2610.00610v2)
- **Published**: 2026-09-30
- **Categories**: cs.CL, cs.LG

> Explainable suicide-risk assessment requires models not only to estimate risk severity, but also to identify supporting language and the risk and protective factors expressed in a post. We present our system for the IEEE BigData 2026 Cup on Explainable Suicide Risk Assessment on Social Media, which ...

### Score the Update, Not the Token: Descent-Aligned Routing for Combinatorial LoRA Experts
- **Authors**: Priya Nair, Lukas Brenner, Maya Lindqvist, Daniel Whitmore, Wen-Hsuan Liu, Tom Saliencro, Amara Okonkwo, Rohan Desai
- **arXiv**: [2610.00493](http://arxiv.org/abs/2610.00493v1)
- **Published**: 2026-09-30
- **Categories**: cs.LG

> Mixture-of-LoRA-experts methods raise the capacity of low-rank adaptation by routing each token to a few low-rank experts. Nearly all of them tie one input-side factor to one output-side factor per expert, and nearly all of them route by scoring the token: the router picks experts without seeing wha...

### ChainLoRA: Geometry-Preserving Task Vector Merging for Continual Learning in LLMs
- **Authors**: Hang Yin, Haozhe Wang, Yuhua Luo, Zhangqi Pan, Xiaoxing Wang, Junchi Yan
- **arXiv**: [2610.00431](http://arxiv.org/abs/2610.00431v1)
- **Published**: 2026-09-30
- **Categories**: stat.ML, cs.LG

> Continual parameter-efficient fine-tuning for large language models (LLMs) must balance retention of previously acquired knowledge, adaptation to new tasks, and strict parameter budgets. We present \textbf{ChainLoRA}, a replay-free continual merging framework built on chain-updated task-vector geome...

### LARC: Low-Rank Adaptive Residual Connections for Learning in Frozen Models
- **Authors**: Junyi Zou, Avrova Donz
- **arXiv**: [2609.40063](http://arxiv.org/abs/2609.40063v1)
- **Published**: 2026-09-30
- **Categories**: cs.LG, cs.CL

> Low-Rank Adaptive Residual Connections (LARC) give a frozen model a compact numerical state that can learn from feedback. The map $h+BAh$ adds a low-rank correction to a hidden representation. A slow state $ρ$ learns starting factors across tasks; a private fast state $Φ$ copies them, changes with f...

### Dynamic LoRA-Experts and Prototype-Ensemble Matching for Class-Incremental Learning
- **Authors**: Hongwei Zhao, Rui Liu, Yansong Liu
- **arXiv**: [2609.39839](http://arxiv.org/abs/2609.39839v1)
- **Published**: 2026-09-30
- **Categories**: cs.LG

> Class-Incremental Learning (CIL) aims to continuously learn new classes without forgetting previously acquired knowledge. Parameter-efficient fine-tuning with pre-trained models reduces parameter overhead but can suffer from cumulative interference and suboptimal alignment between inference samples ...

### SE-ADD: Self-Evolving Audio Deepfake Detection with Mistake-Driven Supervision
- **Authors**: Rong Wan, Wei Xie, Jiaxi Li, Wenwu Wang, Lu Yin, Yiliao Song, Xilu Wang
- **arXiv**: [2609.39679](http://arxiv.org/abs/2609.39679v1)
- **Published**: 2026-09-30
- **Categories**: cs.SD, cs.LG

> Audio deepfake detection (ADD) must remain effective when new spoofing attacks emerge after deployment. Emerging audio language model (ALM)-based ADD methods are built on predefined supervision from ground-truth labels or verified forensic rationales. However, this paradigm overlooks an ALM's own mi...

### Hyperbolic Prototype Routing for Rehearsal-Free Class-Incremental Learning
- **Authors**: HongWei Zhao, Rui Liu, Yong Chen
- **arXiv**: [2609.39550](http://arxiv.org/abs/2609.39550v1)
- **Published**: 2026-09-30
- **Categories**: cs.LG

> Class-Incremental Learning (CIL) aims to continually learn new classes while preserving prior knowledge. Parameter-efficient fine-tuning with pre-trained models enables CIL with minimal parameter updates, but existing approaches still suffer from catastrophic forgetting caused by cumulative interfer...

### Comparative study of adapting pre-trained models for driving behavior video captioning
- **Authors**: Sayak Mallick, Philipp Geiger, Augustin Kelava
- **arXiv**: [2609.39542](http://arxiv.org/abs/2609.39542v1)
- **Published**: 2026-09-30
- **Categories**: cs.CV, cs.LG

> This report examines and compares some of the many fine tuning and prompting methods existing, applying them within the domain of autonomous driving. The idea is to compare these methods by adapting a Large Language Model (LLM) on a video dataset. LLM's have become extremely good at achieving a good...

### Decoupled and Distilled: Task-Adaptive LoRA-Teachers with Ensemble Knowledge Transfer for Few-Shot Class-Incremental Learning
- **Authors**: Hongwei Zhao, Rui Liu, Yansong Liu, Zhiyuan Zou, Yong Chen
- **arXiv**: [2609.39390](http://arxiv.org/abs/2609.39390v1)
- **Published**: 2026-09-30
- **Categories**: cs.LG

> Few-Shot Class-Incremental Learning (FSCIL) addresses the challenge of learning new classes from very limited samples while retaining knowledge of previously learned ones. Although parameter-efficient fine-tuning methods with pre-trained models show promise for class-incremental learning, strict gra...

### A Dynamical Theory of LoRA in Continual Learning
- **Authors**: Théo Marchetta, Filippo Alessandroni, Alessandro Breccia, Alessandro Ingrosso, Federica Gerace
- **arXiv**: [2609.39367](http://arxiv.org/abs/2609.39367v1)
- **Published**: 2026-09-30
- **Categories**: stat.ML, cond-mat.stat-mech, cs.LG, math.PR, math.ST

> Despite the widespread use of Low-Rank Adaptation (LoRA), little is known about its dynamics in continual learning and the mechanisms by which low-rank updates affect catastrophic forgetting. We provide an asymptotically exact dynamical characterization of LoRA in a solvable two-task teacher-student...

### Beyond Text: LLM-Based Dimensional Emotion Evaluation in Multimodal Dialogue
- **Authors**: Yutong Hu, Jinho Choi
- **arXiv**: [2609.39072](http://arxiv.org/abs/2609.39072v1)
- **Published**: 2026-09-30
- **Categories**: cs.CL, cs.AI, cs.LG, cs.MM

> Emotion recognition in conversation has been widely studied, but applying Large Language Models (LLMs) to continuous dimensional emotion evaluation in multimodal dialogue remains largely unexplored. We propose an LLM-based framework that performs discrete emotion recognition and Valence-Arousal-Domi...

### MetaSteer: Context-Conditioned, nonlinear Steering via Attention-Projection Adaptation
- **Authors**: Mehdi Jafari, Hao Xue, Flora Salim
- **arXiv**: [2609.38718](http://arxiv.org/abs/2609.38718v1)
- **Published**: 2026-09-30
- **Categories**: cs.CL

> Steering large language models typically relies on linear, context-independent interventions in activation space, an assumption that recent work has challenged and that can induce an information bottleneck when a fixed representation must encode many behavioral distinctions. We introduce MetaSteer, ...

### Storage Is Not Strategy: State-Conditioned Support Control for LLM Unlearning
- **Authors**: Tianhao Qian, Ziming Hong, Chongyang Gao, Kezhen Chen, Lixu Wang
- **arXiv**: [2609.37858](http://arxiv.org/abs/2609.37858v1)
- **Published**: 2026-09-29
- **Categories**: cs.LG, cs.CL

> Many localized large language model (LLM) unlearning methods select a small parameter subset from a localization signal and keep it fixed during optimization. The parameters most associated with a target, however, need not be the best ones to update, and candidate interventions can change value as o...

### A Model-Agnostic Physics-Guided Adapter for Few-Shot Transfer of Coastal Flood Prediction Models to Unseen Regions
- **Authors**: Bilal Hassan, Areg Karapetyan, Samer Madanat
- **arXiv**: [2609.37565](http://arxiv.org/abs/2609.37565v1)
- **Published**: 2026-09-29
- **Categories**: cs.LG

> Deep learning surrogates can produce high-resolution coastal flood maps orders of magnitude faster than physics-based hydrodynamic simulators, yet transferring them to new coastal regions remains costly, since generating target-region data for fine-tuning typically requires numerous time-consuming s...

### SQUARE: Structured Quantum Representation Adapters as Compact Quadratic Feature Maps for Frozen Language Models
- **Authors**: Emily Jimin Roh, Hyojun Ahn, Hoyeong Lee, Soohyun Park, Sung Whan Yoon, Vaneet Aggarwal, Joongheon Kim
- **arXiv**: [2609.37134](http://arxiv.org/abs/2609.37134v1)
- **Published**: 2026-09-29
- **Categories**: quant-ph, cs.AI

> Frozen language models (LMs) are increasingly used as fixed feature extractors for downstream reranking, scoring, and preference modeling, raising a practical question: how should a compact module represent interactions among features in a fixed low-dimensional bottleneck? Common linear and low-rank...

### FedLAFP: Low-Rank Aggregation Meets Full-Rank Personalization in Federated Fine-Tuning
- **Authors**: Mengjun Yi, Huaian Gu, Yinghao Ai, Furao Shen, Jian Zhao
- **arXiv**: [2609.37033](http://arxiv.org/abs/2609.37033v1)
- **Published**: 2026-09-29
- **Categories**: cs.AI

> Federated parameter-efficient fine-tuning enables clients to adapt pre-trained models without sharing raw data or communicating the full model, but statistical heterogeneity makes a single global adapter insufficient for personalized prediction. Existing personalized methods typically use the same l...

### Beyond Low-Rank Parameterization: Narrowing the Gap Between LoRA and Full Fine-Tuning via Gradient Decomposition
- **Authors**: Yihao Ouyang, Shiwei Li, Haozhao Wang, Xiandi Luo, Zhuoqi Hu, Jinglun Yu, Yichen Li, Ruixuan Li
- **arXiv**: [2609.37027](http://arxiv.org/abs/2609.37027v1)
- **Published**: 2026-09-29
- **Categories**: cs.AI

> Low-Rank Adaptation (LoRA) is a widely used approach to parameter-efficient fine-tuning (PEFT), yet a performance gap can remain relative to full fine-tuning (FFT). Many LoRA variants improve the initialization or optimization of low-rank factors. At each training step, however, their first-order we...

### CF-LoRA: Decoupled Factor Aggregation and Adaptation-Aware Client Clustering for Federated LoRA Fine-Tuning
- **Authors**: Mengjun Yi, Langxing Yang, Suhan Guo, Furao Shen, Jian Zhao
- **arXiv**: [2609.36986](http://arxiv.org/abs/2609.36986v1)
- **Published**: 2026-09-29
- **Categories**: cs.AI, cs.DC

> Federated LoRA fine-tuning enables parameter-efficient adaptation of pre-trained models without sharing private data, but suffers from two fundamental mismatches under heterogeneous client data: a structural aggregation mismatch caused by independently averaging LoRA factors, and a statistical colla...

### When Can Prefixes Compile LoRA? Exact Resource-Capped Tests for Frozen Attention
- **Authors**: Joyanta Jyoti Mondal, Ibne Farabi Shihab
- **arXiv**: [2609.36766](http://arxiv.org/abs/2609.36766v1)
- **Published**: 2026-09-29
- **Categories**: cs.LG

> Can a fixed continuous prefix replace a given low-rank adapter while the attention head stays frozen? In this research, we show that the answer depends on the adapter's target through three conditions. First, observability: at one causal readout, every independent key--value prefix sees the content ...

### Routing in Gradient Space: Balanced Usage Is Not Expert Specialization
- **Authors**: Yuchen Li, Mingyu Du, Zongqi Fan, Nguyen H. Tran, Ken-Tye Yong
- **arXiv**: [2609.36724](http://arxiv.org/abs/2609.36724v1)
- **Published**: 2026-09-29
- **Categories**: cs.LG

> Sparse expert models can distribute traffic evenly while still grouping incompatible training signals within the same experts. We study routing as a gradient-partitioning problem and introduce gradient-aligned routing (GAR), whose load-normalized router objective rewards grouping observations with a...

### ATTUNER: Recomputation-Free KV Cache Reuse via Query-Side Adaptation
- **Authors**: Xinghao Chen, Junnan Dong, Cai Ke, Chak Tou Leong, Haocheng Sun, Keyu Chen, Siyu An, Ruizhi Qiao, Xing Sun, Wenjie Li, Xiaoyu Shen
- **arXiv**: [2609.36722](http://arxiv.org/abs/2609.36722v1)
- **Published**: 2026-09-29
- **Categories**: cs.CL

> Large language model (LLM) agents repeatedly load reusable content, such as skills, documents, and memory entries, into the current context. Re-encoding this content for every request wastes computation. Position-independent caching (PIC) alleviates this by encoding each artifact independently and r...

### Constitutional adapters: Inference-time interventions for misalignment and misuse
- **Authors**: Adam S. Lowet, Mark Kurzeja
- **arXiv**: [2609.36657](http://arxiv.org/abs/2609.36657v1)
- **Published**: 2026-09-29
- **Categories**: cs.LG, cs.AI

> Training models to act in accordance with an explicitly defined set of principles, or "constitution," has shown promise as a robust and transparent mechanism for AI alignment. However, the generality and flexibility of such methods remain unclear. Here, we show that constitution-consistent behavior ...

### Reducing the Adaptation Gap Through Reachable Fisher Geometry
- **Authors**: Wasif Jalal, Sachin Deb, Asif Salekin
- **arXiv**: [2609.36329](http://arxiv.org/abs/2609.36329v1)
- **Published**: 2026-09-28
- **Categories**: cs.LG

> Parameter-efficient fine-tuning (PEFT) determines not only how many parameters are trained, but also which local directions a model can move in, so similar adapters can affect subgroup losses differently. Since curvature matrices are infeasible to form at adapter scale, scalar summaries such as the ...

### Tokenized Key-Gated Adapter Routing: A Secure Access Control Mechanism Against Private Data Leakage in LLMs
- **Authors**: Mohamed Shaaban, Mohamed Elmahallawy
- **arXiv**: [2610.00309](http://arxiv.org/abs/2610.00309v1)
- **Published**: 2026-09-28
- **Categories**: cs.CR, cs.AI, cs.CL

> Large language models (LLMs) are increasingly deployed in privacy-critical domains (e.g., healthcare, finance, and government), but their propensity to memorize and disclose personally identifiable information (PII) poses serious security and compliance risks. Existing defenses typically force a tra...

### EvE: An Alternate Optimizer to Adam
- **Authors**: Shashank Raj, Kalyanmoy Deb
- **arXiv**: [2609.35614](http://arxiv.org/abs/2609.35614v1)
- **Published**: 2026-09-28
- **Categories**: cs.LG, cs.NE

> Adam and its variants dominate neural network training, but a single run only reveals whether a configuration works well after most of its budget is spent, a poor fit for hyperparameter or architecture search, where configurations must be ranked cheaply and pruned early. We introduce EvE (Evolutiona...

### Style-Driven Data Synthesis and Degradation-Aware Enhancement for Ultrasound Image Restoration
- **Authors**: Yu-Kai Wang, Chun-Xin Tan, Manh-Hung Nguyen, Ching-Chun Huang
- **arXiv**: [2609.35120](http://arxiv.org/abs/2609.35120v1)
- **Published**: 2026-09-28
- **Categories**: cs.CV

> Low-cost handheld ultrasound devices can be widely deployed compared to professional hospital ultrasound machines. However, their images suffer from compound degradation that can mislead clinical judgment. Motivated by this observation, mapping handheld low-quality (LQ) to hospital high-quality (HQ)...

### From One-Shot Generation to Incremental Music Composition: Adapting a General-Purpose Instruction LLM for Persistent Symbolic Editing
- **Authors**: André Ricardo Ducca Fernandes, Jean-Pierre Briot, Simone Diniz Junqueira Barbosa1, Hélio Côrtes Vieira Lopes
- **arXiv**: [2609.34994](http://arxiv.org/abs/2609.34994v1)
- **Published**: 2026-09-28
- **Categories**: cs.AI, cs.LG

> Most music-generation systems are still framed and evaluated primarily as producers of complete outputs, whereas composition often proceeds through successive revisions to a shared musical artifact. This paper studies a different use of a general-purpose instruction-following large language model: n...

### Just MLPs: Efficient Visual State Reconstruction for Multimodal Language Models
- **Authors**: Jingdi lei, Junxian Li, Di Zhang, Zhanqiu Zhang, Yiwen Guo, Soujanya Poria
- **arXiv**: [2609.34972](http://arxiv.org/abs/2609.34972v1)
- **Published**: 2026-09-28
- **Categories**: cs.CV, cs.AI

> Long visual token sequences often account for a substantial fraction of the computational overhead in multimodal large language models~(MLLMs). Existing approaches reduce this cost by pruning redundant visual tokens, but permanently discard visual evidence that may become useful in subsequent layers...

### RoboFL: Federated Expert Assembly for World Action Models
- **Authors**: Rongyu Zhang, Ruizhi Fan, Yunfan Lou, Hengyu Fang, Shenli Zheng, Chenrui Wu, Yili Jin, Li Du, Dan Wang, Yuan Du, Shanghang Zhang
- **arXiv**: [2609.34968](http://arxiv.org/abs/2609.34968v1)
- **Published**: 2026-09-28
- **Categories**: cs.RO, cs.AI

> Vision-language-action and world-action models are increasingly popular, yet remain bottlenecked by physical interaction data that is scarce, institutionally siloed, and task-heterogeneous. A natural federated solution is to let each client adapt a shared foundation model through parameter-efficient...

### Brain-Conditioned Action Policies for Neural Motor Decoding
- **Authors**: Luyao Jin, Running Zhao, Huan Zhao, Vincent C. K. Cheung, Wei-Hsin Liao
- **arXiv**: [2609.34561](http://arxiv.org/abs/2609.34561v1)
- **Published**: 2026-09-28
- **Categories**: cs.LG

> Motor brain-computer interfaces (BCIs) aim to decode motor intention, enabling people with paralysis to control external devices. Neural motor decoding typically learns task-specific mappings from neural activity to kinematics, yet remains constrained by scarce paired neural-action data. We propose ...

### SPACE-LoRA: Allocating Activation-Subspace Protection for Continual Learning
- **Authors**: Seunghyun Yoo, Kiseok Kim, Hyeontae Joo, Junyeop Bang, Hwangnam Kim
- **arXiv**: [2609.34453](http://arxiv.org/abs/2609.34453v1)
- **Published**: 2026-09-28
- **Categories**: cs.LG, cs.AI

> This study addresses the catastrophic forgetting problem that occurs when sequentially learning successive tasks using Low-Rank Adaptation (LoRA) from a lifelong learning perspective. While existing approaches have primarily constrained parameter updates or learning subspaces to reduce interference ...

### Rotated Manifold Optimization for Low-Rank Adaptation
- **Authors**: Yuhui Ding, Javier Zazo, James Hensman
- **arXiv**: [2609.34264](http://arxiv.org/abs/2609.34264v1)
- **Published**: 2026-09-28
- **Categories**: cs.LG

> We propose a novel optimizer for low-rank adaptation (LoRA) that explicitly incorporates the gauge symmetry of low-rank factorization. Our optimizer extends recent matrix optimizers for full-parameter training to the manifold of fixed-rank matrices by interpreting them as normalization under a rotat...

### Loop Dropout: Regularizing Shared Updates in Looped Language Models
- **Authors**: Zirui Zhu, Hailun Xu, Xuanlei Zhao, Yong Liu, Yingxuan Ren, Kanchan Sarkar, Kun Xu, Yang You
- **arXiv**: [2609.34218](http://arxiv.org/abs/2609.34218v1)
- **Published**: 2026-09-28
- **Categories**: cs.LG, cs.CL

> Looped language models separate computational depth from parameter count by repeatedly applying the same transformer block. Adapting these models requires a shared update that remains effective as hidden states evolve throughout the recurrent computation. Our empirical analysis reveals a pronounced ...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "jain-2026",
    "title": "Query-aware routing for Cross-lingual performance gains in Encoders",
    "authors": [
      "Akshay Jain",
      "Edward Kim"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.02875",
    "paper_url": "https://arxiv.org/abs/2610.02875",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "tian-2026",
    "title": "Learn the Directions, Normalize the Gains: Post-Training Normalization for LoRA",
    "authors": [
      "Zailong Tian",
      "Yanzhe Chen",
      "Zhuoheng Han",
      "Houfeng Wang",
      "Lizi Liao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.02067",
    "paper_url": "https://arxiv.org/abs/2610.02067",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "lopez-2026",
    "title": "Task-Oriented Rank Adaptation for Continual Learning in Text Classification",
    "authors": [
      "Rey Sanchez Lopez",
      "Eduardo Morales Manzanares",
      "Hugo Jair Escalante"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.01702",
    "paper_url": "https://arxiv.org/abs/2610.01702",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "liu-2026",
    "title": "MuLoRA: Spectrally Balanced Low-Rank Adaptation for Continual Learning",
    "authors": [
      "Junkang Liu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.02283",
    "paper_url": "https://arxiv.org/abs/2610.02283",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "yue-2026",
    "title": "Beyond Domain-Level Adaptation: Margin-Oriented Semantic-Appearance Interaction Correction for Personalized Federated Vision-Language Models",
    "authors": [
      "Wentao Yue",
      "Qingyu Mao",
      "Tianyou Lai",
      "Ahmed M. Abdelmoniem",
      "Qilei Li"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.01625",
    "paper_url": "https://arxiv.org/abs/2610.01625",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "liu-2026",
    "title": "FedLore: Communication and Memory Efficient Federated Learning via Shared Gradient Low-Rank Projection",
    "authors": [
      "Junkang Liu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.01620",
    "paper_url": "https://arxiv.org/abs/2610.01620",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "zou-2026",
    "title": "FedFit: Federated Fine-Tuning of LLMs via Vector-Bank Parameterization and Quantization",
    "authors": [
      "Hang Zou",
      "Chao Zhang",
      "Yuzhi Yang",
      "Yu Tian",
      "Samson Lasaulce",
      "Mérouane Debbah"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.01537",
    "paper_url": "https://arxiv.org/abs/2610.01537",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "gromski-2026",
    "title": "CLASP: Continual Low-rank Adapters for Spatially Placed Concepts from One Hypernetwork",
    "authors": [
      "Wojciech Gromski",
      "Patryk Krukowski",
      "Jan Miksa",
      "Maciej Zieba",
      "Przemysław Spurek"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.01331",
    "paper_url": "https://arxiv.org/abs/2610.01331",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "park-2026",
    "title": "Platonic Task Arithmetic",
    "authors": [
      "Junghwan Park",
      "Woojin Cho"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.00929",
    "paper_url": "https://arxiv.org/abs/2610.00929",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "park-2026",
    "title": "Efficient Task Adaptation in Large Language Models: A Survey of Weight-Based, Prompt-Based, and Embedding-Based Adaptations",
    "authors": [
      "Jungwon Park",
      "Changin Choi",
      "Jimyeong Kim",
      "Nojun Kwak",
      "Wonjong Rhee"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.00928",
    "paper_url": "https://arxiv.org/abs/2610.00928",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "aarnes-2026",
    "title": "Towards Robust Numerical Claim Verification",
    "authors": [
      "Peter Røysland Aarnes",
      "Vinay Setty"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.00689",
    "paper_url": "https://arxiv.org/abs/2610.00689",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "li-2026",
    "title": "Backdoor Purification for LoRA-Tuned LLMs via Null-Space Projection",
    "authors": [
      "Jianwei Li",
      "Jung-Eun Kim"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.00685",
    "paper_url": "https://arxiv.org/abs/2610.00685",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "zeisler-2026",
    "title": "Analysis of Quantized and Efficiently Adapted Protein Language Models",
    "authors": [
      "Ilan Yaniv Zeisler",
      "Sebastian Clancy",
      "Pouriya Bayat",
      "Saaim Raad",
      "Ivan Kraskov",
      "Matthew Xie",
      "Vivian White",
      "Spencer Perkins",
      "Serena Singh",
      "Sepehr Bayat",
      "Keith Pardee"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.00665",
    "paper_url": "https://arxiv.org/abs/2610.00665",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "jahin-2026",
    "title": "PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation",
    "authors": [
      "Rashid Azraf Jahin",
      "Saadman Sajid",
      "Khan Raiyan Ibne Reza",
      "Sumaiya Tabassum Nimi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.00664",
    "paper_url": "https://arxiv.org/abs/2610.00664",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "feng-2026",
    "title": "Explainable Suicide Risk Assessment on Social Media with Multi-Task QLoRA",
    "authors": [
      "Xuan Zhong Feng",
      "Geoffrey Martin",
      "Hexin Dong",
      "Yifan Peng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.00610",
    "paper_url": "https://arxiv.org/abs/2610.00610",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "nair-2026",
    "title": "Score the Update, Not the Token: Descent-Aligned Routing for Combinatorial LoRA Experts",
    "authors": [
      "Priya Nair",
      "Lukas Brenner",
      "Maya Lindqvist",
      "Daniel Whitmore",
      "Wen-Hsuan Liu",
      "Tom Saliencro",
      "Amara Okonkwo",
      "Rohan Desai"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.00493",
    "paper_url": "https://arxiv.org/abs/2610.00493",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "yin-2026",
    "title": "ChainLoRA: Geometry-Preserving Task Vector Merging for Continual Learning in LLMs",
    "authors": [
      "Hang Yin",
      "Haozhe Wang",
      "Yuhua Luo",
      "Zhangqi Pan",
      "Xiaoxing Wang",
      "Junchi Yan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.00431",
    "paper_url": "https://arxiv.org/abs/2610.00431",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "zou-2026",
    "title": "LARC: Low-Rank Adaptive Residual Connections for Learning in Frozen Models",
    "authors": [
      "Junyi Zou",
      "Avrova Donz"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.40063",
    "paper_url": "https://arxiv.org/abs/2609.40063",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "zhao-2026",
    "title": "Dynamic LoRA-Experts and Prototype-Ensemble Matching for Class-Incremental Learning",
    "authors": [
      "Hongwei Zhao",
      "Rui Liu",
      "Yansong Liu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.39839",
    "paper_url": "https://arxiv.org/abs/2609.39839",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "wan-2026",
    "title": "SE-ADD: Self-Evolving Audio Deepfake Detection with Mistake-Driven Supervision",
    "authors": [
      "Rong Wan",
      "Wei Xie",
      "Jiaxi Li",
      "Wenwu Wang",
      "Lu Yin",
      "Yiliao Song",
      "Xilu Wang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.39679",
    "paper_url": "https://arxiv.org/abs/2609.39679",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "zhao-2026",
    "title": "Hyperbolic Prototype Routing for Rehearsal-Free Class-Incremental Learning",
    "authors": [
      "HongWei Zhao",
      "Rui Liu",
      "Yong Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.39550",
    "paper_url": "https://arxiv.org/abs/2609.39550",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "mallick-2026",
    "title": "Comparative study of adapting pre-trained models for driving behavior video captioning",
    "authors": [
      "Sayak Mallick",
      "Philipp Geiger",
      "Augustin Kelava"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.39542",
    "paper_url": "https://arxiv.org/abs/2609.39542",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "zhao-2026",
    "title": "Decoupled and Distilled: Task-Adaptive LoRA-Teachers with Ensemble Knowledge Transfer for Few-Shot Class-Incremental Learning",
    "authors": [
      "Hongwei Zhao",
      "Rui Liu",
      "Yansong Liu",
      "Zhiyuan Zou",
      "Yong Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.39390",
    "paper_url": "https://arxiv.org/abs/2609.39390",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "marchetta-2026",
    "title": "A Dynamical Theory of LoRA in Continual Learning",
    "authors": [
      "Théo Marchetta",
      "Filippo Alessandroni",
      "Alessandro Breccia",
      "Alessandro Ingrosso",
      "Federica Gerace"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.39367",
    "paper_url": "https://arxiv.org/abs/2609.39367",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "hu-2026",
    "title": "Beyond Text: LLM-Based Dimensional Emotion Evaluation in Multimodal Dialogue",
    "authors": [
      "Yutong Hu",
      "Jinho Choi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.39072",
    "paper_url": "https://arxiv.org/abs/2609.39072",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "jafari-2026",
    "title": "MetaSteer: Context-Conditioned, nonlinear Steering via Attention-Projection Adaptation",
    "authors": [
      "Mehdi Jafari",
      "Hao Xue",
      "Flora Salim"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.38718",
    "paper_url": "https://arxiv.org/abs/2609.38718",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "qian-2026",
    "title": "Storage Is Not Strategy: State-Conditioned Support Control for LLM Unlearning",
    "authors": [
      "Tianhao Qian",
      "Ziming Hong",
      "Chongyang Gao",
      "Kezhen Chen",
      "Lixu Wang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.37858",
    "paper_url": "https://arxiv.org/abs/2609.37858",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "hassan-2026",
    "title": "A Model-Agnostic Physics-Guided Adapter for Few-Shot Transfer of Coastal Flood Prediction Models to Unseen Regions",
    "authors": [
      "Bilal Hassan",
      "Areg Karapetyan",
      "Samer Madanat"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.37565",
    "paper_url": "https://arxiv.org/abs/2609.37565",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "roh-2026",
    "title": "SQUARE: Structured Quantum Representation Adapters as Compact Quadratic Feature Maps for Frozen Language Models",
    "authors": [
      "Emily Jimin Roh",
      "Hyojun Ahn",
      "Hoyeong Lee",
      "Soohyun Park",
      "Sung Whan Yoon",
      "Vaneet Aggarwal",
      "Joongheon Kim"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.37134",
    "paper_url": "https://arxiv.org/abs/2609.37134",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "yi-2026",
    "title": "FedLAFP: Low-Rank Aggregation Meets Full-Rank Personalization in Federated Fine-Tuning",
    "authors": [
      "Mengjun Yi",
      "Huaian Gu",
      "Yinghao Ai",
      "Furao Shen",
      "Jian Zhao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.37033",
    "paper_url": "https://arxiv.org/abs/2609.37033",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "ouyang-2026",
    "title": "Beyond Low-Rank Parameterization: Narrowing the Gap Between LoRA and Full Fine-Tuning via Gradient Decomposition",
    "authors": [
      "Yihao Ouyang",
      "Shiwei Li",
      "Haozhao Wang",
      "Xiandi Luo",
      "Zhuoqi Hu",
      "Jinglun Yu",
      "Yichen Li",
      "Ruixuan Li"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.37027",
    "paper_url": "https://arxiv.org/abs/2609.37027",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "yi-2026",
    "title": "CF-LoRA: Decoupled Factor Aggregation and Adaptation-Aware Client Clustering for Federated LoRA Fine-Tuning",
    "authors": [
      "Mengjun Yi",
      "Langxing Yang",
      "Suhan Guo",
      "Furao Shen",
      "Jian Zhao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.36986",
    "paper_url": "https://arxiv.org/abs/2609.36986",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "mondal-2026",
    "title": "When Can Prefixes Compile LoRA? Exact Resource-Capped Tests for Frozen Attention",
    "authors": [
      "Joyanta Jyoti Mondal",
      "Ibne Farabi Shihab"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.36766",
    "paper_url": "https://arxiv.org/abs/2609.36766",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "li-2026",
    "title": "Routing in Gradient Space: Balanced Usage Is Not Expert Specialization",
    "authors": [
      "Yuchen Li",
      "Mingyu Du",
      "Zongqi Fan",
      "Nguyen H. Tran",
      "Ken-Tye Yong"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.36724",
    "paper_url": "https://arxiv.org/abs/2609.36724",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "chen-2026",
    "title": "ATTUNER: Recomputation-Free KV Cache Reuse via Query-Side Adaptation",
    "authors": [
      "Xinghao Chen",
      "Junnan Dong",
      "Cai Ke",
      "Chak Tou Leong",
      "Haocheng Sun",
      "Keyu Chen",
      "Siyu An",
      "Ruizhi Qiao",
      "Xing Sun",
      "Wenjie Li",
      "Xiaoyu Shen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.36722",
    "paper_url": "https://arxiv.org/abs/2609.36722",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "lowet-2026",
    "title": "Constitutional adapters: Inference-time interventions for misalignment and misuse",
    "authors": [
      "Adam S. Lowet",
      "Mark Kurzeja"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.36657",
    "paper_url": "https://arxiv.org/abs/2609.36657",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "jalal-2026",
    "title": "Reducing the Adaptation Gap Through Reachable Fisher Geometry",
    "authors": [
      "Wasif Jalal",
      "Sachin Deb",
      "Asif Salekin"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.36329",
    "paper_url": "https://arxiv.org/abs/2609.36329",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "shaaban-2026",
    "title": "Tokenized Key-Gated Adapter Routing: A Secure Access Control Mechanism Against Private Data Leakage in LLMs",
    "authors": [
      "Mohamed Shaaban",
      "Mohamed Elmahallawy"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.00309",
    "paper_url": "https://arxiv.org/abs/2610.00309",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "raj-2026",
    "title": "EvE: An Alternate Optimizer to Adam",
    "authors": [
      "Shashank Raj",
      "Kalyanmoy Deb"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.35614",
    "paper_url": "https://arxiv.org/abs/2609.35614",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "wang-2026",
    "title": "Style-Driven Data Synthesis and Degradation-Aware Enhancement for Ultrasound Image Restoration",
    "authors": [
      "Yu-Kai Wang",
      "Chun-Xin Tan",
      "Manh-Hung Nguyen",
      "Ching-Chun Huang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.35120",
    "paper_url": "https://arxiv.org/abs/2609.35120",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "fernandes-2026",
    "title": "From One-Shot Generation to Incremental Music Composition: Adapting a General-Purpose Instruction LLM for Persistent Symbolic Editing",
    "authors": [
      "André Ricardo Ducca Fernandes",
      "Jean-Pierre Briot",
      "Simone Diniz Junqueira Barbosa1",
      "Hélio Côrtes Vieira Lopes"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.34994",
    "paper_url": "https://arxiv.org/abs/2609.34994",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "lei-2026",
    "title": "Just MLPs: Efficient Visual State Reconstruction for Multimodal Language Models",
    "authors": [
      "Jingdi lei",
      "Junxian Li",
      "Di Zhang",
      "Zhanqiu Zhang",
      "Yiwen Guo",
      "Soujanya Poria"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.34972",
    "paper_url": "https://arxiv.org/abs/2609.34972",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "zhang-2026",
    "title": "RoboFL: Federated Expert Assembly for World Action Models",
    "authors": [
      "Rongyu Zhang",
      "Ruizhi Fan",
      "Yunfan Lou",
      "Hengyu Fang",
      "Shenli Zheng",
      "Chenrui Wu",
      "Yili Jin",
      "Li Du",
      "Dan Wang",
      "Yuan Du",
      "Shanghang Zhang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.34968",
    "paper_url": "https://arxiv.org/abs/2609.34968",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "jin-2026",
    "title": "Brain-Conditioned Action Policies for Neural Motor Decoding",
    "authors": [
      "Luyao Jin",
      "Running Zhao",
      "Huan Zhao",
      "Vincent C. K. Cheung",
      "Wei-Hsin Liao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.34561",
    "paper_url": "https://arxiv.org/abs/2609.34561",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "yoo-2026",
    "title": "SPACE-LoRA: Allocating Activation-Subspace Protection for Continual Learning",
    "authors": [
      "Seunghyun Yoo",
      "Kiseok Kim",
      "Hyeontae Joo",
      "Junyeop Bang",
      "Hwangnam Kim"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.34453",
    "paper_url": "https://arxiv.org/abs/2609.34453",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "ding-2026",
    "title": "Rotated Manifold Optimization for Low-Rank Adaptation",
    "authors": [
      "Yuhui Ding",
      "Javier Zazo",
      "James Hensman"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.34264",
    "paper_url": "https://arxiv.org/abs/2609.34264",
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
    "added_date": "2026-10-05"
  },
  {
    "id": "zhu-2026",
    "title": "Loop Dropout: Regularizing Shared Updates in Looped Language Models",
    "authors": [
      "Zirui Zhu",
      "Hailun Xu",
      "Xuanlei Zhao",
      "Yong Liu",
      "Yingxuan Ren",
      "Kanchan Sarkar",
      "Kun Xu",
      "Yang You"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.34218",
    "paper_url": "https://arxiv.org/abs/2609.34218",
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
    "added_date": "2026-10-05"
  }
]
```
