from rag.llm_router import LLMRouter
from prompts.system_prompt import SYSTEM_PROMPT


class Generator:

    def __init__(self):

        self.router = LLMRouter()

    def generate(self, query, documents):

        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        prompt = SYSTEM_PROMPT.format(
            context=context,
            question=query
        )

        response = self.router.generate(prompt)

        return response