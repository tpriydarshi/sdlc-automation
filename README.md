# SDLC Automation with AI Agents

[![Python](https://img.shields.io/badge/Python-3.10--3.13-blue)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Framework](https://img.shields.io/badge/Framework-CrewAI-green)](https://github.com/joaomdmoura/crewAI)

This project implements an automated Software Development Life Cycle (SDLC) process using AI agents. It leverages OpenAI's GPT models and the CrewAI framework to generate user stories and implement web applications based on project requirements.

## Quick Start

```bash
git clone https://github.com/tpriydarshi/sdlc-automation.git
cd sdlc-automation
cp .env.example .env        # Add your OpenAI API key
poetry install
poetry shell
streamlit run app.py
```

## Features

- Gather project requirements through a user-friendly Streamlit interface
- Generate user stories based on project requirements using an AI Product Manager agent
- Implement responsive web applications using an AI Developer agent
- Oversee project progress with an AI Scrum Master agent
- Utilize CrewAI for orchestrating AI agent interactions
- Download generated HTML implementations directly from the app

## Prerequisites

- Python 3.10 – 3.13
- [Poetry](https://python-poetry.org/docs/#installation) (for dependency management)
- An [OpenAI API key](https://platform.openai.com/api-keys)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tpriydarshi/sdlc-automation.git
   cd sdlc-automation
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Set up your environment variables:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your OpenAI API key.

   > **Note:** The `.env` file contains secrets and is excluded from version control via `.gitignore`. Never commit it.

## Usage

1. Activate the Poetry virtual environment:
   ```bash
   poetry shell
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

4. Fill in the project requirements in the Streamlit interface.

5. Click **"Start SDLC Process"** to generate user stories and a web application implementation.

## Project Structure

```
sdlc-automation/
├── app.py                        # Main Streamlit application
├── agents/
│   ├── product_manager.py        # Product Manager agent — generates user stories from requirements
│   ├── developer.py              # Developer agent — implements web apps (HTML/CSS/JS) from user stories
│   └── scrum_master.py           # Scrum Master agent — oversees project progress and provides guidance
├── .env.example                  # Template for environment variables
├── .gitignore
├── pyproject.toml                # Poetry configuration and dependencies
├── poetry.lock
└── README.md
```

## Technologies Used

- [Streamlit](https://streamlit.io/) — Web application interface
- [LangChain](https://python.langchain.com/) — LLM application framework
- [CrewAI](https://github.com/joaomdmoura/crewAI) — AI agent orchestration
- [OpenAI GPT Models](https://openai.com/) — Content and code generation

## Troubleshooting

| Problem | Solution |
|---|---|
| `OPENAI_API_KEY is not set` | Make sure you copied `.env.example` to `.env` and added a valid API key. |
| `ModuleNotFoundError` | Run `poetry install` and make sure you're inside `poetry shell`. |
| Port 8501 already in use | Stop the other Streamlit process, or run with `streamlit run app.py --server.port 8502`. |
| Poetry not found | Install Poetry: `curl -sSL https://install.python-poetry.org \| python3 -` |
| Python version mismatch | This project requires Python 3.10–3.13. Check with `python --version`. |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the GPT models
- [Streamlit](https://streamlit.io/) for the web application framework
- [LangChain](https://python.langchain.com/) for the LLM framework
- [CrewAI](https://github.com/joaomdmoura/crewAI) for AI agent orchestration
