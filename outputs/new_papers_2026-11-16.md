# New arXiv PEFT papers — 2026-11-16

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **31**.

## Candidates

### Structural Self-Teaching for Compositional Generation in Unified Multimodal Models
- **Authors**: Jaeyoo Park, Bohyung Han
- **arXiv**: [2611.18261](http://arxiv.org/abs/2611.18261v1)
- **Published**: 2026-11-13
- **Categories**: cs.CV

> We propose Structural Self-Teaching (SST), a novel framework that enhances compositional image generation in diffusion-based unified multimodal models (UMMs) by leveraging their internal understanding path as a source of structural supervision. The generation path of UMMs often struggles with dense ...

### NER-D: A cross-domain benchmark for German NER
- **Authors**: Marc Brinner, Philipp Cimiano, Karolina Hanna Czok, Regina Stodden, Viju Sudhi, Sina Zarrieß
- **arXiv**: [2611.18257](http://arxiv.org/abs/2611.18257v1)
- **Published**: 2026-11-13
- **Categories**: cs.CL

> We present NER-D, a cross-domain benchmark for German NER comprising 13 datasets spanning 9 domains, including General/Politics, Wikipedia, Legal, Medical, Historical, Financial, Agriculture and Archaeology. We examine the performance of both proprietary LLMs and state-of-the-art small open-source m...

### InfiHall-Bench: A Benchmark for Hallucination Evaluation in Autoregressive Text-to-Image Generation
- **Authors**: Yuxia Qiao, Xinhao Zhong, Junhao Li, Yi Sun, Jiaxin Hong, Shuoyang Sun, Bin Chen
- **arXiv**: [2611.18053](http://arxiv.org/abs/2611.18053v1)
- **Published**: 2026-11-13
- **Categories**: cs.CV

> Hallucination benchmarks for text-to-image generation are predominantly designed around diffusion models, limiting their diagnostic value for visual autoregressive (VAR) models and the development of mitigation methods. We identify two limitations in existing prompt construction paradigms: many prom...

### Direction or Magnitude? Learning Scalars over Task-Calibrated Directions
- **Authors**: Ziqing Wen, Xiaohui Song, Jiahuan Wang, Ping Luo, Junlin Zeng, Dongsheng Li, Kele Xu, Tao Sun
- **arXiv**: [2611.17784](http://arxiv.org/abs/2611.17784v1)
- **Published**: 2026-11-13
- **Categories**: cs.LG

> Parameter-efficient fine-tuning (PEFT) aims to preserve adaptation quality while reducing training costs. We propose SCALAR, which achieves performance comparable to LoRA with substantially fewer trainable parameters, lower peak training memory, and higher throughput. SCALAR constructs a fixed input...

### Maximizing Capacity Utilization of LoRA Adapters for Mitigating the Learning-Forgetting Trade-off
- **Authors**: Tomohiro Sawada, Kartik Goyal
- **arXiv**: [2611.17191](http://arxiv.org/abs/2611.17191v1)
- **Published**: 2026-11-12
- **Categories**: cs.LG, cs.CL

> Low-Rank Adaptation (LoRA) often underperforms full fine-tuning, especially in heterogeneous and continual-learning settings in which substantial forgetting occurs. In general, it suffers from an undesirable learning-forgetting trade-off across diverse fine-tuning settings. We identify a potential c...

### Parameter-Efficient Conciseness Adaptation: Differentiable Length Control for Concise Clinical Reasoning in Smaller Language Models
- **Authors**: Tanzeel Abbas, Ahmad Kamran Malik, Nafees Qamar, Sana Liaqat
- **arXiv**: [2611.17128](http://arxiv.org/abs/2611.17128v1)
- **Published**: 2026-11-12
- **Categories**: cs.CL, cs.AI

> Smaller language models (SLMs) make it feasible to deploy clinical natural language processing where large proprietary models are too costly, and parameter-efficient fine-tuning allows them to be specialised on commodity hardware. One obstacle persists after training: on medical tasks these models a...

### Predicting Ethanol Drinking Status from Nonhuman Primate Liver Histology: A Proof of Concept for Parameter-efficient Fine-tuning in Few-Shot Vision-Language Modeling
- **Authors**: Amirmohammad Mohammadi, Rupak Khadka, Kathleen A. Grant, Mary Lauren Benton, Joshua Peeples
- **arXiv**: [2611.17105](http://arxiv.org/abs/2611.17105v1)
- **Published**: 2026-11-12
- **Categories**: cs.CV, cs.AI

> Combining vision-language models (VLMs) with parameter-efficient fine-tuning (PEFT) offers a promising approach to few-shot whole-slide image (WSI) classification in computational pathology. This study evaluates this approach for predicting ethanol drinking status from nonhuman primate liver histolo...

### SALT: State-Aligned Low-Rank Transfer for Single-Temporal Cross-Dataset Structural Localization in Remote Sensing
- **Authors**: Aggelos Psiris, Georgios Angelidis, Giorgos Sfikas, Maria Vakalopoulou, Thomas Lagkas, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos
- **arXiv**: [2611.17077](http://arxiv.org/abs/2611.17077v1)
- **Published**: 2026-11-12
- **Categories**: cs.CV

> Change detection in remote sensing conventionally relies on spatially aligned bi-temporal imagery, which may be unavailable or unreliable in practical scenarios. Recent single-temporal approaches address this limitation by learning structural evidence, such as building regions, from a labeled source...

### Reasoning Supervision and Capability Retention in LoRA Domain Adaptation
- **Authors**: Saleh Ashkboos, Dhruv Desai, Lavinia Ghita
- **arXiv**: [2611.17072](http://arxiv.org/abs/2611.17072v1)
- **Published**: 2026-11-12
- **Categories**: cs.AI, cs.CL, cs.LG

> Fine-tuning foundation models on financial data has a wide range of applications, including identifying event types from news, monitoring risk and compliance language, and answering questions over filings and earnings calls. In this setting, the main challenge is to improve task performance without ...

### Report of the 8th LSVOS Challenge: Mobile Unified Multimodal Understanding
- **Authors**: Chang Liu, Henghui Ding, Tong Yang, Dayoung Kil, Seong-heum Kim, Qilin Xiang, Ronghao Zheng, Ziyang Zhang, Shanlin Jiang, Ruohan Shi, Qilin Fan, Chengfeng Qiu, Kaifeng Wei
- **arXiv**: [2611.16925](http://arxiv.org/abs/2611.16925v1)
- **Published**: 2026-11-12
- **Categories**: cs.CV

> This report summarizes the Mobile Unified Multimodal Understanding (MUMU) track of the 8th Large-scale Video Object Segmentation (LSVOS) Challenge, held in conjunction with ECCV 2026. MUMU asks for a single unified model that jointly performs multi-concept image tagging over quality, scene, and even...

### Sustainable Federated Fine-Tuning with LoRA: Environmental Impact and Performance Footprint
- **Authors**: Pedro Augusto Londe Ribeiro, Rodrigo Moreira, Larissa Ferreira Rodrigues Moreira, Joberto S. B. Martins, Tereza C. Carvalho, Flávio de Oliveira Silva
- **arXiv**: [2611.16856](http://arxiv.org/abs/2611.16856v1)
- **Published**: 2026-11-12
- **Categories**: cs.LG, cs.NI

> Federated Learning (FL) with Parameter-Efficient Fine-Tuning (PEFT) enables efficient adaptation of Large Language Models (LLMs), yet its energy and carbon costs across hardware remain poorly understood. We evaluated federated Low-Rank Adaptation (LoRA) fine-tuning on NVIDIA A40, RTX 6000 Ada, and A...

### Detection Is Not Early Warning: Evaluating Token-Level Alarms on Language Model Failures
- **Authors**: Marco De Negri, Luca Sartori, Lorenzo Baggi, Moritz Reihs, Eduard Frank Ďurech, Mennatallah El-Assady, Valentina Pyatkin, Anna Hedström
- **arXiv**: [2611.16803](http://arxiv.org/abs/2611.16803v2)
- **Published**: 2026-11-12
- **Categories**: cs.LG, cs.CL

> Many failures of language models begin at a specific token, the onset. A monitor that reads the model during generation can classify the finished response, detect the failure once it is under way, or warn before it begins, and only a warning leaves time to stop or steer the generation. Monitors are ...

### Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents
- **Authors**: Yiheng Zhao, Runze Ji, Chenyu Yi, Yi Yu, Bingquan Shen, Alex Kot, Xudong Jiang
- **arXiv**: [2611.16744](http://arxiv.org/abs/2611.16744v1)
- **Published**: 2026-11-12
- **Categories**: cs.AI

> Visual content in multimedia systems may be resized, compressed, or re-rendered before it is interpreted by a vision-language model. We study a security failure mode in which these transformations change the machine-readable semantics of an image: a textual instruction is not recovered at a $512\tim...

### Context-Predictive Low-Rank Adaptation for Face Presentation Attack Detection
- **Authors**: Aminu Yusuf, Shakeel Muhammad Ibrahim, Sulaimon Oyeniyi Adebayo, Muhammad Sohail Ibrahim, Muhammad Shahid Jabbar, Shujaat Khan
- **arXiv**: [2611.16534](http://arxiv.org/abs/2611.16534v1)
- **Published**: 2026-11-12
- **Categories**: cs.CV, eess.IV, eess.SP, stat.ML

> Face presentation attack detection requires representations that distinguish physical spoofing cues across changes in acquisition devices, subjects, and attack media. Large visual encoders offer transferable representations, but conventional binary fine-tuning supervises their final decisions withou...

### EvenVLM: A Text and Multimodal Dataset for the Even Language with Vision-Language Fine-Tuning
- **Authors**: Daniil Makovetskii, Ivan Bondarenko
- **arXiv**: [2611.16500](http://arxiv.org/abs/2611.16500v1)
- **Published**: 2026-11-12
- **Categories**: cs.CL

> We present EvenVLM, the first text and multimodal (VQA) dataset for Even (Lamut), an endangered Northern Tungusic language spoken by approximately 6,800 people in Siberia. Our dataset comprises 50,521 structured Even-Russian entries extracted from dictionary and phrasebook sources via GPT-4o Mini-ba...

### Fine-Tuned Small Language Model for Synthetic Clinical Data Generation and Predictive Healthcare Analytics
- **Authors**: Mihnea Sebastian Burlacu, Ionut Anghel, Tudor Cioara
- **arXiv**: [2611.16460](http://arxiv.org/abs/2611.16460v1)
- **Published**: 2026-11-12
- **Categories**: cs.AI

> The reduced availability of medical datasets represents an important challenge in the development of predictive models for remote healthcare solutions, especially when the available data are imbalanced or difficult to extend through traditional methods. Small Language Models (SLMs) have become a pro...

### IsharaBART: An efficient BART-Based Framework for Low-Resource Bangla Sign Language Translation
- **Authors**: Aonmoy Das, Ananna Dev Aishi, Md. Fazlul Kader
- **arXiv**: [2611.16359](http://arxiv.org/abs/2611.16359v1)
- **Published**: 2026-11-12
- **Categories**: cs.CL

> Millions of Bangla Sign Language (BdSL) users lack reliable automatic translation tools. Existing systems are limited by data scarcity, unidirectional design, and computationally expensive architectures that are not suitable for low-resource deployment. We introduce IsharaBART, a bidirectional gener...

### SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0
- **Authors**: Chandra N Sekharan, Vishakan Umapathy, Abhishek Phadke
- **arXiv**: [2611.16300](http://arxiv.org/abs/2611.16300v1)
- **Published**: 2026-11-12
- **Categories**: cs.AI, cs.LG

> Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when the passage lacks adequate evidence. SQuAD 2.0 is a widely used benchmark for this setting, scored by Exact Match (EM) i.e., character-level agreement with huma...

### Low Language Transfer Speech-to-Text
- **Authors**: Husein Zolkepli
- **arXiv**: [2611.16260](http://arxiv.org/abs/2611.16260v1)
- **Published**: 2026-11-12
- **Categories**: cs.CL

> A multilingual speech recogniser has heard much speech in its own languages. We ask how much of that it brings to a language it was never trained on, when it is fine-tuned on the little that language has. We score 28 open multilingual models untouched on Low-Language-TTS, 50 low-resource languages i...

### What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation
- **Authors**: Jinze Tao, Yuxiao Han, Kangkang Dong, Yancong Wei, Xiaojun Zhu, Bokui Chen, Houde Liu
- **arXiv**: [2611.16246](http://arxiv.org/abs/2611.16246v1)
- **Published**: 2026-11-12
- **Categories**: cs.RO, cs.LG

> Navigation agents use a large language model (LLM) planner to call a vision-language-action (VLA) model. Each episode needs the LLM, adding cost and delay. We distill successful agent experience into the VLA instead of distilling the planner. The VLA then navigates alone at test time. Agent sessions...

### Paired Geometric Supervision for Generalizable Deepfake Detection
- **Authors**: Luke Collins, Chang-Tsun Li, Duc Thanh Nguyen, Victor Sanchez
- **arXiv**: [2611.14851](http://arxiv.org/abs/2611.14851v1)
- **Published**: 2026-11-11
- **Categories**: cs.CV

> We present OrthoPairGTL, a geometric training framework for cross-domain deepfake detection, built on a partially frozen DINOv3 backbone ($\sim$300M parameters), and make three contributions: (1) We re-evaluate six recent transfer-learning detectors (Forensics Adapter, Effort, three GenD variants an...

### Sophon: A Procedural Diagnostic for Spatial Reasoning in Vision-Language Models
- **Authors**: J. Zach Gazak, Ryan Swindle, Justin Fletcher
- **arXiv**: [2611.14838](http://arxiv.org/abs/2611.14838v1)
- **Published**: 2026-11-10
- **Categories**: cs.CV, cs.LG

> Open-weight Vision-Language Models (VLMs) score 85-94% on spatial benchmarks (BLINK Spatial, What's Up CLEVR) yet collapse to chance on simple geometric questions when object, scene, and texture priors are stripped away. We introduce and open-source Sophon, a procedurally generated diagnostic of pai...

### From Classification to Generation: Vision-Language Models for Roman Imperial Coin Description
- **Authors**: Pedro Lourenco, Ognjen Arandjelović
- **arXiv**: [2611.14821](http://arxiv.org/abs/2611.14821v1)
- **Published**: 2026-11-10
- **Categories**: cs.CV

> Cataloguing a Roman Imperial coin involves reading its legends and identifying its imagery in order to match it to an entry in the standard reference catalogue. Previous work has automated individual parts of this process, such as identifying the issuer or recognizing reverse motifs, by formulating ...

### A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter Merging (MaLoRA)
- **Authors**: Ziqing Xu, Hancheng Min, Lachlan Ewen MacDonald, Salma Tarmoun, Enrique Mallada, Weijie Su, Rene Vidal
- **arXiv**: [2611.14397](http://arxiv.org/abs/2611.14397v1)
- **Published**: 2026-11-10
- **Categories**: cs.LG

> Low-rank adaptation (LoRA) is the de facto method for parameter-efficient fine-tuning of large neural networks, achieving strong task adaptation with minimal trainable parameters and low optimization cost. Beyond this efficiency, practitioners have observed two striking properties: \textit{robustnes...

### TaoMate-R1: Temporal Role Specialization for Streaming Multi-Reference Video Generation
- **Authors**: Qijun Gan, Chenwei Zhang, Xinyang Li, Meiguang Jin, Junfeng Ma
- **arXiv**: [2611.14307](http://arxiv.org/abs/2611.14307v1)
- **Published**: 2026-11-10
- **Categories**: cs.CV

> Streaming multi-reference video generation establishes a scene from specified people and objects, then continues it under changing instructions. We introduce TaoMate-R1, a streaming multi-reference generator that organizes adaptation parameters through temporal role specialization. It assigns separa...

### Alania-2: Turkish text-to-speech with instant and fine-tuned voice cloning
- **Authors**: Sezgin Saygili, Emre Kaplaner, Oncel Ozgul, Fikri San Koktas
- **arXiv**: [2611.13845](http://arxiv.org/abs/2611.13845v1)
- **Published**: 2026-11-10
- **Categories**: cs.CL, cs.SD

> We present Alania-2, a Turkish text-to-speech (TTS) system with two built-in voices, voice design from text descriptions, and two kinds of voice cloning. Alania-2 is a 488M-parameter model with the VoxCPM architecture, which generates continuous audio latents with a diffusion head on top of a langua...

### Camera3R: Feed-Forward 3D Reconstruction from Heterogeneous Camera Models
- **Authors**: Ruxiao Duan, Yunwen Zhou, Erin Hong, Dongxu Zhao, Eric Turner, Federico Tombari, Alex Wong
- **arXiv**: [2611.13453](http://arxiv.org/abs/2611.13453v1)
- **Published**: 2026-11-10
- **Categories**: cs.CV

> Feed-forward 3D reconstruction (3R) from unconstrained multi-view images has recently emerged as a prominent research direction in 3D computer vision. Various foundational reconstruction models have been proposed with different architectures and reconstruction paradigms. Despite being trained on lar...

### Stochastic Projections and Rank-Aware Learning Rates for Federated LoRA
- **Authors**: Saber Malekmohammadi, Kevin Kuo, Virginia Smith, Golnoosh Farnadi
- **arXiv**: [2611.13331](http://arxiv.org/abs/2611.13331v2)
- **Published**: 2026-11-09
- **Categories**: cs.LG, cs.AI

> Fine-tuning large-scale foundation models across resource-constrained, distributed clients presents significant computational and communication challenges. While merging Low-Rank Adaptation (LoRA) with Federated Learning (FL) enables rank-based flexibility, the interdependence of the adaptation matr...

### 3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model
- **Authors**: Zixiang Ai, Zhenyu Cui, Xu Zou, Jiahuan Zhou
- **arXiv**: [2611.11964](http://arxiv.org/abs/2611.11964v1)
- **Published**: 2026-11-09
- **Categories**: cs.CV

> Feed-forward 3D reconstruction models have demonstrated strong generalization under large-scale pre-training, yet they struggle in long-tail scenarios such as low-light reconstruction, joint human-scene reconstruction, and test-time adaptation. We observe relational attention structure collapse, man...

### RBA: A Read-out Basis Adapter for Parameter-Efficient Interactive OCTA Vessel Segmentation with SEEM
- **Authors**: Jaafar M. Al-Ghabban, Mohammad Reza Mohammadi
- **arXiv**: [2611.11906](http://arxiv.org/abs/2611.11906v1)
- **Published**: 2026-11-09
- **Categories**: cs.CV, cs.LG

> Retinal disease monitoring with optical coherence tomography angiography (OCTA) relies on segmentation of vessels and the foveal avascular zone (FAZ). Promptable models such as SEEM (Segment Everything Everywhere All at Once) allow click-based refinement, but without adaptation SEEM segments thin ve...

### BridgeKV: Large-Model Prefill and Small-Model Decoding for LLM Inference via KV Cache Translation
- **Authors**: Payman Behnam, Debopam Sanyal, Pranav Ponnusamy, Kusum Meda Ravi, Pranav Sastry, Mani Chandana Bandaru, Alind Khare, Myungjin Lee, Alexey Tumanov
- **arXiv**: [2611.11761](http://arxiv.org/abs/2611.11761v1)
- **Published**: 2026-11-09
- **Categories**: cs.CL

> LLM inference has two phases with different bottlenecks: LLM prefill runs once per request and is compute-intensive. Decoding repeats for every output token and is limited by memory bandwidth. To address the challenges associated with this issue, different solutions have been proposed. All of these ...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "park-2026",
    "title": "Structural Self-Teaching for Compositional Generation in Unified Multimodal Models",
    "authors": [
      "Jaeyoo Park",
      "Bohyung Han"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.18261",
    "paper_url": "https://arxiv.org/abs/2611.18261",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "brinner-2026",
    "title": "NER-D: A cross-domain benchmark for German NER",
    "authors": [
      "Marc Brinner",
      "Philipp Cimiano",
      "Karolina Hanna Czok",
      "Regina Stodden",
      "Viju Sudhi",
      "Sina Zarrieß"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.18257",
    "paper_url": "https://arxiv.org/abs/2611.18257",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "qiao-2026",
    "title": "InfiHall-Bench: A Benchmark for Hallucination Evaluation in Autoregressive Text-to-Image Generation",
    "authors": [
      "Yuxia Qiao",
      "Xinhao Zhong",
      "Junhao Li",
      "Yi Sun",
      "Jiaxin Hong",
      "Shuoyang Sun",
      "Bin Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.18053",
    "paper_url": "https://arxiv.org/abs/2611.18053",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "wen-2026",
    "title": "Direction or Magnitude? Learning Scalars over Task-Calibrated Directions",
    "authors": [
      "Ziqing Wen",
      "Xiaohui Song",
      "Jiahuan Wang",
      "Ping Luo",
      "Junlin Zeng",
      "Dongsheng Li",
      "Kele Xu",
      "Tao Sun"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.17784",
    "paper_url": "https://arxiv.org/abs/2611.17784",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "sawada-2026",
    "title": "Maximizing Capacity Utilization of LoRA Adapters for Mitigating the Learning-Forgetting Trade-off",
    "authors": [
      "Tomohiro Sawada",
      "Kartik Goyal"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.17191",
    "paper_url": "https://arxiv.org/abs/2611.17191",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "abbas-2026",
    "title": "Parameter-Efficient Conciseness Adaptation: Differentiable Length Control for Concise Clinical Reasoning in Smaller Language Models",
    "authors": [
      "Tanzeel Abbas",
      "Ahmad Kamran Malik",
      "Nafees Qamar",
      "Sana Liaqat"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.17128",
    "paper_url": "https://arxiv.org/abs/2611.17128",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "mohammadi-2026",
    "title": "Predicting Ethanol Drinking Status from Nonhuman Primate Liver Histology: A Proof of Concept for Parameter-efficient Fine-tuning in Few-Shot Vision-Language Modeling",
    "authors": [
      "Amirmohammad Mohammadi",
      "Rupak Khadka",
      "Kathleen A. Grant",
      "Mary Lauren Benton",
      "Joshua Peeples"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.17105",
    "paper_url": "https://arxiv.org/abs/2611.17105",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "psiris-2026",
    "title": "SALT: State-Aligned Low-Rank Transfer for Single-Temporal Cross-Dataset Structural Localization in Remote Sensing",
    "authors": [
      "Aggelos Psiris",
      "Georgios Angelidis",
      "Giorgos Sfikas",
      "Maria Vakalopoulou",
      "Thomas Lagkas",
      "Panagiotis Sarigiannidis",
      "Georgios Th. Papadopoulos"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.17077",
    "paper_url": "https://arxiv.org/abs/2611.17077",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "ashkboos-2026",
    "title": "Reasoning Supervision and Capability Retention in LoRA Domain Adaptation",
    "authors": [
      "Saleh Ashkboos",
      "Dhruv Desai",
      "Lavinia Ghita"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.17072",
    "paper_url": "https://arxiv.org/abs/2611.17072",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "liu-2026",
    "title": "Report of the 8th LSVOS Challenge: Mobile Unified Multimodal Understanding",
    "authors": [
      "Chang Liu",
      "Henghui Ding",
      "Tong Yang",
      "Dayoung Kil",
      "Seong-heum Kim",
      "Qilin Xiang",
      "Ronghao Zheng",
      "Ziyang Zhang",
      "Shanlin Jiang",
      "Ruohan Shi",
      "Qilin Fan",
      "Chengfeng Qiu",
      "Kaifeng Wei"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16925",
    "paper_url": "https://arxiv.org/abs/2611.16925",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "ribeiro-2026",
    "title": "Sustainable Federated Fine-Tuning with LoRA: Environmental Impact and Performance Footprint",
    "authors": [
      "Pedro Augusto Londe Ribeiro",
      "Rodrigo Moreira",
      "Larissa Ferreira Rodrigues Moreira",
      "Joberto S. B. Martins",
      "Tereza C. Carvalho",
      "Flávio de Oliveira Silva"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16856",
    "paper_url": "https://arxiv.org/abs/2611.16856",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "negri-2026",
    "title": "Detection Is Not Early Warning: Evaluating Token-Level Alarms on Language Model Failures",
    "authors": [
      "Marco De Negri",
      "Luca Sartori",
      "Lorenzo Baggi",
      "Moritz Reihs",
      "Eduard Frank Ďurech",
      "Mennatallah El-Assady",
      "Valentina Pyatkin",
      "Anna Hedström"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16803",
    "paper_url": "https://arxiv.org/abs/2611.16803",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "zhao-2026",
    "title": "Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents",
    "authors": [
      "Yiheng Zhao",
      "Runze Ji",
      "Chenyu Yi",
      "Yi Yu",
      "Bingquan Shen",
      "Alex Kot",
      "Xudong Jiang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16744",
    "paper_url": "https://arxiv.org/abs/2611.16744",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "yusuf-2026",
    "title": "Context-Predictive Low-Rank Adaptation for Face Presentation Attack Detection",
    "authors": [
      "Aminu Yusuf",
      "Shakeel Muhammad Ibrahim",
      "Sulaimon Oyeniyi Adebayo",
      "Muhammad Sohail Ibrahim",
      "Muhammad Shahid Jabbar",
      "Shujaat Khan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16534",
    "paper_url": "https://arxiv.org/abs/2611.16534",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "makovetskii-2026",
    "title": "EvenVLM: A Text and Multimodal Dataset for the Even Language with Vision-Language Fine-Tuning",
    "authors": [
      "Daniil Makovetskii",
      "Ivan Bondarenko"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16500",
    "paper_url": "https://arxiv.org/abs/2611.16500",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "burlacu-2026",
    "title": "Fine-Tuned Small Language Model for Synthetic Clinical Data Generation and Predictive Healthcare Analytics",
    "authors": [
      "Mihnea Sebastian Burlacu",
      "Ionut Anghel",
      "Tudor Cioara"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16460",
    "paper_url": "https://arxiv.org/abs/2611.16460",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "das-2026",
    "title": "IsharaBART: An efficient BART-Based Framework for Low-Resource Bangla Sign Language Translation",
    "authors": [
      "Aonmoy Das",
      "Ananna Dev Aishi",
      "Md. Fazlul Kader"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16359",
    "paper_url": "https://arxiv.org/abs/2611.16359",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "sekharan-2026",
    "title": "SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0",
    "authors": [
      "Chandra N Sekharan",
      "Vishakan Umapathy",
      "Abhishek Phadke"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16300",
    "paper_url": "https://arxiv.org/abs/2611.16300",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "zolkepli-2026",
    "title": "Low Language Transfer Speech-to-Text",
    "authors": [
      "Husein Zolkepli"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16260",
    "paper_url": "https://arxiv.org/abs/2611.16260",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "tao-2026",
    "title": "What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation",
    "authors": [
      "Jinze Tao",
      "Yuxiao Han",
      "Kangkang Dong",
      "Yancong Wei",
      "Xiaojun Zhu",
      "Bokui Chen",
      "Houde Liu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.16246",
    "paper_url": "https://arxiv.org/abs/2611.16246",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "collins-2026",
    "title": "Paired Geometric Supervision for Generalizable Deepfake Detection",
    "authors": [
      "Luke Collins",
      "Chang-Tsun Li",
      "Duc Thanh Nguyen",
      "Victor Sanchez"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.14851",
    "paper_url": "https://arxiv.org/abs/2611.14851",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "gazak-2026",
    "title": "Sophon: A Procedural Diagnostic for Spatial Reasoning in Vision-Language Models",
    "authors": [
      "J. Zach Gazak",
      "Ryan Swindle",
      "Justin Fletcher"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.14838",
    "paper_url": "https://arxiv.org/abs/2611.14838",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "lourenco-2026",
    "title": "From Classification to Generation: Vision-Language Models for Roman Imperial Coin Description",
    "authors": [
      "Pedro Lourenco",
      "Ognjen Arandjelović"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.14821",
    "paper_url": "https://arxiv.org/abs/2611.14821",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "xu-2026",
    "title": "A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter Merging (MaLoRA)",
    "authors": [
      "Ziqing Xu",
      "Hancheng Min",
      "Lachlan Ewen MacDonald",
      "Salma Tarmoun",
      "Enrique Mallada",
      "Weijie Su",
      "Rene Vidal"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.14397",
    "paper_url": "https://arxiv.org/abs/2611.14397",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "gan-2026",
    "title": "TaoMate-R1: Temporal Role Specialization for Streaming Multi-Reference Video Generation",
    "authors": [
      "Qijun Gan",
      "Chenwei Zhang",
      "Xinyang Li",
      "Meiguang Jin",
      "Junfeng Ma"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.14307",
    "paper_url": "https://arxiv.org/abs/2611.14307",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "saygili-2026",
    "title": "Alania-2: Turkish text-to-speech with instant and fine-tuned voice cloning",
    "authors": [
      "Sezgin Saygili",
      "Emre Kaplaner",
      "Oncel Ozgul",
      "Fikri San Koktas"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.13845",
    "paper_url": "https://arxiv.org/abs/2611.13845",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "duan-2026",
    "title": "Camera3R: Feed-Forward 3D Reconstruction from Heterogeneous Camera Models",
    "authors": [
      "Ruxiao Duan",
      "Yunwen Zhou",
      "Erin Hong",
      "Dongxu Zhao",
      "Eric Turner",
      "Federico Tombari",
      "Alex Wong"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.13453",
    "paper_url": "https://arxiv.org/abs/2611.13453",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "malekmohammadi-2026",
    "title": "Stochastic Projections and Rank-Aware Learning Rates for Federated LoRA",
    "authors": [
      "Saber Malekmohammadi",
      "Kevin Kuo",
      "Virginia Smith",
      "Golnoosh Farnadi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.13331",
    "paper_url": "https://arxiv.org/abs/2611.13331",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "ai-2026",
    "title": "3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model",
    "authors": [
      "Zixiang Ai",
      "Zhenyu Cui",
      "Xu Zou",
      "Jiahuan Zhou"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.11964",
    "paper_url": "https://arxiv.org/abs/2611.11964",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "al-ghabban-2026",
    "title": "RBA: A Read-out Basis Adapter for Parameter-Efficient Interactive OCTA Vessel Segmentation with SEEM",
    "authors": [
      "Jaafar M. Al-Ghabban",
      "Mohammad Reza Mohammadi"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.11906",
    "paper_url": "https://arxiv.org/abs/2611.11906",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  },
  {
    "id": "behnam-2026",
    "title": "BridgeKV: Large-Model Prefill and Small-Model Decoding for LLM Inference via KV Cache Translation",
    "authors": [
      "Payman Behnam",
      "Debopam Sanyal",
      "Pranav Ponnusamy",
      "Kusum Meda Ravi",
      "Pranav Sastry",
      "Mani Chandana Bandaru",
      "Alind Khare",
      "Myungjin Lee",
      "Alexey Tumanov"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.11761",
    "paper_url": "https://arxiv.org/abs/2611.11761",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-16"
  }
]
```
