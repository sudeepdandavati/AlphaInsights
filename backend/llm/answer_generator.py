import ollama


class AnswerGenerator:
    """
    Generates answers using a local Ollama model.
    """

    def __init__(self, model="llama3.2"):
        self.model = model

    def generate(self, prompt):
        """
        Generate an answer from the LLM.
        """

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]