from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import OPENAI_API_KEY
import os

VECTORSTORE_PATH = "rag/faiss_index"

DOCS_PATH = "rag/docs"


def ingest_documents():
    documents = []

    for filename in os.listdir(DOCS_PATH):
        if filename.endswith(".md"):
            with open(os.path.join(DOCS_PATH, filename), "r", encoding="utf-8") as f:
                documents.append(
                    Document(page_content=f.read(), metadata={"source": filename})
                )
    if not documents:
        raise RuntimeError("No documents found to ingest.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )
    chunks = splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

    vectorstore = FAISS.from_documents(chunks, embeddings)
    os.makedirs(VECTORSTORE_PATH, exist_ok=True)
    vectorstore.save_local(VECTORSTORE_PATH)

    print("✅ Vector store created and saved.")


if __name__ == "__main__":
    ingest_documents()
