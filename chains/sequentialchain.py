from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, GROQ_MODEL


def sequentialchain():
    llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model=GROQ_MODEL
        )
    # Step 1: Generate a book title
    title_prompt = PromptTemplate.from_template("Give me a book title about {topic}")
    title_chain = LLMChain(llm=llm, prompt=title_prompt, output_key="title")

    # Step 2: Generate a summary using that title
    summary_prompt = PromptTemplate.from_template("Write a short summary for the book titled '{title}'")
    summary_chain = LLMChain(llm=llm, prompt=summary_prompt, output_key="summary")

    # Step 3: Generate a review using both
    review_prompt = PromptTemplate.from_template("Write a positive review of the book '{title}'. Summary: {summary}")
    review_chain = LLMChain(llm=llm, prompt=review_prompt, output_key="review")

    # Combine chains
    overall_chain = SequentialChain(
        chains=[title_chain, summary_chain, review_chain],
        input_variables=["topic"],
        output_variables=["title", "summary", "review"],
        verbose=True
    )

    result = overall_chain({"topic": "love and friendship"})
    return result
