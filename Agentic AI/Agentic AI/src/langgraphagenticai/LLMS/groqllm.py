from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,model,api_key):
        self.model = model
        self.api_key = api_key
    
    def init_model(self):
        if self.model and self.api_key:
            llm = ChatGroq(model=self.model,api_key=self.api_key)
            return llm