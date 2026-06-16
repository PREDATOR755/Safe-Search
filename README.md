### By [Siyam Waheed] | Data Science enthusiast 

## 🛠️ Project: Safe-Search (Semantic Video Search)
**"Google for Surveillance Footage"**
* **Tech Stack:** Python, Streamlit, CLIP Embeddings, Vector Search.
* **What it does:** Allows users to search video footage using natural language (e.g., "Find a pink taxi"). It uses vector embeddings to "watch" and understand video frames semantically.
* **Key Feature:** Achieved <1 second retrieval time for object detection without pre-labeled data.
  ## 📊 Performance Benchmarks
To validate the system's reliability, I conducted a "Human-in-the-Loop" benchmark on a diverse set of 10 queries

**Test Environment:**
- **Model:** CLIP-ViT-B-32
- **Hardware:** [12th Gen Intel(R) Core(TM) i5-1235U (1.30 GHz)]
- **Dataset:** Raw CCTV Footage (1080p, 30fps)

**Results:**
| Query Category | Query Example | Avg Latency | Success Rate |
| :--- | :--- | :--- | :--- |
| **High Confidence** | "White car", "Traffic jam" | 0.32s | 100% |
| **Medium Complexity** | "People walking" | 0.35s | 80% |
| **Known Failure Cases** | "Red car" (<50px size) | 0.31s | 0% (See Limitations) |

============================================================
📊 REAL-WORLD PERFORMANCE REPORT
============================================================
| Query                |   Latency (s) |   Confidence | Human Verdict   |
|:---------------------|--------------:|-------------:|:----------------|
| A white car          |        0.5838 |        0.219 | ✅ PASS         |
| Traffic jam          |        0.031  |        0.255 | ✅ PASS         |
| A silver SUV         |        0.03   |        0.219 | ✅ PASS         |
| The bridge structure |        0.0312 |        0.234 | ✅ PASS         |
| A black van          |        0.0397 |        0.209 | ✅ PASS         |
| People walking       |        0.036  |        0.248 | ❌ FAIL         |
| A motorcycle         |        0.0314 |        0.234 | ✅ PASS         |
| Shadows on the road  |        0.034  |        0.223 | ✅ PASS         |
| A car turning right  |        0.0326 |        0.254 | ✅ PASS         |
| Red car              |        0.0345 |        0.225 | ❌ FAIL         |

🏆 Final Accuracy: 80.0%


> **Key Insight:** The system maintains sub-second latency (avg ~0.33s) suitable for real-time applications, though accuracy degrades on small objects due to resolution constraints.

---

## 🏗️ System Architecture
The system uses a hybrid retrieval pipeline to balance speed and semantic understanding.

![System Architecture]
<img width="889" height="146" alt="image" src="https://github.com/user-attachments/assets/cfce19d1-f1e5-4350-8775-af79b7f93f59" />


1.  **Ingestion:** Video is sampled at 1 FPS to reduce redundancy.
2.  **Embedding:** Frames are passed through **CLIP (ViT-B-32)** to generate 512-dimensional vectors.
3.  **Indexing:** Vectors are stored in a **FAISS** index (FlatL2) for valid similarity search.
4.  **Retrieval:** User text queries are converted to vectors and compared using Cosine Similarity.

---

## ⚠️ Limitations & Trade-offs
 Here are the current known limitations of this V1 prototype:

1.  **Small Object Detection:**
    * *Issue:* CLIP resizes input images to **224x224**. Small objects (like a red car in the distance) become less than 5 pixels wide, causing the model to miss them.
    * *Solution:* Future versions will implement **SAHI (Slicing Aided Hyper Inference)** to crop high-res tiles before embedding.

2.  **Temporal Blindness:**
    * *Issue:* The model embeds static frames, not video clips. It cannot distinguish between "A car turning right" and "A car driving straight."
    * *Solution:* Upgrade to **VideoMAE** or **X-CLIP** to capture temporal dynamics and motion vectors.




### 💻 How to Run
1. Clone the repo:
   `git clone https://github.com/PREDATOR755/ai-portfolio.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the apps:
   `streamlit run app.py`

   
   ## 💻 Technical Skills

## 💻 Technical Skills

| Domain | Technologies |
| :--- | :--- |
| **Languages** | Python, SQL, C++, Java |
| **Computer Vision & Embeddings** | CLIP (ViT), FAISS (Vector Indexing), OpenCV, Vector Search, Image Processing |
| **AI & NLP** | OpenAI API, LLMs, RAG, LangChain, ChromaDB |
| **Data Science & Analytics** | Pandas, NumPy, Scikit-Learn, Matplotlib, Plotly |
| **Deployment & Tools** | Streamlit, Git, PyArrow, GitHub Actions |

---

### 📫 Connect with Me
* [LinkedIn](https://www.linkedin.com/in/siyam-waheed)
* [Email](mailto:waheedsiyam315@gmail.com)
