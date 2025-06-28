import streamlit as st

st.set_page_config(
    page_title="📚 Personal Notes Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        .big-title {
            font-size: 2.6rem;
            font-weight: 800;
            color: #007acc;
            text-align: center;
            margin-top: 20px;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #444;
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="big-title">📚 Personal Notes Assistant</div>
<div class="subtitle">Smartly upload, summarize, and chat with your personal documents using AI</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
### 🚀 How to Use:
1. Go to **Document Insights** in the sidebar to upload and summarize your document.
2. Head over to **Notes Chatbot** to ask questions from your ingested notes.
""")
