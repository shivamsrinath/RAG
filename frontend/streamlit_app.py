import sys
import os

# Fix Python import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from rag.ingestion import DataIngestion
from rag.pipeline import RAGPipeline


st.set_page_config(page_title="RAG Chat", layout="wide")

st.title("📄 Chat with your Documents")


# -------------------------
# CACHE THE RAG PIPELINE
# -------------------------

@st.cache_resource
def load_rag_pipeline():

    print("Loading RAG Pipeline...")

    return RAGPipeline()


rag = load_rag_pipeline()


# -------------------------
# SESSION MEMORY
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -------------------------
# FILE UPLOAD
# -------------------------

st.sidebar.header("Upload Document")

uploaded_file = st.sidebar.file_uploader("Upload PDF", type="pdf")

if uploaded_file:

    save_path = f"data/uploads/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.sidebar.success("PDF uploaded successfully!")

    if st.sidebar.button("Process Document"):

        with st.spinner("Processing document..."):

            ingestion = DataIngestion(save_path)
            ingestion.run_pipeline()

        st.sidebar.success("Document processed!")


# -------------------------
# DISPLAY CHAT HISTORY
# -------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# -------------------------
# USER INPUT
# -------------------------

query = st.chat_input("Ask something about the document...")


if query:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.write(query)

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = rag.run(query)

            st.write(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )