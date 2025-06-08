# 🤖 Agents: Advanced AI Agent Implementations with LangGraph

Welcome to the **Agents** repository! This project is a comprehensive exploration of cutting-edge AI agent architectures, leveraging **LangGraph**, a powerful framework for building complex agentic workflows. From reasoning agents to advanced retrieval-augmented systems, this repository showcases innovative implementations designed to push the boundaries of AI reasoning, retrieval, interaction, and structured output generation. 🚀

## 📖 Project Overview

This repository serves as a hub for experimenting with and advancing AI agent technologies. I’ve implemented a diverse set of agent types, each tackling unique challenges in reasoning, retrieval, conversational tasks, and structured data processing. Using **LangGraph**, these implementations are modular, scalable, and efficient, making them ideal for research, experimentation, or real-world applications. Whether you're interested in agentic reasoning, retrieval-augmented generation (RAG), conversational AI, or structured output generation, there’s something here for you!

### 🛠️ What’s Implemented So Far

Here’s a rundown of the exciting work completed in this repository:

- **ReAct Agents**:  
  Built ReAct (Reasoning + Acting) agents from scratch, including versions with custom tools and LangGraph integration. These agents iteratively reason about tasks, act on decisions, and incorporate human feedback for improved decision-making (see `LangGraph/human_in_the_loop.ipynb`).

- **Corrective-RAG**:  
  Developed a Corrective Retrieval-Augmented Generation (RAG) system that enhances retrieval accuracy by iteratively refining retrieved information, ensuring more relevant and precise responses from the language model.

- **Self-RAG**:  
  Implemented a Self-RAG system where the agent autonomously evaluates and improves its retrieval process without relying on a language model for every step, optimizing for efficiency and accuracy.

- **Agentic RAG**:  
  Created an advanced Agentic RAG system that integrates agentic workflows with RAG, enabling dynamic reasoning over retrieved information and informed decision-making.

- **Simple LangGraph-Based Agents**:  
  Designed lightweight agents using LangGraph to perform tasks like task decomposition, state management, and workflow orchestration, serving as a foundation for more complex systems.

- **Chatbot with LangGraph**:  
  Built an interactive chatbot powered by LangGraph (`Bot_with_LangGraph/app.py`, `Bot_with_LangGraph/bot.py`), capable of maintaining conversational context, managing multi-turn dialogues, and integrating reasoning capabilities for more intelligent responses.

- **Structured Output Generation**:  
  Developed a system for generating structured outputs (e.g., JSON, tables) from agent workflows, useful for integrating AI outputs into downstream applications.

- **Database Integration**:  
  Integrated LangGraph agents with databases (`LG_Projects/employee.db`, `LG_Projects/SQL_db_agent_pro.ipynb`), enabling agents to query and manipulate structured data for tasks like employee management or data analysis.

- **Self-Ask Agent**:  
  Built a self-ask agent that autonomously generates follow-up questions to deepen its understanding and improve task performance.

### 📂 Repository Structure

The repository is organized into directories and files to make it easy to explore each implementation:

- **`Bot_with_LangGraph/`**: Chatbot implementation with LangGraph.
  - `app.py`: Main application for the chatbot.
  - `bot.py`: Core chatbot logic.
- **`LangGraph/`**: Core LangGraph-based agent implementations.
  - `LangGraphWithRAG.ipynb`: Agentic RAG implementation.
  - `basicLevelWithLLM.ipynb`: Corrective-RAG implementation.
  - `basicLevelWithoutLLM.ipynb`: Self-RAG implementation.
  - `human_in_the_loop.ipynb`: ReAct agents with human-in-the-loop feedback.
  - `llama3.txt`: Notes and configurations for LLaMA 3 integration.
- **`LG_Projects/`**: Database-integrated LangGraph projects.
  - `employee.db`: SQLite database for employee data.
  - `SQL_db_agent_pro.ipynb`: Agent for querying and managing the database.
- **`RAG_With_LangGraph/`**: Advanced RAG implementations.
  - `AgenticRAG(ARAG).ipynb`: Agentic RAG system.
  - `CorrectiveRAG.ipynb`: Corrective-RAG system.
  - `SRAG(SELF-RAG).ipynb`: Self-RAG system.
- **`ReAct_Agent_From_Very_Scratch/`**: ReAct agent implementations.
  - `ReAct_Agent.py`: Basic ReAct agent built from scratch.
  - `reactAgent_with_LG.py`: ReAct agent with LangGraph integration.
  - `ReAct_With_CUSTOM_tools.py`: ReAct agent with custom tools.
  - `SelfAsk.py`: Self-ask agent for autonomous question generation.
- **`structure_output.py`**: Script for generating structured outputs from agent workflows.

Each file contains detailed code, comments, and explanations to help you understand the implementation and adapt it for your own use cases.

## 🚀 Future Plans: Multi-AI Agents

The journey doesn’t stop here! I’m actively working on expanding this repository with **multi-AI agent systems**, including:

- **Supervisor Agents**: Agents that oversee and coordinate the activities of other agents, ensuring efficient task delegation and execution.
- **Network Agents**: A network of agents that collaborate and communicate to solve complex problems, leveraging collective intelligence.
- **Hierarchical Agents**: A hierarchical structure of agents where higher-level agents manage lower-level ones, enabling scalable and organized workflows.

These upcoming implementations aim to tackle advanced challenges in distributed AI systems, multi-agent collaboration, and hierarchical decision-making. Stay tuned for updates! 🌟

## 🧠 Why This Matters

AI agents are at the forefront of transforming how we interact with technology. By combining reasoning, retrieval, action-taking, and structured output generation, these agents can solve complex problems, automate workflows, and enhance human-AI collaboration. This repository serves as a playground for exploring these concepts, with practical implementations that you can build upon for research, experimentation, or real-world applications.

## 🛠️ Getting Started

### Prerequisites
- Python 3.8+
- Install dependencies:

#### Running the Code
Clone the repository:

```
git clone https://github.com/Sunilyadav03/Agents.git
cd Agents
```
Explore the `.ipynb` files or run Python scripts (e.g., python Bot_with_LangGraph/app.py) to test the implementations.

## 🌟 Contributing
Contributions are welcome! If you have ideas for new agent architectures, improvements, or bug fixes, feel free to open an issue or submit a pull request. Let’s build the future of AI agents together! 🤝

## 📜 License
This project is licensed under the MIT License—see the LICENSE file for details.

## 📬 Contact
For questions, feedback, or collaboration, reach out via: GitHub Issues ,LinkedIn: [Sunil Yadav](https://www.linkedin.com/in/sunil-yadav-96a541289/)

**Built with 💡 by Sunil Yadav | Last Updated: June 2025**
