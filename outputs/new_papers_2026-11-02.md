# New arXiv PEFT papers — 2026-11-02

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **24**.

## Candidates

### IGDA-ICMH: an Importance Guided Feature and Network Dual Adaptation Framework towards Image Compression for Machine and Human Vision
- **Authors**: Yanbo Gao, Xinyu Zhao, Shuai Li, Xun Cai, Mao Ye, Li Li
- **arXiv**: [2610.41924](http://arxiv.org/abs/2610.41924v1)
- **Published**: 2026-10-30
- **Categories**: eess.IV, cs.CV

> With the surge of machine vision applications, image compression for both machine and human vision (ICMH) has become an important research area. Existing studies mainly focus on task-specific adaptation or multi-task joint optimization, yet they often overlook the unequal contributions of different ...

### Advancing Clinical Trial Outcome Prediction with Domain-Specific Large Language Models
- **Authors**: Burak Bakkar, Hana Moalla, Mohamed Salem Jedidi, Haifa Ben Messaoud, Nicolas Lopez Carranza
- **arXiv**: [2610.41710](http://arxiv.org/abs/2610.41710v1)
- **Published**: 2026-10-30
- **Categories**: cs.AI

> Clinical trial failures are a major barrier to efficient drug development, incurring substantial costs and delaying patient access to effective therapies. Structured approaches such as the Hierarchical Interaction Network (HINT) predict trial outcomes by explicitly modelling interactions between dru...

### Breaking Information Islands in Sparse Tuning via Small-World Connectivity
- **Authors**: Xianchao Guan, Zijun Xiong, Yifeng Wang, Yubo Cui, Yaowei Wang, Guo-Sen Xie, Xin Li, Zheng Zhang
- **arXiv**: [2610.41665](http://arxiv.org/abs/2610.41665v1)
- **Published**: 2026-10-30
- **Categories**: cs.AI

> Sparse tuning is widely used to adapt large language models due to its parameter efficiency. However, its effectiveness depends not only on the number of trainable parameters, but also on the feature-interaction topology of the sparse update's structural support. Limited or uneven connectivity in th...

### Parameter-Efficient Fine-Tuning of Transformer Encoders for Audio-Image-Symbolic Music Retrieval
- **Authors**: Eliseo Fuentes-Martinez, Antonio Hidalgo-Centeno, Jorge Calvo-Zaragoza, Antonio Javier Gallego
- **arXiv**: [2610.41512](http://arxiv.org/abs/2610.41512v1)
- **Published**: 2026-10-30
- **Categories**: cs.CV, cs.SD, eess.AS

> Score-based multimodal music retrieval requires representations that are both discriminative within each modality and compatible across audio recordings, sheet music images, and symbolic scores. This paper investigates the effectiveness of parameter-efficient fine-tuning (PEFT) for adapting pretrain...

### KV-Cache Patching: Tracing How and Where Fine-Tuned Behaviors Arise
- **Authors**: Jonas Loos, Oliver Eberle
- **arXiv**: [2610.41480](http://arxiv.org/abs/2610.41480v1)
- **Published**: 2026-10-30
- **Categories**: cs.CL, cs.LG

> Fine-tuning a language model changes how it responds, but where is this fine-tuned behavior instantiated? To better understand this, we evaluate whether the change in model behavior arises only during the generation of the answer tokens where the change manifests, or whether altered processing of pr...

### How to Loop Your Transformer: Loop Scaling, Specialization, and Parallel Inference
- **Authors**: Chanakya Ekbote, Artidoro Pagnoni, Devendra Singh Sachan, Shruti Bhosale, Mike Lewis, Maryam Fazel-Zarandi, Shashank Rajput, Sujan Kumar Gonugondla
- **arXiv**: [2610.40325](http://arxiv.org/abs/2610.40325v1)
- **Published**: 2026-10-29
- **Categories**: cs.LG, cs.AI

> Looping in transformer models reuses weights by repeatedly applying the same transformer, or parts of it, making the model deeper without increasing its parameter count. Whether looping is useful depends on which constraint dominates: model size, training compute, or autoregressive inference efficie...

### Upcycling Language Models for Multiple Specialized Domains
- **Authors**: Mingzi Cao, Xi Wang, Nikolaos Aletras
- **arXiv**: [2610.40091](http://arxiv.org/abs/2610.40091v1)
- **Published**: 2026-10-29
- **Categories**: cs.CL, cs.AI

> Effective multi-domain adaptation of large language models requires prioritizing relevant domain knowledge while minimizing interference from irrelevant domains. Existing approaches commonly use Low-Rank Adaptation (LoRA) to train a separate adapter for each domain and combine these adapters within ...

### Intrinsic Distribution Matching
- **Authors**: Deyuan Liu, Yansen Han, Kaiwen Zheng, Jun Xie, Jiacheng Liu, Zhenglin Cheng, Peng Sun, Jintao Zhang, Jianguo Li, Tao Lin
- **arXiv**: [2610.39633](http://arxiv.org/abs/2610.39633v1)
- **Published**: 2026-10-29
- **Categories**: cs.CV, cs.AI

> One-step and few-step text-to-image generation must accurately render the details specified in the prompt despite limited opportunities for refinement. Distribution matching distillation (DMD) uses score differences to bring the generated distribution closer to a reference distribution. Following pr...

### Sparse Fine-Tuning for Parameter-Efficient Adversarial Training
- **Authors**: Zhaoxin Wang, Zihang Ding, Handing Wang
- **arXiv**: [2610.39455](http://arxiv.org/abs/2610.39455v1)
- **Published**: 2026-10-29
- **Categories**: cs.LG, cs.AI

> Deep neural networks achieve strong performance across many tasks but remain vulnerable to adversarial perturbations. Adversarial training (AT) is one of the most effective defenses, yet it suffers from high memory cost on large models and the persistent clean-robust accuracy trade-off. Recent work ...

### Structure-retained low-rank adapters for weather synthesis
- **Authors**: Shunxin Wang, Alexandros Stergiou, Luuk Spreeuwers, Estefania Talavera, Nicola Strisciuglio
- **arXiv**: [2610.38413](http://arxiv.org/abs/2610.38413v1)
- **Published**: 2026-10-28
- **Categories**: cs.CV

> Real-world deployment of computer vision models, particularly in outdoor scenarios, is often limited by environmental interferences, such as adverse weather. Improving model robustness across weather conditions is thus critical for reliability. However, sourcing high-quality data relevant to isolate...

### Predicting What Answer Engines Cite: Open Decision Models, Rerankers and a Distilled 4B Student on Ten Engines under Controlled Retrieval
- **Authors**: Elisha Bajemon, Andre-Louis Rochet
- **arXiv**: [2610.38090](http://arxiv.org/abs/2610.38090v1)
- **Published**: 2026-10-28
- **Categories**: cs.IR, cs.AI

> Generative engine optimization needs a scorer that ranks candidate pages by the share of an answer they will receive as citations. We measure pretrained rerankers, a hosted typed decision model (Jev), eight open decision models and distilled students on GEO-Bench queries answered by ten engines that...

### Preserving Safety During Sequential Fine-Tuning: A Factorial and Geometric Analysis of Replay
- **Authors**: George Ruellan, Diana Benavides-Prado
- **arXiv**: [2610.38001](http://arxiv.org/abs/2610.38001v1)
- **Published**: 2026-10-27
- **Categories**: cs.LG

> Benign fine-tuning can erode safety alignment in large language models, and sequential adaptation substantially compounds this risk. Prior work mitigates this erosion by replaying harmful-prompt refusals and benign-compliance examples, while other work instead matches base-model logits via distillat...

### QMUL_AK at AISA-ArabicFC: Schema-Constrained Function Calling with ALLaM
- **Authors**: Ali Khairallah, Arkaitz Zubiaga
- **arXiv**: [2610.37995](http://arxiv.org/abs/2610.37995v1)
- **Published**: 2026-10-27
- **Categories**: cs.CL

> We describe the QMUL_AK submission to AISA-ArabicFC 2026. The system adapts the Arabic-English ALLaM-7B-Instruct model to function calling with low-rank adaptation (LoRA). It combines an Arabic schema-aware prompt, dialect and no-call resampling, a token-weighted training objective, and deterministi...

### Bi-Phase Training: Learning Efficiently From Scratch
- **Authors**: Abel Gurung, Joseph Campbell
- **arXiv**: [2610.37934](http://arxiv.org/abs/2610.37934v1)
- **Published**: 2026-10-27
- **Categories**: cs.LG

> Pre-training foundational models is computationally expensive as models scale. In this work, we introduce Bi-Phase Training (BPT), a parameter-efficient pre-training method that preserves the high-rank learning dynamics observed in full-parameter optimization with substantially reduced trainable par...

### A note on data-efficient finetuning of vision foundation models
- **Authors**: Niclas Hergenröther, Antonio Orvieto
- **arXiv**: [2610.37510](http://arxiv.org/abs/2610.37510v1)
- **Published**: 2026-10-27
- **Categories**: cs.CV, cs.LG

> Adapting foundation models to a new task within or beyond the training domain is the de facto standard for building specialized machine learning models. Recently, Visual Prompting (VP) has emerged as a promising technique for efficient knowledge transfer. As new foundation model families~(like Mamba...

### SimplexLoRA: Dynamic Rank Updating via Alternating Minimization with Simplex Projection
- **Authors**: Igor Shalygin, Grigorii Davydenko, Andrey Veprikov, Aleksey Antonov, Nikolay Bushkov, Stanislav Moiseev, Aleksandr Beznosikov
- **arXiv**: [2610.37206](http://arxiv.org/abs/2610.37206v1)
- **Published**: 2026-10-27
- **Categories**: cs.LG

> The success of large language models in real-world applications relies on parameter-efficient fine-tuning methods such as Low-Rank Adaptation (LoRA), which inserts compact, trainable adapters into selected layers. In this paper, we propose SimplexLoRA, a LoRA variant that adaptively adjusts adapter ...

### Hierarchical Low-Rank Reparameterization for Parameter-Efficient Fine-Tuning
- **Authors**: Rong Huang, Yi Xiong, Yuan-Yuan Cheng, Xiao-Ming Fu
- **arXiv**: [2610.37068](http://arxiv.org/abs/2610.37068v1)
- **Published**: 2026-10-27
- **Categories**: cs.CL

> Parameter-efficient fine-tuning (PEFT) methods adapt large models by introducing a small number of trainable parameters. However, we find that these parameters still contain redundancy and can be further compressed while maintaining strong task performance. To this end, we propose a novel hierarchic...

### Provenance Signatures for Low Rank Adaptations of Image Diffusion Models
- **Authors**: Tobias Cheung, Mohan Dantam, Marc Juarez, Rik Sarkar
- **arXiv**: [2610.36933](http://arxiv.org/abs/2610.36933v1)
- **Published**: 2026-10-27
- **Categories**: cs.LG

> Diffusion models have revolutionized the generation of realistic artificial images. Efficient techniques such as Low Rank Adaptation (LoRA) can modify these models for particular use cases, making them more diverse and widely usable. At the same time, open base models may be adapted to deliver biase...

### LoRA on a Budget: Function-Aware Post-Hoc Compression for Adapter Fleets
- **Authors**: Shenghui Li, Thiemo voigt
- **arXiv**: [2610.36386](http://arxiv.org/abs/2610.36386v1)
- **Published**: 2026-10-26
- **Categories**: cs.AI

> Low-Rank Adaptation (LoRA) has become a key mechanism for efficiently specializing foundation models into many task- and user-specific variants. Serving many LoRA adapters under a shared resource budget turns post-hoc compression into a two-level allocation problem: rank must be distributed across l...

### HiFiPix: Bringing High-Fidelity Real-World Super-Resolution Back to Pixel Space
- **Authors**: Wenjie Li, Du Chen, Hui Wang, Linlong Fan, Youwei Lv, Zeyi Chen, Zehan Chen, Jinwei Chen, Heng Guo, Zhanyu Ma, Qingnan Fan
- **arXiv**: [2610.35515](http://arxiv.org/abs/2610.35515v1)
- **Published**: 2026-10-26
- **Categories**: cs.CV

> Diffusion-based real-world image super-resolution suffers from limited reconstruction fidelity due to information loss in VAE-based latent representations. Recently, pixel-space diffusion models offer a promising high-faithfulness alternative by avoiding latent compression, but adapting them to Real...

### Prior Predictive Matching for Bayesian LoRA
- **Authors**: Tomasz Kuśmierczyk, Eliezer de Souza da Silva, Marcin Sendera
- **arXiv**: [2610.35457](http://arxiv.org/abs/2610.35457v1)
- **Published**: 2026-10-26
- **Categories**: cs.LG, stat.ML

> Bayesian variants of Low-Rank Adaptation (LoRA) provide principled uncertainty estimation when fine-tuning large foundation models, but require specifying the prior over the low-rank weight updates. We address this hyperparameter selection problem by introducing a closed-form prior-predictive estima...

### Synthetic Child-Adult Interactions Are Not Developmentally Plausible
- **Authors**: Bastian Bunzeck, Francesca Padovani
- **arXiv**: [2610.35029](http://arxiv.org/abs/2610.35029v1)
- **Published**: 2026-10-26
- **Categories**: cs.CL

> Synthetic data has become a common resource for training language models, and this trend has spilled over into research on developmentally plausible language modeling. However, it remains unclear whether LM-generated child-adult interactions actually resemble natural ones. We compare the synthetic T...

### DocTalk: Enhancing Medical Knowledge Retrieval via Fine-tuned Large Language Models with Chain-of-Thought Reasoning for Robust Clinical Decision Support
- **Authors**: Asad Gohar, Md Ariful Islam Mozumder, Moon-Il Joo, Hee-Cheol Kim
- **arXiv**: [2610.34871](http://arxiv.org/abs/2610.34871v1)
- **Published**: 2026-10-26
- **Categories**: cs.AI, cs.CL, cs.CV

> Objective: The rapid advancement of large language models (LLMs) in healthcare has opened new possibilities for AI-assisted clinical decision-making; however, safe and effective deployment remains challenging because of hallucination and domain misalignment. This study introduces DocTalk, a doctor-a...

### Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching
- **Authors**: Fei Zuo, Yizhou Huang, Kezhi Wang
- **arXiv**: [2610.34756](http://arxiv.org/abs/2610.34756v1)
- **Published**: 2026-10-26
- **Categories**: cs.LG, cs.CL

> Low-Rank Adaptation (LoRA) has emerged as the dominant paradigm for parameter-efficient fine-tuning of large language models. Standard all-layer LoRA applies adaptation throughout the transformer, despite heterogeneous contributions from its components. In this work, we conduct a systematic mechanis...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "gao-2026",
    "title": "IGDA-ICMH: an Importance Guided Feature and Network Dual Adaptation Framework towards Image Compression for Machine and Human Vision",
    "authors": [
      "Yanbo Gao",
      "Xinyu Zhao",
      "Shuai Li",
      "Xun Cai",
      "Mao Ye",
      "Li Li"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.41924",
    "paper_url": "https://arxiv.org/abs/2610.41924",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "bakkar-2026",
    "title": "Advancing Clinical Trial Outcome Prediction with Domain-Specific Large Language Models",
    "authors": [
      "Burak Bakkar",
      "Hana Moalla",
      "Mohamed Salem Jedidi",
      "Haifa Ben Messaoud",
      "Nicolas Lopez Carranza"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.41710",
    "paper_url": "https://arxiv.org/abs/2610.41710",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "guan-2026",
    "title": "Breaking Information Islands in Sparse Tuning via Small-World Connectivity",
    "authors": [
      "Xianchao Guan",
      "Zijun Xiong",
      "Yifeng Wang",
      "Yubo Cui",
      "Yaowei Wang",
      "Guo-Sen Xie",
      "Xin Li",
      "Zheng Zhang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.41665",
    "paper_url": "https://arxiv.org/abs/2610.41665",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "fuentes-martinez-2026",
    "title": "Parameter-Efficient Fine-Tuning of Transformer Encoders for Audio-Image-Symbolic Music Retrieval",
    "authors": [
      "Eliseo Fuentes-Martinez",
      "Antonio Hidalgo-Centeno",
      "Jorge Calvo-Zaragoza",
      "Antonio Javier Gallego"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.41512",
    "paper_url": "https://arxiv.org/abs/2610.41512",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "loos-2026",
    "title": "KV-Cache Patching: Tracing How and Where Fine-Tuned Behaviors Arise",
    "authors": [
      "Jonas Loos",
      "Oliver Eberle"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.41480",
    "paper_url": "https://arxiv.org/abs/2610.41480",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "ekbote-2026",
    "title": "How to Loop Your Transformer: Loop Scaling, Specialization, and Parallel Inference",
    "authors": [
      "Chanakya Ekbote",
      "Artidoro Pagnoni",
      "Devendra Singh Sachan",
      "Shruti Bhosale",
      "Mike Lewis",
      "Maryam Fazel-Zarandi",
      "Shashank Rajput",
      "Sujan Kumar Gonugondla"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.40325",
    "paper_url": "https://arxiv.org/abs/2610.40325",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "cao-2026",
    "title": "Upcycling Language Models for Multiple Specialized Domains",
    "authors": [
      "Mingzi Cao",
      "Xi Wang",
      "Nikolaos Aletras"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.40091",
    "paper_url": "https://arxiv.org/abs/2610.40091",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "liu-2026",
    "title": "Intrinsic Distribution Matching",
    "authors": [
      "Deyuan Liu",
      "Yansen Han",
      "Kaiwen Zheng",
      "Jun Xie",
      "Jiacheng Liu",
      "Zhenglin Cheng",
      "Peng Sun",
      "Jintao Zhang",
      "Jianguo Li",
      "Tao Lin"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.39633",
    "paper_url": "https://arxiv.org/abs/2610.39633",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "wang-2026",
    "title": "Sparse Fine-Tuning for Parameter-Efficient Adversarial Training",
    "authors": [
      "Zhaoxin Wang",
      "Zihang Ding",
      "Handing Wang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.39455",
    "paper_url": "https://arxiv.org/abs/2610.39455",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "wang-2026",
    "title": "Structure-retained low-rank adapters for weather synthesis",
    "authors": [
      "Shunxin Wang",
      "Alexandros Stergiou",
      "Luuk Spreeuwers",
      "Estefania Talavera",
      "Nicola Strisciuglio"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.38413",
    "paper_url": "https://arxiv.org/abs/2610.38413",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "bajemon-2026",
    "title": "Predicting What Answer Engines Cite: Open Decision Models, Rerankers and a Distilled 4B Student on Ten Engines under Controlled Retrieval",
    "authors": [
      "Elisha Bajemon",
      "Andre-Louis Rochet"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.38090",
    "paper_url": "https://arxiv.org/abs/2610.38090",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "ruellan-2026",
    "title": "Preserving Safety During Sequential Fine-Tuning: A Factorial and Geometric Analysis of Replay",
    "authors": [
      "George Ruellan",
      "Diana Benavides-Prado"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.38001",
    "paper_url": "https://arxiv.org/abs/2610.38001",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "khairallah-2026",
    "title": "QMUL_AK at AISA-ArabicFC: Schema-Constrained Function Calling with ALLaM",
    "authors": [
      "Ali Khairallah",
      "Arkaitz Zubiaga"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.37995",
    "paper_url": "https://arxiv.org/abs/2610.37995",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "gurung-2026",
    "title": "Bi-Phase Training: Learning Efficiently From Scratch",
    "authors": [
      "Abel Gurung",
      "Joseph Campbell"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.37934",
    "paper_url": "https://arxiv.org/abs/2610.37934",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "hergenr-ther-2026",
    "title": "A note on data-efficient finetuning of vision foundation models",
    "authors": [
      "Niclas Hergenröther",
      "Antonio Orvieto"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.37510",
    "paper_url": "https://arxiv.org/abs/2610.37510",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "shalygin-2026",
    "title": "SimplexLoRA: Dynamic Rank Updating via Alternating Minimization with Simplex Projection",
    "authors": [
      "Igor Shalygin",
      "Grigorii Davydenko",
      "Andrey Veprikov",
      "Aleksey Antonov",
      "Nikolay Bushkov",
      "Stanislav Moiseev",
      "Aleksandr Beznosikov"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.37206",
    "paper_url": "https://arxiv.org/abs/2610.37206",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "huang-2026",
    "title": "Hierarchical Low-Rank Reparameterization for Parameter-Efficient Fine-Tuning",
    "authors": [
      "Rong Huang",
      "Yi Xiong",
      "Yuan-Yuan Cheng",
      "Xiao-Ming Fu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.37068",
    "paper_url": "https://arxiv.org/abs/2610.37068",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "cheung-2026",
    "title": "Provenance Signatures for Low Rank Adaptations of Image Diffusion Models",
    "authors": [
      "Tobias Cheung",
      "Mohan Dantam",
      "Marc Juarez",
      "Rik Sarkar"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.36933",
    "paper_url": "https://arxiv.org/abs/2610.36933",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "li-2026",
    "title": "LoRA on a Budget: Function-Aware Post-Hoc Compression for Adapter Fleets",
    "authors": [
      "Shenghui Li",
      "Thiemo voigt"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.36386",
    "paper_url": "https://arxiv.org/abs/2610.36386",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "li-2026",
    "title": "HiFiPix: Bringing High-Fidelity Real-World Super-Resolution Back to Pixel Space",
    "authors": [
      "Wenjie Li",
      "Du Chen",
      "Hui Wang",
      "Linlong Fan",
      "Youwei Lv",
      "Zeyi Chen",
      "Zehan Chen",
      "Jinwei Chen",
      "Heng Guo",
      "Zhanyu Ma",
      "Qingnan Fan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.35515",
    "paper_url": "https://arxiv.org/abs/2610.35515",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "ku-mierczyk-2026",
    "title": "Prior Predictive Matching for Bayesian LoRA",
    "authors": [
      "Tomasz Kuśmierczyk",
      "Eliezer de Souza da Silva",
      "Marcin Sendera"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.35457",
    "paper_url": "https://arxiv.org/abs/2610.35457",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "bunzeck-2026",
    "title": "Synthetic Child-Adult Interactions Are Not Developmentally Plausible",
    "authors": [
      "Bastian Bunzeck",
      "Francesca Padovani"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.35029",
    "paper_url": "https://arxiv.org/abs/2610.35029",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "gohar-2026",
    "title": "DocTalk: Enhancing Medical Knowledge Retrieval via Fine-tuned Large Language Models with Chain-of-Thought Reasoning for Robust Clinical Decision Support",
    "authors": [
      "Asad Gohar",
      "Md Ariful Islam Mozumder",
      "Moon-Il Joo",
      "Hee-Cheol Kim"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.34871",
    "paper_url": "https://arxiv.org/abs/2610.34871",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  },
  {
    "id": "zuo-2026",
    "title": "Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching",
    "authors": [
      "Fei Zuo",
      "Yizhou Huang",
      "Kezhi Wang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2610.34756",
    "paper_url": "https://arxiv.org/abs/2610.34756",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-11-02"
  }
]
```
