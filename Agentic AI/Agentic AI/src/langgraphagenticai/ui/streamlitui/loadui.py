import streamlit as st
from src.langgraphagenticai.ui.uiconfigfile import Config
import os
from dotenv import load_dotenv
load_dotenv()

class LoadUI:
    def __init__(self):
        self.config = Config()
        self.control = {}

    def loadUI(self):
        st.set_page_config(page_title=self.config.get_page_title())
        st.header(self.config.get_page_title())

        with st.sidebar:
            llm_option = self.config.get_llm_options()
            model = self.config.get_groq_model_options()
            usecases = self.config.get_usecase_options()

            self.control["Selected_LLM"] = st.selectbox("Select the LLM ",llm_option)
            self.control["Selected_model"] = st.selectbox("Select the Model",model)
            self.control["Selected_usecase"] = st.selectbox("Select the Usecase",usecases)

            if self.control["Selected_LLM"] == "Groq":
                self.control["groq_api_key"] = Groq_api_key = st.text_input("Enter the Groq API Key",type="password")
            
            if not self.control["groq_api_key"]:
                st.warning("Please Provide the API Key")
            
        return self.control
            
            