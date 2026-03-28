from langchain_openai import OpenAIEmbeddings

def get_embeddings():
    return OpenAIEmbeddings(api_key="APIKEY")