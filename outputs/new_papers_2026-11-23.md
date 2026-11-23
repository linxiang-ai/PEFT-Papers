# New arXiv PEFT papers — 2026-11-23

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **33**.

## Candidates

### Mixture of Latent Recursions for Low-Rank Adaptation
- **Authors**: Weixun Luo, Ye Mao, Ranran Huang, Junpeng Jing, Krystian Mikolajczyk
- **arXiv**: [2611.27823](http://arxiv.org/abs/2611.27823v1)
- **Published**: 2026-11-20
- **Categories**: cs.LG

> Low-Rank Adaptation (LoRA) performs task-specific adaptation using a fixed low-rank architecture, whose expressiveness is typically increased by enlarging or adding learnable modules with a proportional parameter overhead. We introduce Mixture of Latent Recursions (MoLR), an adaptive recursion frame...

### More Bits Won't Fix It: Diagnosing and Treating an Ill-Conditioned Backward Pass (A Case Study on Gemma-4)
- **Authors**: Jeong Hyun Lee
- **arXiv**: [2611.27243](http://arxiv.org/abs/2611.27243v1)
- **Published**: 2026-11-20
- **Categories**: cs.LG

> During LoRA fine-tuning of Gemma-4 (12B and 31B) on long prompts, whether they contain CT images, natural photos, or about 2,000 tokens of text, bf16 and fp32 gradients agree in the upper third of the language model (cosine similarity 0.96 or above) but are nearly orthogonal in the lower third. On i...

### Parameter-Efficient Adaptation of Qwen3-VL for Handwritten Mathematical Expression Recognition
- **Authors**: Manh Tuan Ha, Xuan Bao Viet Tran, Vo Minh Dat Nguyen, Minh Nhat Vo, Quoc Trung Nguyen, Van Bay Nguyen
- **arXiv**: [2611.27208](http://arxiv.org/abs/2611.27208v1)
- **Published**: 2026-11-20
- **Categories**: cs.CV, cs.AI

> Handwritten mathematical expression recognition (HMER) requires joint recovery of symbol identity and two-dimensional syntax, so a locally plausible transcription may still be structurally wrong. We study whether a compact vision-language model can be adapted to generate linearized Symbol Label Grap...

### Backbone-Specific LoRA Geometry: Orthogonality, Superposition, and Provenance
- **Authors**: Kazuhiko Kawamoto, Keigo Watanabe, Hiroshi Kera
- **arXiv**: [2611.27201](http://arxiv.org/abs/2611.27201v1)
- **Published**: 2026-11-20
- **Categories**: cs.CV, cs.LG

> Sharing one low-rank adaptation (LoRA) update across pretrained models simplifies deployment. Composition methods typically combine updates from a common backbone, while cross-model transfer transforms updates for a target backbone. The conditions for sharing updates across backbones while preservin...

### Learning Adaptive Defense Strategies: Fine-Tuned LLMs for Network Security Games under Network Mobility
- **Authors**: Md Abu Sayed, Asif Rahman, Ahmed Ryen, Ahmed Hemida, Charles Kamhoua, Christopher Kiekintveld
- **arXiv**: [2611.27180](http://arxiv.org/abs/2611.27180v1)
- **Published**: 2026-11-20
- **Categories**: cs.AI

> Large language models(LLM) show promise for strategic reasoning, yet their ability to compute game-theoretic equilibria under dynamic conditions remains largely unexplored. This work investigates whether fine-tuned LLMs can serve as solver-free surrogates for online equilibrium computation in honeyp...

### Structure Over Scale: Rethinking Adaptation for Reinforcement Learning with Verifiable Rewards
- **Authors**: Allan Kazakov, Abdurrahman Javat
- **arXiv**: [2611.27148](http://arxiv.org/abs/2611.27148v1)
- **Published**: 2026-11-20
- **Categories**: cs.LG, cs.AI

> Reinforcement Learning with Verifiable Rewards (RLVR) is often framed as a choice between the expressivity of Full Fine-Tuning (FFT) and the efficiency of Low-Rank Adaptation (LoRA). We find that this framing misses an important variable: the geometry of the update. Under a common cold-start GRPO pr...

### How Does SAM-3 Adapt? Capacity, Update Geometry, and Domain Transfer
- **Authors**: Allan Kazakov, Abdurrahman Javat, Duygu Cakir
- **arXiv**: [2611.27142](http://arxiv.org/abs/2611.27142v1)
- **Published**: 2026-11-20
- **Categories**: cs.CV, cs.AI

> Promptable segmentation foundation models are increasingly used in specialized domains, but it remains unclear how SAM-3 should be fine-tuned when adapting it beyond its original training distribution. We study this question by comparing five adaptation families --LoRA, HiRA, KRAdapter, QuanTA, and ...

### Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation
- **Authors**: Yalin Yang, Xiao Huang, Yanan Wu, Hao Yang, Ryan Zhenqi Zhou
- **arXiv**: [2611.27089](http://arxiv.org/abs/2611.27089v1)
- **Published**: 2026-11-20
- **Categories**: cs.AI, cs.LG

> Weight-space programming lets a language model inspect and edit another model's weights, offering an alternative to gradient-based adaptation. We evaluated both approaches using Qwen3.5-0.8B on a fixed reference-frame task (128 items), StepGame (200 items), and two untrained distance-comparison task...

### Improving the Optimisation Landscape for Particle Mixtures
- **Authors**: Yan Lin, David T. Frazier, Paula Cordero Encinar, Chris J. Oates
- **arXiv**: [2611.26931](http://arxiv.org/abs/2611.26931v1)
- **Published**: 2026-11-20
- **Categories**: cs.LG

> Several methods in statistics and machine learning represent a predictive distribution as an equally weighted mixture of models, or particles, trained via the mixture predictive likelihood. However, we prove that the mixture predictive likelihood is poorly suited to gradient-based optimisation, beca...

### LoCo-WAM: Test-Time Training as Long Context for World-Action Models
- **Authors**: Sheng Cheng, Deqian Kong
- **arXiv**: [2611.26853](http://arxiv.org/abs/2611.26853v1)
- **Published**: 2026-11-19
- **Categories**: cs.RO, cs.AI, cs.LG

> World-action models guide robot actions by predicting what happens next, but typically condition on a short observation history. Extending this history increases computation at every decision and can require a separately trained model. We introduce LoCo-WAM, which learns from the outcomes of its act...

### Rethinking Full-Weight LoRA with Domain and Task Adapter Scaling for Question Answering over Portuguese Well Drilling Reports
- **Authors**: Luan B. Guerra, Diogo M. Paes, Marcelo N. Grimberg, Arnaldo C. Junior, Wallace Casaca, Lucas C. Ribas
- **arXiv**: [2611.26833](http://arxiv.org/abs/2611.26833v1)
- **Published**: 2026-11-19
- **Categories**: cs.CL, cs.AI

> Adapting large language models (LLMs) to specialized domains remains challenging, particularly for technical documents such as Portuguese well drilling reports, where annotated data are scarce and domain adaptation may compromise instruction-following capabilities. Although Low-Rank Adaptation (LoRA...

### LEAN: Library-Based Adaptation for Asynchronous, Federated Fine-Tuning
- **Authors**: Erdong Hu, Zhimin Ding, Yuxin Tang, Chris Jermaine
- **arXiv**: [2611.26805](http://arxiv.org/abs/2611.26805v1)
- **Published**: 2026-11-19
- **Categories**: cs.LG

> Federated fine-tuning of foundation models with low-rank adapters (LoRA) is typically reconciled by averaging locally trained adapters. In cross-device settings, where participants hold heterogeneous data and join or leave asynchronously, averaging is poorly suited: locally trained adapters are not ...

### Language-Oriented Semantic Modeling for Target Language Extraction
- **Authors**: Mehmet Sinan Yıldırım, Ke Zhang, Shuai Wang, Haizhou Li
- **arXiv**: [2611.26317](http://arxiv.org/abs/2611.26317v1)
- **Published**: 2026-11-19
- **Categories**: cs.CL, eess.AS

> Target Language Extraction (TLE) aims to isolate speech in a target language from multilingual mixtures. Existing approaches primarily rely on acoustic modeling with language identity labels, which provide only coarse categorical guidance. In this work, we propose a language-oriented semantic modeli...

### Why Flat Drafts Stay Flat: Region-Mean Latents Govern Texture in Flow-Based Image Generation
- **Authors**: Zihan Gu, Jiangcan Jia, Hua Zhang, Lulu Zhao
- **arXiv**: [2611.25930](http://arxiv.org/abs/2611.25930v1)
- **Published**: 2026-11-19
- **Categories**: cs.CV

> Flat color-block drafts specify layout and regional color while leaving interior detail unspecified, yet pretrained flow-based generators can preserve their flat appearance even under photorealistic prompts. We trace this behavior to a cross-scale mechanism linking fine pixel variation to regional m...

### Parameter-Efficient Adaptation of Self-supervised Vision Backbones Survives Distribution Shift in Radar Micro-Doppler HAR
- **Authors**: Keryan Chelouche, Petr Dobias, Nistor Grozavu, Olivier Romain
- **arXiv**: [2611.25874](http://arxiv.org/abs/2611.25874v1)
- **Published**: 2026-11-19
- **Categories**: cs.LG

> Micro-Doppler radar enables contactless, privacy-preserving human activity recognition (HAR), but deployment robustness remains underexplored. We compared full fine-tuning, frozen probing, and parameter-efficient fine-tuning (PEFT) using subject-disjoint in-distribution cross-validation and few-shot...

### Efficient and Robust Drafting with Multi-Token Prediction
- **Authors**: Filippo Galgani, Ziwei Ji, Omri Homburger, Ganesh Jawahar, Michelle Ramanovich, Ivan Korotkov, Luciano Martins, Utku Evci, Edouard Yvinec, Pooja Consul, Vivek Kumar, Tal Schuster
- **arXiv**: [2611.25813](http://arxiv.org/abs/2611.25813v1)
- **Published**: 2026-11-19
- **Categories**: cs.CL

> Speculative decoding has emerged as a critical technique for accelerating Large Language Model (LLM) inference by decoupling generation into a drafting phase and a parallel verification phase. A crucial challenge is therefore designing a drafter that is both lightweight and accurate enough to approx...

### Can LLMs Resolve Entity Conflicts in Domain Specific NLU Pipelines?
- **Authors**: Akansha Bhardwaj, Mingbo Cui, Victor Guimaraes, Dominik Kohler, Diana Nicoleta Popa, Meghana M. Reddy, Paolo Rosso
- **arXiv**: [2611.25733](http://arxiv.org/abs/2611.25733v1)
- **Published**: 2026-11-19
- **Categories**: cs.IR, cs.LG

> Resolving entity conflicts is a critical step in Pipeline-based NLU architectures, especially when multiple extractors provide overlapping or conflicting outputs. Traditional rule-based entity conflict resolution methods often lack flexibility and are unscalable. In this work, we aim to study if the...

### Can an LLM Repair a Language Model in Weight Space Without Gradient Training?
- **Authors**: Bharath Kumar Bolla, Raghavender Surya Upadhayula, Vishnu Surya Reddy Nandi, Ramesh Nandipalli
- **arXiv**: [2611.25613](http://arxiv.org/abs/2611.25613v2)
- **Published**: 2026-11-19
- **Categories**: cs.AI

> Although an external language model can select and test repairs to another model's weights, behavior can also be recovered through fixed numerical edits. We assessed the value of interactive selection in a controlled study of Transformer repair. After inspecting predictions, activation summaries, an...

### NativeSeg: Native Vision Language Segmentation of 3D Computed Tomography via Spatial Visual Tokens and Verified Local Zoom
- **Authors**: Chengqian Ma, Gaole Dai, Zijie Meng, Weixuan Jin, Yijie Du, Yuexiao Ma, Xiawu Zheng, Fei Chao
- **arXiv**: [2611.24443](http://arxiv.org/abs/2611.24443v1)
- **Published**: 2026-11-18
- **Categories**: cs.CV

> Text prompted 3D computed tomography (CT) segmentation requires both full slice context and fine boundary precision across volumes where over $80\%$ of organ prompted slices lack the queried target. Existing medical vision language models (VLMs) are largely non native segmenters: they delegate pixel...

### A Hybrid RAG Framework for Deceptive Review Detection: Integrating RoBERTa-LoRA, FAISS-Based Retrieval, and LLM Reasoning
- **Authors**: Andrei Kostin, José Ángel Diaz-Garcia, Karel Gutiérrez-Batista
- **arXiv**: [2611.24049](http://arxiv.org/abs/2611.24049v1)
- **Published**: 2026-11-18
- **Categories**: cs.CL

> The growth of deceptive online opinions poses a critical risk of misinformation and fraud. This paper proposes a Retrieval-Augmented Generation (RAG) system to automatically distinguish spam reviews. The architecture integrates RoBERTa with Low-Rank Adaptation (LoRA) classification, FAISS semantic v...

### Same Rank, Different Needs: Rethinking LoRA Redistribution in Federated Learning
- **Authors**: Jinqian Chen, Jihua Zhu, Chang Liu
- **arXiv**: [2611.23742](http://arxiv.org/abs/2611.23742v1)
- **Published**: 2026-11-18
- **Categories**: cs.LG

> Federated low-rank adaptation (LoRA) enables clients with different resource budgets to collaboratively fine-tune foundation models. To distribute an aggregated update within each client's rank budget, existing methods commonly retain its leading singular directions. However, directions that best re...

### Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need
- **Authors**: Artur Kuramshin, Charlotte Cloutier, Michael Przystupa, Kirsty Ellis, Mohammad S. Akhter, Glen Berseth
- **arXiv**: [2611.23676](http://arxiv.org/abs/2611.23676v1)
- **Published**: 2026-11-18
- **Categories**: cs.RO, cs.LG

> Vision-Language-Action models have demonstrated strong manipulation capabilities. A limitation of VLA models is that most manipulation datasets focus on parallel-jaw gripper systems, making transfer to multi-finger hands challenging, particularly as teleoperation datasets are harder to collect with ...

### LusoClin: A Synthetic Clinical Note Dataset for Medical Information Retrieval in European Portuguese
- **Authors**: Carla Teixeira Lopes, Daniel Félix
- **arXiv**: [2611.23454](http://arxiv.org/abs/2611.23454v1)
- **Published**: 2026-11-17
- **Categories**: cs.AI, cs.IR

> Access to large-scale clinical text collections is crucial for advancing medical information retrieval research, including clinical note search, patient cohort identification, and domain-adapted retrieval models. However, real clinical notes are rarely available due to privacy regulations, which par...

### Fine-Tuning Gemma 4 Edge Models for MATLAB Signal-Processing Code with SFT and QLoRA on a Laptop iGPU
- **Authors**: Mehmet Altan Toksöz
- **arXiv**: [2611.23205](http://arxiv.org/abs/2611.23205v1)
- **Published**: 2026-11-17
- **Categories**: cs.LG, cs.AI, cs.SE, eess.SP

> Small language models that run on a laptop are attractive for writing signal-processing code offline, but they make systematic errors on digital signal processing (DSP) conventions. We apply supervised fine-tuning (SFT) to the Gemma 4 edge models E2B and E4B with 66 checked examples covering 11 sign...

### MoE--LoRA Methods for Multilingual Adaptation: A Systematic Empirical Study
- **Authors**: Nikit Srivastava, Joel Dag, René Speck, Axel-Cyrille Ngonga Ngomo
- **arXiv**: [2611.23158](http://arxiv.org/abs/2611.23158v2)
- **Published**: 2026-11-17
- **Categories**: cs.CL, cs.LG

> Routed low-rank adapters offer a parameter-efficient means to improve the performance of large language models (LLMs) across tasks. Hence, it is assumed that they can also be used to improve the support of low-resource languages in LLMs, which currently serve English far better than the thousands of...

### Impact of Pretraining Length, Model Size, and Annotation Budget on Downstream Clinical Tasks of Foundation Models in Radiotherapy
- **Authors**: Alejandro Cortina Uribe, Sidsel Højklint Poulsen, Ivan Richter Vogelius, Jens Petersen
- **arXiv**: [2611.22896](http://arxiv.org/abs/2611.22896v1)
- **Published**: 2026-11-17
- **Categories**: cs.CV

> Cone-beam CT (CBCT) scans acquired during radiotherapy capture changes such as tumor shrinkage and radiation-induced tissue changes, offering great potential for foundation models that help monitor individual treatment responses. However, to our knowledge, no large-scale pretrained models for radiot...

### Efficient Self-Supervised Adaptation of 3D Abdominal Vision-Language Model for Institution-Specific HCC Classification via Full Fine-Tuning and PEFT
- **Authors**: Febryan Putra Kartika, Cheng-Yu Ma, Ying-Jia Lin, Chi-Tung Cheng, Kuan-Fu Chen
- **arXiv**: [2611.22504](http://arxiv.org/abs/2611.22504v1)
- **Published**: 2026-11-17
- **Categories**: cs.CV, cs.LG

> Medical vision-language models (VLMs) capture cross-modal relationships between image and text, yet their adaptation to institution-specific clinical tasks remains underexplored. In this study, we fine-tuned a pretrained 3D medical VLM for hepatocellular carcinoma (HCC) classification using paired a...

### CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation
- **Authors**: Mehul Arora, Dhruv Agarwal, Ambuj Agrawal
- **arXiv**: [2611.22395](http://arxiv.org/abs/2611.22395v1)
- **Published**: 2026-11-17
- **Categories**: cs.CV, cs.RO

> Vision-Language-Action (VLA) models achieve high success rates on the LIBERO benchmark but remain sensitive to paraphrasing. Existing VLAs ranging from 0.6B to 7.5B parameters experience a 22-52 point performance drop on LIBERO-Para while SmolVLA exhibits an even larger decline, from 83\% to 8\%. Be...

### BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning
- **Authors**: Juyoung Park, Heejun Lee
- **arXiv**: [2611.22334](http://arxiv.org/abs/2611.22334v1)
- **Published**: 2026-11-17
- **Categories**: cs.LG

> Parameter-efficient fine-tuning of quantized large language models is dominated by QLoRA, which combines 4-bit weight quantization with FP16 low-rank adapters. We ask whether the FP16 adapter precision is necessary. Replacing it with a single binary bit per adapter parameter, combined with a learned...

### SARVIA: Fast-Adapting the Strong SAR Foundation Models That Are Already in Your MLLMs
- **Authors**: Yuxuan Li, Zichen Tian, Qianru Sun
- **arXiv**: [2611.22273](http://arxiv.org/abs/2611.22273v1)
- **Published**: 2026-11-17
- **Categories**: cs.CV

> Synthetic aperture radar (SAR) foundation models provide transferable representations for diverse perception tasks in all-weather Earth observation. However, their development often relies on costly large-scale SAR pretraining, raising the question of whether such extensive domain-specific pretraini...

### Watermark Evidence under Open-Weight LLM Modification: Exact Bounds for Low-Rank Output Watermarks
- **Authors**: Prashant Shekhar, Dumindu Samaraweera, Caroline Howard
- **arXiv**: [2611.21702](http://arxiv.org/abs/2611.21702v1)
- **Published**: 2026-11-16
- **Categories**: cs.CR, cs.AI, cs.CL

> Open-weight language models can continue generating after their released weights are modified, while a watermark verifier still scores outputs against the original base and marked models. We study how such modifications change the evidence available to an OpenStamp-style verifier. At each shared pre...

### Tight PAC-Bayes Generalisation Guarantees for Large Language Model Judges
- **Authors**: Tom A. Lamb, Philip H. S. Torr, Tim G. J. Rudner
- **arXiv**: [2611.20818](http://arxiv.org/abs/2611.20818v1)
- **Published**: 2026-11-16
- **Categories**: cs.LG

> Large language model (LLM) judges are increasingly used to monitor the outputs of LLM-based AI agents, yet formal guarantees on the reliability of these judges remain largely absent, limiting confidence in their use for safety-critical oversight. We consider certifying such a judge and define its ri...

### Instant Weight-Space Consolidation for Long-Term Memory in LLMs
- **Authors**: Manan Suri, Dinesh Manocha
- **arXiv**: [2611.20759](http://arxiv.org/abs/2611.20759v1)
- **Published**: 2026-11-16
- **Categories**: cs.CL

> Agentic memory systems give LLMs persistent memory by extracting experience into text and retrieving it at query time, but the model itself does not evolve: however many interactions it has had, it starts each query the same. Extraction errors compound, implicit cross-session patterns that no single...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "luo-2026",
    "title": "Mixture of Latent Recursions for Low-Rank Adaptation",
    "authors": [
      "Weixun Luo",
      "Ye Mao",
      "Ranran Huang",
      "Junpeng Jing",
      "Krystian Mikolajczyk"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.27823",
    "paper_url": "https://arxiv.org/abs/2611.27823",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "lee-2026",
    "title": "More Bits Won't Fix It: Diagnosing and Treating an Ill-Conditioned Backward Pass (A Case Study on Gemma-4)",
    "authors": [
      "Jeong Hyun Lee"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.27243",
    "paper_url": "https://arxiv.org/abs/2611.27243",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "ha-2026",
    "title": "Parameter-Efficient Adaptation of Qwen3-VL for Handwritten Mathematical Expression Recognition",
    "authors": [
      "Manh Tuan Ha",
      "Xuan Bao Viet Tran",
      "Vo Minh Dat Nguyen",
      "Minh Nhat Vo",
      "Quoc Trung Nguyen",
      "Van Bay Nguyen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.27208",
    "paper_url": "https://arxiv.org/abs/2611.27208",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "kawamoto-2026",
    "title": "Backbone-Specific LoRA Geometry: Orthogonality, Superposition, and Provenance",
    "authors": [
      "Kazuhiko Kawamoto",
      "Keigo Watanabe",
      "Hiroshi Kera"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.27201",
    "paper_url": "https://arxiv.org/abs/2611.27201",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "sayed-2026",
    "title": "Learning Adaptive Defense Strategies: Fine-Tuned LLMs for Network Security Games under Network Mobility",
    "authors": [
      "Md Abu Sayed",
      "Asif Rahman",
      "Ahmed Ryen",
      "Ahmed Hemida",
      "Charles Kamhoua",
      "Christopher Kiekintveld"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.27180",
    "paper_url": "https://arxiv.org/abs/2611.27180",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "kazakov-2026",
    "title": "Structure Over Scale: Rethinking Adaptation for Reinforcement Learning with Verifiable Rewards",
    "authors": [
      "Allan Kazakov",
      "Abdurrahman Javat"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.27148",
    "paper_url": "https://arxiv.org/abs/2611.27148",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "kazakov-2026",
    "title": "How Does SAM-3 Adapt? Capacity, Update Geometry, and Domain Transfer",
    "authors": [
      "Allan Kazakov",
      "Abdurrahman Javat",
      "Duygu Cakir"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.27142",
    "paper_url": "https://arxiv.org/abs/2611.27142",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "yang-2026",
    "title": "Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation",
    "authors": [
      "Yalin Yang",
      "Xiao Huang",
      "Yanan Wu",
      "Hao Yang",
      "Ryan Zhenqi Zhou"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.27089",
    "paper_url": "https://arxiv.org/abs/2611.27089",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "lin-2026",
    "title": "Improving the Optimisation Landscape for Particle Mixtures",
    "authors": [
      "Yan Lin",
      "David T. Frazier",
      "Paula Cordero Encinar",
      "Chris J. Oates"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.26931",
    "paper_url": "https://arxiv.org/abs/2611.26931",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "cheng-2026",
    "title": "LoCo-WAM: Test-Time Training as Long Context for World-Action Models",
    "authors": [
      "Sheng Cheng",
      "Deqian Kong"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.26853",
    "paper_url": "https://arxiv.org/abs/2611.26853",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "guerra-2026",
    "title": "Rethinking Full-Weight LoRA with Domain and Task Adapter Scaling for Question Answering over Portuguese Well Drilling Reports",
    "authors": [
      "Luan B. Guerra",
      "Diogo M. Paes",
      "Marcelo N. Grimberg",
      "Arnaldo C. Junior",
      "Wallace Casaca",
      "Lucas C. Ribas"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.26833",
    "paper_url": "https://arxiv.org/abs/2611.26833",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "hu-2026",
    "title": "LEAN: Library-Based Adaptation for Asynchronous, Federated Fine-Tuning",
    "authors": [
      "Erdong Hu",
      "Zhimin Ding",
      "Yuxin Tang",
      "Chris Jermaine"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.26805",
    "paper_url": "https://arxiv.org/abs/2611.26805",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "y-ld-r-m-2026",
    "title": "Language-Oriented Semantic Modeling for Target Language Extraction",
    "authors": [
      "Mehmet Sinan Yıldırım",
      "Ke Zhang",
      "Shuai Wang",
      "Haizhou Li"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.26317",
    "paper_url": "https://arxiv.org/abs/2611.26317",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "gu-2026",
    "title": "Why Flat Drafts Stay Flat: Region-Mean Latents Govern Texture in Flow-Based Image Generation",
    "authors": [
      "Zihan Gu",
      "Jiangcan Jia",
      "Hua Zhang",
      "Lulu Zhao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.25930",
    "paper_url": "https://arxiv.org/abs/2611.25930",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "chelouche-2026",
    "title": "Parameter-Efficient Adaptation of Self-supervised Vision Backbones Survives Distribution Shift in Radar Micro-Doppler HAR",
    "authors": [
      "Keryan Chelouche",
      "Petr Dobias",
      "Nistor Grozavu",
      "Olivier Romain"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.25874",
    "paper_url": "https://arxiv.org/abs/2611.25874",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "galgani-2026",
    "title": "Efficient and Robust Drafting with Multi-Token Prediction",
    "authors": [
      "Filippo Galgani",
      "Ziwei Ji",
      "Omri Homburger",
      "Ganesh Jawahar",
      "Michelle Ramanovich",
      "Ivan Korotkov",
      "Luciano Martins",
      "Utku Evci",
      "Edouard Yvinec",
      "Pooja Consul",
      "Vivek Kumar",
      "Tal Schuster"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.25813",
    "paper_url": "https://arxiv.org/abs/2611.25813",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "bhardwaj-2026",
    "title": "Can LLMs Resolve Entity Conflicts in Domain Specific NLU Pipelines?",
    "authors": [
      "Akansha Bhardwaj",
      "Mingbo Cui",
      "Victor Guimaraes",
      "Dominik Kohler",
      "Diana Nicoleta Popa",
      "Meghana M. Reddy",
      "Paolo Rosso"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.25733",
    "paper_url": "https://arxiv.org/abs/2611.25733",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "bolla-2026",
    "title": "Can an LLM Repair a Language Model in Weight Space Without Gradient Training?",
    "authors": [
      "Bharath Kumar Bolla",
      "Raghavender Surya Upadhayula",
      "Vishnu Surya Reddy Nandi",
      "Ramesh Nandipalli"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.25613",
    "paper_url": "https://arxiv.org/abs/2611.25613",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "ma-2026",
    "title": "NativeSeg: Native Vision Language Segmentation of 3D Computed Tomography via Spatial Visual Tokens and Verified Local Zoom",
    "authors": [
      "Chengqian Ma",
      "Gaole Dai",
      "Zijie Meng",
      "Weixuan Jin",
      "Yijie Du",
      "Yuexiao Ma",
      "Xiawu Zheng",
      "Fei Chao"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.24443",
    "paper_url": "https://arxiv.org/abs/2611.24443",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "kostin-2026",
    "title": "A Hybrid RAG Framework for Deceptive Review Detection: Integrating RoBERTa-LoRA, FAISS-Based Retrieval, and LLM Reasoning",
    "authors": [
      "Andrei Kostin",
      "José Ángel Diaz-Garcia",
      "Karel Gutiérrez-Batista"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.24049",
    "paper_url": "https://arxiv.org/abs/2611.24049",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "chen-2026",
    "title": "Same Rank, Different Needs: Rethinking LoRA Redistribution in Federated Learning",
    "authors": [
      "Jinqian Chen",
      "Jihua Zhu",
      "Chang Liu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.23742",
    "paper_url": "https://arxiv.org/abs/2611.23742",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "kuramshin-2026",
    "title": "Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need",
    "authors": [
      "Artur Kuramshin",
      "Charlotte Cloutier",
      "Michael Przystupa",
      "Kirsty Ellis",
      "Mohammad S. Akhter",
      "Glen Berseth"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.23676",
    "paper_url": "https://arxiv.org/abs/2611.23676",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "lopes-2026",
    "title": "LusoClin: A Synthetic Clinical Note Dataset for Medical Information Retrieval in European Portuguese",
    "authors": [
      "Carla Teixeira Lopes",
      "Daniel Félix"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.23454",
    "paper_url": "https://arxiv.org/abs/2611.23454",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "toks-z-2026",
    "title": "Fine-Tuning Gemma 4 Edge Models for MATLAB Signal-Processing Code with SFT and QLoRA on a Laptop iGPU",
    "authors": [
      "Mehmet Altan Toksöz"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.23205",
    "paper_url": "https://arxiv.org/abs/2611.23205",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "srivastava-2026",
    "title": "MoE--LoRA Methods for Multilingual Adaptation: A Systematic Empirical Study",
    "authors": [
      "Nikit Srivastava",
      "Joel Dag",
      "René Speck",
      "Axel-Cyrille Ngonga Ngomo"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.23158",
    "paper_url": "https://arxiv.org/abs/2611.23158",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "uribe-2026",
    "title": "Impact of Pretraining Length, Model Size, and Annotation Budget on Downstream Clinical Tasks of Foundation Models in Radiotherapy",
    "authors": [
      "Alejandro Cortina Uribe",
      "Sidsel Højklint Poulsen",
      "Ivan Richter Vogelius",
      "Jens Petersen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.22896",
    "paper_url": "https://arxiv.org/abs/2611.22896",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "kartika-2026",
    "title": "Efficient Self-Supervised Adaptation of 3D Abdominal Vision-Language Model for Institution-Specific HCC Classification via Full Fine-Tuning and PEFT",
    "authors": [
      "Febryan Putra Kartika",
      "Cheng-Yu Ma",
      "Ying-Jia Lin",
      "Chi-Tung Cheng",
      "Kuan-Fu Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.22504",
    "paper_url": "https://arxiv.org/abs/2611.22504",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "arora-2026",
    "title": "CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation",
    "authors": [
      "Mehul Arora",
      "Dhruv Agarwal",
      "Ambuj Agrawal"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.22395",
    "paper_url": "https://arxiv.org/abs/2611.22395",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "park-2026",
    "title": "BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning",
    "authors": [
      "Juyoung Park",
      "Heejun Lee"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.22334",
    "paper_url": "https://arxiv.org/abs/2611.22334",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "li-2026",
    "title": "SARVIA: Fast-Adapting the Strong SAR Foundation Models That Are Already in Your MLLMs",
    "authors": [
      "Yuxuan Li",
      "Zichen Tian",
      "Qianru Sun"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.22273",
    "paper_url": "https://arxiv.org/abs/2611.22273",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "shekhar-2026",
    "title": "Watermark Evidence under Open-Weight LLM Modification: Exact Bounds for Low-Rank Output Watermarks",
    "authors": [
      "Prashant Shekhar",
      "Dumindu Samaraweera",
      "Caroline Howard"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.21702",
    "paper_url": "https://arxiv.org/abs/2611.21702",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "lamb-2026",
    "title": "Tight PAC-Bayes Generalisation Guarantees for Large Language Model Judges",
    "authors": [
      "Tom A. Lamb",
      "Philip H. S. Torr",
      "Tim G. J. Rudner"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.20818",
    "paper_url": "https://arxiv.org/abs/2611.20818",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  },
  {
    "id": "suri-2026",
    "title": "Instant Weight-Space Consolidation for Long-Term Memory in LLMs",
    "authors": [
      "Manan Suri",
      "Dinesh Manocha"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2611.20759",
    "paper_url": "https://arxiv.org/abs/2611.20759",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-23"
  }
]
```
