from langchain_community.vectorstores import FAISS   

def create_vector_store(texts, embedding_model):
    return FAISS.from_texts(texts, embedding_model)

def query_vector_store(db, query):
    return db.similarity_search(query, k=2)