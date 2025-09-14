from chains import simplesequentialchain
from chains import sequentialchain
from chains.summarize_chain import get_summarize_chain
from chains.qa_chain import ask_question

def main():
    # # QnA example
    # answer = ask_question("What is LangChain?")
    # print("QnA Response:", answer)

    # # Summarization example
    # summarize_chain = get_summarize_chain()
    # summary = summarize_chain.run(
    #     "LangChain is a framework to build applications powered by LLMs. "
    #     "It supports agents, memory, and retrieval to make apps more intelligent."
    # )
    # output = simplesequentialchain.simplesequentialchain()
    output = sequentialchain.sequentialchain()

    print("output:", output)
    return output

if __name__ == "__main__":
    main()