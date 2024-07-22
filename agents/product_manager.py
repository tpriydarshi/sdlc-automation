# sdlc_agents/agents/product_manager.py

from crewai import Agent
from langchain.schema import HumanMessage

class ProductManagerAgent(Agent):
    def __init__(self, llm, role, goal):
        super().__init__(
            name="Product Manager",
            role=role,
            goal=goal,
            backstory="An experienced product manager with a keen understanding of user needs and market trends",
            llm=llm
        )
        self.llm = llm

    def create_user_stories(self, requirements):
        prompt = f"""
        Based on these project requirements, create 3-5 user stories:
        {requirements}
        
        Format each user story as:
        As a [type of user], I want [an action] so that [a benefit/a value].
        
        Include acceptance criteria for each story.

        Ensure the user stories cover the main features and align with the project description and target users.
        Prioritize the most important functionalities first.

        Return the user stories in a clear, numbered list format.
        """
        messages = [HumanMessage(content=prompt)]
        return self.llm(messages).content

    def prioritize_backlog(self, user_stories):
        prompt = f"""
        Prioritize the following user stories for the product backlog:
        {user_stories}

        Consider the following factors:
        1. Business value
        2. User impact
        3. Dependencies between stories
        4. Complexity and effort required

        Provide a prioritized list of the user stories with brief explanations for their priority.
        """
        messages = [HumanMessage(content=prompt)]
        return self.llm(messages).content