# adk-cli

A modern CLI tool to scaffold, develop, and deploy [Google ADK](https://google.github.io/adk-docs/) (Agent Development Kit) projects in Python.

## Features
- Quickly scaffold a new ADK agent project with best practices
- Generates agent, runner, .env, Streamlit chat, tests, and deployment files
- Supports [uv](https://github.com/astral-sh/uv) for fast dependency management
- Built-in deploy command for Google Cloud Run
- Pre-configured with [ruff](https://docs.astral.sh/ruff/) for linting
- Installable as a CLI tool: `adk-cli`

## Installation

### From PyPI (recommended)
Once published, you can install globally:
```bash
pip install adk-cli
```

### Local development
Clone this repo and install locally:
```bash
pip install .
```
Or, for development mode:
```bash
pip install -e .
```

## Usage

### Scaffold a new project
```bash
adk-cli new
```
You will be prompted for project name, GCP project, and API key. A new folder will be created with all necessary files.

### Deploy to Google Cloud Run
From within your generated project:
```bash
adk-cli deploy
```

### Run the agent locally
```bash
python runner.py
```

### Run the Streamlit chat UI
```bash
streamlit run streamlit_app/app.py
```

## Project Structure
```
myproject/
├── agent.py
├── runner.py
├── __init__.py
├── .env.example
├── pyproject.toml
├── README.md
├── streamlit_app/
│   └── app.py
├── tests/
│   └── test_agent.py
├── deploy/
│   ├── Dockerfile
│   └── cloudrun.yaml
└── ...
```

## Development
- The CLI is implemented in the `adk_cli` Python package.
- Entry point is defined in `pyproject.toml` as `adk-cli`.
- Uses [Typer](https://typer.tiangolo.com/) for CLI logic.
- To test locally, use `pip install -e .` and run `adk-cli` from anywhere.

## Contributing
PRs and issues welcome! Please lint with `ruff` and follow best practices for Python packaging and CLI design.

## License
Apache 2.0 