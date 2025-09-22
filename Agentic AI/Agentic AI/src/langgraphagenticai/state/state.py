from typing import TypedDict

class State(TypedDict):
    ticket_id: int
    customer_name: str
    issue_type: str
    product_id: str
    issue: str
    description: str
    created_ticket: str

class StateAIPreference(TypedDict):
    message:str
    input:str
    preferences:str
    recommended_products:str

class StateCompetitor(TypedDict):
    product_name: str
    competitor_name: str
    our_company: str
    competitor_price: str
    our_price: str
    adjust_price: str