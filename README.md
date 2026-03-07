# 📄 Chat with Your Documents — Modular RAG Application

A **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions about them. The system retrieves relevant information from the document using embeddings and a vector database, then generates answers using a local LLM.

This project demonstrates a **production-style modular RAG architecture** including document ingestion, semantic retrieval, reranking, and a chat interface.

---

# 🚀 Features

* Upload PDF documents
* Automatic document ingestion
* Semantic search using embeddings
* Vector database storage
* Cross-encoder reranking
* Local LLM generation
* Chat interface for querying documents
* Modular architecture for easy extension

---

# 🧠 Architecture

The system follows a typical **RAG pipeline**:

```
User Query
    ↓
Query Embedding
    ↓
Vector Database Search
    ↓
Top-K Document Retrieval
    ↓
Reranking
    ↓
Context Construction
    ↓
LLM Generation
    ↓
Answer
```

Document ingestion pipeline:

```
PDF Upload
    ↓
Document Loader
    ↓
Chunking
    ↓
Embedding
    ↓
Vector Database Storage
```

---

# 📁 Project Structure

```
RAG_01
│
├── data
│   └── uploads
│
├── frontend
│   └── streamlit_app.py
│
├── rag
│   ├── ingestion.py
│   ├── retriever.py
│   ├── reranker.py
│   ├── generator.py
│   └── pipeline.py
│
├── utils
│   ├── document_loader.py
│   ├── chunking.py
│   └── embeddings.py
│
├── vectorstore
│   └── vector_store.py
│
├── prompts
│   └── system_prompt.py
│
├── test_ingestion.py
├── test_query.py
│
└── requirements.txt
```

---

# ⚙️ Technologies Used

* Python
* Streamlit
* FAISS Vector Database
* Sentence Transformers
* Cross Encoder Reranking
* PyMuPDF
* Ollama Local LLM
* LangChain Components

---

# 🧩 Components Explanation

## Document Loader

Extracts text from PDF files using PyMuPDF and converts them into structured documents.

```
PDF → Extract text → Document objects
```

---

## Chunking

Large documents are split into smaller overlapping chunks to improve retrieval.

Typical configuration:

```
chunk_size = 500
chunk_overlap = 100
```

This ensures the retriever captures meaningful context.

---

## Embedding Model

The system uses the **BGE embedding model**:

```
BAAI/bge-small-en
```

This model converts text into vector embeddings for semantic search.

---

## Vector Database

The project uses **FAISS** to store embeddings and perform fast similarity search.

FAISS allows efficient retrieval of semantically similar document chunks.

---

## Retriever

The retriever performs semantic search on the vector database.

Steps:

```
Query → Embedding → Similarity Search → Top-K Documents
```

To improve retrieval quality, a query instruction is used:

```
Represent this sentence for searching relevant passages: {query}
```

---

## Reranker

The retriever may return multiple documents. A **cross-encoder reranker** improves accuracy by scoring relevance between the query and documents.

Model used:

```
cross-encoder/ms-marco-MiniLM-L-6-v2
```

---

## Prompt Construction

Retrieved document chunks are merged into a prompt with a system instruction:

```
Context + User Question → LLM
```

The LLM is instructed to answer **only using the provided context**.

---

## LLM Generation

The project uses a **local language model via Ollama**.

Example models:

* llama3
* phi3
* mistral

The LLM generates answers using retrieved document context.

---

# 🖥️ Frontend

The frontend is built using **Streamlit**.

Features:

* Upload PDF documents
* Process documents
* Chat interface for asking questions
* Conversation history

---

# 📦 Installation

Clone the repository:

```
git clone <repository-url>
cd RAG_01
```

Create a virtual environment:

```
python -m venv rag-env
```

Activate environment:

Windows:

```
rag-env\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 🤖 Install Local LLM

Install Ollama:

https://ollama.com/download

Download a model:

```
ollama pull phi3
```

Start the Ollama server:

```
ollama serve
```

---

# 📄 Document Ingestion

Place a PDF inside:

```
data/uploads/
```

Run ingestion:

```
python test_ingestion.py
```

This will:

* load the document
* split into chunks
* generate embeddings
* store them in FAISS

---

# ❓ Query the System

Run:

```
python test_query.py
```

Example:

```
Ask question: What is object detection?
```

---

# 💬 Run the Web Interface

Start the Streamlit application:

```
streamlit run frontend/streamlit_app.py
```

Open the browser:

```
http://localhost:8501
```

Upload a document and start chatting.

---

# ⚡ Performance Optimizations

To improve response time:

1. Cache the RAG pipeline using Streamlit caching
2. Reduce retrieved chunks
3. Use smaller LLM models like `phi3`
4. Limit context sent to LLM
5. Disable reranking if speed is critical


# 🎯 Use Cases

* Research paper QA
* Legal document analysis
* Company knowledge base
* Study assistant
* Internal document search




