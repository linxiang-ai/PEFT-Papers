# New arXiv PEFT papers — 2026-09-14

_Window: last 7 days. Queries:_
- `parameter-efficient fine-tuning`
- `LoRA fine-tuning`
- `adapter tuning`
- `prompt tuning large language model`
- `low-rank adaptation`

Total new (deduped against papers.json): **10**.

## Candidates

### DementiaCare-Bench: A Modality-Validated Video Benchmark
- **Authors**: Afrouz Sheikholeslami, Yuankai Qi, Xuyun Zhang, Luping Zhou, Amin Beheshti, Quan Z. Sheng, Ming-Hsuan Yang
- **arXiv**: [2609.12929](http://arxiv.org/abs/2609.12929v1)
- **Published**: 2026-09-11
- **Categories**: cs.CV, cs.MA

> Dementia affects an estimated 57 million people worldwide, and for most families the hardest part of care is not memory loss but the behavioral and psychological symptoms of dementia (BPSD): agitation, wandering, resistance to care, sundowning. Understanding these symptoms requires more than recogni...

### Partition-Invariant Tuning for 3D Scene Understanding
- **Authors**: Hongqiang Lin, Tianle Wang, Shuiwang Li, Dongxu Zhang, Yiding Sun, Zihao Guo, Dongfu Yin
- **arXiv**: [2609.12473](http://arxiv.org/abs/2609.12473v1)
- **Published**: 2026-09-11
- **Categories**: cs.CV

> Scene-level point cloud understanding remains challenging due to diverse geometries and spatial layouts. While pre-trained 3D point cloud foundation models (PFMs) offer strong transferability, full fine-tuning (FFT) incurs substantial computational and storage costs. Parameter-efficient fine-tuning ...

### Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models
- **Authors**: Gautam Rajendrakumar Gare, Siyi Li, Hewei Wang, Cesar Daniel Hernandez, Wei Zhao, Wolfgang M. Pauli, John Galeotti, Deva Ramanan
- **arXiv**: [2609.11310](http://arxiv.org/abs/2609.11310v1)
- **Published**: 2026-09-10
- **Categories**: cs.CV, cs.AI, cs.LG, eess.IV, stat.ML

> We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision. Existing adaptation methods are discrete prompt optimization and LoRA fine-tuning. We revisit a third op...

### Rebalancing Token Importance in Language Models with TF-IDF Weighted Cross-Entropy Loss
- **Authors**: Zhijian Li, Stefan Larson, Kevin Leach
- **arXiv**: [2609.11029](http://arxiv.org/abs/2609.11029v1)
- **Published**: 2026-09-10
- **Categories**: cs.CL, cs.LG

> Large language models are typically trained under uniform token weighting, which allows frequent and low-information tokens to dominate learning and can increase the tendency to memorize surface-level text spans. To address this, we present an information-weighted cross-entropy loss that rescales to...

### MetroLLM-Bench: Evaluating Language Models as Transit Kiosk Runtimes
- **Authors**: Remco Hendriks
- **arXiv**: [2609.10016](http://arxiv.org/abs/2609.10016v1)
- **Published**: 2026-09-09
- **Categories**: cs.LG, cs.AI, cs.CL

> We introduce MetroLLM-Bench, a 955-case benchmark for testing language models as the policy layer of a transit kiosk. It covers six real metro systems, ranging from 37 to 414 stations, and eleven categories that include routing, fare calculation, disruptions, accessibility, and adversarial input. In...

### 5-Dialects-BN: Unmasking the Impact of Transliteration on Bangla Dialectal LLMs
- **Authors**: Md Mahir Jawad, Galib Mahmud Jim, Rafid Ahmed, Mir Sazzat Hossain, Md Fahim, Md Farhad Alam Bhuiyan
- **arXiv**: [2609.09964](http://arxiv.org/abs/2609.09964v1)
- **Published**: 2026-09-09
- **Categories**: cs.CL

> Large Language Models (LLMs) have achieved remarkable progress across natural language processing (NLP) tasks, yet their capabilities degrade sharply for low-resource languages and dialectally diverse settings. Bangla, the world's sixth most spoken language, exemplifies this gap: existing resources ...

### Geometry-Aware Bayesian Parameter-Efficient Fine-Tuning on the Stiefel Manifold via Stein Variational Gradient Descent
- **Authors**: Quang-Duy Tran, Trung Le, Bao Duong, Phuoc Nguyen, Thin Nguyen
- **arXiv**: [2609.08354](http://arxiv.org/abs/2609.08354v1)
- **Published**: 2026-09-08
- **Categories**: cs.LG

> Several geometry-aware approaches to low-rank adaptation have emerged for parameter-efficient fine-tuning of large pre-trained models. These methods aim to take full advantage of the geometric structure of low-rank manifolds for improving the efficiency in subspace utilization and reducing redundanc...

### MI-PEFT: Mixture-of-Experts Integrated Parameter-Efficient Fine-Tuning Protein Language Models Improves Acidophilic Proteins Classification
- **Authors**: Honghan Shen
- **arXiv**: [2609.08059](http://arxiv.org/abs/2609.08059v1)
- **Published**: 2026-09-07
- **Categories**: q-bio.QM, cs.LG

> Acidophilic proteins that remain stable and functional under highly acidic conditions, are important for industrial biocatalysis, acid-related bioprocessing, and the discovery of acid-stable enzymes. However, their identification relies heavily on time-consuming experimental screening methods. With ...

### DroneGround: Open-Vocabulary Drone Payload Characterization Using Synthetic Data and Grounded Vision-Language Models
- **Authors**: Ami Pandat, Rajasekhar Punna, Gopika Vinod, Rohit Shukla
- **arXiv**: [2609.07780](http://arxiv.org/abs/2609.07780v1)
- **Published**: 2026-09-07
- **Categories**: cs.CV

> Automated drone surveillance has become increasingly important for public safety, critical infrastructure protection,and restricted airspace monitoring. While existing vision-based systems achieve strong performance for drone detection and tracking, reliable payload characterization remains highly c...

### DeepTable: Structural Attention Biases and Tree Path Encoding for Hierarchical Table Understanding
- **Authors**: Jyun-Ying Yen, Cheng-Kuan Lin, Yu-Chee Tseng
- **arXiv**: [2609.07707](http://arxiv.org/abs/2609.07707v1)
- **Published**: 2026-09-07
- **Categories**: cs.CL

> Large language models (LLMs) have demonstrated strong performance in table understanding. However, they typically process table content and headers as linearized token sequences. This representation weakens the two-dimensional and hierarchical structural relationships encoded by multi-level row and ...

---

## Suggested papers.json entries (DRAFT — review before merging)

```json
[
  {
    "id": "sheikholeslami-2026",
    "title": "DementiaCare-Bench: A Modality-Validated Video Benchmark",
    "authors": [
      "Afrouz Sheikholeslami",
      "Yuankai Qi",
      "Xuyun Zhang",
      "Luping Zhou",
      "Amin Beheshti",
      "Quan Z. Sheng",
      "Ming-Hsuan Yang"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.12929",
    "paper_url": "https://arxiv.org/abs/2609.12929",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-09-14"
  },
  {
    "id": "lin-2026",
    "title": "Partition-Invariant Tuning for 3D Scene Understanding",
    "authors": [
      "Hongqiang Lin",
      "Tianle Wang",
      "Shuiwang Li",
      "Dongxu Zhang",
      "Yiding Sun",
      "Zihao Guo",
      "Dongfu Yin"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.12473",
    "paper_url": "https://arxiv.org/abs/2609.12473",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-09-14"
  },
  {
    "id": "gare-2026",
    "title": "Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models",
    "authors": [
      "Gautam Rajendrakumar Gare",
      "Siyi Li",
      "Hewei Wang",
      "Cesar Daniel Hernandez",
      "Wei Zhao",
      "Wolfgang M. Pauli",
      "John Galeotti",
      "Deva Ramanan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.11310",
    "paper_url": "https://arxiv.org/abs/2609.11310",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-09-14"
  },
  {
    "id": "li-2026",
    "title": "Rebalancing Token Importance in Language Models with TF-IDF Weighted Cross-Entropy Loss",
    "authors": [
      "Zhijian Li",
      "Stefan Larson",
      "Kevin Leach"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.11029",
    "paper_url": "https://arxiv.org/abs/2609.11029",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-09-14"
  },
  {
    "id": "hendriks-2026",
    "title": "MetroLLM-Bench: Evaluating Language Models as Transit Kiosk Runtimes",
    "authors": [
      "Remco Hendriks"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.10016",
    "paper_url": "https://arxiv.org/abs/2609.10016",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-09-14"
  },
  {
    "id": "jawad-2026",
    "title": "5-Dialects-BN: Unmasking the Impact of Transliteration on Bangla Dialectal LLMs",
    "authors": [
      "Md Mahir Jawad",
      "Galib Mahmud Jim",
      "Rafid Ahmed",
      "Mir Sazzat Hossain",
      "Md Fahim",
      "Md Farhad Alam Bhuiyan"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.09964",
    "paper_url": "https://arxiv.org/abs/2609.09964",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-09-14"
  },
  {
    "id": "tran-2026",
    "title": "Geometry-Aware Bayesian Parameter-Efficient Fine-Tuning on the Stiefel Manifold via Stein Variational Gradient Descent",
    "authors": [
      "Quang-Duy Tran",
      "Trung Le",
      "Bao Duong",
      "Phuoc Nguyen",
      "Thin Nguyen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.08354",
    "paper_url": "https://arxiv.org/abs/2609.08354",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-09-14"
  },
  {
    "id": "shen-2026",
    "title": "MI-PEFT: Mixture-of-Experts Integrated Parameter-Efficient Fine-Tuning Protein Language Models Improves Acidophilic Proteins Classification",
    "authors": [
      "Honghan Shen"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.08059",
    "paper_url": "https://arxiv.org/abs/2609.08059",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-09-14"
  },
  {
    "id": "pandat-2026",
    "title": "DroneGround: Open-Vocabulary Drone Payload Characterization Using Synthetic Data and Grounded Vision-Language Models",
    "authors": [
      "Ami Pandat",
      "Rajasekhar Punna",
      "Gopika Vinod",
      "Rohit Shukla"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.07780",
    "paper_url": "https://arxiv.org/abs/2609.07780",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-09-14"
  },
  {
    "id": "yen-2026",
    "title": "DeepTable: Structural Attention Biases and Tree Path Encoding for Hierarchical Table Understanding",
    "authors": [
      "Jyun-Ying Yen",
      "Cheng-Kuan Lin",
      "Yu-Chee Tseng"
    ],
    "venue": "arXiv",
    "year": 2026,
    "arxiv": "2609.07707",
    "paper_url": "https://arxiv.org/abs/2609.07707",
    "code_url": null,
    "category": [
      "other"
    ],
    "domain": [
      "nlp"
    ],
    "backbone": [],
    "key_idea": "TODO: one-sentence summary",
    "trainable_params_ratio": "",
    "open_source": "none",
    "tags": [
      "new"
    ],
    "added_date": "2026-09-14"
  }
]
```
