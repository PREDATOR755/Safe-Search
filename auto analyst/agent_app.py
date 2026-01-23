import streamlit as st
import pandas as pd
import os
from groq import Groq
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="Auto-Analyst Agent", page_icon="🤖", layout="wide")

# Custom CSS for the "Terminal" aesthetic
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stTextInput > div > div > input { background-color: #262730; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: CONFIG ---
with st.sidebar:
    st.title("🤖 Agent Config")
    api_key = st.text_input("Enter Groq API Key:", type="password")
    st.caption("Get one for free at console.groq.com")
    
    st.markdown("---")
    st.markdown("### 📂 Data Source")
    # Load the file we generated earlier
    try:
        df = pd.read_csv("global_tech_sales.csv")
        st.success("✅ global_tech_sales.csv loaded")
        st.dataframe(df.head(3), hide_index=True)
    except:
        st.error("❌ CSV file not found! Run generate_data.py first.")
        st.stop()

# --- MAIN APP ---
st.title("📊 Auto-Analyst: The Code-Writing Agent")
st.markdown("Ask a question, and I will **write and execute Python code** to answer it.")

# 1. The User Query
query = st.text_input("Ask the Agent:", placeholder="e.g., Plot the total sales per region as a bar chart")

# 2. The Agent Logic
if query and api_key:
    client = Groq(api_key=api_key)
    
    # 3. Construct the Prompt (The "Brain" Instructions)
    # We give the AI the column names so it knows how to write the code.
    columns = list(df.columns)
    prompt = f"""
    You are a Python Data Science Agent. You have a pandas DataFrame named 'df'.
    Columns: {columns}
    
    User Request: "{query}"
    
    YOUR GOAL: Write Python code to visualize or calculate the answer.
    
    RULES:
    1. Use 'matplotlib.pyplot' as plt.
    2. If plotting, use specific colors (cyan, magenta, yellow) for a dark theme.
    3. Do NOT show the plot (plt.show()). Just create it.
    4. Return ONLY the python code. No explanations. No markdown backticks.
    """
    
    with st.spinner("🤖 Writing Python code..."):
        try:
            # Call Llama 3
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile", # Fast & Free model
            )
            
            # Extract Code
            code = chat_completion.choices[0].message.content
            
            # Clean up the code (remove markdown ` ```python ` if the AI added it)
            code = code.replace("```python", "").replace("```", "").strip()
            
            # Show the user the code (Transparency)
            with st.expander("👁️ View Generated Code", expanded=False):
                st.code(code, language='python')
            
            # 4. EXECUTION (The Dangerous/Magical Part)
            # We create a local environment where 'df' and 'plt' exist
            local_vars = {"df": df, "plt": plt}
            exec(code, {}, local_vars)
            
            # 5. Display Result
            st.pyplot(plt)
            plt.clf() # Clear memory
            
        except Exception as e:
            st.error(f"💥 Agent Failed: {e}")
            st.warning("Try re-phrasing your prompt!")

elif query and not api_key:
    st.warning("⚠️ Please enter your Groq API Key in the sidebar.")