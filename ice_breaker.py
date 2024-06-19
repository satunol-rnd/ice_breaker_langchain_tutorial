import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == "__main__":
    load_dotenv()
    print("Hello, LangChain!")
    print(os.environ.get("APP_MODE_", "not found!"))

    information = """
    Elon Reeve Musk (/ˈiːlɒn/; EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$232 billion as of December 2023, according to the Bloomberg Billionaires Index, and $254 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.[5][6]

A member of the wealthy South African Musk family, Elon was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University. However, Musk dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and, that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal.

In October 2002, eBay acquired PayPal for $1.5 billion, and that same year, with $100 million of the money he made, Musk founded SpaceX, a spaceflight services company. In 2004, he became an early investor in electric vehicle manufacturer Tesla Motors, Inc. (now Tesla, Inc.). He became its chairman and product architect, assuming the position of CEO in 2008. In 2006, Musk helped create SolarCity, a solar-energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, Musk co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and the Boring Company, a tunnel construction company. In 2022, he acquired Twitter for $44 billion. He subsequently merged the company into newly created X Corp. and rebranded the service as X the following year. In March 2023, he founded xAI, an artificial intelligence company.

    """
    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})

    print(res)
    # Expected ouput:
    """
    content='
    1. Elon Musk is a South African-born businessman and investor known for his roles in founding and leading companies such as SpaceX, Tesla, Inc., and the Boring Company. 
    He is also involved in various other ventures in the fields of artificial intelligence and transportation.\n\n
    2. Two interesting facts about Elon Musk:\n- He dropped out of Stanford University after just two days to pursue entrepreneurial ventures, 
    eventually co-founding successful companies like Zip2, PayPal, and SpaceX.\n
    - Musk is known for his ambitious goals, such as colonizing Mars with SpaceX and developing brain-computer interfaces with Neuralink, showcasing his innovative and 
    forward-thinking approach to technology and business.
    ' 

    response_metadata={'token_usage': {'completion_tokens': 130, 'prompt_tokens': 593, 'total_tokens': 723}, 'model_name': 'gpt-3.5-turbo', 
    'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-cfb4497a-c09a-48ae-9526-3e0694ed2bf9-0' 
    usage_metadata={'input_tokens': 593, 'output_tokens': 130, 'total_tokens': 723}
    """
