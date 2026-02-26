from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class AgentTeam():
    """AgentTeam crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def strategy_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['strategy_lead'], # type: ignore[index]
            verbose=True
        )

    @agent
    def learner_research(self) -> Agent:
        return Agent(
            config=self.agents_config['learner_research'], # type: ignore[index]
            verbose=True
        )

    @agent
    def learning_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['learning_architect'], # type: ignore[index]
            verbose=True
        )

    @agent
    def instructional_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['instructional_designer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def storyboard(self) -> Agent:
        return Agent(
            config=self.agents_config['storyboard'], # type: ignore[index]
            verbose=True
        )

    @agent
    def media_producer(self) -> Agent:
        return Agent(
            config=self.agents_config['media_producer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def assessment_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['assessment_designer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def change_management(self) -> Agent:
        return Agent(
            config=self.agents_config['change_management'], # type: ignore[index]
            verbose=True
        )

    @agent
    def operations_librarian(self) -> Agent:
        return Agent(
            config=self.agents_config['operations_librarian'], # type: ignore[index]
            verbose=True
        )

    @agent
    def quality_review(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_review'], # type: ignore[index]
            verbose=True
        )

    @agent
    def qa(self) -> Agent:
        return Agent(
            config=self.agents_config['qa'], # type: ignore[index]
            verbose=True
        )

    @task
    def strategy_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['strategy_planning_task'], # type: ignore[index]
        )

    @task
    def learner_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['learner_analysis_task'], # type: ignore[index]
        )

    @task
    def curriculum_blueprint_task(self) -> Task:
        return Task(
            config=self.tasks_config['curriculum_blueprint_task'], # type: ignore[index]
        )

    @task
    def instructional_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['instructional_design_task'], # type: ignore[index]
        )

    @task
    def storyboard_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['storyboard_creation_task'], # type: ignore[index]
        )

    @task
    def media_specification_task(self) -> Task:
        return Task(
            config=self.tasks_config['media_specification_task'], # type: ignore[index]
        )

    @task
    def assessment_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['assessment_design_task'], # type: ignore[index]
        )

    @task
    def change_management_task(self) -> Task:
        return Task(
            config=self.tasks_config['change_management_task'], # type: ignore[index]
        )

    @task
    def library_organization_task(self) -> Task:
        return Task(
            config=self.tasks_config['library_organization_task'], # type: ignore[index]
        )

    @task
    def pedagogical_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['pedagogical_review_task'], # type: ignore[index]
        )

    @task
    def final_qa_validation_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_qa_validation_task'], # type: ignore[index]
            output_file='final_course_payload.json'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
