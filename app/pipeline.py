def generate_response(query, db, llm):
    docs = db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.predict(prompt)
    return response