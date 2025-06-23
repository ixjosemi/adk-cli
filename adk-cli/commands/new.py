import typer
import os
from pathlib import Path
from .templates import AGENT_PY, RUNNER_PY, INIT_PY, ENV_EXAMPLE, STREAMLIT_APP_PY, TEST_AGENT_PY, DOCKERFILE, CLOUDRUN_YAML, GITIGNORE, README_MD, PYPROJECT_TOML

app = typer.Typer()


def new_project():
    """Scaffold a new Google ADK project."""
    project_name = typer.prompt("Project name", type=str)
    gcp_project = typer.prompt("GCP project name", type=str)
    ai_studio_api_key = typer.prompt("AI Studio API Key", hide_input=True)

    base_path = Path(project_name)
    if base_path.exists():
        typer.echo(f"Directory {project_name} already exists.")
        raise typer.Exit(code=1)

    # Create root project directory
    base_path.mkdir(parents=True)

    # Create main ADK files at root
    (base_path / "agent.py").write_text(AGENT_PY)
    (base_path / "runner.py").write_text(RUNNER_PY)
    (base_path / "__init__.py").write_text(INIT_PY)
    (base_path / ".env.example").write_text(ENV_EXAMPLE + f"AI_STUDIO_API_KEY={ai_studio_api_key}\nGCP_PROJECT={gcp_project}\n")
    (base_path / ".gitignore").write_text(GITIGNORE)
    (base_path / "README.md").write_text(README_MD.format(project_name=project_name))
    (base_path / "pyproject.toml").write_text(PYPROJECT_TOML)

    # Optional: Streamlit app and tests
    (base_path / "streamlit_app").mkdir()
    (base_path / "streamlit_app" / "app.py").write_text(STREAMLIT_APP_PY)
    (base_path / "tests").mkdir()
    (base_path / "tests" / "test_agent.py").write_text(TEST_AGENT_PY)
    (base_path / "deploy").mkdir()
    (base_path / "deploy" / "Dockerfile").write_text(DOCKERFILE)
    (base_path / "deploy" / "cloudrun.yaml").write_text(CLOUDRUN_YAML)

    typer.echo(f"Project {project_name} created successfully!")
