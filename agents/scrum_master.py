# sdlc_agents/agents/scrum_master.py

from crewai import Agent

class ScrumMasterAgent(Agent):
    def __init__(self, llm, role, goal):
        super().__init__(
            name="Team Lead",
            role=role,
            goal=goal,
            backstory="An experienced team lead with a track record of successful project deliveries",
            llm=llm
        )

    def oversee_process(self, project_state):
        return self.run(f"""
        As a {self.role} with the goal to {self.goal}, oversee the current project state:
        {project_state}

        Provide guidance on:
        1. Next steps or priorities
        2. Potential risks or issues to address
        3. Any necessary adjustments to the project direction

        Your oversight should ensure the project is progressing effectively towards its goals.
        """)