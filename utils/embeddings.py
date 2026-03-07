from langchain_community.embeddings import HuggingFaceEmbeddings


class EmbeddingModel:

    def __init__(self):

        self.model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en"
        )

    def get_model(self):
        return self.model