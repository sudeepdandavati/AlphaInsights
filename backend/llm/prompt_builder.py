class PromptBuilder:
    """
    Builds prompts for the LLM using the retrieved document chunks.
    """

    def build_prompt(self, question, retrieved_chunks):
        """
        Build a prompt from the user's question and retrieved context.
        """

        context = "\n\n".join(
            chunk["text"] for chunk in retrieved_chunks
        )

        prompt = f"""
You are an expert financial analyst.

Answer the user's question ONLY using the information provided below.

If the answer cannot be found in the context, reply:

"I could not find that information in the provided financial report."

Context:
----------------------------
{context}

----------------------------

Question:
{question}

Answer:
"""

        return prompt.strip()