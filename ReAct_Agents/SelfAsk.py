from langchain_community.tools.tavily_search import TavilyAnswer
from langchain.agents import Tool
from langchain.agents import AgentExecutor, create_self_ask_with_search_agent
from langchain_openai import ChatOpenAI
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

web_search= TavilyAnswer()

llm= ChatOpenAI()

tools= [
    Tool(
        name= "Intermediate Answer",
        func= web_search.run,
        description="useful when any question is asked",
        verbose= True    
    )
]

prompt= hub.pull("hwchase17/self-ask-with-search")
print(prompt.template)
search_agent= create_self_ask_with_search_agent(llm, tools, prompt)

agent_executor= AgentExecutor(
    agent= search_agent,
    tools= tools,
    verbose= True,
    return_intermediate_steps= True,
    handle_parsing_errors=True,
)


agent_executor.invoke(
                      {"input": "Who is the current cricket captain of team India?"})