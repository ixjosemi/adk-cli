import typer
import subprocess
from pathlib import Path


def deploy_project():
    """Deploy the current project to Google Cloud Run."""
    typer.echo("Deploying to Google Cloud Run...")
    # Build Docker image
    project_name = Path.cwd().name
    image_name = f"gcr.io/$GCP_PROJECT/{project_name}:latest"
    typer.echo(f"Building Docker image: {image_name}")
    subprocess.run(["docker", "build", "-t", image_name, "."], check=True)
    # Push Docker image
    typer.echo(f"Pushing Docker image: {image_name}")
    subprocess.run(["docker", "push", image_name], check=True)
    # Deploy to Cloud Run
    typer.echo("Deploying to Cloud Run...")
    subprocess.run(
        [
            "gcloud",
            "run",
            "deploy",
            project_name,
            "--image",
            image_name,
            "--platform",
            "managed",
            "--region",
            "us-central1",
            "--allow-unauthenticated",
        ],
        check=True,
    )
    typer.echo("Deployment complete!")
