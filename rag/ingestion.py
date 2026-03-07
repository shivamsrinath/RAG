from utils.document_loader import DocumentLoader
from utils.chunking import Chunker
from utils.embeddings import EmbeddingModel
from vectorstore.vector_store import VectorStore


class DataIngestion:

    def __init__(self, file_path):

        self.file_path = file_path

        # Initialize components
        self.loader = DocumentLoader(self.file_path)
        self.chunker = Chunker()
        self.embedding_model = EmbeddingModel().get_model()
        self.vector_store = VectorStore(self.embedding_model)

    def run_pipeline(self):

        print("Loading document...")
        docs = self.loader.load()

        print("Chunking document...")
        chunks = self.chunker.split(docs)

        print("Adding documents to vector store...")
        db = self.vector_store.add_documents(chunks)

        print("Vector store updated successfully")

        return db