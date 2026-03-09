class ContextCompressor:

    def compress(self, query, documents):

        relevant_docs = []

        for doc in documents:

            text = doc.page_content.lower()
            q_words = query.lower().split()

            # simple keyword relevance check
            if any(word in text for word in q_words):

                relevant_docs.append(doc)

        return relevant_docs