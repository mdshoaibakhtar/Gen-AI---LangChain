from langchain_groq import ChatGroq
from prompts.base_prompt import base_prompt
from config.settings import GROQ_API_KEY, GROQ_MODEL

def ask_question(question: str):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=GROQ_MODEL
    )
    messages = base_prompt.format_messages(question=question)
    response = llm.invoke(messages)
    return response.content
