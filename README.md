# 📄 RAG Document Chat Application

A **Retrieval-Augmented Generation (RAG)** application that allows users to **upload PDF documents and ask questions about them**.
The system retrieves relevant information from the document using embeddings and a vector database, then generates answers using **Gemini API with an Ollama fallback**.

---

# 🚀 Features

* Upload PDF documents through a web interface
* Automatic document ingestion
* Semantic search using embeddings
* Hybrid retrieval (**Vector Search + BM25**)
* Reranking for better relevance
* Context compression for efficient prompts
* LLM routing (**Gemini API → Ollama fallback**)
* Interactive chat interface

---

# 🧠 System Architecture

```
User
 ↓
Streamlit UI
 ↓
Upload PDF
 ↓
Data Ingestion Pipeline
 ↓
Chunking
 ↓
Embeddings (BGE Small)
 ↓
Vector Database (FAISS)
 ↓
Hybrid Retrieval (Vector + BM25)
 ↓
Reranker
 ↓
Context Compression
 ↓
Prompt Construction
 ↓
LLM Router
      ↓
   Gemini API
      ↓ (fallback)
   Ollama Local Model
 ↓
Answer
```

---

# 📁 Project Structure

```
RAG_01
│
├── frontend
│   └── streamlit_app.py
│
├── rag
│   ├── ingestion.py
│   ├── pipeline.py
│   ├── retriever.py
│   ├── reranker.py
│   ├── compressor.py
│   ├── generator.py
│   └── llm_router.py
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
├── data
│   └── uploads
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

* Python
* Streamlit
* FAISS Vector Database
* Sentence Transformers
* BM25 Retrieval
* Cross Encoder Reranking
* PyMuPDF
* Gemini API
* Ollama

---

# 🧩 Pipeline Explanation

## 1️⃣ Document Upload

Users upload a PDF through the Streamlit interface.

The file is stored in:

```
data/uploads
```

---

## 2️⃣ Document Loading

The PDF is processed using **PyMuPDF** and converted into text documents.

```
PDF → Text → Document objects
```

---

## 3️⃣ Chunking

Large documents are split into smaller chunks.

Typical configuration:

```
chunk_size = 500
chunk_overlap = 100
```

This improves retrieval accuracy.

---

## 4️⃣ Embedding Generation

The system converts chunks into vector embeddings using:

```
BAAI/bge-small-en
```

Embeddings represent the **semantic meaning of text**.

---

## 5️⃣ Vector Storage

Embeddings are stored in **FAISS**.

FAISS enables fast similarity search.

Stored files:

```
vectorstore/faiss_index
    ├── index.faiss
    └── index.pkl
```

---

## 6️⃣ Hybrid Retrieval

To improve retrieval accuracy, the system uses:

```
Vector Search (semantic similarity)
+
BM25 (keyword search)
```

This ensures both **semantic meaning and exact keywords** are captured.

---

## 7️⃣ Reranking

Retrieved chunks are reranked using a **cross encoder model**:

```
cross-encoder/ms-marco-MiniLM-L-6-v2
```

This improves relevance before sending context to the LLM.

---

## 8️⃣ Context Compression

Context compression removes irrelevant chunks.

Instead of sending all retrieved chunks to the LLM:

```
Retriever → 10 chunks
```

The compressor filters them:

```
Compressor → 3–4 relevant chunks
```

Benefits:

* faster responses
* smaller prompts
* better accuracy

---

## 9️⃣ LLM Router

The system uses a **model routing strategy**.

```
Gemini API
↓
If API fails
↓
Ollama Local Model
```

Advantages:

* fast cloud inference
* offline capability
* improved reliability

---

# 🖥️ Frontend

The UI is built using **Streamlit**.

Features:

* upload PDF
* process document
* ask questions
* chat interface
* conversation history

---

# 📦 Installation

Clone the repository:

```
git clone <repo-url>
cd RAG_01
```

Create virtual environment:

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

# 🔑 Gemini API Setup

Create an API key from:

```
https://aistudio.google.com/app/apikey
```

Set environment variable.

Windows CMD:

```
setx GEMINI_API_KEY "your_api_key"
```

Restart the terminal afterward.

---

# ▶️ Run the Application

Start the Streamlit app:

```
streamlit run frontend/streamlit_app.py
```

Open:

```
http://localhost:8501
```

Workflow:

1. Upload PDF
2. Click **Process Document**
3. Ask questions


# ⚡ Performance Optimizations

Implemented optimizations:

* hybrid retrieval
* reranking
* context compression
* smaller embedding model
* prompt optimization

These improvements significantly improve RAG accuracy.




