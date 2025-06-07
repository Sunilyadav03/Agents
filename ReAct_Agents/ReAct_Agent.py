from langchain_tavily import TavilySearch
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool
from langchain.prompts import PromptTemplate
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
import streamlit  as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="ReAct-Agent",
    page_icon="👋",
)
st.write("# Welcome to Basic Web Search ReAct_Agent! 👋")


# google_search= GoogleSerperAPIWrapper()
google_search= TavilySearch()

llm= ChatOpenAI()

tools= [
    Tool(
        name= "Web Search",
        func= google_search.run,
        description="useful when any question is asked",
        verbose= True    
    )
]

template= '''Answer the following questions as best you can. You have access to the following tools:
{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
Begin!
Question: {input}
Thought: {agent_scratchpad}'''

prompt= PromptTemplate.from_template(template)
search_agent= create_react_agent(llm, tools, prompt)

agent_executor= AgentExecutor(
    agent= search_agent,
    tools= tools,
    verbose= True,
    return_intermediate_steps= True,
)
title = st.text_input("Write Your Query", "Highest score of the MS Dhoni?")

searched_output= agent_executor.invoke({"input": title})
st.write(searched_output)

