# 🚀 HYBRID-MODEL-RAG-ASSISTANT | Project-8 | Live RAG Chatbot

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mxaiaw9fjycwwiveyxpspj.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/LLM-Groq%20gpt--oss--120b-orange)](https://groq.com/)

### 🌐 Live Demo
**👉 https://mxaiaw9fjycwwiveyxpspj.streamlit.app/**

### 📌 About
**Project-7 (Day 61-63):** Custom CNN 93.36% + YOLOv8n.pt + Hybrid 99.98%
**Project-8 (Day 64-67):** This Repo - RAG Chatbot for Hybrid Model using FAISS + Groq + Streamlit

### 🏗️ Architecture
User Question -> Keyword Retrieval (FAISS Concept) -> Top Docs -> Groq LLM (openai/gpt-oss-120b) -> Final Answer

### 💻 Tech Stack
- LLM: Groq API `openai/gpt-oss-120b`
- Vector DB Concept: FAISS
- Embeddings: all-MiniLM-L6-v2 (384-dim)
- Frontend: Streamlit
- Deployment: Streamlit Cloud

### ✨ Features
- Ask about Hybrid Model, Accuracy, YOLO, CNN
- Blue Box = Retrieved Docs (RAG Retrieval)
- Green Box = LLM Answer (RAG Generation)
- Secured with Streamlit Secrets

### 🚀 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
