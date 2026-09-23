import faiss
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 1. Load documents
with open("documents.txt", "r", encoding="utf-8") as f:
    text = f.read()


# 2. Chunk documents
def chunk_text(text, chunk_size=100):
    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


chunks = chunk_text(text)



# 3. Create embeddings
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = embedding_model.encode(chunks)

dimension = embeddings.shape[1]


# 4. Create vector index
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)


# 5. Ask a question
question = "What are the main stages of RAG?"


# 6. Retrieve relevant chunks
question_embedding = embedding_model.encode(
    [question]
)

distances, indices = index.search(
    question_embedding,
    k=2
)

retrieved_chunks = [
    chunks[i]
    for i in indices[0]
]


# 7. Build LLM prompt
context = "\n\n".join(retrieved_chunks)

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

If the answer cannot be found in the context,
say "I don't know based on the provided documents."
"""

# 8. Generate answer
client = OpenAI()

response = client.responses.create(
    model="gpt-5.6",
    input=prompt
)

print(response.output_text)
