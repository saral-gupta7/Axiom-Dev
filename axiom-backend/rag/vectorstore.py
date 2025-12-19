from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from config import OPENAI_API_KEY

VECTORSTORE_PATH = "rag/faiss_index"


def load_vectorstore():
    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True
    )

    return vectorstore
