import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class ProductManagerAgent:
    def __init__(self, llm):
        self.llm = llm

    def create_user_stories(self, requirements):
        prompt = f"""
        Based on these project requirements, create 3-5 user stories:
        {requirements}
        
        Format each user story as:
        As a [type of user], I want [an action] so that [a benefit/a value].
        
        Include acceptance criteria for each story.
        """
        messages = [HumanMessage(content=prompt)]
        return self.llm(messages).content

class DeveloperAgent:
    def __init__(self, llm):
        self.llm = llm

    def implement_product_listing(self, user_stories):
        prompt = f"""
        Based on these user stories, provide Python code for a Flask app that implements a product listing page:
        {user_stories}
        
        Include both the Flask route and a simple HTML template.
        """
        messages = [HumanMessage(content=prompt)]
        return self.llm(messages).content

def initialize_chat_model():
    try:
        model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')  # Default to gpt-4-omni
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")
        return ChatOpenAI(model_name=model, api_key=api_key)
    except Exception as e:
        st.error(f"Error initializing ChatOpenAI model: {str(e)}")
        return None

def gather_requirements():
    st.subheader("Project Requirements")
    project_name = st.text_input("Project Name")
    project_description = st.text_area("Project Description")
    main_features = st.text_area("Main Features (one per line)")
    target_users = st.text_input("Target Users")
    
    requirements = {
        "Project Name": project_name,
        "Project Description": project_description,
        "Main Features": main_features.split('\n'),
        "Target Users": target_users,
    }
    
    return requirements

def main():
    st.title("SDLC Automation with AI Agents")

    chat_model = initialize_chat_model()

    if chat_model is None:
        st.error("Failed to initialize OpenAI model. Please check your API key and model settings.")
        return

    product_manager = ProductManagerAgent(chat_model)
    developer = DeveloperAgent(chat_model)

    requirements = gather_requirements()

    if st.button("Start SDLC Process"):
        with st.spinner("Creating user stories..."):
            user_stories = product_manager.create_user_stories(str(requirements))
            st.subheader("User Stories")
            st.write(user_stories)

        with st.spinner("Implementing product listing..."):
            implementation = developer.implement_product_listing(user_stories)
            st.subheader("Product Listing Implementation")
            st.code(implementation, language='python')

if __name__ == "__main__":
    main()