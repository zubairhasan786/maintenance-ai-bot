from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

def create_vector_db(df):
    docs = []
    for _, row in df.iterrows():
        text = f"Issue: {row['issue']}, Solution: {row['solution']}"
        docs.append(Document(page_content=text))

    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embeddings)