# pages/2_Notes_Chatbot.py
import streamlit as st
from genai_services import answer_with_context
from chroma_services import query_documents

st.set_page_config(page_title="💬 Notes Chatbot", layout="wide")

st.markdown("""
    <style>
        .chat-title {
            font-size: 2rem;
            font-weight: bold;
            color: #007acc;
            margin-top: 10px;
        }
        .context-box {
            background-color: #f3f9ff;
            border-left: 4px solid #007acc;
            padding: 1rem;
            border-radius: 6px;
            font-size: 0.95rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='chat-title'>💬 Notes Chatbot</div>", unsafe_allow_html=True)
st.write("Ask intelligent questions from your uploaded notes below.")

if not st.session_state.get("doc_uploaded"):
    st.warning("⚠️ No document has been uploaded and ingested yet. Please go to 'Note Analyzer' and upload your notes first.")
else:
    user_input = st.chat_input("Type your question about your notes...")

    if user_input:
        st.chat_message("user").markdown(user_input)

        with st.spinner("🔍 Searching your notes and generating answer..."):
            context_chunks = query_documents(user_input, n_results=3)
            answer = answer_with_context(user_input, context_chunks)

        st.chat_message("assistant").markdown(answer)

        with st.expander("📎 Show Retrieved Context"):
            for i, chunk in enumerate(context_chunks):
                st.markdown(f"<div class='context-box'><strong>Chunk {i+1}:</strong><br>{chunk}</div>", unsafe_allow_html=True)
