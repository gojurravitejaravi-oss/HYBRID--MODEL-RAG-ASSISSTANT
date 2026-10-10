import streamlit as st
from groq import Groq
import os

st.set_page_config(page_title="Ravi's RAG Assistant")
st.title("🚀 HYBRID-MODEL-RAG-ASSISTANT | Project-8")
st.markdown("Built by **Ravi Teja** | CNN 93.36% + YOLOv8 + RAG + Groq")

# Docs - no heavy embedding, simple keyword RAG
DOCS = [
    "Day 61 Custom CNN model.h5 accuracy 93.36% - detects WHAT is image",
    "Day 62 YOLOv8n.pt detects WHERE - bounding box with 90% confidence",
    "Day 63 Hybrid = YOLO + CNN = 99.98% accuracy - YOLO finds, CNN classifies",
    "FAISS is Facebook AI vector database for similarity search",
    "RAG = Retrieval Augmented Generation = LLM + Private Docs",
    "Groq is fastest LLM inference - model openai/gpt-oss-120b",
    "GitHub Project-7: Hybrid-YOLO-Custom-Model by Ravi Teja",
    "Streamlit is used to deploy Python apps as website in 10 lines"
]

st.header("Ask about Hybrid Model")
question = st.text_input("Your question: ex - What is hybrid accuracy?")

# Get API key from Secrets (Cloud) or text input (Local)
try:
    groq_key = st.secrets["GROQ_API_KEY"]
except:
    groq_key = st.text_input("Enter Groq API Key (for local only)", type="password")

if st.button("Get Answer"):
    if not groq_key:
        st.error("Add GROQ_API_KEY in Streamlit Secrets! See README.")
    else:
        # Simple retrieval - keyword matching (no heavy model)
        retrieved = "\n".join([d for d in DOCS if any(w.lower() in d.lower() for w in question.split())][:3])
        if not retrieved:
            retrieved = "\n".join(DOCS[:3])

        st.info(f"**Retrieved from Docs:**\n{retrieved}")

        try:
            client = Groq(api_key=groq_key)
            comp = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {"role": "system", "content": f"You are RAG assistant. Answer ONLY from this context: {retrieved}. If not in context, say I don't know from docs."},
                    {"role": "user", "content": question}
                ]
            )
            st.success(comp.choices[0].message.content)
            st.balloons()
        except Exception as e:
            st.error(f"Groq Error: {e} - Check API Key in Secrets")
