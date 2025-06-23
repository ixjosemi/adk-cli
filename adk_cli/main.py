import typer

from adk_cli.commands.new import new_project
from adk_cli.commands.deploy import deploy_project

app = typer.Typer(help="Google ADK CLI - Scaffold and deploy Google ADK projects.")

app.command()(new_project)
app.command()(deploy_project) 