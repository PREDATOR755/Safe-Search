# 🚀 AI Engineering Portfolio
### By [Siyam Waheed] | Data Science enthusiast 

A collection of advanced AI tools demonstrating **Computer Vision**, **Geospatial Intelligence**, and **Agentic Workflows**.

---

## 🛠️ Project 1: Search-Light (Semantic Video Search)
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

## 🛰️ Project 2: Solar-Gaze (AI-Powered Solar ROI)
**"Business Intelligence for Renewable Energy"**
<img width="1887" height="896" alt="{FBE37E6F-3469-4EA3-8932-E6AE6BB100F3}" src="https://github.com/user-attachments/assets/dff26422-030e-4585-9cd2-721bf726eaf9" />

* **Tech Stack:** OpenCV (Computer Vision), Folium, Streamlit, NumPy, PyArrow.
* **What it does:** A hybrid intelligence dashboard that combines satellite imagery with financial modeling. It allows users to analyze specific sectors of Islamabad (e.g., F-7, Blue Area) and uses **Computer Vision** to estimate usable rooftop surface area from satellite snapshots. It then calculates potential solar energy yield and financial ROI in real-time based on 2026 NEPRA tariffs.

### 🚀 Key Features
* **Automated Segmentation:** Uses HSV color masking (OpenCV) to mathematically distinguish concrete rooftops from vegetation in user-uploaded satellite images.
* **Dynamic ROI Engine:** Instantly calculates Payback Period and Annual Savings as users adjust system size via interactive sliders.
* **Geospatial Navigation:** Integrated `folium` maps for high-resolution satellite inspection of residential and commercial zones.
* **Real-Time Financials:** Pre-configured with Islamabad's average irradiance (5.2 kWh/m²/day) and current electricity rates (65 PKR/unit) for accurate forecasting.

### ⚠️ Limitations & Roadmap
* **Human-in-the-Loop Segmentation:** The current V1 uses a semi-automated workflow where the user must take a screenshot of the map and upload it for analysis.
    * *Roadmap:* Integrate **Google Solar API** or **Mask R-CNN** to auto-detect roof boundaries directly on the live map without manual uploading.
* **Satellite Resolution:** Utilizes free Esri World Imagery, which limits zoom clarity for small residential roofs.
    * *Roadmap:* Acquire commercial satellite tiles (Maxar/Airbus) for sub-meter precision.
* **Color-Based Masking:** The HSV masking algorithm relies on color contrast (Green vs. Grey). It may struggle with grey roads looking like roofs or green roofs looking like trees.
    * *Roadmap:* Upgrade to a Deep Learning Semantic Segmentation model (U-Net) for context-aware detection.

## 🤖 Project 3: Auto-Analyst (Agentic Data Scientist)
**"Self-Coding AI Agent"**
* **Tech Stack:** Groq API (Llama 3), Pandas, Matplotlib, Python Exec().
* **What it does:** An autonomous agent that accepts raw datasets and executes its own Python code to generate visualizations and insights.
* **Key Feature:** Implements a "Code-Execution Sandbox" allowing the AI to debug and run its own scripts.

---

### 💻 How to Run
1. Clone the repo:
   `git clone https://github.com/PREDATOR755/ai-portfolio.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the apps:
   `streamlit run Project_3_auto analyst/agent_app.py`
