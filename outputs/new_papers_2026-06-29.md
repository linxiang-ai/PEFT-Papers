# New arXiv PEFT papers — 2026-06-29

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **22**.

## Candidates

### Parameter Efficient Hybrid Transformer (PEHT) for Network Traffic Prediction via Dynamic Urban Congestion Integration
- **Authors**: Abdolazim Rezaei, Mehdi Sookhak, Mahboobeh Haghparast
- **arXiv**: [2606.28274](http://arxiv.org/abs/2606.28274v1)
- **Published**: 2026-06-26
- **Categories**: cs.LG, cs.AI

> Accurate network traffic prediction is a critical element for efficient resource allocation in dynamic urban cellular networks. However, prediction remains challenging because network demand is influenced by complex mobility patterns, congestion dynamics, and heterogeneous user behavior. This paper ...

### Monocular Avatar Reconstruction via Cascaded Diffusion Priors and UV-Space Differentiable Shading
- **Authors**: Hong Li, Minqi Meng, Yanjun Liang, Chongjie Ye, Houyuan Chen, Weiqing Xiao, Xianda Guo, Guojun Lei, Xuhui Liu, Chaojie Yang, Yanlun Peng, Hao Zhao, Baochang Zhang
- **arXiv**: [2606.28144](http://arxiv.org/abs/2606.28144v1)
- **Published**: 2026-06-26
- **Categories**: cs.CV

> Reconstructing high-fidelity, relightable 3D avatars from a single in-the-wild image is a challenging ill-posed problem, primarily hindered by the scarcity of high-quality PBR data and the complexity of disentangling illumination from intrinsic materials. In this paper, we present a data-efficient f...

### When One Adapter Speaks for Many: Discovering Low-Rank Redundancy in Continual Fine-Tuning
- **Authors**: Tanguy Dieudonné, Giulia Lanzillotta, Enis Simsar, Louis Barinka, Thomas Hofmann
- **arXiv**: [2606.28117](http://arxiv.org/abs/2606.28117v1)
- **Published**: 2026-06-26
- **Categories**: cs.LG

> Low-Rank Adaptation (LoRA) has become the standard tool for parameter-efficient fine-tuning of large pretrained models. When applied sequentially across tasks in Continual Learning (CL), the standard assumption is that each new task requires a dedicated low-rank adapter. In this work, we challenge t...

### Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA
- **Authors**: Sambaran Bandyopadhyay
- **arXiv**: [2606.28050](http://arxiv.org/abs/2606.28050v1)
- **Published**: 2026-06-26
- **Categories**: cs.CL, cs.AI

> LLM-as-a-Judge and self-evaluation pipelines implicitly assume that evaluation is easier than generation. We test this in a controlled in-context QA setting where a context passage is the sole information source and each model judges the answer it generated, removing the parametric-knowledge confoun...

### OrthoTryOn: Geometric Orthogonalization for Conflict-Free Unified Fashion Generation
- **Authors**: Zhaotong Yang, Ying Tai, Jiahui Zhan, Yu Zheng, Jianjun Qian, Jian Yang
- **arXiv**: [2606.27880](http://arxiv.org/abs/2606.27880v1)
- **Published**: 2026-06-26
- **Categories**: cs.CV

> Unified fashion generation integrates tasks like virtual try-on and garment reconstruction into a single model to reduce task-specific adaptation costs. However, naive parameter sharing across semantically distinct tasks induces negative transfer through severe inter-task gradient conflict. We propo...

### Fine-tuning a multimodal large language model for clinician-grade autism behavioral scoring from short home videos
- **Authors**: Mohammadmahdi Honarmand, Parnian Azizian, Aaron Kline, Kae Nurge, Zerin Nasrin Tumpa, Saimourya Surabhi, Kaitlyn Dunlap, Yang Qian, Ali Kargarandehkordi, Sameer Neupane, Peter Washington, Dennis P. Wall
- **arXiv**: [2606.27484](http://arxiv.org/abs/2606.27484v1)
- **Published**: 2026-06-25
- **Categories**: cs.CV

> Autism spectrum disorder (ASD) affects 1 in 31 US children, yet median age at diagnosis exceeds four years. Artificial intelligence pipelines that provide quantified diagnosis using easy to access observational data (e.g., home videos) could help with earlier diagnosis, and timely delivery of early ...

### RoPEMover: Depth-Aware Object Relocation via Positional Embeddings
- **Authors**: Ipek Oztas, Duygu Ceylan, Aybars Bugra Aksoy, Aysegul Dundar
- **arXiv**: [2606.27332](http://arxiv.org/abs/2606.27332v1)
- **Published**: 2026-06-25
- **Categories**: cs.CV

> Moving an object in a single image requires geometry-consistent spatial rearrangement, including handling occlusions, revealing previously unseen regions, and maintaining coherent shadows and reflections. Existing approaches are not well suited to this setting and often fail to preserve such scene-l...

### Escaping Iterative Parameter-Space Noise: Differentially Private Learning with a Hypernetwork
- **Authors**: Naoki Nishikawa, Shokichi Takakura, Satoshi Hasegawa
- **arXiv**: [2606.26772](http://arxiv.org/abs/2606.26772v1)
- **Published**: 2026-06-25
- **Categories**: cs.LG, stat.ML

> Differentially private (DP) training of neural networks is often hindered by the large amount of noise required by gradient-based methods such as DP-SGD, which repeatedly inject high-dimensional noise in parameter space throughout training. In this paper, we propose a new framework for DP learning t...

### DeCoFlow: Structural Decomposition of Normalizing Flows for Continual Anomaly Detection
- **Authors**: Hun Im, Jungi Lee, Subeen Cha, Pilsung Kang
- **arXiv**: [2606.26687](http://arxiv.org/abs/2606.26687v1)
- **Published**: 2026-06-25
- **Categories**: cs.CV

> In industrial environments, new product categories arrive sequentially, requiring continual anomaly detection without access to past data. Normalizing Flows (NFs) provide exact density estimation but suffer from catastrophic forgetting as parameter updates across tasks distort the density manifold. ...

### Closing the Quality Gap in Low-Resource Text-to-Speech: LoRA Fine-Tuning of VoxCPM2 for Khmer and Korean
- **Authors**: Phannet Pov, Sovandara Chhoun, Hyun Woo Park, Wan-Sup Cho, Saksonita Khoeurn
- **arXiv**: [2606.26618](http://arxiv.org/abs/2606.26618v1)
- **Published**: 2026-06-25
- **Categories**: cs.CL

> Large pretrained text-to-speech (TTS) models sound almost human for well-resourced languages, but much worse for languages that are rare in their training data. We study this quality gap for Khmer and Korean using VoxCPM2, a 2.4B-parameter, tokenizer-free TTS model that joins a MiniCPM-4 language-mo...

### Layer-Specific Prompt Fusion Discovery via Differentiable Search in Vision Foundation Models
- **Authors**: Xi Xiao, Xingjian Li, Yunbei Zhang, Cheng Han, Tianming Liu, Tianyang Wang, Runmin Jiang, Jihun Hamm, Xiao Wang, Min Xu
- **arXiv**: [2606.26379](http://arxiv.org/abs/2606.26379v1)
- **Published**: 2026-06-24
- **Categories**: cs.CV

> Visual prompt tuning has emerged as a parameter-efficient fine-tuning approach for adapting large-scale Vision Transformers (ViTs) to downstream tasks. As its learnable prompts are applied in input and feature spaces, prior to jointly going through attention in transformer layers, the most commonly ...

### SSM Adapters via Hankel Reduced-order Modeling: Injection Site Determines Task Suitability in Long-Context Fine-Tuning
- **Authors**: Omanshu Thapliyal
- **arXiv**: [2606.26290](http://arxiv.org/abs/2606.26290v1)
- **Published**: 2026-06-24
- **Categories**: cs.LG, cs.AI

> While parameter-efficient fine-tuning (PEFT) typically targets attention projectors, its efficacy for tasks requiring sequential state accumulation remains under-explored. We examine if PEFT for such tasks can benefit from state space model (SSMs) adapters, and if MLP blocks are better injection sit...

### LiMoDE: Rethinking Lifelong Robot Manipulation from a Mixture-of-Dynamic-Experts Perspective
- **Authors**: Zhihao Gu, Lin Wang
- **arXiv**: [2606.26183](http://arxiv.org/abs/2606.26183v1)
- **Published**: 2026-06-24
- **Categories**: cs.RO, cs.AI, cs.LG

> Building a generalist robot that can leverage prior knowledge for continuous task adaptation remains a significant challenge. Previous works alleviate the catastrophic forgetting problem by parameter-efficient fine-tuning for single-task adaptation. However, they fail to extract reusable skills and ...

### Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning
- **Authors**: Samuel Valland Lyngset, Tor Viljen Raanaas, Gard Sveipe, Eirik Møller Nilsen, Jim Torresen, Kai Olav Ellefsen, Tobias Lømo
- **arXiv**: [2606.25700](http://arxiv.org/abs/2606.25700v1)
- **Published**: 2026-06-24
- **Categories**: cs.LG, cs.RO

> When fine-tuning Large Language Models (LLMs), there has been success in minimizing both memory usage and computation with Parameter-Efficient Fine-Tuning (PEFT), like Low Rank Adaptation (LoRA). In this article, we have explored whether this approach is transferable to the world of robotics and Rei...

### Cross-Attention Multimodal Learning for Predicting Response to Neoadjuvant Imatinib in Gastrointestinal Stromal Tumors: A Multicenter Retrospective Study
- **Authors**: Fariba Tohidinezhad, Douwe J. Spaanderman, Natalia Oviedo Acosta, Kaouther Mouheb, Karthik Prathaban, David F. Hanff, Dirk J. Grünhagen, Cornelis Verhoef, Joris M. van Sabben, Evelyne Roets, Jette J. Slettenhaar, Hans Gelderblom, Ingrid M. E. Desar, Anna K. L. Reyners, Neeltje Steeghs, Stefan Klein, Martijn P. A. Starmans
- **arXiv**: [2606.25579](http://arxiv.org/abs/2606.25579v1)
- **Published**: 2026-06-24
- **Categories**: eess.IV, cs.CV

> Background: Response to neoadjuvant imatinib in gastrointestinal stromal tumors (GISTs) is highly variable and cannot be reliably predicted using current clinical or molecular markers. This study developed and evaluated an explainable multimodal deep learning framework integrating computed tomograph...

### Dream at SemEval-2026 Task 13: SALSA for Single-Pass Machine-Generated Code Detection
- **Authors**: Ruslan Berdichevsky, Shai Nahum-Gefen, Elad Ben-Zaken
- **arXiv**: [2606.25102](http://arxiv.org/abs/2606.25102v1)
- **Published**: 2026-06-23
- **Categories**: cs.CL

> Large language models have transformed code generation, raising concerns around authorship, assessment integrity, and software trust. SemEval-2026 Task 13 Subtask A operationalizes detection as binary classification over code snippets, with a particular emphasis on out-of-distribution (OOD) generali...

### Ill-Posed by Design: Probing Evidence Use in VLMs
- **Authors**: Boaz Meivar, Shaked Perek, Shani Shvartzman, Eli Schwartz, Shai Avidan
- **arXiv**: [2606.24335](http://arxiv.org/abs/2606.24335v1)
- **Published**: 2026-06-23
- **Categories**: cs.CV

> Counterfactual analysis is widely used to study evidence use in vision-language models, but its diagnostic value is limited on well-posed tasks: when several cues independently support the same answer, removing one may not change the prediction. We propose monocular metric object-size estimation as ...

### Tri-Efficient Transfer Learning for Point Cloud Videos
- **Authors**: Yiding Sun, Dongxu Zhang, Jihua Zhu, Haozhe Cheng, Zhengqiao Li, Pengcheng Li, Chaowei Fang, Yonghao Dong, Lin Chen
- **arXiv**: [2606.24175](http://arxiv.org/abs/2606.24175v1)
- **Published**: 2026-06-23
- **Categories**: cs.CV

> While point cloud foundation models have significantly advanced point cloud video understanding, existing parameter-efficient fine-tuning (PEFT) methods still suffer from two critical limitations: prohibitive annotation costs for large-scale point cloud datasets and severe memory bottlenecks. In thi...

### CADRE: Stable, Parameter Efficient Adaptation of Medical Vision Language Models with Bounded Forgetting and Prior Drift
- **Authors**: Amrita Singh, Rishabh Jha
- **arXiv**: [2606.23487](http://arxiv.org/abs/2606.23487v1)
- **Published**: 2026-06-22
- **Categories**: cs.AI

> Medical vision-language models (VLMs) such as BiomedCLIP generalize broadly, but adapting them to a clinical service is as much a safety problem as an accuracy one. Updating a deployed model for a new imaging modality can fail silently in two ways that harm patients: it can forget modalities it alre...

### ScalingAttention: Discovering Intrinsic Sparse Attention Topology for Video Diffusion Transformers
- **Authors**: Ruiliang Zhou, Xuecheng Wu, Kang He, Guangyun Han, Bin Liu, Qinqin Chen, Wende Xu, Qingjie Zhao, Chengru Song
- **arXiv**: [2606.23019](http://arxiv.org/abs/2606.23019v1)
- **Published**: 2026-06-22
- **Categories**: cs.CV, cs.AI

> While Diffusion Transformers (DiTs) have revolutionized high-fidelity video generation, their reliance on 3D full attention creates a quadratic computational bottleneck. Existing sparse methods face a dilemma: dynamic pruning suffers from prohibitive runtime overhead and memory fragmentation, while ...

### Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Evolving Agentic Retrieval
- **Authors**: Wangding Xia, Ye Du, Jiashi Lin, Meng Wang, Danli Shi, Shujun Wang
- **arXiv**: [2606.22955](http://arxiv.org/abs/2606.22955v1)
- **Published**: 2026-06-22
- **Categories**: cs.CV

> Large-scale pretrained foundation models have revolutionized general medical screening, but often falter on rare diseases because such conditions are underrepresented in real-world clinical datasets. While retrieval-augmented diagnosis attempts to mitigate this, conventional static methods frequentl...

### Priority-Aware Learning-Unlearning Correction for Dynamic Decentralized LoRA Fine-Tuning
- **Authors**: Nuocheng Yang, Yechen He, Sihua Wang, Zihan Chen, Tony Q. S. Quek, Changchuan Yin
- **arXiv**: [2606.22878](http://arxiv.org/abs/2606.22878v1)
- **Published**: 2026-06-22
- **Categories**: cs.LG, cs.AI

> As large language models (LLMs) are increasingly deployed at the network edge to provide pervasive generative AI services, decentralized federated learning (DFL) provides a vital mechanism for privacy-preserving, domain-specific fine-tuning through peer-to-peer exchanges of parameter-efficient updat...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "rezaei-2026",
    "title": "Parameter Efficient Hybrid Transformer (PEHT) for Network Traffic Prediction via Dynamic Urban Congestion Integration",
    "authors": [
      "Abdolazim Rezaei",
      "Mehdi Sookhak",
      "Mahboobeh Haghparast"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.28274",
    "paper_url": "https://arxiv.org/abs/2606.28274",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "li-2026",
    "title": "Monocular Avatar Reconstruction via Cascaded Diffusion Priors and UV-Space Differentiable Shading",
    "authors": [
      "Hong Li",
      "Minqi Meng",
      "Yanjun Liang",
      "Chongjie Ye",
      "Houyuan Chen",
      "Weiqing Xiao",
      "Xianda Guo",
      "Guojun Lei",
      "Xuhui Liu",
      "Chaojie Yang",
      "Yanlun Peng",
      "Hao Zhao",
      "Baochang Zhang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.28144",
    "paper_url": "https://arxiv.org/abs/2606.28144",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "dieudonn-2026",
    "title": "When One Adapter Speaks for Many: Discovering Low-Rank Redundancy in Continual Fine-Tuning",
    "authors": [
      "Tanguy Dieudonné",
      "Giulia Lanzillotta",
      "Enis Simsar",
      "Louis Barinka",
      "Thomas Hofmann"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.28117",
    "paper_url": "https://arxiv.org/abs/2606.28117",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "bandyopadhyay-2026",
    "title": "Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA",
    "authors": [
      "Sambaran Bandyopadhyay"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.28050",
    "paper_url": "https://arxiv.org/abs/2606.28050",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "yang-2026",
    "title": "OrthoTryOn: Geometric Orthogonalization for Conflict-Free Unified Fashion Generation",
    "authors": [
      "Zhaotong Yang",
      "Ying Tai",
      "Jiahui Zhan",
      "Yu Zheng",
      "Jianjun Qian",
      "Jian Yang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.27880",
    "paper_url": "https://arxiv.org/abs/2606.27880",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "honarmand-2026",
    "title": "Fine-tuning a multimodal large language model for clinician-grade autism behavioral scoring from short home videos",
    "authors": [
      "Mohammadmahdi Honarmand",
      "Parnian Azizian",
      "Aaron Kline",
      "Kae Nurge",
      "Zerin Nasrin Tumpa",
      "Saimourya Surabhi",
      "Kaitlyn Dunlap",
      "Yang Qian",
      "Ali Kargarandehkordi",
      "Sameer Neupane",
      "Peter Washington",
      "Dennis P. Wall"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.27484",
    "paper_url": "https://arxiv.org/abs/2606.27484",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "oztas-2026",
    "title": "RoPEMover: Depth-Aware Object Relocation via Positional Embeddings",
    "authors": [
      "Ipek Oztas",
      "Duygu Ceylan",
      "Aybars Bugra Aksoy",
      "Aysegul Dundar"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.27332",
    "paper_url": "https://arxiv.org/abs/2606.27332",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "nishikawa-2026",
    "title": "Escaping Iterative Parameter-Space Noise: Differentially Private Learning with a Hypernetwork",
    "authors": [
      "Naoki Nishikawa",
      "Shokichi Takakura",
      "Satoshi Hasegawa"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.26772",
    "paper_url": "https://arxiv.org/abs/2606.26772",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "im-2026",
    "title": "DeCoFlow: Structural Decomposition of Normalizing Flows for Continual Anomaly Detection",
    "authors": [
      "Hun Im",
      "Jungi Lee",
      "Subeen Cha",
      "Pilsung Kang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.26687",
    "paper_url": "https://arxiv.org/abs/2606.26687",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "pov-2026",
    "title": "Closing the Quality Gap in Low-Resource Text-to-Speech: LoRA Fine-Tuning of VoxCPM2 for Khmer and Korean",
    "authors": [
      "Phannet Pov",
      "Sovandara Chhoun",
      "Hyun Woo Park",
      "Wan-Sup Cho",
      "Saksonita Khoeurn"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.26618",
    "paper_url": "https://arxiv.org/abs/2606.26618",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "xiao-2026",
    "title": "Layer-Specific Prompt Fusion Discovery via Differentiable Search in Vision Foundation Models",
    "authors": [
      "Xi Xiao",
      "Xingjian Li",
      "Yunbei Zhang",
      "Cheng Han",
      "Tianming Liu",
      "Tianyang Wang",
      "Runmin Jiang",
      "Jihun Hamm",
      "Xiao Wang",
      "Min Xu"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.26379",
    "paper_url": "https://arxiv.org/abs/2606.26379",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "thapliyal-2026",
    "title": "SSM Adapters via Hankel Reduced-order Modeling: Injection Site Determines Task Suitability in Long-Context Fine-Tuning",
    "authors": [
      "Omanshu Thapliyal"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.26290",
    "paper_url": "https://arxiv.org/abs/2606.26290",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "gu-2026",
    "title": "LiMoDE: Rethinking Lifelong Robot Manipulation from a Mixture-of-Dynamic-Experts Perspective",
    "authors": [
      "Zhihao Gu",
      "Lin Wang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.26183",
    "paper_url": "https://arxiv.org/abs/2606.26183",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "lyngset-2026",
    "title": "Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning",
    "authors": [
      "Samuel Valland Lyngset",
      "Tor Viljen Raanaas",
      "Gard Sveipe",
      "Eirik Møller Nilsen",
      "Jim Torresen",
      "Kai Olav Ellefsen",
      "Tobias Lømo"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.25700",
    "paper_url": "https://arxiv.org/abs/2606.25700",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "tohidinezhad-2026",
    "title": "Cross-Attention Multimodal Learning for Predicting Response to Neoadjuvant Imatinib in Gastrointestinal Stromal Tumors: A Multicenter Retrospective Study",
    "authors": [
      "Fariba Tohidinezhad",
      "Douwe J. Spaanderman",
      "Natalia Oviedo Acosta",
      "Kaouther Mouheb",
      "Karthik Prathaban",
      "David F. Hanff",
      "Dirk J. Grünhagen",
      "Cornelis Verhoef",
      "Joris M. van Sabben",
      "Evelyne Roets",
      "Jette J. Slettenhaar",
      "Hans Gelderblom",
      "Ingrid M. E. Desar",
      "Anna K. L. Reyners",
      "Neeltje Steeghs",
      "Stefan Klein",
      "Martijn P. A. Starmans"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.25579",
    "paper_url": "https://arxiv.org/abs/2606.25579",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "berdichevsky-2026",
    "title": "Dream at SemEval-2026 Task 13: SALSA for Single-Pass Machine-Generated Code Detection",
    "authors": [
      "Ruslan Berdichevsky",
      "Shai Nahum-Gefen",
      "Elad Ben-Zaken"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.25102",
    "paper_url": "https://arxiv.org/abs/2606.25102",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "meivar-2026",
    "title": "Ill-Posed by Design: Probing Evidence Use in VLMs",
    "authors": [
      "Boaz Meivar",
      "Shaked Perek",
      "Shani Shvartzman",
      "Eli Schwartz",
      "Shai Avidan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.24335",
    "paper_url": "https://arxiv.org/abs/2606.24335",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "sun-2026",
    "title": "Tri-Efficient Transfer Learning for Point Cloud Videos",
    "authors": [
      "Yiding Sun",
      "Dongxu Zhang",
      "Jihua Zhu",
      "Haozhe Cheng",
      "Zhengqiao Li",
      "Pengcheng Li",
      "Chaowei Fang",
      "Yonghao Dong",
      "Lin Chen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.24175",
    "paper_url": "https://arxiv.org/abs/2606.24175",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "singh-2026",
    "title": "CADRE: Stable, Parameter Efficient Adaptation of Medical Vision Language Models with Bounded Forgetting and Prior Drift",
    "authors": [
      "Amrita Singh",
      "Rishabh Jha"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.23487",
    "paper_url": "https://arxiv.org/abs/2606.23487",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "zhou-2026",
    "title": "ScalingAttention: Discovering Intrinsic Sparse Attention Topology for Video Diffusion Transformers",
    "authors": [
      "Ruiliang Zhou",
      "Xuecheng Wu",
      "Kang He",
      "Guangyun Han",
      "Bin Liu",
      "Qinqin Chen",
      "Wende Xu",
      "Qingjie Zhao",
      "Chengru Song"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.23019",
    "paper_url": "https://arxiv.org/abs/2606.23019",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "xia-2026",
    "title": "Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Evolving Agentic Retrieval",
    "authors": [
      "Wangding Xia",
      "Ye Du",
      "Jiashi Lin",
      "Meng Wang",
      "Danli Shi",
      "Shujun Wang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.22955",
    "paper_url": "https://arxiv.org/abs/2606.22955",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  },
  {
    "id": "yang-2026",
    "title": "Priority-Aware Learning-Unlearning Correction for Dynamic Decentralized LoRA Fine-Tuning",
    "authors": [
      "Nuocheng Yang",
      "Yechen He",
      "Sihua Wang",
      "Zihan Chen",
      "Tony Q. S. Quek",
      "Changchuan Yin"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2606.22878",
    "paper_url": "https://arxiv.org/abs/2606.22878",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-06-29"
  }
]
```
