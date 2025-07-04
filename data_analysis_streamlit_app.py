import os
import streamlit as st

# Set environment variables
os.environ["STREAMLIT_SERVER_MAX_UPLOAD_SIZE"] = "2000"
os.environ["OPENAI_API_KEY"] = "sk-proj-7it5V-..."  # Consider using secrets instead

# Set Streamlit page config
st.set_page_config(layout="wide", page_title="Main Dashboard", page_icon="📊")

# Main page content
st.title("📊 Main Dashboard")
st.write("Welcome to the Agentic Data Analysis Dashboard!")

st.info("Use the sidebar to navigate to the Visualisation Agent or other tools.")
