import os
import ollama
from google import genai


class LLMRouter:

    def __init__(self):

        # configure Gemini client
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        # fallback local model
        self.local_model = "phi3"

    def generate(self, prompt):

        try:

            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print("Gemini error:", e)
            print("Switching to Ollama")

            response = ollama.chat(
                model=self.local_model,
                messages=[{"role": "user", "content": prompt}]
            )

            return response["message"]["content"]