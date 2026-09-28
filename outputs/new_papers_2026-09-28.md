# New arXiv PEFT papers — 2026-09-28

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **31**.

## Candidates

### New LoRA Skills Should Read but Never Write
- **Authors**: Zeyan Li, Panqi Yang, Qirong Guo, Shengda Zhuo, SIyuan Qiu, Hu Xu, Chun Li, Jianfeng Xu
- **arXiv**: [2609.31600](http://arxiv.org/abs/2609.31600v1)
- **Published**: 2026-09-25
- **Categories**: cs.LG

> Low-rank adapters (LoRA) make it cheap to fine-tune a large language model once per task, but combining several independently trained adapters into one model remains difficult: merging the updates in weight space causes interference, retraining on all task data is expensive, and routing between sepa...

### From Reward Signal to Visual Utility: A Controlled Audit of Medical VLM Post-Training
- **Authors**: Wang Jingxin
- **arXiv**: [2609.31450](http://arxiv.org/abs/2609.31450v1)
- **Published**: 2026-09-25
- **Categories**: cs.CV, cs.AI

> Medical vision-language model (VLM) post-training is commonly evaluated through answer accuracy. We examine how changes in accuracy and training objectives relate to image-conditioned decisions in a controlled Qwen2.5-VL-3B study on PMC-VQA. We compare supervised fine-tuning (SFT) with low-rank adap...

### ViSTA: A Simple Bridge Extends Visual Alignment to Clinical Time-Series Understanding in Multimodal LLMs
- **Authors**: Junyi Gao, Yu Shi, Pingzhao Hu, Ewen M Harrison
- **arXiv**: [2609.31448](http://arxiv.org/abs/2609.31448v1)
- **Published**: 2026-09-25
- **Categories**: cs.CL, cs.AI

> Clinical prediction models estimate risk from patient measurements, while large language models support medical text understanding and question answering. Yet their language capabilities do not ensure accurate prediction from structured, high-dimensional clinical time series. Improving this ability ...

### Audio emotion recognition for atypical hearing
- **Authors**: Ulysse Roussel
- **arXiv**: [2609.31168](http://arxiv.org/abs/2609.31168v1)
- **Published**: 2026-09-25
- **Categories**: cs.LG

> My doctoral work aims to explore Audio Emotion Recognition (AER) in the context of atypical listening. This research focuses on auditory hypersensitivity in people with autism, a phenomenon that is often difficult to evaluate and unique to each individual. Our core idea is to leverage our understand...

### FAVoR: Measuring and Mitigating Author-Style Homogenization in Federated Personalized Generation
- **Authors**: Lu Han, Jingyao Zhang, Katy Ilonka Gero, Nguyen H. Tran
- **arXiv**: [2609.30968](http://arxiv.org/abs/2609.30968v1)
- **Published**: 2026-09-25
- **Categories**: cs.CL

> Large language models are increasingly used as personalized writing assistants, but adapting a model across many authors can compromise individual writing style by pulling author-specific signals toward a shared register. Federated parameter-efficient fine-tuning (PEFT) offers a data-local setting f...

### JevSoup: System-One Routing for Training-Free LoRA Composition
- **Authors**: Xiuying Wang, Jiahua Cheng, Shuotian Li, Yufan Cheng, Bowen Deng, Zhexuan Bai, Yichen Li
- **arXiv**: [2609.30922](http://arxiv.org/abs/2609.30922v1)
- **Published**: 2026-09-25
- **Categories**: cs.AI

> Building adaptable AI systems requires effective coordination of specialized capabilities across diverse tasks. Low-rank adaptation (LoRA) enables modular expertise, but existing routing approaches may require auxiliary data, additional training, or autoregressive decoding. We propose JevSoup, a tra...

### Adaptive Fisher-Whitened Cross-Covariance for Low-Resource Speech Recognition
- **Authors**: Asmee Mishra, Mengjie Qian, Brechtje Post, Kate Knill
- **arXiv**: [2609.29800](http://arxiv.org/abs/2609.29800v1)
- **Published**: 2026-09-24
- **Categories**: cs.CL

> Adapting multilingual speech foundation models to low-resource languages remains difficult, especially for languages that are poorly represented during pre-training. While parameter-efficient fine-tuning (PEFT) reduces the cost of adapting large models, conventional approaches such as LoRA rely on g...

### On Growth and Form, and Function: Reusable Regulatory Handles Control Phenotypic Variation
- **Authors**: Benedikt Hartl, Milton L. Montero, Marcello Barylli, Sebastian Risi, Michael Levin
- **arXiv**: [2609.29755](http://arxiv.org/abs/2609.29755v1)
- **Published**: 2026-09-24
- **Categories**: cs.NE, cs.LG

> How phenotypic transformations are implemented by changes in underlying regulatory dynamics remains a central question in developmental biology. Inspired by D'Arcy Thompson's 1917 "On Growth and Form", we ask whether coherent large-scale transformations of morphology can be encoded as low-dimensiona...

### Where LLM Graders Succeed and Break: Evidence from Two Computer-Science Exams
- **Authors**: Ali Habibullah, Yazan Alshoibi, Mohammad Alshiekh, Salman Khan, Naeemullah Khan
- **arXiv**: [2609.29333](http://arxiv.org/abs/2609.29333v1)
- **Published**: 2026-09-24
- **Categories**: cs.CL, cs.AI, cs.CY

> One long-form exam in a large course costs hundreds of grader-hours, and qualified graders are scarce; LLM graders are a tempting alternative. To show its pitfalls we grade a practical Computer Vision exam ($570$ dual-graded students) under $171$ configurations spanning closed and open-weights model...

### Automatic Rank Allocation for Low-Rank Adaptation in Large Language Models via lp Regularization
- **Authors**: Zebang Xie, Chuanyang Zheng, Yik-Chung Wu, Yihang Gao
- **arXiv**: [2609.28998](http://arxiv.org/abs/2609.28998v1)
- **Published**: 2026-09-24
- **Categories**: cs.LG

> Low-rank adaptation (LoRA) has become a popular parameter-efficient fine-tuning method for large language models. A key challenge in LoRA is how to determine the rank of each adaptation matrix, as rank directly controls its capacity and efficiency. Existing adaptive-rank methods typically allocate r...

### Personalized Korean Lipreading as Visual Speech Recognition: Transfer, Census and Adaptation on OLKAVS
- **Authors**: Se Un Park, Hakjun Kim, Taehoon Roh, Junyoung Park
- **arXiv**: [2609.28988](http://arxiv.org/abs/2609.28988v1)
- **Published**: 2026-09-24
- **Categories**: eess.AS, cs.CL, cs.CV

> We present a personalized Korean visual speech recognition (VSR) system and quantify, on the nine-camera OLKAVS corpus, the gap between the population-level benchmark score and an individual user's error. A video-only Conformer initialized from English-trained weights attains 9.95 - 12.19% character...

### Multimodal Routing and Region Refinement for Language-Guided Medical Image Segmentation
- **Authors**: Md Maklachur Rahman, Md Hasan Al Banna, Saraf Anjum, Assame Arnob, Tracy Hammond
- **arXiv**: [2609.28860](http://arxiv.org/abs/2609.28860v1)
- **Published**: 2026-09-24
- **Categories**: cs.CV, cs.LG

> Textual descriptions can reduce ambiguity in medical image segmentation by specifying the finding and location to be delineated. Existing text-guided methods mainly improve where image and language features interact but generally retain a single learned update pathway across all image-text pairs. We...

### MEVL-STP: Multi-Encoder and Vision Language Model for Arbitrarily Shaped Scene Text Spotting
- **Authors**: Aman Anand, Partha Pratim Roy, Shivakumara Palaiahnakote
- **arXiv**: [2609.28857](http://arxiv.org/abs/2609.28857v1)
- **Published**: 2026-09-23
- **Categories**: cs.CV

> Scene text spotting remains challenging for arbitrarily shaped text instances such as curved signs and dense multi-oriented characters in natural images, where tightly coupled architectures propagate localization errors directly into recognition failures. We present a two-stage pipeline that combine...

### Spooftral: Can Voxtral Audio-Language Model Detect Speech Spoofing?
- **Authors**: Avishai Weizman, Yehuda Ben-Shimol, Itshak Lapidot
- **arXiv**: [2609.28713](http://arxiv.org/abs/2609.28713v1)
- **Published**: 2026-09-23
- **Categories**: eess.AS, cs.CL

> Self-supervised learning (SSL) countermeasures (CMs) have shown strong performance in recent years. However, they often show degraded performance while facing unseen spoofing attacks and mismatched conditions. This study examines the Voxtral audio-language model (ALM) framework for spoofing detectio...

### Cross-Scale Transfer Learning for Depression Severity Prediction: From PHQ-8 to HAMD-17 Across Languages and Clinical Paradigms
- **Authors**: Wenjie Feng, Sahba Zojaji, Satoshi Nakamura
- **arXiv**: [2609.28430](http://arxiv.org/abs/2609.28430v1)
- **Published**: 2026-09-23
- **Categories**: cs.CL

> This work addresses continuous depression-severity score prediction from clinical interview transcripts under data scarcity. We propose a sequential low-rank adaptation (LoRA) protocol for cross-scale transfer: a Qwen3 backbone with a bounded regression head is first fine-tuned on the English DAIC-W...

### Riemannian Structure and Optimization for a Class of Low-Parametric Orthogonal Matrices
- **Authors**: Ali Aliev, Maxim Rakhuba
- **arXiv**: [2609.27982](http://arxiv.org/abs/2609.27982v1)
- **Published**: 2026-09-23
- **Categories**: cs.LG, cs.AI, math.DG, math.NA

> In this paper, we are concerned with matrices formed by block-diagonal factors interleaved with fixed permutations -- a flexible family of structured matrices. This class has recently drawn interest in deep learning architectures for its balanced expressivity-efficiency trade-off, yet efficient comp...

### Alignment Inertia: Auditing the Durability of Training Data Influence Through Policy Override Resistance
- **Authors**: Renata Barreto, Markelle Roesti, Mohammad Tahaei
- **arXiv**: [2609.27333](http://arxiv.org/abs/2609.27333v1)
- **Published**: 2026-09-23
- **Categories**: cs.AI

> Platform operators increasingly rely on system prompts and fine-tuning to govern model behavior, yet it remains unclear how reliably these interventions override behavior inherited from prior training. We propose Override Success Rate (OSR) and alignment inertia to measure when operator intervention...

### Can One Adapted Model Do It All? Fine-Tuning Strategy Selection for Customer Support LLMs
- **Authors**: Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN
- **arXiv**: [2609.27262](http://arxiv.org/abs/2609.27262v1)
- **Published**: 2026-09-23
- **Categories**: cs.CL

> Production customer-support systems often require LLMs to support multiple skills, such as intent classification, question answering, summarization, or tool-use decisions. A central deployment question is whether these skills should be handled by separate task-specialist models or by a single model ...

### Mammo-LIFE: Longitudinal Mammographic Imaging and Clinical Feature Enrichment for Post-Radiotherapy Outcome Prediction
- **Authors**: Farnoush Bayatmakou, Maryam Hosseini, Reza Taleei, Arash Mohammadi
- **arXiv**: [2609.26443](http://arxiv.org/abs/2609.26443v1)
- **Published**: 2026-09-22
- **Categories**: cs.CV, eess.IV

> Recent advances in Artificial Intelligence (AI)-powered Computer-Aided Diagnosis (CAD) systems have substantially improved breast cancer screening, diagnosis, and prognosis. Comparatively, postradiotherapy outcome prediction using paired longitudinal mammograms has received considerably less attenti...

### Combining Hierarchical Cognitive Process with Process Supervision for Interpretable Scene Safety Understanding
- **Authors**: Zhiyun Jiang, Hanyong Wang, Binbin Liang, Yu Xie, Zhengjie Wang, Menglong Yang, Wei Li
- **arXiv**: [2609.26399](http://arxiv.org/abs/2609.26399v1)
- **Published**: 2026-09-22
- **Categories**: cs.CL

> Scene safety understanding plays a life-or-death role in situational awareness in various critical domains. Traditional methods that rely on learning direct mappings between scenes and safety levels often lack interpretability, limiting their reliability in critical applications. An effective approa...

### LoRango: It Takes Two LoRAs to Unlock Hidden Behaviors in Diffusion Models
- **Authors**: Jin Wei, Rundong Li, Ruihao Yang, Yikai Wang, Xiaoyuan Duan, Jianxiong Wu, Yanbo Wang, Chang Xu, Lingyun Zhang, Zhuyang Yu, Ping Chen, Jun Dai, Xiaoyan Sun
- **arXiv**: [2609.25884](http://arxiv.org/abs/2609.25884v1)
- **Published**: 2026-09-22
- **Categories**: cs.CR, cs.CV

> Users commonly combine multiple Low-Rank Adaptation (LoRA) adapters to personalize images with different subjects, styles, and visual attributes. Yet inspecting adapters individually does not establish the safety of their composition. We identify and characterize a pair-conditioned attack in text-to...

### From Experts to Sub-experts: Fine-grained Parameter-Efficient Fine-Tuning for MoE LLMs
- **Authors**: Zhentao Tan, Chang Liu, Yao Liu, Yue Wu, Jieping Ye
- **arXiv**: [2609.25655](http://arxiv.org/abs/2609.25655v1)
- **Published**: 2026-09-22
- **Categories**: cs.LG, cs.AI

> As large language models (LLMs) scale rapidly, dense full-parameter adaptation becomes increasingly expensive, motivating sparse and modular architectures such as Mixture-of-Experts (MoE) models. This shift raises a key question for parameter-efficient fine-tuning (PEFT): at what granularity should ...

### Reasoning-Preserving Fine-Tuning of Post-RL LLMs with Null-Basis LoRA
- **Authors**: Wenzhi Fang, Nicholas Tzou, Lazar Valkov, Srinivas Chappidi
- **arXiv**: [2609.25618](http://arxiv.org/abs/2609.25618v1)
- **Published**: 2026-09-22
- **Categories**: cs.AI

> Reinforcement learning (RL)-based post-training has become an effective approach for eliciting reasoning capabilities in large language models (LLMs). However, adapting post-RL models to new knowledge domains or behaviors through subsequent supervised fine-tuning (SFT) can severely overwrite these c...

### ImIR: Image-Instruction Tuning for All-in-One Image Restoration
- **Authors**: Süleyman Aslan, Görkay Aydemir, Mısra Yavuz, Yunus Bilge Kurt, Nasrin Rahimi, Ahmet Rasim Emirdağı, Burak Can Biner, M. Akın Yılmaz
- **arXiv**: [2609.25267](http://arxiv.org/abs/2609.25267v1)
- **Published**: 2026-09-21
- **Categories**: cs.CV

> Degradations vary widely across images, so a practical restoration system has to handle many degradation types with one model. A recent and effective recipe adapts a large pretrained image-editing model to restoration using a small low-rank adapter with a text prompt. We replace that prompt with an ...

### LoRA-generating hypernetworks for efficient on-device LLM generative personalization
- **Authors**: Sean Augenstein, Li Ding, Jihwan Lee, Keith Rush, Andrey Zhmoginov
- **arXiv**: [2609.24979](http://arxiv.org/abs/2609.24979v1)
- **Published**: 2026-09-21
- **Categories**: cs.LG

> On-device large language models (`LLMs'), e.g. running on mobile phones, are ripe for improvement via personalization. The limited compute resources of mobile devices impose limits on model scale and thus model quality, making any realizable quality gains highly impactful. At the same time, their pe...

### Muon Can Outperform Dedicated Continual Learning Methods
- **Authors**: Sebastian George Sincari, Bogdan Alexandru Gheorghe, Antonio Barbalau
- **arXiv**: [2609.24678](http://arxiv.org/abs/2609.24678v1)
- **Published**: 2026-09-21
- **Categories**: cs.LG, cs.CL

> Continual learning with Low-Rank Adapters (LoRA) typically mitigates forgetting by penalizing the overlap between a new update and the accumulated past weights, which discourages certain update directions without controlling how an update distributes its energy over the ones that remain. We ask whet...

### Circuit Hypernetworks for Quantum-Augmented Diffusion Language Models
- **Authors**: Xiaoqiang Wang, Mengyang Xiong, Jun Dai, Bang Liu
- **arXiv**: [2609.24657](http://arxiv.org/abs/2609.24657v1)
- **Published**: 2026-09-21
- **Categories**: quant-ph, cs.CL

> Language models can be adapted by changing the computations applied to individual tokens. Quantum circuits offer one such approach, but evaluating wider circuits inside a large model can be computationally demanding. Here we introduce HyperQ, which adds token-conditioned quantum residual branches to...

### QLoRA Fine-Tuning of Ministral LLM for Sequence-to-Function Protein Annotation
- **Authors**: Demian Pavlyshenko, Bohdan Pavlyshenko
- **arXiv**: [2609.24538](http://arxiv.org/abs/2609.24538v1)
- **Published**: 2026-09-21
- **Categories**: cs.CL, cs.AI, cs.NE, q-bio.QM

> Functional annotation of newly sequenced proteins remains a bottleneck in molecular biology: the number of sequences in public repositories grows far faster than the capacity for manual curation. Most computational approaches consider annotation as multi-label classification over a fixed ontology, w...

### 0.5%>100%: Bidirectional Reciprocal Learning for Referring Image Segmentation
- **Authors**: Xiaoqiang Lu, Licheng Jiao, Lingling Li, Yuting Yang, Long Sun, Wenping Ma, Xu Liu, Fang Liu
- **arXiv**: [2609.24510](http://arxiv.org/abs/2609.24510v2)
- **Published**: 2026-09-21
- **Categories**: cs.CV

> Recent advances in vision foundation models (VFMs) have shown remarkable capabilities across diverse unimodal visual tasks. However, adapting VFMs to referring image segmentation (RIS) typically necessitates precise vision-language alignment via full fine-tuning, incurring substantial computational ...

### A Distributional Optimisation Perspective on Combining Models in Deep Learning
- **Authors**: Congye Wang, Yan Lin, Zheyang Shen, Matthew A. Fisher, Chris. J. Oates
- **arXiv**: [2609.24328](http://arxiv.org/abs/2609.24328v1)
- **Published**: 2026-09-21
- **Categories**: cs.LG, stat.ML

> Combining predictions from different models can improve performance at machine learning tasks, but the training of the individual models and the rule used to combine them are typically chosen separately, and by ad hoc means. Recent advances in distributional optimisation (i.e. where the optimisation...

### AnalogDepth: Multi-view Geometry from FPV drones under Analog Video Transmission
- **Authors**: André Amorim, Pedro F. Proença
- **arXiv**: [2609.24312](http://arxiv.org/abs/2609.24312v1)
- **Published**: 2026-09-21
- **Categories**: cs.CV, cs.RO

> Analog video transmission (VTX) remains widespread in FPV drones due to low latency, weight and low cost. However analog VTX suffers from complex spatially structured image degradation which differ fundamentally from digital image corruption (e.g. AWGN) used in standard training augmentation. This w...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "li-2026",
    "title": "New LoRA Skills Should Read but Never Write",
    "authors": [
      "Zeyan Li",
      "Panqi Yang",
      "Qirong Guo",
      "Shengda Zhuo",
      "SIyuan Qiu",
      "Hu Xu",
      "Chun Li",
      "Jianfeng Xu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.31600",
    "paper_url": "https://arxiv.org/abs/2609.31600",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "jingxin-2026",
    "title": "From Reward Signal to Visual Utility: A Controlled Audit of Medical VLM Post-Training",
    "authors": [
      "Wang Jingxin"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.31450",
    "paper_url": "https://arxiv.org/abs/2609.31450",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "gao-2026",
    "title": "ViSTA: A Simple Bridge Extends Visual Alignment to Clinical Time-Series Understanding in Multimodal LLMs",
    "authors": [
      "Junyi Gao",
      "Yu Shi",
      "Pingzhao Hu",
      "Ewen M Harrison"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.31448",
    "paper_url": "https://arxiv.org/abs/2609.31448",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "roussel-2026",
    "title": "Audio emotion recognition for atypical hearing",
    "authors": [
      "Ulysse Roussel"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.31168",
    "paper_url": "https://arxiv.org/abs/2609.31168",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "han-2026",
    "title": "FAVoR: Measuring and Mitigating Author-Style Homogenization in Federated Personalized Generation",
    "authors": [
      "Lu Han",
      "Jingyao Zhang",
      "Katy Ilonka Gero",
      "Nguyen H. Tran"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.30968",
    "paper_url": "https://arxiv.org/abs/2609.30968",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "wang-2026",
    "title": "JevSoup: System-One Routing for Training-Free LoRA Composition",
    "authors": [
      "Xiuying Wang",
      "Jiahua Cheng",
      "Shuotian Li",
      "Yufan Cheng",
      "Bowen Deng",
      "Zhexuan Bai",
      "Yichen Li"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.30922",
    "paper_url": "https://arxiv.org/abs/2609.30922",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "mishra-2026",
    "title": "Adaptive Fisher-Whitened Cross-Covariance for Low-Resource Speech Recognition",
    "authors": [
      "Asmee Mishra",
      "Mengjie Qian",
      "Brechtje Post",
      "Kate Knill"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.29800",
    "paper_url": "https://arxiv.org/abs/2609.29800",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "hartl-2026",
    "title": "On Growth and Form, and Function: Reusable Regulatory Handles Control Phenotypic Variation",
    "authors": [
      "Benedikt Hartl",
      "Milton L. Montero",
      "Marcello Barylli",
      "Sebastian Risi",
      "Michael Levin"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.29755",
    "paper_url": "https://arxiv.org/abs/2609.29755",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "habibullah-2026",
    "title": "Where LLM Graders Succeed and Break: Evidence from Two Computer-Science Exams",
    "authors": [
      "Ali Habibullah",
      "Yazan Alshoibi",
      "Mohammad Alshiekh",
      "Salman Khan",
      "Naeemullah Khan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.29333",
    "paper_url": "https://arxiv.org/abs/2609.29333",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "xie-2026",
    "title": "Automatic Rank Allocation for Low-Rank Adaptation in Large Language Models via lp Regularization",
    "authors": [
      "Zebang Xie",
      "Chuanyang Zheng",
      "Yik-Chung Wu",
      "Yihang Gao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.28998",
    "paper_url": "https://arxiv.org/abs/2609.28998",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "park-2026",
    "title": "Personalized Korean Lipreading as Visual Speech Recognition: Transfer, Census and Adaptation on OLKAVS",
    "authors": [
      "Se Un Park",
      "Hakjun Kim",
      "Taehoon Roh",
      "Junyoung Park"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.28988",
    "paper_url": "https://arxiv.org/abs/2609.28988",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "rahman-2026",
    "title": "Multimodal Routing and Region Refinement for Language-Guided Medical Image Segmentation",
    "authors": [
      "Md Maklachur Rahman",
      "Md Hasan Al Banna",
      "Saraf Anjum",
      "Assame Arnob",
      "Tracy Hammond"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.28860",
    "paper_url": "https://arxiv.org/abs/2609.28860",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "anand-2026",
    "title": "MEVL-STP: Multi-Encoder and Vision Language Model for Arbitrarily Shaped Scene Text Spotting",
    "authors": [
      "Aman Anand",
      "Partha Pratim Roy",
      "Shivakumara Palaiahnakote"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.28857",
    "paper_url": "https://arxiv.org/abs/2609.28857",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "weizman-2026",
    "title": "Spooftral: Can Voxtral Audio-Language Model Detect Speech Spoofing?",
    "authors": [
      "Avishai Weizman",
      "Yehuda Ben-Shimol",
      "Itshak Lapidot"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.28713",
    "paper_url": "https://arxiv.org/abs/2609.28713",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "feng-2026",
    "title": "Cross-Scale Transfer Learning for Depression Severity Prediction: From PHQ-8 to HAMD-17 Across Languages and Clinical Paradigms",
    "authors": [
      "Wenjie Feng",
      "Sahba Zojaji",
      "Satoshi Nakamura"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.28430",
    "paper_url": "https://arxiv.org/abs/2609.28430",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "aliev-2026",
    "title": "Riemannian Structure and Optimization for a Class of Low-Parametric Orthogonal Matrices",
    "authors": [
      "Ali Aliev",
      "Maxim Rakhuba"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.27982",
    "paper_url": "https://arxiv.org/abs/2609.27982",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "barreto-2026",
    "title": "Alignment Inertia: Auditing the Durability of Training Data Influence Through Policy Override Resistance",
    "authors": [
      "Renata Barreto",
      "Markelle Roesti",
      "Mohammad Tahaei"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.27333",
    "paper_url": "https://arxiv.org/abs/2609.27333",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "laskar-2026",
    "title": "Can One Adapted Model Do It All? Fine-Tuning Strategy Selection for Customer Support LLMs",
    "authors": [
      "Md Tahmid Rahman Laskar",
      "Xue-Yong Fu",
      "Shashi Bhushan TN"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.27262",
    "paper_url": "https://arxiv.org/abs/2609.27262",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "bayatmakou-2026",
    "title": "Mammo-LIFE: Longitudinal Mammographic Imaging and Clinical Feature Enrichment for Post-Radiotherapy Outcome Prediction",
    "authors": [
      "Farnoush Bayatmakou",
      "Maryam Hosseini",
      "Reza Taleei",
      "Arash Mohammadi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.26443",
    "paper_url": "https://arxiv.org/abs/2609.26443",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "jiang-2026",
    "title": "Combining Hierarchical Cognitive Process with Process Supervision for Interpretable Scene Safety Understanding",
    "authors": [
      "Zhiyun Jiang",
      "Hanyong Wang",
      "Binbin Liang",
      "Yu Xie",
      "Zhengjie Wang",
      "Menglong Yang",
      "Wei Li"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.26399",
    "paper_url": "https://arxiv.org/abs/2609.26399",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "wei-2026",
    "title": "LoRango: It Takes Two LoRAs to Unlock Hidden Behaviors in Diffusion Models",
    "authors": [
      "Jin Wei",
      "Rundong Li",
      "Ruihao Yang",
      "Yikai Wang",
      "Xiaoyuan Duan",
      "Jianxiong Wu",
      "Yanbo Wang",
      "Chang Xu",
      "Lingyun Zhang",
      "Zhuyang Yu",
      "Ping Chen",
      "Jun Dai",
      "Xiaoyan Sun"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.25884",
    "paper_url": "https://arxiv.org/abs/2609.25884",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "tan-2026",
    "title": "From Experts to Sub-experts: Fine-grained Parameter-Efficient Fine-Tuning for MoE LLMs",
    "authors": [
      "Zhentao Tan",
      "Chang Liu",
      "Yao Liu",
      "Yue Wu",
      "Jieping Ye"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.25655",
    "paper_url": "https://arxiv.org/abs/2609.25655",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "fang-2026",
    "title": "Reasoning-Preserving Fine-Tuning of Post-RL LLMs with Null-Basis LoRA",
    "authors": [
      "Wenzhi Fang",
      "Nicholas Tzou",
      "Lazar Valkov",
      "Srinivas Chappidi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.25618",
    "paper_url": "https://arxiv.org/abs/2609.25618",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "aslan-2026",
    "title": "ImIR: Image-Instruction Tuning for All-in-One Image Restoration",
    "authors": [
      "Süleyman Aslan",
      "Görkay Aydemir",
      "Mısra Yavuz",
      "Yunus Bilge Kurt",
      "Nasrin Rahimi",
      "Ahmet Rasim Emirdağı",
      "Burak Can Biner",
      "M. Akın Yılmaz"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.25267",
    "paper_url": "https://arxiv.org/abs/2609.25267",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "augenstein-2026",
    "title": "LoRA-generating hypernetworks for efficient on-device LLM generative personalization",
    "authors": [
      "Sean Augenstein",
      "Li Ding",
      "Jihwan Lee",
      "Keith Rush",
      "Andrey Zhmoginov"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.24979",
    "paper_url": "https://arxiv.org/abs/2609.24979",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "sincari-2026",
    "title": "Muon Can Outperform Dedicated Continual Learning Methods",
    "authors": [
      "Sebastian George Sincari",
      "Bogdan Alexandru Gheorghe",
      "Antonio Barbalau"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.24678",
    "paper_url": "https://arxiv.org/abs/2609.24678",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "wang-2026",
    "title": "Circuit Hypernetworks for Quantum-Augmented Diffusion Language Models",
    "authors": [
      "Xiaoqiang Wang",
      "Mengyang Xiong",
      "Jun Dai",
      "Bang Liu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.24657",
    "paper_url": "https://arxiv.org/abs/2609.24657",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "pavlyshenko-2026",
    "title": "QLoRA Fine-Tuning of Ministral LLM for Sequence-to-Function Protein Annotation",
    "authors": [
      "Demian Pavlyshenko",
      "Bohdan Pavlyshenko"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.24538",
    "paper_url": "https://arxiv.org/abs/2609.24538",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "lu-2026",
    "title": "0.5%>100%: Bidirectional Reciprocal Learning for Referring Image Segmentation",
    "authors": [
      "Xiaoqiang Lu",
      "Licheng Jiao",
      "Lingling Li",
      "Yuting Yang",
      "Long Sun",
      "Wenping Ma",
      "Xu Liu",
      "Fang Liu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.24510",
    "paper_url": "https://arxiv.org/abs/2609.24510",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "wang-2026",
    "title": "A Distributional Optimisation Perspective on Combining Models in Deep Learning",
    "authors": [
      "Congye Wang",
      "Yan Lin",
      "Zheyang Shen",
      "Matthew A. Fisher",
      "Chris. J. Oates"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.24328",
    "paper_url": "https://arxiv.org/abs/2609.24328",
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
    "added_date": "2026-09-28"
  },
  {
    "id": "amorim-2026",
    "title": "AnalogDepth: Multi-view Geometry from FPV drones under Analog Video Transmission",
    "authors": [
      "André Amorim",
      "Pedro F. Proença"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.24312",
    "paper_url": "https://arxiv.org/abs/2609.24312",
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
    "added_date": "2026-09-28"
  }
]
```
