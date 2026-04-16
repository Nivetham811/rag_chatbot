from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from embeddings import get_embeddings

def create_vector_store():
    loader = TextLoader("data/docs.txt")
    docs = loader.load()

    embeddings = get_embeddings()
    db = FAISS.from_documents(docs, embeddings)

    return db