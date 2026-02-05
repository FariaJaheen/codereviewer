# Codereviewer Crew
**Autonomous Multi-Agent Code Review & Refactoring System using CrewAI**

Welcome to the Codereviewer Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

Codereviewer is an intelligent multi-agent AI system built using the **CrewAI open-source framework** that performs automated:

- Code review  
- Security analysis  
- Performance optimization  
- Architectural refactoring  
- Clean code generation  

The system simulates a collaborative **AI software engineering team** where specialized agents work together to analyze and improve real-world codebases.

---

# Project Overview

Modern software systems require continuous review, optimization, and refactoring. Codereviewer automates this process using a coordinated crew of AI agents that collaborate like an experienced engineering team.

Given a codebase, Codereviewer:

1. Reviews code quality and logic  
2. Detects security vulnerabilities  
3. Identifies performance bottlenecks  
4. Proposes architectural improvements  
5. Generates refactored production-ready code  

This project demonstrates real-world **agentic AI orchestration** for developer productivity and intelligent automation.

---

# System Architecture

The system is composed of specialized AI agents:

| Agent | Responsibility |
|------|---------------|
| **Code Reviewer** | Detect bugs, smells, and maintainability issues |
| **Security Analyst** | Identify vulnerabilities and unsafe practices |
| **Performance Engineer** | Optimize efficiency and scalability |
| **Software Architect** | Design refactoring strategy |
| **Refactoring Editor** | Produce clean improved code |

Agents collaborate sequentially using CrewAI orchestration.

---

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/codereviewer/config/agents.yaml` to define your agents
- Modify `src/codereviewer/config/tasks.yaml` to define your tasks
- Modify `src/codereviewer/crew.py` to add your own logic, tools and specific args
- Modify `src/codereviewer/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the codereviewer Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The codereviewer Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Project Structure

```
codereviewer/
│
├── src/codereviewer/
│   ├── config/
│   │   ├── agents.yaml
│   │   └── tasks.yaml
│   │
│   ├── crew.py          # Multi-agent orchestration
│   ├── main.py          # Entry point
│   └── sample_app.py    # Example codebase for testing
│
├── .env
├── pyproject.toml
└── README.md
```

Let's create wonders together with the power and simplicity of crewAI.

## Author

Faria Jaheen
AI Researcher
Specializing in:
	•	Multi-agent AI systems
	•	Generative AI engineering
	•	Autonomous software systems
	•	Intelligent developer tooling
