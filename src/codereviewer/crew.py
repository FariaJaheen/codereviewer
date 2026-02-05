from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Codereviewer():
    """Codereviewer crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['code_reviewer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def security_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['security_analyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def performance_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['performance_engineer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def software_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['software_architect'], # type: ignore[index]
            verbose=True
        )

    @agent
    def refactoring_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['refactoring_editor'], # type: ignore[index]
            verbose=True
        )


    @task
    def code_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_review_task'], # type: ignore[index]
        )

    @task
    def security_audit_task(self) -> Task:
        return Task(
            config=self.tasks_config['security_audit_task'], # type: ignore[index]
        )

    @task
    def performance_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['performance_review_task'], # type: ignore[index]
        )

    @task
    def refactor_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['refactor_strategy_task'], # type: ignore[index]
        )

    @task
    def refactor_implementation_task(self) -> Task:
        return Task(
            config=self.tasks_config['refactor_implementation_task'], # type: ignore[index]
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the Codereviewer crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
