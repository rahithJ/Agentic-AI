from langgraph.graph import START,END,StateGraph
from src.langgraphagenticai.nodes.node_ai_preference import NodeAiPreference
from src.langgraphagenticai.state.state import StateAIPreference
class GraphAiPreference:
    def __init__(self,llm):
        self.llm = llm
    
    def init_graph(self):
        node = NodeAiPreference(self.llm)
        graph = StateGraph(StateAIPreference)
        graph.add_node("collect_preferences",node.collect_preferences)
        graph.add_node("recommend_products",node.recommend_products)
        graph.add_node("confirm_order",node.confirm_order)

        graph.add_edge(START,"collect_preferences")
        graph.add_edge("collect_preferences","recommend_products")
        graph.add_edge("recommend_products","confirm_order")
        graph.add_edge("confirm_order",END)

        return graph.compile()
