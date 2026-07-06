import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from retrieval.retriever import Retriever
from llm.prompt_builder import PromptBuilder
from llm.answer_generator import AnswerGenerator


print("=" * 60)
print("RAG PIPELINE TEST")
print("=" * 60)

question = "What was Apple's revenue in 2024?"

# Retrieve relevant chunks
retriever = Retriever()

chunks = retriever.retrieve(
    question=question,
    top_k=3,
)

print(f"Retrieved Chunks : {len(chunks)}")

# Build prompt
builder = PromptBuilder()

prompt = builder.build_prompt(
    question=question,
    retrieved_chunks=chunks,
)

print("\nPrompt Preview")
print("-" * 60)
print(prompt[:1000])
print("...")

# Generate answer
generator = AnswerGenerator()

answer = generator.generate(prompt)

print("\nGenerated Answer")
print("-" * 60)
print(answer)