import fitz
from langchain_core.documents import Document
import os


class DocumentLoader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)

    def load(self):

        docs = []
        pdf = fitz.open(self.file_path)

        for page_num, page in enumerate(pdf):

            text = page.get_text()

            docs.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": self.file_name,
                        "page": page_num
                    }
                )
            )

        return docs