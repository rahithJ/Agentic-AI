from src.langgraphagenticai.nodes.node_competitor import NodeCompetitor
from langgraph.graph import START,END,StateGraph
from src.langgraphagenticai.state.state import StateCompetitor

class GraphCompetitor:
    def __init__(self,llm):
        self.llm = llm

    def init_graph(self):
        node = NodeCompetitor(self.llm)

        graph = StateGraph(StateCompetitor)
        graph.add_node("get_competitor_price",node.get_competitor_price)
        graph.add_node("get_our_price",node.get_our_price)
        graph.add_node("adjust_price",node.adjust_price)

        graph.add_edge(START,"get_competitor_price")
        graph.add_edge("get_competitor_price","get_our_price")
        graph.add_edge("get_our_price","adjust_price")
        graph.add_edge("adjust_price",END)

        return graph.compile()
