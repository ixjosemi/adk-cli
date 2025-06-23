import typer

from commands.new import new_project
from commands.deploy import deploy_project

app = typer.Typer(help="Google ADK CLI - Scaffold and deploy Google ADK projects.")

app.command()(new_project)
app.command()(deploy_project)

if __name__ == "__main__":
    app()
