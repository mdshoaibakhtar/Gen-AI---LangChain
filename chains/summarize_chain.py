from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, GROQ_MODEL

def get_summarize_chain():
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=GROQ_MODEL
    )
    prompt = PromptTemplate.from_template("Summarize this text:\n\n{text}")
    return LLMChain(llm=llm, prompt=prompt)
