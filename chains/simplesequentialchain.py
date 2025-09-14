from langchain.chains import SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, GROQ_MODEL


def simplesequentialchain():
    # Step 1: English → French
    llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model=GROQ_MODEL
        )

    prompt1 = PromptTemplate.from_template("Suggest me title for my:\n\n{text}")
    chain1 = LLMChain(llm=llm, prompt=prompt1)

    # Step 2: French → German
    prompt2 = PromptTemplate.from_template("Provide the best slogan for:\n\n{text}")
    chain2 = LLMChain(llm=llm, prompt=prompt2)

    # Combine into a sequential chain
    overall_chain = SimpleSequentialChain(chains=[chain1, chain2], verbose=True)

    result = overall_chain.run("Gym")
    return result
