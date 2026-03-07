import os
from langchain_community.vectorstores import FAISS


class VectorStore:

    def __init__(self, embedding_model):

        self.embedding_model = embedding_model
        self.index_path = "vectorstore/faiss_index"

    def add_documents(self, documents):

        # If vector store already exists → load it
        if os.path.exists(self.index_path):

            print("Loading existing vector database...")

            db = FAISS.load_local(
                self.index_path,
                self.embedding_model,
                allow_dangerous_deserialization=True
            )

            db.add_documents(documents)

        else:

            print("Creating new vector database...")

            db = FAISS.from_documents(
                documents,
                self.embedding_model
            )

        # Save updated DB
        db.save_local(self.index_path)

        return db

    def load(self):

        db = FAISS.load_local(
            self.index_path,
            self.embedding_model,
            allow_dangerous_deserialization=True
        )

        return db