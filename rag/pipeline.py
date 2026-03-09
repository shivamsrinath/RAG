from rag.retriever import Retriever
from rag.reranker import Reranker
from rag.generator import Generator
from rag.compressor import ContextCompressor


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()
        self.reranker = Reranker()
        self.compressor = ContextCompressor()
        self.generator = Generator()

    def run(self, query):

        docs = self.retriever.retrieve(query)

        print("Retrieved docs:", len(docs))

        ranked_docs = self.reranker.rerank(query, docs)

        # compress context
        compressed_docs = self.compressor.compress(query, ranked_docs)

        print("Compressed docs:", len(compressed_docs))

        if len(compressed_docs) == 0:
            return "No relevant information found in the documents."

        top_docs = compressed_docs[:3]

        answer = self.generator.generate(query, top_docs)

        return answer