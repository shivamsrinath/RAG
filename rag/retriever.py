from vectorstore.vector_store import VectorStore
from utils.embeddings import EmbeddingModel


class Retriever:

    def __init__(self, top_k=5):

        self.embedding_model = EmbeddingModel().get_model()
        self.vector_store = VectorStore(self.embedding_model)
        self.db = self.vector_store.load()

        self.top_k = top_k

    def retrieve(self, query):

        # BGE query instruction
        query = f"Represent this sentence for searching relevant passages: {query}"

        docs = self.db.similarity_search(
            query,
            k=self.top_k
        )

        return docs