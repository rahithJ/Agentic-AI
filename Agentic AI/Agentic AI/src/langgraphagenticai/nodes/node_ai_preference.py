from src.langgraphagenticai.state.state import StateAIPreference
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

class NodeAiPreference:
    def __init__(self,llm):
        self.llm = llm

    def collect_preferences(self,state:StateAIPreference):
        system = (
            """"You are the best AI Assistant get the
                user input: {input} from the user and make the perfect
                preference, give it in a way as a simple text in 50 words as brief of what the user need
            """
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system",system),
            ("user","{input}")
        ])

        prompt_chain = prompt | self.llm

        response = prompt_chain.invoke(state["input"])

        return {"preferences":response.content}
    
    def recommend_products(self,state:StateAIPreference):
        prompt_text = PromptTemplate.from_template("""
                                you are the best LLM give the product recommendation
                                for the given preferences {preference} in the retail department field
                                you are the best llm behave like the way. choose the best 5 produts and give the link for the them to buy along 
                                with the price and user review for the product
                            """)
        
        prompt_chain = prompt_text | self.llm

        response = prompt_chain.invoke({
            "preference":state["preferences"]
        })

        return {"recommended_products":response.content}
    
    def confirm_order(self,state:StateAIPreference):
        System = PromptTemplate.from_template("""
                    give the order confirmation detail message based on the recommendation {recommendation},
                                              like how usually the confirmation order looks like        
                    """)
        p_text = System | self.llm
        result = p_text.invoke({
            "recommendation": state["recommended_products"]
        })
        return {"message": result.content}