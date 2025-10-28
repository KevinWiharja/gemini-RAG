import google.generativeai as genai
from config.settings import GOOGLE_API_KEY
from modules.retriever import get_retriever

genai.configure(api_key=GOOGLE_API_KEY)

retriever = get_retriever()

def chat_with_bot(query):
    # Retrieve relevant docs
    docs = retriever.invoke(query)
    context = "\n\n".join([d.page_content for d in docs])

    # Sending request to gemini model
    prompt = f"""
    You are a helpful assistant that answers based on company knowledge.
    Use only the information below to answer.

    Context:
    {context}

    Question:
    {query}
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text
