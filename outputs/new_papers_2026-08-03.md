# New arXiv PEFT papers — 2026-08-03

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **24**.

## Candidates

### The Parts Are Greater Than the Sum: Automated Task Sequencing for Efficient Training of Multi-Policy LLMs
- **Authors**: Jiajia Tang, Sizhe Yuen, Francisco Gomez Medina, Yali Du, Adam Sobey
- **arXiv**: [2607.29601](http://arxiv.org/abs/2607.29601v1)
- **Published**: 2026-07-31
- **Categories**: cs.LG

> Parameter-Efficient Fine-Tuning (PEFT) commonly adapts large language models using a single shared Low-Rank Adapter (LoRA). This shared optimization space often suffers from interference when adapting heterogeneous task sequences, leading to poor transfer and catastrophic forgetting. Existing approa...

### MoPET: Parameter-Efficient Mixture-of-Experts for Unified Medical Image Classification
- **Authors**: Sebastian Doerrich, Daniel Würtinger, Francesco Di Salvo, Shyam Nandan Rai, Christian Ledig
- **arXiv**: [2607.29462](http://arxiv.org/abs/2607.29462v1)
- **Published**: 2026-07-31
- **Categories**: eess.IV, cs.CV, cs.LG

> Adapting deep learning models to profound clinical heterogeneity typically relies on parameter-efficient fine-tuning (PEFT) to avoid the severe overfitting associated with full end-to-end network updates. Although PEFT successfully navigates limited data scenarios, it inherently forces the training ...

### Parameter-Efficient Fine-Tuning for Spiking Point Cloud Models
- **Authors**: Zihao Guo, Jihua Zhu, Yiding Sun, Lin Chen, Danwei Wang
- **arXiv**: [2607.29048](http://arxiv.org/abs/2607.29048v1)
- **Published**: 2026-07-31
- **Categories**: cs.CV

> Spiking Neural Networks (SNNs) offer energy-efficient solutions for point cloud analysis on resource-constrained devices through event-driven computation. However, existing pre-trained spiking point cloud models rely on full fine-tuning for downstream task adaptation, incurring substantial parameter...

### SAM+D: Parameter-Efficient Dimensional Lifting of SAM-Family Models via Depth-Routed LoRA and Depth Shifting
- **Authors**: Yu Song, Hao Sun, Shiyu Teng, Ikuko Nishikawa, Yen-wei Chen
- **arXiv**: [2607.29033](http://arxiv.org/abs/2607.29033v1)
- **Published**: 2026-07-31
- **Categories**: cs.CV

> Existing methods for adapting 2D foundation models such as SAM to 3D volumes either process slices independently---ignoring inter-slice context---or require substantial architectural changes and retraining. In this paper, we present \textbf{SAM+D}, a parameter-efficient framework that lifts SAM-fami...

### DeltaServe: Host-Agnostic Co-Serving of Inference and Fine-Tuning for LLMs
- **Authors**: Jiaxuan Chen, Jianshu She, Ye Yuan, Rajat Ghosh, Karan Gupta, Qirong Ho, Xue Liu, Oana Balmau
- **arXiv**: [2607.28848](http://arxiv.org/abs/2607.28848v1)
- **Published**: 2026-07-30
- **Categories**: cs.DC, cs.LG

> LLM serving systems are provisioned for peak load to meet strict latency targets, leaving substantial GPU compute idle whenever traffic falls below peak. We present DeltaServe, a host-agnostic co-serving design that converts this idle inference capacity into LoRA fine-tuning throughput while preserv...

### Towards Autonomous Aircraft Surveillance from Nanosatellites through On-Board Inference and Generative Data Augmentation
- **Authors**: Antonio Delgado-Rosa, David Muñoz-Valero, Enrique Adrian Villarrubia-Martin, Juan Moreno-Garcia
- **arXiv**: [2607.28470](http://arxiv.org/abs/2607.28470v1)
- **Published**: 2026-07-30
- **Categories**: cs.AI, cs.CV

> Airborne surveillance from low Earth orbit is hindered by two interconnected bottlenecks: nanosatellites have a limited downlink budget, yet the conventional approach still transmits terabytes of raw imagery to the ground for processing, and open satellite datasets for aircraft are scarce and severe...

### CACHE-UK: A Stability-Aware Memory Editor for Sequentially Updated Quantized LLMs in Finance
- **Authors**: Anubhav Lakra, Yue Feng
- **arXiv**: [2607.28292](http://arxiv.org/abs/2607.28292v1)
- **Published**: 2026-07-30
- **Categories**: cs.CL, cs.AI, cs.CE, cs.LG

> Large Language Models (LLMs) deployed in dynamic financial environments face a critical challenge: maintaining factual accuracy as market conditions, regulations, and corporate facts change continuously. While 4-bit quantization enables efficient deployment, it severely limits the viability of seque...

### Tight Sample Complexity for Low-Rank Adaptation: Matching Bounds and Rank Selection
- **Authors**: Arunan J
- **arXiv**: [2607.27680](http://arxiv.org/abs/2607.27680v1)
- **Published**: 2026-07-30
- **Categories**: cs.LG, cs.CL

> Low-Rank Adaptation (LoRA) has become the standard mechanism for fine-tuning large pretrained models, yet its statistical properties remain only partially understood. Existing generalization results provide upper bounds of the form O~(sqrt(rd/n)) or O~(rd/n), but a matching lower bound is missing, a...

### Arm2Air: Cross-Embodiment Skeleton Transfer for 3D Relay Formation
- **Authors**: Dohun Lee, Kyeonghyun Yoo, Seokmin Kim, Byongho Lee, Seungjoo Oh, Hwangnam Kim
- **arXiv**: [2607.27627](http://arxiv.org/abs/2607.27627v1)
- **Published**: 2026-07-30
- **Categories**: cs.RO, cs.AI

> Unmanned aerial vehicle (UAV) relay networks can restore connectivity after communication infrastructure is damaged. Urban relay placement is difficult because line-of-sight blockage, communication range, altitude, and three-dimensional obstacles must be considered jointly. Arm2Air transfers obstacl...

### Towards Grounded GI Endoscopy VQA via Multi-Task Learning on Small VLMs
- **Authors**: Itbaan Safwan, Ramail Khan, Muhammad Annas Shaikh, Muhammad Atif Tahir
- **arXiv**: [2607.27122](http://arxiv.org/abs/2607.27122v1)
- **Published**: 2026-07-29
- **Categories**: cs.CV

> Gastrointestinal (GI) endoscopic image analysis has shifted from single-label classification toward visual question answering (VQA), where a model must answer free-form clinical questions about an image. While recent vision-language models (VLMs) achieve promising answer accuracy on this task, clini...

### Language Models are not Equally Robust to Non-Canonical Tokenization across Languages
- **Authors**: Poulami Ghosh, Preethi Jyothi
- **arXiv**: [2607.26831](http://arxiv.org/abs/2607.26831v1)
- **Published**: 2026-07-29
- **Categories**: cs.CL

> Despite the existence of exponentially many valid tokenizations for a given string, language models operate on a single canonical sequence deterministically produced by the tokenizer, leaving the broader tokenization space largely uncharacterized. In this paper, we investigate this overlooked space ...

### FARI: Robust One-Step Inversion for Watermarking in Diffusion Models
- **Authors**: Jindong Yang, Han Fang, Weiming Zhang, Nenghai Yu, Kejiang Chen
- **arXiv**: [2607.26723](http://arxiv.org/abs/2607.26723v1)
- **Published**: 2026-07-29
- **Categories**: cs.CR, cs.AI

> Inversion-based watermarking is a promising approach to authenticate diffusion-generated images, yet practical use is bottlenecked by inversion that is both slow and error-prone. While the primary challenge in the watermarking setting is robustness against external distortions, existing approaches o...

### Between Gradient and Natural Gradient: A Continuum of LoRA Initializations
- **Authors**: Dianze Liu, Farshid Ghezelbash
- **arXiv**: [2607.26247](http://arxiv.org/abs/2607.26247v1)
- **Published**: 2026-07-28
- **Categories**: cs.LG

> Low-rank adaptation (LoRA) fine-tunes large pretrained models at a fraction of the cost of full fine-tuning, but its performance depends strongly on how the adapters are initialized. Recent schemes initialize the adapters from the downstream loss gradient: some project the raw gradient onto its top ...

### WildShadowRemover: In-the-Wild Video Shadow Removal via Detail-Preserving Video Diffusion Models
- **Authors**: Jiamin Xu, Cong Wang, Zheng Dong, Chi Wang, Renshu Gu, Weiwei Xu, Gang Xu
- **arXiv**: [2607.26203](http://arxiv.org/abs/2607.26203v1)
- **Published**: 2026-07-28
- **Categories**: cs.CV

> Video shadow removal in the wild remains challenging due to complex illumination, diverse shadow appearances, and limited training data. Despite its importance to numerous vision and graphics applications, it remains largely unexplored in unconstrained real-world scenarios. To address this gap, we p...

### Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA
- **Authors**: Tom Saliencro, Rohan Desai, Priya Nair, Maya Lindqvist, Daniel Whitmore
- **arXiv**: [2607.26052](http://arxiv.org/abs/2607.26052v1)
- **Published**: 2026-07-28
- **Categories**: cs.LG

> Mixture-of-Experts (MoE) variants of Low-Rank Adaptation (LoRA) route every token to a fixed number of experts $k$. Tokens differ in how uncertain the model is about them, so a single k over-spends on easy tokens and under-serves hard ones. We observe that the router's output distribution is already...

### WALoMA: A Multitask Wireless Foundation Model via Adaptive Low-Rank Masked Autoencoders
- **Authors**: Madi Makin, Asmaa Abdallah, Abdulkadir Celik, Ahmed M. Eltawil
- **arXiv**: [2607.25763](http://arxiv.org/abs/2607.25763v1)
- **Published**: 2026-07-28
- **Categories**: cs.NI, cs.LG

> This paper proposes a multitask wireless foundation model via adaptive low-rank masked autoencoders (WALoMA), a unified multi-task foundation model for sixth-generation (6G) wireless physical layer architectures, to address the limitations of specialized, task-specific deep learning models and the p...

### Detecting CSAM Text-to-Image LoRAs From Weights
- **Authors**: David Demitri Africa, Cate Heine, Nadine Staes-Polet, Kimberly Mai
- **arXiv**: [2607.25750](http://arxiv.org/abs/2607.25750v1)
- **Published**: 2026-07-28
- **Categories**: cs.LG, cs.CY

> Low-rank adaptation (LoRA) fine-tuning has made it cheap and easy to customize open-weight image generation models for specific tasks, including the production of child sexual abuse material (CSAM). Existing moderation relies on metadata or generated outputs, but metadata can be deceptive and genera...

### How Small Can You Go? A Controlled Study of LoRA Rank, Target Modules, and Quantization Trade-offs for Text-to-SQL on a 60M-Parameter Model
- **Authors**: Mahendra Singh Rathor, Anagheem Azzam
- **arXiv**: [2607.25583](http://arxiv.org/abs/2607.25583v1)
- **Published**: 2026-07-28
- **Categories**: cs.AI

> Parameter-efficient fine-tuning (PEFT) and low-bit quantization are now standard tools for adapting language models under tight compute budgets, yet their interaction is most often studied on billion-parameter models where the design space is expensive to explore. We ask a complementary question: on...

### RDVSv2: A Large-scale Benchmark for RGB-D Video Salient Object Detection
- **Authors**: Tianyu Li, Jiahao He, Keren Fu, Qijun Zhao
- **arXiv**: [2607.25392](http://arxiv.org/abs/2607.25392v1)
- **Published**: 2026-07-28
- **Categories**: cs.CV

> We introduce RDVSv2, a large-scale benchmark for RGB-D video salient object detection (RGB-D VSOD) with dense frame-level annotations. Existing datasets in this emerging field are often limited in scale and annotation quality, while also relying on less geometry-consistent depth cues. To address the...

### Retraction-Free Optimization over the Stiefel Manifold for the LoRA Fine-Tuning
- **Authors**: Yuan Zhang, Jiang Hu, Zhijian Lai, Lin Lin, Zaiwen Wen
- **arXiv**: [2607.25299](http://arxiv.org/abs/2607.25299v1)
- **Published**: 2026-07-28
- **Categories**: cs.LG, cs.AI

> Optimization over the Stiefel manifold plays a significant role in various machine learning tasks. Existing methods either use the retraction operators, requiring costly orthonormalization for large-scale matrices, or employ landing methods that rely on careful step size selection and penalty parame...

### ScaleResfusion: Residual Rectified Flow based on Residual Vector Field
- **Authors**: Zhenning Shi, Chen Xu, Junhao Zhang, Kefei Zhang, Linjie Liu, Zhedong Zheng, Tao Li
- **arXiv**: [2607.25275](http://arxiv.org/abs/2607.25275v1)
- **Published**: 2026-07-28
- **Categories**: cs.CV, cs.AI

> Real-world Image Restoration (Real-IR) aims to recover high-quality (HQ) images from complex and unknown degradations. Although recent diffusion-based methods have substantially improved perceptual quality, their current designs leave two key challenges unresolved. Methods that start from Gaussian n...

### Enhancing Law-Enforcement Audio Transcription: A LoRA-Based Adaptation of Whisper for BWC Footage
- **Authors**: Vivek Senthil, Zhiqiang Tao, Ernest Fokoué
- **arXiv**: [2607.27245](http://arxiv.org/abs/2607.27245v1)
- **Published**: 2026-07-27
- **Categories**: cs.SD, cs.AI

> Modern policing faces a "visibility paradox" where law enforcement agencies possess petabytes of Body-Worn Camera (BWC) footage that remains largely unutilized for accountability or systemic review due to the prohibitive labor costs of manual transcription. This research presents a framework for ada...

### Harm is not Universal: Community-Specific Toxicity Detection is Urgently Needed
- **Authors**: Xinnuo Xu, Anja Thieme, Daniela Massiceti, Ioana Tanase, Rita Marques, Melanie Fernandez Pradier, Martin Grayson, Camilla Longden, Cecily Morrison
- **arXiv**: [2607.24898](http://arxiv.org/abs/2607.24898v1)
- **Published**: 2026-07-27
- **Categories**: cs.CV, cs.AI

> State-of-the-art toxicity detectors for text-to-image generation adopt a one-size-fits-all approach: a single universal model applying fixed safety guidelines to all users. Our empirical evidence shows that these detectors fail to shield marginalized communities: approximately 35% of generated image...

### MoLGE: Mixture of Language Group Experts for Efficient Scaling of Massively Multilingual Speech Recognition
- **Authors**: Sangmin Lee, Woojin Chung, Woongjib Choi, Hong-Goo Kang
- **arXiv**: [2607.24030](http://arxiv.org/abs/2607.24030v1)
- **Published**: 2026-07-27
- **Categories**: cs.CL, cs.SD

> Massively multilingual automatic speech recognition (ASR) models covering hundreds of languages must maintain robust performance across diverse linguistic and acoustic conditions. However, these models often encounter the curse of multilinguality, where model capacity is diluted across languages. To...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "tang-2026",
    "title": "The Parts Are Greater Than the Sum: Automated Task Sequencing for Efficient Training of Multi-Policy LLMs",
    "authors": [
      "Jiajia Tang",
      "Sizhe Yuen",
      "Francisco Gomez Medina",
      "Yali Du",
      "Adam Sobey"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.29601",
    "paper_url": "https://arxiv.org/abs/2607.29601",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "doerrich-2026",
    "title": "MoPET: Parameter-Efficient Mixture-of-Experts for Unified Medical Image Classification",
    "authors": [
      "Sebastian Doerrich",
      "Daniel Würtinger",
      "Francesco Di Salvo",
      "Shyam Nandan Rai",
      "Christian Ledig"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.29462",
    "paper_url": "https://arxiv.org/abs/2607.29462",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "guo-2026",
    "title": "Parameter-Efficient Fine-Tuning for Spiking Point Cloud Models",
    "authors": [
      "Zihao Guo",
      "Jihua Zhu",
      "Yiding Sun",
      "Lin Chen",
      "Danwei Wang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.29048",
    "paper_url": "https://arxiv.org/abs/2607.29048",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "song-2026",
    "title": "SAM+D: Parameter-Efficient Dimensional Lifting of SAM-Family Models via Depth-Routed LoRA and Depth Shifting",
    "authors": [
      "Yu Song",
      "Hao Sun",
      "Shiyu Teng",
      "Ikuko Nishikawa",
      "Yen-wei Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.29033",
    "paper_url": "https://arxiv.org/abs/2607.29033",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "chen-2026",
    "title": "DeltaServe: Host-Agnostic Co-Serving of Inference and Fine-Tuning for LLMs",
    "authors": [
      "Jiaxuan Chen",
      "Jianshu She",
      "Ye Yuan",
      "Rajat Ghosh",
      "Karan Gupta",
      "Qirong Ho",
      "Xue Liu",
      "Oana Balmau"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.28848",
    "paper_url": "https://arxiv.org/abs/2607.28848",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "delgado-rosa-2026",
    "title": "Towards Autonomous Aircraft Surveillance from Nanosatellites through On-Board Inference and Generative Data Augmentation",
    "authors": [
      "Antonio Delgado-Rosa",
      "David Muñoz-Valero",
      "Enrique Adrian Villarrubia-Martin",
      "Juan Moreno-Garcia"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.28470",
    "paper_url": "https://arxiv.org/abs/2607.28470",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "lakra-2026",
    "title": "CACHE-UK: A Stability-Aware Memory Editor for Sequentially Updated Quantized LLMs in Finance",
    "authors": [
      "Anubhav Lakra",
      "Yue Feng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.28292",
    "paper_url": "https://arxiv.org/abs/2607.28292",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "j-2026",
    "title": "Tight Sample Complexity for Low-Rank Adaptation: Matching Bounds and Rank Selection",
    "authors": [
      "Arunan J"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.27680",
    "paper_url": "https://arxiv.org/abs/2607.27680",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "lee-2026",
    "title": "Arm2Air: Cross-Embodiment Skeleton Transfer for 3D Relay Formation",
    "authors": [
      "Dohun Lee",
      "Kyeonghyun Yoo",
      "Seokmin Kim",
      "Byongho Lee",
      "Seungjoo Oh",
      "Hwangnam Kim"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.27627",
    "paper_url": "https://arxiv.org/abs/2607.27627",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "safwan-2026",
    "title": "Towards Grounded GI Endoscopy VQA via Multi-Task Learning on Small VLMs",
    "authors": [
      "Itbaan Safwan",
      "Ramail Khan",
      "Muhammad Annas Shaikh",
      "Muhammad Atif Tahir"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.27122",
    "paper_url": "https://arxiv.org/abs/2607.27122",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "ghosh-2026",
    "title": "Language Models are not Equally Robust to Non-Canonical Tokenization across Languages",
    "authors": [
      "Poulami Ghosh",
      "Preethi Jyothi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.26831",
    "paper_url": "https://arxiv.org/abs/2607.26831",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "yang-2026",
    "title": "FARI: Robust One-Step Inversion for Watermarking in Diffusion Models",
    "authors": [
      "Jindong Yang",
      "Han Fang",
      "Weiming Zhang",
      "Nenghai Yu",
      "Kejiang Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.26723",
    "paper_url": "https://arxiv.org/abs/2607.26723",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "liu-2026",
    "title": "Between Gradient and Natural Gradient: A Continuum of LoRA Initializations",
    "authors": [
      "Dianze Liu",
      "Farshid Ghezelbash"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.26247",
    "paper_url": "https://arxiv.org/abs/2607.26247",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "xu-2026",
    "title": "WildShadowRemover: In-the-Wild Video Shadow Removal via Detail-Preserving Video Diffusion Models",
    "authors": [
      "Jiamin Xu",
      "Cong Wang",
      "Zheng Dong",
      "Chi Wang",
      "Renshu Gu",
      "Weiwei Xu",
      "Gang Xu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.26203",
    "paper_url": "https://arxiv.org/abs/2607.26203",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "saliencro-2026",
    "title": "Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA",
    "authors": [
      "Tom Saliencro",
      "Rohan Desai",
      "Priya Nair",
      "Maya Lindqvist",
      "Daniel Whitmore"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.26052",
    "paper_url": "https://arxiv.org/abs/2607.26052",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "makin-2026",
    "title": "WALoMA: A Multitask Wireless Foundation Model via Adaptive Low-Rank Masked Autoencoders",
    "authors": [
      "Madi Makin",
      "Asmaa Abdallah",
      "Abdulkadir Celik",
      "Ahmed M. Eltawil"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.25763",
    "paper_url": "https://arxiv.org/abs/2607.25763",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "africa-2026",
    "title": "Detecting CSAM Text-to-Image LoRAs From Weights",
    "authors": [
      "David Demitri Africa",
      "Cate Heine",
      "Nadine Staes-Polet",
      "Kimberly Mai"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.25750",
    "paper_url": "https://arxiv.org/abs/2607.25750",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "rathor-2026",
    "title": "How Small Can You Go? A Controlled Study of LoRA Rank, Target Modules, and Quantization Trade-offs for Text-to-SQL on a 60M-Parameter Model",
    "authors": [
      "Mahendra Singh Rathor",
      "Anagheem Azzam"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.25583",
    "paper_url": "https://arxiv.org/abs/2607.25583",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "li-2026",
    "title": "RDVSv2: A Large-scale Benchmark for RGB-D Video Salient Object Detection",
    "authors": [
      "Tianyu Li",
      "Jiahao He",
      "Keren Fu",
      "Qijun Zhao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.25392",
    "paper_url": "https://arxiv.org/abs/2607.25392",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "zhang-2026",
    "title": "Retraction-Free Optimization over the Stiefel Manifold for the LoRA Fine-Tuning",
    "authors": [
      "Yuan Zhang",
      "Jiang Hu",
      "Zhijian Lai",
      "Lin Lin",
      "Zaiwen Wen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.25299",
    "paper_url": "https://arxiv.org/abs/2607.25299",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "shi-2026",
    "title": "ScaleResfusion: Residual Rectified Flow based on Residual Vector Field",
    "authors": [
      "Zhenning Shi",
      "Chen Xu",
      "Junhao Zhang",
      "Kefei Zhang",
      "Linjie Liu",
      "Zhedong Zheng",
      "Tao Li"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.25275",
    "paper_url": "https://arxiv.org/abs/2607.25275",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "senthil-2026",
    "title": "Enhancing Law-Enforcement Audio Transcription: A LoRA-Based Adaptation of Whisper for BWC Footage",
    "authors": [
      "Vivek Senthil",
      "Zhiqiang Tao",
      "Ernest Fokoué"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.27245",
    "paper_url": "https://arxiv.org/abs/2607.27245",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "xu-2026",
    "title": "Harm is not Universal: Community-Specific Toxicity Detection is Urgently Needed",
    "authors": [
      "Xinnuo Xu",
      "Anja Thieme",
      "Daniela Massiceti",
      "Ioana Tanase",
      "Rita Marques",
      "Melanie Fernandez Pradier",
      "Martin Grayson",
      "Camilla Longden",
      "Cecily Morrison"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.24898",
    "paper_url": "https://arxiv.org/abs/2607.24898",
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
    "added_date": "2026-08-03"
  },
  {
    "id": "lee-2026",
    "title": "MoLGE: Mixture of Language Group Experts for Efficient Scaling of Massively Multilingual Speech Recognition",
    "authors": [
      "Sangmin Lee",
      "Woojin Chung",
      "Woongjib Choi",
      "Hong-Goo Kang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2607.24030",
    "paper_url": "https://arxiv.org/abs/2607.24030",
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
    "added_date": "2026-08-03"
  }
]
```
