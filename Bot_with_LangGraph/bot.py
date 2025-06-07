from typing import Annotated, Literal, TypedDict
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END, MessagesState
from langchain.chat_models import init_chat_model
from langchain_community.tools.tavily_search import TavilySearchResults  
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(model='gpt-3.5-turbo')  

graph = StateGraph(MessagesState)

tool = TavilySearchResults(max_results=2)  
tools = [tool]
tool_node = ToolNode(tools)
llm_with_tool = llm.bind_tools(tools)

class ChatBot:
    def __init__(self):
        self.llm = init_chat_model(model='gpt-4o')  
    
    def call_tool(self):
        tool = TavilySearchResults(max_results=2)
        tools = [tool]
        self.tool_node = ToolNode(tools=tools)
        self.llm_with_tool = self.llm.bind_tools(tools)
    
    def call_model(self, state: MessagesState):
        messages = state['messages']
        response = self.llm_with_tool.invoke(messages)
        return {'messages': response}

    def router_function(self, state: MessagesState) -> Literal['tools', END]:
        messages = state['messages']
        last_message = messages[-1]
        if last_message.tool_calls:
            return 'tools'
        return END
    
    def __call__(self):
        self.call_tool()
        graph = StateGraph(MessagesState)
        graph.add_node("agent", self.call_model)
        graph.add_node('tools', self.tool_node)
        graph.add_edge(START, 'agent')
        graph.add_conditional_edges('agent', self.router_function, {'tools': 'tools', END: END})
        graph.add_edge('tools', 'agent')
        self.app = graph.compile()
        return self.app

if __name__ == '__main__':
    mybot = ChatBot()
    graph = mybot()
    response = graph.invoke({'messages': [HumanMessage(content="who is the current president of India?")]})
    print(response['messages'][-1].content)