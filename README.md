# SDLC Automation with AI Agents

This project implements an automated Software Development Life Cycle (SDLC) process using AI agents. It leverages OpenAI's GPT models and the CrewAI framework to generate user stories and implement a basic product listing feature based on project requirements.

## Features

- Gather project requirements through a user-friendly Streamlit interface
- Generate user stories based on project requirements using an AI Product Manager agent
- Implement a basic product listing feature using an AI Developer agent
- Utilize CrewAI for orchestrating AI agent interactions
- Display generated user stories and implementation code in the Streamlit app

## Prerequisites

- Python 3.8+
- Poetry (for dependency management)
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sdlc-automation.git
   cd sdlc-automation
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

## Usage

1. Activate the Poetry virtual environment:
   ```
   poetry shell
   ```

2. Run the Streamlit app:
   ```
   streamlit run sdlc_agents/app.py
   ```

3. Open your web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

4. Fill in the project requirements in the Streamlit interface.

5. Click "Start SDLC Process" to generate user stories and implementation code.

## Project Structure

- `sdlc_agents/`
  - `app.py`: Main Streamlit application
  - `agents/`: Contains AI agent implementations
- `.env`: Environment variables (not tracked by Git)
- `pyproject.toml`: Poetry configuration and dependencies
- `README.md`: This file

## Technologies Used

- [Streamlit](https://streamlit.io/): For creating the web application interface
- [LangChain](https://python.langchain.com/): For building applications with large language models
- [CrewAI](https://github.com/joaomdmoura/crewAI): For orchestrating AI agent interactions
- [OpenAI GPT Models](https://openai.com/): For generating content and code

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for providing the GPT models
- Streamlit for the web application framework
- LangChain for the AI agent framework
- CrewAI for AI agent orchestration