from fastapi import FastAPI
from pydantic import BaseModel

from retriever import create_vector_store
from llm import get_llm
from pipeline import generate_response

app = FastAPI()

db = create_vector_store()
llm = get_llm()

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(query: Query):
    answer = generate_response(query.question, db, llm)
    return {"response": answer}