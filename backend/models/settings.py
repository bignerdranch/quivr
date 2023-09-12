from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import PGEmbedding
from pydantic import BaseSettings

CONNECTION_STRING = "postgresql+psycopg2://postgres:password@homebase-chatapp-pg:5432/pgembeddings_db"

COLLECTION_NAME = "homebase-chatbot"

COLLECTION_ID = 'collection_id'


class LLMSettings(BaseSettings):
    private: bool = False
    model_path: str = "./local_models/ggml-gpt4all-j-v1.3-groovy.bin"



def get_embeddings() -> HuggingFaceEmbeddings:
    embeddings = HuggingFaceEmbeddings()
    return embeddings


def get_documents_vector_store():
    db = PGEmbedding(
        embedding_function=get_embeddings(),
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING
    )
    return db
