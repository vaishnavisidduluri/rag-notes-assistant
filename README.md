# rag-notes-assistant

# 🧠 Personal Notes Assistant using RAG

A smart AI-powered assistant that lets you upload documents, get automatic summaries, and ask questions — all in one clean interface.  
Built using **Retrieval-Augmented Generation (RAG)**, **Gemini API**, **ChromaDB**, and **Streamlit**.

---

## 📌 Description

**Personal Notes Assistant** helps you interact with your documents using AI. Just upload a file, get a summary, and ask questions about the content.

---

## 🚀 Features

- Upload PDF, Word, Text, Markdown, or HTML files
- Automatically extract and preview content
- Get quick summaries using Gemini AI
- Ask questions and receive accurate answers using RAG
- Simple and responsive Streamlit web interface

---

## 🧠 Technologies Used

- **Streamlit**: To build the user interface  
- **Gemini API**: To generate summaries and answer questions  
- **ChromaDB**: To store and search chunks of your documents (vector store)  
- **all-MiniLM-L6-v2**: Used for creating text embeddings  
- **MarkItDown**: For converting various file types into clean text  
- **python-dotenv**: For managing environment variables

---

## 📁 Project Structure

```

📦 rag-notes-assistant/
├── main.py                       # Streamlit app launcher
├── genai\_services.py             # Summarization & LLM interaction
├── chroma\_services.py            # Vector DB ingestion & querying
├── requirements.txt              # Python dependencies
├── .env.example                  # Sample env file
├── README.md                     # This file
└── pages/
├── 1\_Document\_Insights.py    # Upload + summarization page
└── 2\_Notes\_Chatbot.py        # Chatbot page

````

---

## 🔧 How to Set Up

### 1. Clone the repository

```bash
git clone https://github.com/vaishnavisidduluri/rag-notes-assistant.git
cd rag-notes-assistant
````

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

---

## 🔐 Set Up Environment Variables

Create a `.env` file in your root directory with the following content:

```env
MODEL_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
MODEL_API_KEY=your_gemini_api_key_here
MODEL_NAME=gemini-2.0-flash
CHROMA_COLLECTION_NAME=rag_collection
```

Or simply copy from `.env.example`.

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 💡 Use Cases

* Students can ask questions on lecture notes
* Teachers can summarize documents and create quizzes
* Professionals can chat with meeting summaries
* Researchers can break down academic papers easily

---




