import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from retrieval.retriever import Retriever

print("=" * 60)
print("RETRIEVAL TEST")
print("=" * 60)

question = "What was Apple's revenue in 2024?"

retriever = Retriever()

results = retriever.retrieve(
    question=question,
    top_k=3
)

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 40)
    print(f"Score    : {result['score']}")
    print(f"Chunk ID : {result['chunk_id']}")
    print(f"Start    : {result['start']}")
    print(f"End      : {result['end']}")
    print(f"Length   : {result['length']}")
    print()
    print(result["text"][:500])