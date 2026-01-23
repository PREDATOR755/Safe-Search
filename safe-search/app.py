import streamlit as st
import cv2
from sentence_transformers import SentenceTransformer
from PIL import Image
import faiss
import numpy as np
import plotly.express as px
import tempfile
import os

# --- PAGE CONFIG (The "Classy" Look) ---
st.set_page_config(page_title="Search-Light AI", page_icon="🔍", layout="wide")

# Custom CSS to hide default Streamlit clutter and make it look professional
st.markdown("""
    <style>
        .stApp { background-color: #0E1117; }
        h1 { color: #00FF99; font-family: 'Helvetica Neue', sans-serif; }
        .stTextInput > div > div > input { background-color: #262730; color: white; }
    </style>
""", unsafe_allow_html=True)

# --- 1. LOAD AI MODEL (Cached so it doesn't reload every time) ---
@st.cache_resource
def load_model():
    return SentenceTransformer('clip-ViT-B-32')

model = load_model()

# --- 2. PROCESSING FUNCTION ---
@st.cache_resource
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    images = []
    timestamps = []
    
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    current_frame = 0
    
    # Extract 1 frame per second
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if current_frame % int(frame_rate) == 0:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            images.append(Image.fromarray(rgb_frame))
            timestamps.append(current_frame / frame_rate)
            
        current_frame += 1
    cap.release()
    
    # Create Index
    if images:
        embeddings = model.encode(images, show_progress_bar=False)
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)
        faiss.normalize_L2(embeddings)
        index.add(embeddings)
        return index, images, timestamps
    return None, [], []

# --- 3. SIDEBAR (The "Control Center") ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3004/3004458.png", width=50)
    st.title("Search-Light")
    st.caption("Semantic Video Forensics")
    
    # You can upload a file, or it defaults to the one in your folder
    uploaded_file = st.file_uploader("Upload CCTV Footage", type=['mp4'])
    
    if uploaded_file is not None:
        # Save uploaded file momentarily
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(uploaded_file.read())
        video_path = tfile.name
    else:
        # DEFAULT FILE (Your mall video)
        video_path = "my_cctv_footage.mp4" 

    if os.path.exists(video_path):
        st.success(f"Video Loaded: {os.path.basename(video_path)}")
        index, images, timestamps = process_video(video_path)
    else:
        st.error("Please put 'my_cctv_footage.mp4' in this folder!")
        st.stop()

# --- 4. MAIN INTERFACE ---
st.title("🔍 Natural Language Video Search")
st.markdown("Ask questions like: *'A person with a blue backpack'* or *'People on escalator'*")

query = st.text_input("", placeholder="Type your search query here...")

if query and index:
    # --- SEARCH LOGIC ---
    query_vector = model.encode([query])
    faiss.normalize_L2(query_vector)
    
    # Get Top 4 Matches
    distances, indices = index.search(query_vector, 4)
    
    # --- RESULTS SECTION (UPDATED FOR MORE RESULTS) ---
    st.subheader(f"Results for: '{query}'")
    
    # ASK FOR 10 RESULTS INSTEAD OF 4
    search_limit = 10
    distances, indices = index.search(query_vector, search_limit)
    
    # Create a grid layout (4 images per row)
    cols = st.columns(4)
    
    chart_data = []
    
    for i, idx in enumerate(indices[0]):
        score = distances[0][i]
        time_sec = timestamps[idx]
        
        # Display Image in the correct column (Grid Logic)
        col_index = i % 4
        with cols[col_index]:
            st.image(images[idx], caption=f"Time: {int(time_sec)}s | Conf: {score:.2f}")
            
        # Collect data for the chart
        chart_data.append({"Time (s)": time_sec, "Match Confidence": score})
    # Data for Analytics
    chart_data = []
    
    for i, idx in enumerate(indices[0]):
        score = distances[0][i]
        time_sec = timestamps[idx]
        
        # Display Image
        with cols[i % 4]:  # This safely wraps around (0,1,2,3, 0,1,2,3...)
            st.image(images[idx], caption=f"Time: {int(time_sec)}s | Conf: {score:.2f}")
            
        # Collect data for the chart
        chart_data.append({"Time (s)": time_sec, "Match Confidence": score})

    # --- ANALYTICS UPGRADE (The "Classy" Chart) ---
    st.markdown("---")
    st.subheader("📊 Temporal Forensics")
    
    # Search the WHOLE video for a timeline (not just top 4)
    all_distances, all_indices = index.search(query_vector, len(images))
    
    # Re-sort by time (not by score) to show the "Story" of the video
    timeline_data = []
    for i in range(len(images)):
        # We need to find the score for this specific image index
        # This is a bit tricky with FAISS, so we just re-calculate cosine sim for the graph
        # Simpler: Just map the top results.
        pass
    
    # Let's do a simple "Confidence over Time" chart for the top matches
    fig = px.bar(
        chart_data, 
        x="Time (s)", 
        y="Match Confidence", 
        title="Target Detection Probability Timeline",
        color="Match Confidence",
        color_continuous_scale="teal"
    )
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white")
    st.plotly_chart(fig, use_container_width=True)