from src.langgraphagenticai.state.state import StateCompetitor
from langchain_core.prompts import PromptTemplate
class NodeCompetitor:
    def __init__(self,llm):
        self.llm = llm

    def get_competitor_price(self,state:StateCompetitor):
        system = PromptTemplate.from_template(
            """ you are the best retail analysis LLM and best in the real time senerio fetching data
            we get the product name from the user, the product name {input},
            NOw the bigger task is to get the best brand for the product name and get the exact
            price of our competitor company the competitor name is {competitor}
            the result should be the "Name:Price"
            """
        )

        chain = system | self.llm

        response = chain.invoke({
            "input":state["product_name"],
            "competitor": state["competitor_name"]
        })

        return {"competitor_price":response.content}

    def get_our_price(self,state:StateCompetitor):
        system = PromptTemplate.from_template(
            """ you are the best retail analysis LLM and best in the real time senerio fetching data
            we get the product name from the user, the product name {input},
            NOw the bigger task is to get the best brand for the product name and get the exact
            price of our own company the company name is {our_company}
            the result should be the "Name:Price"
            """
        )

        chain = system | self.llm

        response = chain.invoke({
            "input":state["product_name"],
            "our_company":state["our_company"]
        })

        return {"our_price":response.content}

    def adjust_price(self,state:StateCompetitor):
        system = PromptTemplate.from_template(
            """ Now we have the both competitor {competitor} and our own company {company}
            data and we now need to adjust the price of our product
            we need to be caution that we have making it to profit venture
            but adjust the price and make it profitable for us and make comapny product
            give detailed report format da.
            """
        )

        chain = system | self.llm

        response = chain.invoke({
            "competitor":state["competitor_price"],
            "company":state["our_price"]
        })

        return {"adjust_price":response.content}

