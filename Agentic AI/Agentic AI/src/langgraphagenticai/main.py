from src.langgraphagenticai.ui.streamlitui.loadui import LoadUI
import streamlit as st
from langchain_groq import ChatGroq
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import Graph
from src.langgraphagenticai.graph.graph_builder_ai_preference import GraphAiPreference
from src.langgraphagenticai.graph.graph_builder_competitor import GraphCompetitor

def load_langgraph_agenticai_app():
    ui = LoadUI().loadUI()
    selected_llm = ui["Selected_LLM"]
    groq_api_key = ui["groq_api_key"]
    selected_model = ui["Selected_model"]
    selected_usecase = ui["Selected_usecase"]

    if selected_llm and groq_api_key:
        print("nmnm",selected_model , groq_api_key)
        llm = GroqLLM(selected_model,groq_api_key).init_model()

    if not llm:
        st.error("Model Not Initiated")

    if selected_usecase == "Customer Service AI Agent":
        with st.form("Form"):
            customer_name = st.text_input("Enter Your Name")
            product_id = st.text_input("Enter ID")
            issue = st.text_input("Your Issue")
            submitted = st.form_submit_button("Submit")
        
        if submitted:
            graph = Graph(llm)
            graph_builder = graph.init_graph()

            if graph_builder:
                response = graph_builder.invoke({
                    "customer_name":customer_name,
                    "product_id":product_id,
                    "issue":issue
                })
                st.success("✅ Ticket processed successfully!")

                st.markdown(f"""
                ### 🧑‍💼 Customer Info
                - **Name:** {response.get('customer_name')}
                - **Product ID:** {response.get('product_id')}
                - **Issue Type:** {response.get('issue_type')}
                - **Reported Issue:** {response.get('issue')}
                ---  
                """)

                with st.expander("📝 Troubleshooting Guidance"):
                    st.markdown(response.get("description", "No description provided."))

                with st.expander("🎫 Ticket Details"):
                    st.markdown(response.get("created_ticket", "No ticket created."))

    elif selected_usecase == "AI Personal Shopping Assistant":
        st.caption("Conversational agent recommending products and placing orders for customers")
        input_preference = st.chat_input("Enter the Preference")
        if input_preference:
            graph = GraphAiPreference(llm).init_graph()
            if graph:
                response = graph.invoke({
                    "input":input_preference
                })

                st.success("Successfully Fetched")

                st.markdown(f"""### Customer Preferences {response.get("preferences")}""")

                st.markdown(response.get("recommended_products", "NIL."))

                with st.expander("Check Message For the Details"):
                    st.markdown(response.get("message"))

    elif selected_usecase == "Dynamic Pricing Agent":
        with st.form("Dynamic Price Adjustment"):
            competitor_name = st.text_input("Enter the Competitor Name")
            our_company = st.text_input("Enter Our Company Name")
            product_name = st.text_input("Enter product Name you wanna dynamically Adjust")
            submitted = st.form_submit_button("Analyze...")

        if submitted:
            graph = GraphCompetitor(llm).init_graph()

            if graph:
                response = graph.invoke({
                    "product_name":product_name,
                    "competitor_name":competitor_name,
                    "our_company": our_company
                })

                st.success("Analyzed Price and Adjusted")

                st.markdown(f"""### Dynamic Price Adjustment of {response.get("product_name")} with respect to our competitor {response.get("competitor_name")}""")

                st.markdown(f"""### Our Current Price {response.get("our_price")}""")
                st.markdown(f"""### Our Competitor Price {response.get("competitor_price")}""")

                st.markdown(response.get("adjust_price"))