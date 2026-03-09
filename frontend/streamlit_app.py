import sys
import os
import streamlit as st

# fix imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag.ingestion import DataIngestion
from rag.pipeline import RAGPipeline


st.set_page_config(page_title="RAG Chat", layout="wide")

st.title("📄 Chat with your Documents")


# session state variables
if "rag" not in st.session_state:
    st.session_state.rag = None

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------------
# Upload Document
# ---------------------------

st.sidebar.header("Upload Document")

uploaded_file = st.sidebar.file_uploader("Upload PDF", type="pdf")

if uploaded_file:

    save_path = f"data/uploads/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.sidebar.success("PDF uploaded successfully")

    if st.sidebar.button("Process Document"):

        with st.spinner("Processing document..."):

            ingestion = DataIngestion(save_path)
            ingestion.run_pipeline()

            # load pipeline AFTER ingestion
            st.session_state.rag = RAGPipeline()

        st.sidebar.success("Document processed successfully!")


# ---------------------------
# Chat UI
# ---------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])


query = st.chat_input("Ask a question about the document")


if query:

    if st.session_state.rag is None:

        st.warning("Please upload and process a document first.")

    else:

        st.session_state.messages.append(
            {"role": "user", "content": query}
        )

        with st.chat_message("user"):
            st.write(query)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = st.session_state.rag.run(query)

                st.write(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )