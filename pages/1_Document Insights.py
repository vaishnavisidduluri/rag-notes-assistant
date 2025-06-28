# pages/1_Document_Insights.py
import streamlit as st
from markitdown import MarkItDown
from genai_services import summarize_text, chunk_text
from chroma_services import ingest_documents, clear_collection
import tempfile, os, shutil

st.set_page_config(page_title="📤 Document Insights", layout="wide")

st.markdown("""
    <style>
        .section-title {
            font-size: 1.6rem;
            font-weight: bold;
            color: #007acc;
            margin-top: 20px;
        }
        .code-box {
            background-color: #f9f9f9;
            border-left: 5px solid #007acc;
            padding: 1rem;
            border-radius: 6px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📤 Document Insights")

st.markdown("""
<div class="section-title">📁 Upload Your Notes</div>
""", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a file (PDF, DOCX, TXT, MD, HTML):", type=["pdf", "docx", "txt", "md", "html"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    doc_text = MarkItDown().convert(tmp_path).text_content

    st.markdown("""
    <div class="section-title">📄 Document Preview</div>
    <div class="code-box">
    """, unsafe_allow_html=True)
    st.text_area("Extracted Text", doc_text, height=200)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">📝 Document Summary</div>
    """, unsafe_allow_html=True)
    with st.spinner("Summarizing and ingesting to vector store..."):
        summary = summarize_text(doc_text)
        chunks = chunk_text(doc_text)
        clear_collection()  # ✅ Clear existing vectors before ingestion
        doc_count = ingest_documents(chunks)
        st.session_state['doc_uploaded'] = True
    st.success(f"Ingested {doc_count} chunks and generated summary!")
    st.write(summary)

    if st.button("💬 Go to Chatbot"):
        st.switch_page("pages/2_Notes_Chatbot.py")
