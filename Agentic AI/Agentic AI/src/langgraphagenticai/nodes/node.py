from src.langgraphagenticai.data import data
from src.langgraphagenticai.state.state import State
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.chains import LLMChain

class Node:
    def __init__(self,llm):
        self.llm = llm
    
    def intent_classify(self, state:State):
        self.product = data.product_policies.get(state['product_id'])
        if self.product['returnable'] and self.product["refundable"]:
            return {"description":"The Product is Returnable and Refundable"}

        else:
            system = (
                """ you are the best LLM you need check and find the issue
                given by the user the issue: {issue}, find the indebt of the
                issue and give the description for the same
                """
            )
            prompt = ChatPromptTemplate.from_messages([
                ("system",system),
                ("user",state["issue"])
            ])
            chain = prompt | self.llm
            response = chain.invoke(state["issue"])
            return {"description":response.content}
            
    def classify_issue(self,state:State):
        if "Returnable" and "Refundable" in state['description']:
            return {"issue_type":"Return"}

        else:
            return {"issue_type":"Product_Issue"}
        
    def ticket_creator(self,state):
        if state["issue_type"] == "Product_Issue":
            prompt = PromptTemplate.from_template(
                """ you are the best LLM you need to create the 
                ticket for the {customer_name} for the {issue_type}
                for the given {issue} and need to send it as whole ticket in a better
                manner for the product seller use the {description} for the better work
                """
            )
            chain = prompt | self.llm
            response = chain.invoke({
                "customer_name": state["customer_name"],
                "issue_type": state["issue_type"],
                "issue": state["issue"],
                "description": state["description"]
            })
            return {"created_ticket":response.content}


