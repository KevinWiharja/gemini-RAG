from langchain.embeddings.base import Embeddings
from pinecone import Pinecone

class LlamaTextEmbedder(Embeddings):
    def __init__(self, model: str = "llama-text-embed-v2", api_key: str = None):
        self.model = model
        self.api_key = api_key
        self.pc = Pinecone(api_key=self.api_key)

    def embed_documents(self, texts):
        res = self.pc.inference.embed(
            model=self.model,
            inputs=texts,
            parameters={
                "input_type": "passage", # passage = document indexing, query = document searching
                "truncate": "END"
            }
        )
        return [item["values"] for item in res.data]

    def embed_query(self, text):
        res = self.pc.inference.embed(
            model=self.model,
            inputs=[text],
            parameters={
                "input_type": "query",
                "truncate": "END"
            }
        )
        return res.data[0]["values"]
