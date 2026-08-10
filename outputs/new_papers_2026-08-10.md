# New arXiv PEFT papers — 2026-08-10

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **23**.

## Candidates

### Unsupervised Adaptation of PDE Foundation Models
- **Authors**: Ziye Song, Zhao Wei, Xin Yu, Ivor Tsang, Yueming Lyu
- **arXiv**: [2608.07053](http://arxiv.org/abs/2608.07053v1)
- **Published**: 2026-08-07
- **Categories**: cs.AI

> Pretrained partial differential equation (PDE) foundation models can generalize across different equations, but adapting them to unseen PDE systems typically requires dense solution data, which is often expensive or unavailable. To address this limitation, we propose an unsupervised PDE-based finetu...

### YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family
- **Authors**: Xu Lin, WenJie Nie, Jinlong Peng, Weifu Fu, YueXiao Ma, Xiawu Zheng, Yong Liu
- **arXiv**: [2608.07051](http://arxiv.org/abs/2608.07051v1)
- **Published**: 2026-08-07
- **Categories**: cs.CV

> Generic parameter-efficient fine-tuning (PEFT) methods transferred from language models can fail silently on real-time detectors, whose heterogeneous operators and detection-specific components impose placement constraints absent from regular Transformer stacks. We propose YOLO-PEFT, a structure-awa...

### Simple-OPD: Demystifying Warm-up for On-policy Distillation
- **Authors**: Tao Liu, Taiqiang Wu, Mao Zheng, Xuan Luo, Runming Yang, Xuewei Yang, Junjie Wang, Yujiu Yang
- **arXiv**: [2608.06802](http://arxiv.org/abs/2608.06802v1)
- **Published**: 2026-08-07
- **Categories**: cs.CL

> On-policy distillation (OPD) trains a student on its own rollouts with token-level supervision from teacher models, but its effectiveness can depend strongly on the warm-up stage before OPD. In this paper, we demystify warm-up for OPD from both data and training perspectives. For data, we find that ...

### LoRAScan: Detecting Backdoor Prompts in Low-Rank Adapters for Large Language Models via Down-Projection Activation Spikes
- **Authors**: Doniyorkhon Obidov, Honggang Yu, Xiaolong Guo, Kaichen Yang
- **arXiv**: [2608.06795](http://arxiv.org/abs/2608.06795v1)
- **Published**: 2026-08-07
- **Categories**: cs.CR, cs.AI, cs.CL

> Low-rank adaptation (LoRA) enables efficient specialization and distribution of large language models through compact adapters. However, untrusted adapters introduce a supply-chain threat: a backdoored adapter can cause a model to generate harmful content, malicious code, political propaganda, or co...

### When Semantics Saturate or Emerge: Adaptation-Conditional Semantic Utility in Source-Free Cross-Domain Few-Shot Learning
- **Authors**: Wei Liu, Xing Deng, Haijian Shao
- **arXiv**: [2608.06673](http://arxiv.org/abs/2608.06673v1)
- **Published**: 2026-08-07
- **Categories**: cs.CV

> Language descriptions in source-free cross-domain few-shot learning (SF-CDFSL) are often selected according to zero-shot accuracy obtained with a frozen vision--language model. This paper asks whether that ranking remains valid after target-domain visual adaptation. Under a strictly paired protocol,...

### Theoretical Foundations of Communication-Efficient, Robust, and Practical Distributed and Federated Optimization
- **Authors**: Grigory Malinovsky
- **arXiv**: [2608.06563](http://arxiv.org/abs/2608.06563v1)
- **Published**: 2026-08-06
- **Categories**: cs.LG, math.OC

> Machine learning and optimization have advanced together, with practical demands motivating new theory and theoretical breakthroughs enabling new applications. Modern large-scale training relies on classical optimization principles, but the constraints of distributed systems require these foundation...

### On the Effectiveness of Adaptation Strategies for VLM-Based Federated Learning in Remote Sensing
- **Authors**: Simon Lösche, Barış Büyüktaş, Mathis Adler, Angelos Zavras, Ioannis Papoutsis, Begüm Demir
- **arXiv**: [2608.04791](http://arxiv.org/abs/2608.04791v1)
- **Published**: 2026-08-05
- **Categories**: cs.CV

> Federated learning (FL) enables collaborative training of deep learning models across decentralized image archives without requiring data centralization. This paradigm is particularly relevant in remote sensing (RS), where legal regulations, privacy concerns, and bandwidth constraints restrict data ...

### Energy- and Memory-Efficient PEFT Methods for Personalized On-Device SLMs on Consumer GPUs
- **Authors**: Kuanysh Akhmetzhanov, Jurn-Gyu Park
- **arXiv**: [2608.04488](http://arxiv.org/abs/2608.04488v1)
- **Published**: 2026-08-05
- **Categories**: cs.CL

> Despite rapid advances in large language models (LLMs), deploying and personalizing them on resource-constrained devices remains impractical due to high VRAM, time, and energy costs. Parameter-Efficient Fine-Tuning (PEFT) of Small Language Models (SLMs) offers a promising alternative, yet few studie...

### MERaLiON-GR: Speech Gender Recognition Model for English and SEA Languages
- **Authors**: Qiongqiong Wang, Ai Ti Aw, Nancy F. Chen, Ying Lay Chiu, Yang Ding, Yingxu He, Ridong Jiang, Zhuohan Liu, Yanfeng Lu, Yi Ma, Muhammad Huzaifah, Nabilah Binte Md Johan, Nattadaporn Lertcheva, Pham Minh Duc, Sailor Hardik Bhupendra, Siti Umairah Binte Mohammad Salleh, Shuo Sun, Tarun Kumar Vangani, Jeremy H. M. Wong, Jinyang Wu, Longyin Zhang
- **arXiv**: [2608.04433](http://arxiv.org/abs/2608.04433v1)
- **Published**: 2026-08-05
- **Categories**: cs.CL, cs.AI

> We present MERaLiON-GR, a speech gender recognition system that performs binary classification (female / male) on English and Southeast Asian (SEA) languages. The model finetunes MERaLiON-SpeechEncoder-2, a large conformer based transformer pre-trained on a broad speech corpus, and applies parameter...

### HyPASE: Hyperbolic Geometry for Parameter-Efficient Speech Emotion Fine-Tuning Framework for Large Audio-Language Models
- **Authors**: Tian Jin, Ruikang Zhang, Zefeng Zhao, Ding Luo, Jin Zeng
- **arXiv**: [2608.04351](http://arxiv.org/abs/2608.04351v1)
- **Published**: 2026-08-05
- **Categories**: cs.SD, cs.AI

> Large Audio-Language Models (LALMs) excel at general speech understanding; however, adapting them to fine-grained tasks like Speech Emotion Recognition (SER) remains a significant bottleneck. Current Parameter-Efficient Fine-Tuning (PEFT) methods typically operate in flat Euclidean space, and this g...

### Geometry-Informed Parameter-Efficient Fine-Tuning of Pre-trained Molecular GNNs for Blood-Brain Barrier Permeability Prediction
- **Authors**: Marco Vieto Vega, Long D. Nguyen, Binh P. Nguyen
- **arXiv**: [2608.04257](http://arxiv.org/abs/2608.04257v1)
- **Published**: 2026-08-04
- **Categories**: cs.LG

> Blood-brain barrier permeability (BBBP) prediction is a critical screening task in central nervous system drug discovery, where candidate molecules must be assessed for whether they can cross, or should be prevented from crossing, the blood-brain barrier. However, this task remains challenging becau...

### Large Language Models for Low-Resource Languages: A Conceptual Framework for an Electronic Explanatory Dictionary of the Tajik Language
- **Authors**: Mullosharaf K. Arabov, S. S. Pirov, B. Sultonov
- **arXiv**: [2608.04186](http://arxiv.org/abs/2608.04186v2)
- **Published**: 2026-08-04
- **Categories**: cs.CL

> This paper presents a conceptual framework for developing an electronic explanatory dictionary of the Tajik language using large language models (LLMs). The relevance of the work stems from the absence of a comprehensive digital lexicographic resource for Tajik that is comparable in functionality to...

### Omega-S: A Functional Resilience Index for LLM Fine-Tuning
- **Authors**: Alberto Acedo
- **arXiv**: [2608.03887](http://arxiv.org/abs/2608.03887v1)
- **Published**: 2026-08-04
- **Categories**: cs.LG, cs.NE, q-bio.MN

> Fine-tuning a large language model on new data degrades what it previously learned. We present Omega-S, a drop-in penalty computed from the weight matrix alone: it needs no previous-task data, no Fisher matrix and no stored copy of the old weights. It is three lines in an existing training loop and ...

### MuRA: Multi-Rank Adaptation for Efficient and Effective Test-Time Vision-Language Generalization
- **Authors**: Gengyuan Liu, Nanzhou Wang, Chang Liu, Qinwen Wu, Zhenhao Wang, Jiacong Wang, Bokui Chen, Xiangyang Ji
- **arXiv**: [2608.03885](http://arxiv.org/abs/2608.03885v1)
- **Published**: 2026-08-04
- **Categories**: cs.CV

> Vision-language models exhibit remarkable zero-shot capabilities but suffer significant performance degradation under distribution shifts. While test-time adaptation (TTA) via Low-Rank Adaptation offers a parameter-efficient solution, we identify a fundamental bottleneck in current methods: the reli...

### FraQ: Efficient Coordinate-Space Recompression for Federated Low-Rank Adaptation
- **Authors**: Shenghui Li, Thiemo Voigt
- **arXiv**: [2608.03605](http://arxiv.org/abs/2608.03605v1)
- **Published**: 2026-08-04
- **Categories**: cs.AI

> Federated fine-tuning with Low-Rank Adaptation (LoRA) enables efficient collaborative adaptation of Large Language Models (LLMs) without centralizing private data. However, LoRA's two-factor parameterization creates an aggregation mismatch across clients: naively averaging the factors does not recov...

### Pin Once, Swap Light: Subspace-Aligned Centroid-Residual Training for Efficient Ultra-LoRA Serving
- **Authors**: Xiang Li, Pengcheng Wang, Huazheng Wang, Saurabh Bagchi
- **arXiv**: [2608.03579](http://arxiv.org/abs/2608.03579v1)
- **Published**: 2026-08-04
- **Categories**: cs.LG, cs.AI

> Modern multi-tenant Low-Rank Adapters (LoRAs) serving systems concurrently host tens to hundreds of LoRA adapters. Though powerful, this introduces a critical system dilemma between serving efficiency and task performance: higher-rank adapters generally achieve better downstream task performance, bu...

### MoEGen: Mixture-of-Experts for Instance-Adaptive LoRA Generation
- **Authors**: Yiming Zeng, Lei Lu, Zexin Li, Zhuochun Li, Shuoqiu Li, Shuyi Liao, Xidong Wu, Zeyu Zhang, Minmei Wang, Yu Zhao, Tingting Yu, Shangqian Gao
- **arXiv**: [2608.03275](http://arxiv.org/abs/2608.03275v1)
- **Published**: 2026-08-04
- **Categories**: cs.CL

> Parameter-efficient fine-tuning (PEFT) enables efficient adaptation of large language models, but existing MoE-based PEFT methods typically improve capacity by storing multiple full LoRA experts, causing adapter storage to grow linearly with the number of experts and restricting adaptation to a fixe...

### LoCA: Forward-Only LLM Tuning after One-Shot Calibration with Local Credit Assignment
- **Authors**: Linhan Xia, Rui Liu, Zhaofeng Zhang, Yihao Wang, Binrui Shen, Shengxin Zhu
- **arXiv**: [2608.03020](http://arxiv.org/abs/2608.03020v2)
- **Published**: 2026-08-04
- **Categories**: cs.AI

> Parameter-efficient post-training reduces the number of trainable parameters, but still requires repeated end-to-end backpropagation through the frozen backbone. Every adaptation step therefore needs backward-capable hardware and must store or recompute activations. We ask whether this repeated back...

### Uncertainty Is Not Enough: Value-of-Information Routing for Mixtures of LoRA Experts
- **Authors**: Tom Saliencro, Rohan Desai, Priya Nair, Maya Lindqvist, Daniel Whitmore
- **arXiv**: [2608.02528](http://arxiv.org/abs/2608.02528v1)
- **Published**: 2026-08-03
- **Categories**: cs.LG

> Mixtures of low-rank adaptation experts increase parameter-efficient capacity by routing each input through a subset of adapters. Recent dynamic routers activate more experts when the router or prediction is uncertain. This rule silently equates uncertainty with useful additional computation: an unc...

### Z-PEFT: Zero-shot Backdoor Detection in Parameter-Efficient Fine-Tuning via Canonical Spectral Signatures
- **Authors**: Nicola Pitzalis, Donald Shenaj, Giacomo Cignoni, Andrea Cossu, Davide Bacciu, Antonio Carta
- **arXiv**: [2608.02271](http://arxiv.org/abs/2608.02271v1)
- **Published**: 2026-08-03
- **Categories**: cs.LG

> Parameter-Efficient Fine-tuned (PEFT) models are frequently downloaded from open repositories by practitioners. This widespread practice creates a significant attack surface, as malicious actors can publish backdoored models that induce specific behaviors in response to predefined triggers. We study...

### Proxy Avatar Meets Low-Rank Caching: Real-Time One-Shot Emotion-Controllable Portrait Animation
- **Authors**: Haijie Yang, Jindi Bao, Yixuan Dong, Hongliang Zhang, Jian Bi, Hao Tang, Zhenyu Zhang, Jianjun Qian, Jian Yang
- **arXiv**: [2608.01978](http://arxiv.org/abs/2608.01978v1)
- **Published**: 2026-08-03
- **Categories**: cs.CV

> Audio-driven portrait animation has advanced rapidly with diffusion-based generative models, yet real-time one-shot generation with expressive emotion control remains challenging. Existing methods often suffer from insufficient emotion-aware motion priors and expensive appearance computation during ...

### Analyzing Speech Condition Effects in Dysarthric ASR: A Layer-wise Probing Study
- **Authors**: Darwin Jelestin Muthu, Navya Gupta, Wei Lin Tay, Zhengchen Zhang, Daniel Wang Zhengkui, Rong Tong
- **arXiv**: [2608.01865](http://arxiv.org/abs/2608.01865v1)
- **Published**: 2026-08-03
- **Categories**: cs.CL

> Automatic speech recognition (ASR) performance degrades sharply on dysarthric speech, yet how disordered articulation reshapes a model's internal representations is underexplored. We present a layer-wise probing analysis of a transformer ASR encoder on Mandarin dysarthric speech under three transcri...

### SPECTRA: Band-Routed Embedding and Stage-Wise LoRA for Cross-Sensor Fine-Tuning of Geospatial Foundation Models
- **Authors**: Xingyan Li, Jordan A. Caraballo-Vega, Jie Gong, Mark L. Carroll, Jianwu Wang
- **arXiv**: [2608.01751](http://arxiv.org/abs/2608.01751v1)
- **Published**: 2026-08-03
- **Categories**: cs.CV, cs.AI

> Geospatial foundation models (GeoFMs), pretrained on large-scale geospatial data such as Earth observation (EO), climate, and weather data, have shown promising performance when fine-tuned on diverse downstream tasks. However, there are two challenges of adapting EO-pretrained GeoFMs to practical do...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "song-2026",
    "title": "Unsupervised Adaptation of PDE Foundation Models",
    "authors": [
      "Ziye Song",
      "Zhao Wei",
      "Xin Yu",
      "Ivor Tsang",
      "Yueming Lyu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.07053",
    "paper_url": "https://arxiv.org/abs/2608.07053",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "lin-2026",
    "title": "YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family",
    "authors": [
      "Xu Lin",
      "WenJie Nie",
      "Jinlong Peng",
      "Weifu Fu",
      "YueXiao Ma",
      "Xiawu Zheng",
      "Yong Liu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.07051",
    "paper_url": "https://arxiv.org/abs/2608.07051",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "liu-2026",
    "title": "Simple-OPD: Demystifying Warm-up for On-policy Distillation",
    "authors": [
      "Tao Liu",
      "Taiqiang Wu",
      "Mao Zheng",
      "Xuan Luo",
      "Runming Yang",
      "Xuewei Yang",
      "Junjie Wang",
      "Yujiu Yang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.06802",
    "paper_url": "https://arxiv.org/abs/2608.06802",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "obidov-2026",
    "title": "LoRAScan: Detecting Backdoor Prompts in Low-Rank Adapters for Large Language Models via Down-Projection Activation Spikes",
    "authors": [
      "Doniyorkhon Obidov",
      "Honggang Yu",
      "Xiaolong Guo",
      "Kaichen Yang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.06795",
    "paper_url": "https://arxiv.org/abs/2608.06795",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "liu-2026",
    "title": "When Semantics Saturate or Emerge: Adaptation-Conditional Semantic Utility in Source-Free Cross-Domain Few-Shot Learning",
    "authors": [
      "Wei Liu",
      "Xing Deng",
      "Haijian Shao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.06673",
    "paper_url": "https://arxiv.org/abs/2608.06673",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "malinovsky-2026",
    "title": "Theoretical Foundations of Communication-Efficient, Robust, and Practical Distributed and Federated Optimization",
    "authors": [
      "Grigory Malinovsky"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.06563",
    "paper_url": "https://arxiv.org/abs/2608.06563",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "l-sche-2026",
    "title": "On the Effectiveness of Adaptation Strategies for VLM-Based Federated Learning in Remote Sensing",
    "authors": [
      "Simon Lösche",
      "Barış Büyüktaş",
      "Mathis Adler",
      "Angelos Zavras",
      "Ioannis Papoutsis",
      "Begüm Demir"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.04791",
    "paper_url": "https://arxiv.org/abs/2608.04791",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "akhmetzhanov-2026",
    "title": "Energy- and Memory-Efficient PEFT Methods for Personalized On-Device SLMs on Consumer GPUs",
    "authors": [
      "Kuanysh Akhmetzhanov",
      "Jurn-Gyu Park"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.04488",
    "paper_url": "https://arxiv.org/abs/2608.04488",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "wang-2026",
    "title": "MERaLiON-GR: Speech Gender Recognition Model for English and SEA Languages",
    "authors": [
      "Qiongqiong Wang",
      "Ai Ti Aw",
      "Nancy F. Chen",
      "Ying Lay Chiu",
      "Yang Ding",
      "Yingxu He",
      "Ridong Jiang",
      "Zhuohan Liu",
      "Yanfeng Lu",
      "Yi Ma",
      "Muhammad Huzaifah",
      "Nabilah Binte Md Johan",
      "Nattadaporn Lertcheva",
      "Pham Minh Duc",
      "Sailor Hardik Bhupendra",
      "Siti Umairah Binte Mohammad Salleh",
      "Shuo Sun",
      "Tarun Kumar Vangani",
      "Jeremy H. M. Wong",
      "Jinyang Wu",
      "Longyin Zhang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.04433",
    "paper_url": "https://arxiv.org/abs/2608.04433",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "jin-2026",
    "title": "HyPASE: Hyperbolic Geometry for Parameter-Efficient Speech Emotion Fine-Tuning Framework for Large Audio-Language Models",
    "authors": [
      "Tian Jin",
      "Ruikang Zhang",
      "Zefeng Zhao",
      "Ding Luo",
      "Jin Zeng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.04351",
    "paper_url": "https://arxiv.org/abs/2608.04351",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "vega-2026",
    "title": "Geometry-Informed Parameter-Efficient Fine-Tuning of Pre-trained Molecular GNNs for Blood-Brain Barrier Permeability Prediction",
    "authors": [
      "Marco Vieto Vega",
      "Long D. Nguyen",
      "Binh P. Nguyen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.04257",
    "paper_url": "https://arxiv.org/abs/2608.04257",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "arabov-2026",
    "title": "Large Language Models for Low-Resource Languages: A Conceptual Framework for an Electronic Explanatory Dictionary of the Tajik Language",
    "authors": [
      "Mullosharaf K. Arabov",
      "S. S. Pirov",
      "B. Sultonov"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.04186",
    "paper_url": "https://arxiv.org/abs/2608.04186",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "acedo-2026",
    "title": "Omega-S: A Functional Resilience Index for LLM Fine-Tuning",
    "authors": [
      "Alberto Acedo"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.03887",
    "paper_url": "https://arxiv.org/abs/2608.03887",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "liu-2026",
    "title": "MuRA: Multi-Rank Adaptation for Efficient and Effective Test-Time Vision-Language Generalization",
    "authors": [
      "Gengyuan Liu",
      "Nanzhou Wang",
      "Chang Liu",
      "Qinwen Wu",
      "Zhenhao Wang",
      "Jiacong Wang",
      "Bokui Chen",
      "Xiangyang Ji"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.03885",
    "paper_url": "https://arxiv.org/abs/2608.03885",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "li-2026",
    "title": "FraQ: Efficient Coordinate-Space Recompression for Federated Low-Rank Adaptation",
    "authors": [
      "Shenghui Li",
      "Thiemo Voigt"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.03605",
    "paper_url": "https://arxiv.org/abs/2608.03605",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "li-2026",
    "title": "Pin Once, Swap Light: Subspace-Aligned Centroid-Residual Training for Efficient Ultra-LoRA Serving",
    "authors": [
      "Xiang Li",
      "Pengcheng Wang",
      "Huazheng Wang",
      "Saurabh Bagchi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.03579",
    "paper_url": "https://arxiv.org/abs/2608.03579",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "zeng-2026",
    "title": "MoEGen: Mixture-of-Experts for Instance-Adaptive LoRA Generation",
    "authors": [
      "Yiming Zeng",
      "Lei Lu",
      "Zexin Li",
      "Zhuochun Li",
      "Shuoqiu Li",
      "Shuyi Liao",
      "Xidong Wu",
      "Zeyu Zhang",
      "Minmei Wang",
      "Yu Zhao",
      "Tingting Yu",
      "Shangqian Gao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.03275",
    "paper_url": "https://arxiv.org/abs/2608.03275",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "xia-2026",
    "title": "LoCA: Forward-Only LLM Tuning after One-Shot Calibration with Local Credit Assignment",
    "authors": [
      "Linhan Xia",
      "Rui Liu",
      "Zhaofeng Zhang",
      "Yihao Wang",
      "Binrui Shen",
      "Shengxin Zhu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.03020",
    "paper_url": "https://arxiv.org/abs/2608.03020",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "saliencro-2026",
    "title": "Uncertainty Is Not Enough: Value-of-Information Routing for Mixtures of LoRA Experts",
    "authors": [
      "Tom Saliencro",
      "Rohan Desai",
      "Priya Nair",
      "Maya Lindqvist",
      "Daniel Whitmore"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.02528",
    "paper_url": "https://arxiv.org/abs/2608.02528",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "pitzalis-2026",
    "title": "Z-PEFT: Zero-shot Backdoor Detection in Parameter-Efficient Fine-Tuning via Canonical Spectral Signatures",
    "authors": [
      "Nicola Pitzalis",
      "Donald Shenaj",
      "Giacomo Cignoni",
      "Andrea Cossu",
      "Davide Bacciu",
      "Antonio Carta"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.02271",
    "paper_url": "https://arxiv.org/abs/2608.02271",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "yang-2026",
    "title": "Proxy Avatar Meets Low-Rank Caching: Real-Time One-Shot Emotion-Controllable Portrait Animation",
    "authors": [
      "Haijie Yang",
      "Jindi Bao",
      "Yixuan Dong",
      "Hongliang Zhang",
      "Jian Bi",
      "Hao Tang",
      "Zhenyu Zhang",
      "Jianjun Qian",
      "Jian Yang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.01978",
    "paper_url": "https://arxiv.org/abs/2608.01978",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "muthu-2026",
    "title": "Analyzing Speech Condition Effects in Dysarthric ASR: A Layer-wise Probing Study",
    "authors": [
      "Darwin Jelestin Muthu",
      "Navya Gupta",
      "Wei Lin Tay",
      "Zhengchen Zhang",
      "Daniel Wang Zhengkui",
      "Rong Tong"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.01865",
    "paper_url": "https://arxiv.org/abs/2608.01865",
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
    "added_date": "2026-08-10"
  },
  {
    "id": "li-2026",
    "title": "SPECTRA: Band-Routed Embedding and Stage-Wise LoRA for Cross-Sensor Fine-Tuning of Geospatial Foundation Models",
    "authors": [
      "Xingyan Li",
      "Jordan A. Caraballo-Vega",
      "Jie Gong",
      "Mark L. Carroll",
      "Jianwu Wang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2608.01751",
    "paper_url": "https://arxiv.org/abs/2608.01751",
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
    "added_date": "2026-08-10"
  }
]
```
