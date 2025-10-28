from fastapi import FastAPI
from modules.chat_handler import chat_with_bot
from models.QueryRequest import QueryRequest

app = FastAPI(title="Company AI Assistant")

@app.post("/chat")
async def chat_endpoint(req: QueryRequest):
    response = chat_with_bot(req.query)
    return {"answer": response}