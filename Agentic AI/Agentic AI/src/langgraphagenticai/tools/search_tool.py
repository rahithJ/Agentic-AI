from langgraph.prebuilt import ToolNode
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import Tool

def gettools():
    tools=[TavilySearchResults(max_results=2),WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())]
    return tools

def gettoolsnode(tools):
    return ToolNode(tools=tools)