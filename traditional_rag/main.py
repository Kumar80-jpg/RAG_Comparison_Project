from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")

print("API KEY:", os.getenv("OPENAI_API_KEY"))


from embedding import get_embeddings
from retriever import create_vector_store, query_vector_store

texts = [
    "AI is used in healthcare",
    "AI is used in finance",
    "Google invests in AI"
]

embedding = get_embeddings()

db = create_vector_store(texts, embedding)

query = "Where is AI used?"
results = query_vector_store(db, query)

for res in results:
    print(res.page_content)