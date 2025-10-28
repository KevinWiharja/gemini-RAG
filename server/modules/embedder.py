from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from models.LlamaTextEmbedder import LlamaTextEmbedder
from config.settings import PINECONE_API_KEY, PINECONE_INDEX_NAME

def create_vectorstore(docs):
    embedder = LlamaTextEmbedder(api_key=PINECONE_API_KEY)

    # Resetting all indexes in cloud to match current updated indexes 
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
    index.delete(delete_all=True)

    # NOTE: from_documents creating VectorStore and UPSERT in one go
    vectorstore = PineconeVectorStore.from_documents(
        docs,
        embedding=embedder,
        index_name=PINECONE_INDEX_NAME
    )
    
    print(f"{len(docs)} chunks successfully uploaded to Index: {PINECONE_INDEX_NAME}")
    return vectorstore