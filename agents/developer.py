# sdlc_agents/agents/developer.py

from crewai import Agent
from langchain.schema import HumanMessage

class DeveloperAgent(Agent):
    def __init__(self, llm, role, goal):
        super().__init__(
            name="Developer",
            role=role,
            goal=goal,
            backstory="A versatile front-end developer with expertise in HTML, CSS, JavaScript, and modern web development practices",
            llm=llm
        )
        self.llm = llm

    def implement_feature(self, user_stories):
        prompt = f"""
        Implement a web application based on these user stories and requirements:
        {user_stories}

        Provide a web implementation using HTML, CSS (with Bootstrap 5), and JavaScript. Include:
        1. An HTML file with the structure of the web app, using Bootstrap 5 classes for styling and layout.
        2. Custom CSS for any additional styling needs beyond Bootstrap.
        3. A JavaScript file for interactivity and dynamic content.

        Ensure the implementation covers the main functionality described in the user stories.
        Create a professional-looking, user-friendly web application. Consider the following:
        - Use Bootstrap 5 components and utilities to create a modern, responsive design.
        - Implement a clean layout with proper spacing and alignment.
        - Include appropriate navigation elements based on the application's requirements.
        - Use Bootstrap's grid system for layout structure.
        - Ensure good color contrast and readability.
        - Add subtle animations or transitions to improve user experience, if appropriate.
        - Implement JavaScript functionality as required by the user stories.

        Adapt the following elements based on the specific requirements:
        - A responsive navigation structure suitable for the application type.
        - Main content area showcasing key features or information.
        - Interactive elements as specified in the user stories.
        - Forms or data input methods if required by the application.
        - Footer with relevant links or information.

        Provide the code for each file (HTML, CSS, JavaScript) separately, clearly labeled.
        Include comments in the code to explain key functionalities and structure.

        Focus on creating a versatile front-end implementation that can be easily adapted to various types of web applications. 
        Ensure the design and functionality align closely with the provided user stories and requirements.
        """
        messages = [HumanMessage(content=prompt)]
        return self.llm(messages).content

    def write_unit_tests(self, implementation):
        prompt = f"""
        Based on this web implementation, write unit tests to verify the key functionalities:
        {implementation}

        Include tests for:
        1. DOM structure and content
        2. Event handling for interactive elements
        3. UI responsiveness
        4. Any specific features mentioned in the user stories

        Use a JavaScript testing framework like Jest. Provide the test code and brief explanations for each test.
        Focus on front-end testing only, without any backend or server-side tests.
        Ensure the tests are adaptable to the specific type of web application implemented.
        """
        messages = [HumanMessage(content=prompt)]
        return self.llm(messages).content