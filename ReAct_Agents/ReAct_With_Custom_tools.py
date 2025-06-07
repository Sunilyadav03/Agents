from langchain.agents import tool
from langchain_community.tools.tavily_search import TavilyAnswer
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain import hub
import streamlit  as st
from dotenv import load_dotenv

load_dotenv()

web_search= TavilyAnswer()

llm= ChatOpenAI()

@tool
def get_employee_id(name):
    """
    To get employee id, it takes employee name as arguments
    name(str): Name of the employee
    """
    fake_employees = {
        "Alice": "E001",
        "Bob": "E002",
        "Charlie": "E003",
        "Diana": "E004",
        "Evan": "E005",
        "Fiona": "E006",
        "George": "E007",
        "Hannah": "E008",
        "Ian": "E009",
        "Jasmine": "E010"
    }
    return fake_employees.get(name, "Employee not found")

@tool
def get_employee_salary(employee_id):
    """
    To get the salary of an employee, it takes employee_id as input and return salary
    """
    employee_salaries = {
        "E001": 56000,
        "E002": 47000,
        "E003": 52000,
        "E004": 61000,
        "E005": 45000,
        "E006": 58000,
        "E007": 49000,
        "E008": 53000,
        "E009": 50000,
        "E010": 55000
    }
    return employee_salaries.get(employee_id, "Employee not found")

prompt= hub.pull("hwchase17/react")
tools= [get_employee_salary, get_employee_id]
agent= create_react_agent(
    llm, tools, prompt
)
agent_executor= AgentExecutor(
    agent= agent,
    tools= tools,
    verbose= True,
    return_intermediate_steps= True,
)

agent_executor.invoke(
                      {"input": "Who have salaries less than 50000?"})