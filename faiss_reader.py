import faiss

# Specify the path to your .faiss file
index_path = "vectorstore/faiss_index/index.faiss" 

# Load the index
index = faiss.read_index(index_path)

# You can now perform operations on the index, like searching:
# distances, indices = index.search(query_vectors, k=k_neighbors)
print(f"Index successfully loaded with {index.ntotal} vectors.")
