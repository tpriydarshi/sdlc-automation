# sdlc_agents/agents/product_manager.py

from crewai import Agent

class ProductManagerAgent(Agent):
    def __init__(self, llm, role, goal):
        super().__init__(
            name="Product Manager",
            role=role,
            goal=goal,
            backstory="A seasoned product manager with a keen understanding of user needs and market trends",
            llm=llm
        )

    def create_user_stories(self, project_requirements):
        return self.run(f"""
        Create user stories based on these project requirements:
        {project_requirements}

        Focus on the essential features, especially the product listing functionality.
        For each user story, include:
        - A clear description in the format "As a [user], I want [feature] so that [benefit]"
        - Acceptance criteria

        Provide a prioritized list of 3-5 user stories.
        """)