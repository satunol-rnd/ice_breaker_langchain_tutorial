import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# from langchain.chains import LLMChain

from thirdparty.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser


def ice_break_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    print("linkedin link: ", linkedin_username)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_username, mock=os.environ.get("MOCK") == "true"
    )

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    \n{format_instructions}
    """
    print("prompt: ", summary_template)
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm | summary_parser

    res = chain.invoke(input={"information": linkedin_data})

    print(res)
    print("profile picture: ", linkedin_data.get("profile_pic_url"))


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    # ice_break_with(name="Emienda Qunurul Bahri Mahardika")
    # ice_break_with(name="Joko Widodo")
    # ice_break_with(name="Muhammad Beni Fajri")
    # ice_break_with(name="Eden MArco Udemy")
    ice_break_with(name="Royyan Wibisono")
