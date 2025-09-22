from langgraph.graph import START,END,StateGraph
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.node import Node
class Graph:
    def __init__(self,llm):
        self.llm = llm

    def init_graph(self):
        node = Node(self.llm)

        graph = StateGraph(State)
        graph.add_node("intent_classify",node.intent_classify)
        graph.add_node("classify_issue",node.classify_issue)
        graph.add_node("ticket_creator",node.ticket_creator)

        graph.add_edge(START,"intent_classify")
        graph.add_edge("intent_classify","classify_issue")
        graph.add_edge("classify_issue","ticket_creator")
        graph.add_edge("ticket_creator",END)

        return graph.compile()
