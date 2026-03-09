from vectorstore.vector_store import VectorStore
from utils.embeddings import EmbeddingModel
from rank_bm25 import BM25Okapi


class Retriever:

    def __init__(self, top_k=5):

        self.embedding_model = EmbeddingModel().get_model()
        self.vector_store = VectorStore(self.embedding_model)
        self.db = self.vector_store.load()

        self.top_k = top_k

        # Load documents for BM25
        self.documents = [doc.page_content for doc in self.db.docstore._dict.values()]

        # Tokenize documents
        tokenized_docs = [doc.split() for doc in self.documents]

        self.bm25 = BM25Okapi(tokenized_docs)

    def vector_search(self, query):

        query = f"Represent this sentence for searching relevant passages: {query}"

        docs = self.db.similarity_search(query, k=self.top_k)

        return docs

    def bm25_search(self, query):

        tokenized_query = query.split()

        scores = self.bm25.get_scores(tokenized_query)

        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:self.top_k]

        bm25_docs = []

        for idx in top_indices:

            bm25_docs.append(list(self.db.docstore._dict.values())[idx])

        return bm25_docs

    def retrieve(self, query):

        vector_docs = self.vector_search(query)

        bm25_docs = self.bm25_search(query)

        # Combine results
        combined_docs = vector_docs + bm25_docs

        # Remove duplicates
        unique_docs = list({doc.page_content: doc for doc in combined_docs}.values())

        return unique_docs