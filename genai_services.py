import os
import tiktoken
from typing import List
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("MODEL_API_KEY"),
    base_url=os.getenv("MODEL_BASE_URL")
)

def call_llm(messages: List[dict]) -> str:
    response = openai_client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=messages,
    )
    return response.choices[0].message.content

def summarize_text(text: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
        {"role": "user", "content": f"Summarize this text:\n\n{text}"}
    ]
    return call_llm(messages)

def chunk_text(text: str, chunk_size: int = 100, chunk_overlap: int = 10) -> List[str]:
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokens = enc.encode(text)
    chunks = []
    i = 0
    while i < len(tokens):
        chunk_end = min(i + chunk_size, len(tokens))
        chunks.append(enc.decode(tokens[i:chunk_end]))
        i = chunk_end - chunk_overlap if chunk_end < len(tokens) else chunk_end
    return chunks

def answer_with_context(question: str, contexts: List[str]) -> str:
    combined_context = "\n\n---\n\n".join(contexts)
    messages = [
        {"role": "system", "content": "Answer questions based on provided context. If unsure, say so."},
        {"role": "user", "content": f"Context:\n{combined_context}\n\nQuestion:\n{question}"}
    ]
    return call_llm(messages)
