# sdlc_agents/app.py

import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os
import base64
from agents.product_manager import ProductManagerAgent
from agents.developer import DeveloperAgent

# Load environment variables
load_dotenv()

def initialize_chat_model():
    try:
        model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
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

def extract_code_blocks(implementation):
    html_code = ""
    css_code = ""
    js_code = ""
    current_block = None
    
    for line in implementation.split('\n'):
        if line.startswith('```html'):
            current_block = 'html'
        elif line.startswith('```css'):
            current_block = 'css'
        elif line.startswith('```javascript'):
            current_block = 'js'
        elif line.startswith('```'):
            current_block = None
        elif current_block == 'html':
            html_code += line + '\n'
        elif current_block == 'css':
            css_code += line + '\n'
        elif current_block == 'js':
            js_code += line + '\n'
    
    return html_code, css_code, js_code

def create_html_file(html_code, css_code, js_code):
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Application</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>{css_code}</style>
    </head>
    <body>
    {html_code}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>{js_code}</script>
    </body>
    </html>
    """
    return full_html

def get_html_download_link(html_string, filename="index.html"):
    b64 = base64.b64encode(html_string.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="{filename}">Download HTML File</a>'
    return href

def main():
    st.title("SDLC Automation with AI Agents")

    chat_model = initialize_chat_model()

    if chat_model is None:
        st.error("Failed to initialize OpenAI model. Please check your API key and model settings.")
        return

    product_manager = ProductManagerAgent(
        llm=chat_model,
        role="Create and manage product backlog, define user stories",
        goal="Translate project requirements into clear, actionable user stories"
    )
    developer = DeveloperAgent(
        llm=chat_model,
        role="Implement features based on user stories",
        goal="Deliver high-quality, responsive web pages that meet project requirements"
    )

    requirements = gather_requirements()

    if st.button("Start SDLC Process"):
        with st.spinner("Creating user stories..."):
            user_stories = product_manager.create_user_stories(str(requirements))
            st.subheader("User Stories")
            st.write(user_stories)

        with st.spinner("Implementing web application..."):
            implementation = developer.implement_feature(user_stories)
            st.subheader("Web Application Implementation")
            st.code(implementation, language='html')

            html_code, css_code, js_code = extract_code_blocks(implementation)
            full_html = create_html_file(html_code, css_code, js_code)
            
            st.markdown(get_html_download_link(full_html), unsafe_allow_html=True)
            st.markdown("Download the HTML file and open it in your browser to see the implementation.")

if __name__ == "__main__":
    main()