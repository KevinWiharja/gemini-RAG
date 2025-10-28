from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from models.LlamaTextEmbedder import LlamaTextEmbedder
from config.settings import PINECONE_API_KEY, PINECONE_INDEX_NAME

def get_retriever():
    embedder = LlamaTextEmbedder(api_key=PINECONE_API_KEY)

    # Create Pinecone client and connect to index
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)

    # Initialize VectorStore
    vectorstore = PineconeVectorStore(
        index=index,
        embedding=embedder
    )

    # Return retriever with top 3 matches
    return vectorstore.as_retriever(search_kwargs={"k": 3})