import ollama
from prompts.system_prompt import SYSTEM_PROMPT


class Generator:

    def __init__(self):

        self.model = "phi3"

    def generate(self, query, documents):

        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        prompt = SYSTEM_PROMPT.format(
            context=context,
            question=query
        )

        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]