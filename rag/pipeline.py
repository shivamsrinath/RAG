from rag.retriever import Retriever
from rag.reranker import Reranker
from rag.generator import Generator


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()
        self.reranker = Reranker()
        self.generator = Generator()

    def run(self, query):

        docs = self.retriever.retrieve(query)

        if len(docs) == 0:
            return "No relevant information found in the documents."

        ranked_docs = self.reranker.rerank(query, docs)

        top_docs = ranked_docs[:2]

        answer = self.generator.generate(query, top_docs)

        return answer