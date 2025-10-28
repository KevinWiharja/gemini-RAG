# Run ONLY WHEN there's an update to the company_docs
from modules.loader import load_and_split_documents
from modules.embedder import create_vectorstore

DATA_DIR = "data" 

if __name__ == "__main__":
    print("Starting RAG Indexing Pipeline...")
    
    print("Loading and splitting documents...")
    split_docs = load_and_split_documents(path=DATA_DIR)
    
    print(f"Created {len(split_docs)} chunks from source documents")

    print("📤 Uploading to Pinecone (llama-text-embed-v2)...")
    create_vectorstore(split_docs)
    print("Done! Vectorstore created successfully.")