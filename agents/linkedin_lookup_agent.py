from dotenv import load_dotenv

from tools.tools import get_profile_url_tavily

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub


def lookup(name: str) -> str:
    """Lookup name and get profile URL"""
    if not ("Linkedin" in name or "linkedin" in name or "LinkedIn" in name):
        name += " LinkedIn"

    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
    )
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
    Your answer should contain only a URL"""
    
    print("prompt: ", template)
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Search Tavily 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    tool_names = ", ".join(tool.name for tool in tools_for_agent)
    print("tools: ", tool_names)

    react_prompt = hub.pull("hwchase17/react")
    print("react_prompt: ", react_prompt.template)
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]
    return linked_profile_url


if __name__ == "__main__":
    print(lookup(name="Royyan Wibisono"))
