# New arXiv PEFT papers — 2026-07-06

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **15**.

## Candidates

### Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation
- **Authors**: Jijie Zhang, Zhe Ren, Quan Zhang, Dandan Guo
- **arXiv**: [2607.02182](http://arxiv.org/abs/2607.02182v1)
- **Published**: 2026-07-02
- **Categories**: cs.LG, cs.CL

> Large language models (LLMs) exhibit remarkable reasoning capabilities, but their task-specific fine-tuning is notoriously plagued by overconfidence, severely hindering trustworthy deployment. We propose Data-Adaptive Lower-Rank Adaptation (DALorRA), a simple and effective variational Bayesian spars...

### Efficient PEFT Methods with Adaptive Checkpointing for Vision Models and VLMs on Resource Constrained Consumer-GPUs
- **Authors**: Altay Toktassyn, Jurn-Gyu Park
- **arXiv**: [2607.02158](http://arxiv.org/abs/2607.02158v1)
- **Published**: 2026-07-02
- **Categories**: cs.CV

> Modern pretrained vision models achieve strong accuracy but demand substantial GPU memory for fine-tuning, making edge deployment impractical. This paper compares five parameter-efficient fine-tuning (PEFT) methods (Full FT, LoRA, AdaLoRA, QLoRA, BitFit) on Transformers- (ViT-Small, TinyViT) and Mam...

### Towards Real-World Ultrasound Understanding: Large Vision-Language Models from Multi-Image Examinations with Long-Form Reports
- **Authors**: Bingcong Yan, Chunlei Li, Jingliang Hu, Yilei Shi, Xiao Xiang Zhu, Lichao Mou
- **arXiv**: [2607.01908](http://arxiv.org/abs/2607.01908v1)
- **Published**: 2026-07-02
- **Categories**: cs.CV

> Large vision-language models (LVLMs) have achieved strong performance across many medical imaging tasks, yet their application to ultrasound remains limited due to its inherent complexity and variability. In this work, we revisit what is truly needed to enable real-world ultrasound understanding. In...

### EPnG: Adaptive Expert Prune-and-Grow for Parameter-Efficient MoE Fine-tuning
- **Authors**: Ahin Lee, Sehyun Yun, Taesik Gong
- **arXiv**: [2607.01789](http://arxiv.org/abs/2607.01789v1)
- **Published**: 2026-07-02
- **Categories**: cs.LG, cs.AI

> Mixture-of-Experts (MoE) models scale efficiently but remain costly to adapt due to redundant experts and uniform parameter allocation. Existing parameter-efficient fine-tuning (PEFT) methods such as LoRA ignore MoE routing dynamics, leading to suboptimal resource use. We propose EPnG, an adaptive p...

### DroneFINE: Domain-Aware Parameter-Efficient Fine-Tuning of Vision-Language Detectors for Drone Images
- **Authors**: Ke Wu, Yanan Zhang, Yingjie Gao, Wenhao Li, Chenyu Zhou, XinZhu Ma, Jiaxin Chen, Di Huang
- **arXiv**: [2607.00338](http://arxiv.org/abs/2607.00338v1)
- **Published**: 2026-07-01
- **Categories**: cs.CV

> Object detection for Unmanned Aerial Vehicles (UAVs) working in open and dynamic environments is a highly challenging task. While Vision-Language Models (VLMs) have offered a powerful solution for universal object detection, adapting them to UAV scenarios remains non-trivial due to a substantial dom...

### RetailSMV: Exocentric vs. Egocentric Adaptation of Foundation Video World Models in Retail
- **Authors**: Amirreza Rouhi, Rajat Aggarwal, Parikshit Sakurikar, Anoop M. Namboodiri, Sashi P. Reddi
- **arXiv**: [2607.00310](http://arxiv.org/abs/2607.00310v1)
- **Published**: 2026-07-01
- **Categories**: cs.CV, cs.AI

> Foundation video diffusion models are increasingly viewed as world simulators for embodied agents, yet their pretraining on internet-scale generic video leaves them poorly aligned with real-world deployment domains. We study parameter-efficient adaptation of a pretrained foundation video world model...

### FRAME: Learning the Adaptation Domain with a Mixture of Fractional-Fourier Experts
- **Authors**: Tom Saliencro, Maya Lindqvist, Rohan Desai, Priya Nair, Daniel Whitmore
- **arXiv**: [2607.00162](http://arxiv.org/abs/2607.00162v1)
- **Published**: 2026-06-30
- **Categories**: cs.LG

> Parameter-efficient fine-tuning (PEFT) reparameterizes weight updates in a fixed basis: low-rank adapters operate in the spatial domain, while a recent line of spectral methods operates in a fixed Fourier domain. We argue that the choice of domain is itself a design degree of freedom that should be ...

### Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR
- **Authors**: Ruijia Zhang, Jiacheng Zhu, Hanqing Zhu, Laixi Shi
- **arXiv**: [2606.31813](http://arxiv.org/abs/2606.31813v1)
- **Published**: 2026-06-30
- **Categories**: cs.LG, cs.AI

> Low-rank adaptation (LoRA) and its variants enable parameter-efficient fine-tuning of large language models under the supervised fine-tuning (SFT) paradigm. However, their efficacy and behavior under Reinforcement learning with verifiable rewards (RLVR) are less well understood. In particular, two s...

### Nonlinearity-Aware LoRA: Structured Gate Adaptation under Low-Rank Constraints
- **Authors**: Shuai Yuan, Sudong Cai, Bingzhi Chen, Shuyuan Zheng, Chuan Xiao, Makoto Onizuka, Rui Mao
- **arXiv**: [2606.31717](http://arxiv.org/abs/2606.31717v1)
- **Published**: 2026-06-30
- **Categories**: cs.LG

> Low-rank adaptation (LoRA) is commonly viewed as an update-space approximation to full fine-tuning, yet this view is incomplete for self-gated Transformer feed-forward networks. In gated FFNs, a low-rank residual can change not only projected features but also the nonlinear selection weights that de...

### Seeing Through Multiple Views: Parameter-Efficient Fine-Tuning via Selective Neurons for Consistent Radiology Report Generation
- **Authors**: Yucheng Chen, Jinjing Zhu, Yang Yu, Yufei Shi, Hane Naghshbandi, Jinhua Liu, Angela S. Koh, Fang Fen, Kian Eng Ong, Si Yong Yeo
- **arXiv**: [2606.31099](http://arxiv.org/abs/2606.31099v1)
- **Published**: 2026-06-30
- **Categories**: cs.CV, cs.AI

> Recent years have seen substantial advances in radiology report generation (RRG), yet existing approaches predominantly adopt direct feature fusion when handling multi-view X-ray images. Such approaches overlook the potential clinical inconsistencies and inaccuracies arising when a single model proc...

### Knowledge Distillation from Large Reasoning Models to Compact Student Models: A Case Study on the John O Bryan Mathematics Competition
- **Authors**: Gaurab Baral, Aaditya Khanal, Yangyang Tao, Junxiu Zhou
- **arXiv**: [2606.31048](http://arxiv.org/abs/2606.31048v1)
- **Published**: 2026-06-30
- **Categories**: cs.LG, cs.AI

> This paper investigates knowledge distillation from a large reasoning model (DeepSeek-R1) to a compact student model (Qwen2.5-7B). Using historical problems from the John O'Bryan Mathematics Competition at Northern Kentucky University (2011-2025), we build a Chain-of-Thought (CoT) training corpus th...

### Towards Continual Motion-Language Agents: LoRA Variants for Incremental Motion Understanding and Generation
- **Authors**: Bertram Taetz, Hugo Albuquerque Cosme da Silva, Gabriele Bleser-Taetz
- **arXiv**: [2606.30266](http://arxiv.org/abs/2606.30266v1)
- **Published**: 2026-06-29
- **Categories**: cs.LG, cs.AI

> Motion-language agents must possess the bidirectional capability to both understand human movement (motion-to-text, M2T) and generate it from natural language (text-to-motion, T2M). While foundational models have achieved strong performance in static settings, autonomous agents operating in dynamic ...

### Few-Shot Domain Incremental Learning via Continual Vision-Language Consolidation
- **Authors**: Naeem Paeedeh, Mahardhika Pratama, Wolfgang Mayer, Mukesh Prasad, Weiping Ding, Yew-Soon Ong
- **arXiv**: [2606.30190](http://arxiv.org/abs/2606.30190v1)
- **Published**: 2026-06-29
- **Categories**: cs.CV, cs.AI, cs.LG

> Existing domain-incremental learning (DIL) strategies call for massive amounts of data to adapt to new domains and suffer from the overfitting problem in the case of data scarcity. This paper puts forward a relatively uncharted problem, namely, few-shot domain incremental learning (FSDIL), taking in...

### Neural Subspace Reallocation: Continual Learning as Retrieval-Based Subspace Memory Management
- **Authors**: Byeong Hoon Yoon
- **arXiv**: [2606.30067](http://arxiv.org/abs/2606.30067v1)
- **Published**: 2026-06-29
- **Categories**: cs.LG, cs.AI, cs.CV

> We introduce Neural Subspace Reallocation (NSR), which reframes continual learning as memory management over parameter subspaces. Instead of treating Low-Rank Adaptation (LoRA) modules as disposable per-task adapters, NSR manages them as compressible, retrievable memory units on a frozen backbone th...

### Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback
- **Authors**: Jiamei Jiang, Jiajing Zhang, Feifei Mo, Linjing Li, Daniel Zeng
- **arXiv**: [2606.29700](http://arxiv.org/abs/2606.29700v1)
- **Published**: 2026-06-29
- **Categories**: cs.AI

> Planning often requires symbolic specifications that are both executable and verifiable. For large language models deployed in autonomous or decision-support systems, failures in such formalization may lead to unverifiable decisions, execution failures, or unsafe downstream behavior. We present NL-P...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "zhang-2026",
    "title": "Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation",
    "authors": [
      "Jijie Zhang",
      "Zhe Ren",
      "Quan Zhang",
      "Dandan Guo"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.02182",
    "paper_url": "https://arxiv.org/abs/2607.02182",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "toktassyn-2026",
    "title": "Efficient PEFT Methods with Adaptive Checkpointing for Vision Models and VLMs on Resource Constrained Consumer-GPUs",
    "authors": [
      "Altay Toktassyn",
      "Jurn-Gyu Park"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.02158",
    "paper_url": "https://arxiv.org/abs/2607.02158",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "yan-2026",
    "title": "Towards Real-World Ultrasound Understanding: Large Vision-Language Models from Multi-Image Examinations with Long-Form Reports",
    "authors": [
      "Bingcong Yan",
      "Chunlei Li",
      "Jingliang Hu",
      "Yilei Shi",
      "Xiao Xiang Zhu",
      "Lichao Mou"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.01908",
    "paper_url": "https://arxiv.org/abs/2607.01908",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "lee-2026",
    "title": "EPnG: Adaptive Expert Prune-and-Grow for Parameter-Efficient MoE Fine-tuning",
    "authors": [
      "Ahin Lee",
      "Sehyun Yun",
      "Taesik Gong"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.01789",
    "paper_url": "https://arxiv.org/abs/2607.01789",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "wu-2026",
    "title": "DroneFINE: Domain-Aware Parameter-Efficient Fine-Tuning of Vision-Language Detectors for Drone Images",
    "authors": [
      "Ke Wu",
      "Yanan Zhang",
      "Yingjie Gao",
      "Wenhao Li",
      "Chenyu Zhou",
      "XinZhu Ma",
      "Jiaxin Chen",
      "Di Huang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.00338",
    "paper_url": "https://arxiv.org/abs/2607.00338",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "rouhi-2026",
    "title": "RetailSMV: Exocentric vs. Egocentric Adaptation of Foundation Video World Models in Retail",
    "authors": [
      "Amirreza Rouhi",
      "Rajat Aggarwal",
      "Parikshit Sakurikar",
      "Anoop M. Namboodiri",
      "Sashi P. Reddi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.00310",
    "paper_url": "https://arxiv.org/abs/2607.00310",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "saliencro-2026",
    "title": "FRAME: Learning the Adaptation Domain with a Mixture of Fractional-Fourier Experts",
    "authors": [
      "Tom Saliencro",
      "Maya Lindqvist",
      "Rohan Desai",
      "Priya Nair",
      "Daniel Whitmore"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.00162",
    "paper_url": "https://arxiv.org/abs/2607.00162",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "zhang-2026",
    "title": "Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR",
    "authors": [
      "Ruijia Zhang",
      "Jiacheng Zhu",
      "Hanqing Zhu",
      "Laixi Shi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.31813",
    "paper_url": "https://arxiv.org/abs/2606.31813",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "yuan-2026",
    "title": "Nonlinearity-Aware LoRA: Structured Gate Adaptation under Low-Rank Constraints",
    "authors": [
      "Shuai Yuan",
      "Sudong Cai",
      "Bingzhi Chen",
      "Shuyuan Zheng",
      "Chuan Xiao",
      "Makoto Onizuka",
      "Rui Mao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.31717",
    "paper_url": "https://arxiv.org/abs/2606.31717",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "chen-2026",
    "title": "Seeing Through Multiple Views: Parameter-Efficient Fine-Tuning via Selective Neurons for Consistent Radiology Report Generation",
    "authors": [
      "Yucheng Chen",
      "Jinjing Zhu",
      "Yang Yu",
      "Yufei Shi",
      "Hane Naghshbandi",
      "Jinhua Liu",
      "Angela S. Koh",
      "Fang Fen",
      "Kian Eng Ong",
      "Si Yong Yeo"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.31099",
    "paper_url": "https://arxiv.org/abs/2606.31099",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "baral-2026",
    "title": "Knowledge Distillation from Large Reasoning Models to Compact Student Models: A Case Study on the John O Bryan Mathematics Competition",
    "authors": [
      "Gaurab Baral",
      "Aaditya Khanal",
      "Yangyang Tao",
      "Junxiu Zhou"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.31048",
    "paper_url": "https://arxiv.org/abs/2606.31048",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "taetz-2026",
    "title": "Towards Continual Motion-Language Agents: LoRA Variants for Incremental Motion Understanding and Generation",
    "authors": [
      "Bertram Taetz",
      "Hugo Albuquerque Cosme da Silva",
      "Gabriele Bleser-Taetz"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.30266",
    "paper_url": "https://arxiv.org/abs/2606.30266",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "paeedeh-2026",
    "title": "Few-Shot Domain Incremental Learning via Continual Vision-Language Consolidation",
    "authors": [
      "Naeem Paeedeh",
      "Mahardhika Pratama",
      "Wolfgang Mayer",
      "Mukesh Prasad",
      "Weiping Ding",
      "Yew-Soon Ong"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.30190",
    "paper_url": "https://arxiv.org/abs/2606.30190",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "yoon-2026",
    "title": "Neural Subspace Reallocation: Continual Learning as Retrieval-Based Subspace Memory Management",
    "authors": [
      "Byeong Hoon Yoon"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.30067",
    "paper_url": "https://arxiv.org/abs/2606.30067",
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
    "added_date": "2026-07-06"
  },
  {
    "id": "jiang-2026",
    "title": "Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback",
    "authors": [
      "Jiamei Jiang",
      "Jiajing Zhang",
      "Feifei Mo",
      "Linjing Li",
      "Daniel Zeng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.29700",
    "paper_url": "https://arxiv.org/abs/2606.29700",
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
    "added_date": "2026-07-06"
  }
]
```
