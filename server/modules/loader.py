from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Loading and splitting documents into chunks
def load_and_split_documents(path: str = "data"):

    loader = DirectoryLoader(path, glob="**/*.txt")
    docs = loader.load()
    
    print(f"Loaded {len(docs)} initial documents from {path}")
    
    CHUNK_SIZE = 800
    CHUNK_OVERLAP = 150
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, 
        chunk_overlap=CHUNK_OVERLAP
    )
    
    split_docs = splitter.split_documents(docs)
    return split_docs