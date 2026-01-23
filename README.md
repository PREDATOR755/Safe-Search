# 🚀 AI Engineering Portfolio
### By [Siyam Waheed] | Data Science enthusiast 

A collection of advanced AI tools demonstrating **Computer Vision**, **Geospatial Intelligence**, and **Agentic Workflows**.

---

## 🛠️ Project 1: Search-Light (Semantic Video Search)
**"Google for Surveillance Footage"**
* **Tech Stack:** Python, Streamlit, CLIP Embeddings, Vector Search.
* **What it does:** Allows users to search video footage using natural language (e.g., "Find a pink taxi"). It uses vector embeddings to "watch" and understand video frames semantically.
* **Key Feature:** Achieved <1 second retrieval time for object detection without pre-labeled data.

## 🛰️ Project 2: Solar-Gaze (Satellite ROI Analyzer)
**"Business Intelligence for Renewable Energy"**
* **Tech Stack:** OpenCV (Computer Vision), Folium, Streamlit.
* **What it does:** Analyzes satellite imagery of Islamabad to detect rooftop surface area automatically. It calculates potential solar energy yield and financial ROI in real-time.
* **Key Feature:** Automated segmentation of concrete vs. vegetation using HSV color masking.

## 🤖 Project 3: Auto-Analyst (Agentic Data Scientist)
**"Self-Coding AI Agent"**
* **Tech Stack:** Groq API (Llama 3), Pandas, Matplotlib, Python Exec().
* **What it does:** An autonomous agent that accepts raw datasets and executes its own Python code to generate visualizations and insights.
* **Key Feature:** Implements a "Code-Execution Sandbox" allowing the AI to debug and run its own scripts.

---

### 💻 How to Run
1. Clone the repo:
   `git clone https://github.com/[PREDATOR755]/ai-portfolio.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the apps:
   `streamlit run Project_3_Auto_Analyst/agent_app.py`