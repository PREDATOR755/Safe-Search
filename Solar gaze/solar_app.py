import streamlit as st
from PIL import Image
import cv2
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="Solar-Gaze", page_icon="☀️", layout="wide")

# Custom CSS for the "Financial Terminal" look
st.markdown("""
    <style>
        /* Main Background - Keep it Dark for contrast */
        .stApp { background-color: #FFF8E1; }
        
        /* Main Titles - Gold */
        h1 { color: #FFD700; font-family: 'Helvetica Neue', sans-serif; font-weight: bold; }
        
        /* The Metric Cards - WHITE Background */
        .metric-card { 
            background-color: #FFFFFF; /* Pure White */
            padding: 25px; 
            border-radius: 12px; 
            border: 1px solid #e6e6e6; 
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1); 
            margin-bottom: 20px;
        }
        
        /* Force text inside cards to be DARK so it shows up on white */
        .metric-card p { color: #333333 !important; font-weight: 500; }
        .metric-card h1 { color: #000000 !important; } /* Make the big numbers Black (or keep colored if preferred) */
        
        /* You can keep the sub-headers colored */
        .metric-card h3 { opacity: 1.0; } 
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: CONTROLS ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/869/869869.png", width=50)
    st.title("Solar-Gaze Controls")
    
    st.header("⚡ Financial Parameters")
    # Interactive Sliders (This is the "Analytics" part)
    elec_rate = st.slider("Electricity Cost (PKR/unit)", min_value=30, max_value=80, value=55)
    panel_effic = st.slider("Panel Efficiency (%)", min_value=15, max_value=25, value=20)
    install_cost = st.slider("Installation Cost (PKR/kW)", min_value=100000, max_value=200000, value=150000)

# --- MAIN PAGE ---
st.title("🛰️ Satellite Solar Potential Mapper")
st.markdown("Automated Rooftop Segmentation & Yield Analysis • **Sector F-7/Blue Area**")

col1, col2 = st.columns([2, 1])

# --- COLUMN 1: THE VISUALS ---
with col1:
    # Load the images
    # NOTE: Ensure these files exist in your folder!
    original = Image.open("satellite_input.png")
    analyzed = Image.open("solar_analysis_output.jpg")
    
    # Image Slider to compare Before/After
    tab1, tab2 = st.tabs(["🔍 Analysis View", "🌍 Raw Satellite"])
    with tab1:
        st.image(analyzed, caption="AI Detected Rooftops (Green)", use_container_width=True)
    with tab2:
        st.image(original, caption="Original Input", use_container_width=True)

# --- COLUMN 2: THE BUSINESS LOGIC ---
with col2:
    st.subheader("📊 ROI Calculator")
    
    # HARDCODED DATA from your Terminal Analysis (The number you just got)
    DETECTED_AREA_SQFT = 599300  # Use the number from your terminal output!
    SOLAR_POTENTIAL_KW = 8989    # Use the number from your terminal output!
    
    # DYNAMIC CALCULATIONS (Updates as you move sliders)
    daily_production = SOLAR_POTENTIAL_KW * 5 # Approx 5 sun hours
    monthly_units = daily_production * 30
    monthly_savings = monthly_units * elec_rate
    total_investment = SOLAR_POTENTIAL_KW * install_cost
    break_even_months = total_investment / monthly_savings if monthly_savings > 0 else 0
    break_even_years = break_even_months / 12

    # DISPLAY METRICS
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="color:#00FF99">Estimated Potential</h3>
        <h1>{SOLAR_POTENTIAL_KW:,} kW</h1>
        <p>Based on {DETECTED_AREA_SQFT:,} sqft of viable roof area</p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="color:#FFD700">Projected Monthly Savings</h3>
        <h1>PKR {int(monthly_savings):,}</h1>
        <p>@ {elec_rate} PKR/unit</p>
    </div>
    <br>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-card">
        <h3 style="color:#FF4B4B">Break-Even Period</h3>
        <h1>{break_even_years:.1f} Years</h1>
        <p>Total Investment: PKR {total_investment/1000000:.1f} Million</p>
    </div>
    """, unsafe_allow_html=True)