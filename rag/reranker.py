from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(self, query, documents):

        if len(documents) == 0:
            return []

        pairs = [[query, doc.page_content] for doc in documents]

        scores = self.model.predict(pairs)

        # pair documents with scores
        scored_docs = list(zip(scores, documents))

        # sort using score only
        scored_docs.sort(key=lambda x: x[0], reverse=True)

        ranked_docs = [doc for score, doc in scored_docs]

        return ranked_docs