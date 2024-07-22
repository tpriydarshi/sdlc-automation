# sdlc_agents/agents/developer.py

from crewai import Agent

class DeveloperAgent(Agent):
    def __init__(self, llm, role, goal):
        super().__init__(
            name="Developer",
            role=role,
            goal=goal,
            backstory="A skilled developer with expertise in Python and web development",
            llm=llm
        )

    def implement_feature(self, user_stories):
        return self.run(f"""
        Implement the product listing feature based on these user stories:
        {user_stories}

        Provide a Python Flask implementation for the product listing page. Include:
        1. A route for the home page that displays the product list
        2. A simple HTML template for rendering the product list
        3. A sample product data structure

        Return the Python code for the implementation.
        """)