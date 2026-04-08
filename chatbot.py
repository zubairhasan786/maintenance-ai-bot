from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def get_response(query, vector_db):
    results = vector_db.similarity_search(query, k=2)
    
    context = "\n".join([doc.page_content for doc in results])
    
    prompt = f"""
    You are a maintenance assistant.

    User Issue: {query}
    Context: {context}

    Give category, solution, and priority.
    """
    
    response = llm.invoke(prompt)
    return response.content
