import streamlit as st
from groq import Groq
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

st.set_page_config(page_title=" Hybrid Model ")
st.title("🚀 Hybrid-YOLO-Custom-Model")
st.markdown("Built by **Ravi Teja** | CNN 93.36% + YOLOv8 + FAISS RAG")

@st.cache_resource
def load_faiss():
    docs = [
        "Day 61 Custom CNN model.h5 accuracy 93.36%",
        "Day 62 YOLOv8n.pt detects WHERE 90% confidence",
        "Day 63 Hybrid = YOLO + CNN = 99.98%",
        "GitHub: Hybrid-YOLO-Custom-Model by Ravi Teja",
        "FAISS is Facebook vector DB for search",
        "Embedding converts text to 384 numbers"
    ]
    embed_model = SentenceTransformer('all-MiniLM-L6-v2')
    vectors = embed_model.encode(docs)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(np.array(vectors))
    return docs, embed_model, index

docs, embed_model, index = load_faiss()

st.header("Ask about project")
groq_key = st.text_input("Enter Groq API Key", type="password")
question = st.text_input("Your question: ex - What is hybrid accuracy?")

if st.button("Get Answer"):
    if not groq_key:
        st.error("Enter API key first!")
    else:
        q_vec = embed_model.encode([question])
        D, I = index.search(np.array(q_vec), k=3)
        retrieved = "\n".join([docs[i] for i in I[0]])
        st.info(f"Retrieved from FAISS: {retrieved}")
        client = Groq(api_key=groq_key)
        comp = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": f"Answer only from: {retrieved}"},
                {"role": "user", "content": question}
            ]
        )
        st.success(comp.choices[0].message.content)