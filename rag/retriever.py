from vectorstore.vector_store import VectorStore
from utils.embeddings import EmbeddingModel


class Retriever:

    def __init__(self, threshold=0.2, top_k=3):

        self.embedding_model = EmbeddingModel().get_model()
        self.vector_store = VectorStore(self.embedding_model)
        self.db = self.vector_store.load()

        self.threshold = threshold
        self.top_k = top_k

    def retrieve(self, query):

        # BGE query instruction
        query = f"Represent this sentence for searching relevant passages: {query}"

        results = self.db.similarity_search_with_score(
            query,
            k=self.top_k
        )

        filtered_docs = []

        for doc, score in results:

            similarity = 1 / (1 + score)

            if similarity >= self.threshold:
                filtered_docs.append(doc)

        return filtered_docs