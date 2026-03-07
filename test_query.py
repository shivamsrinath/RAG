from rag.pipeline import RAGPipeline

rag = RAGPipeline()

query = input("Ask question: ")

response = rag.run(query)

print("\nAnswer:\n", response)