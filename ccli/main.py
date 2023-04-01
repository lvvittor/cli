from typing import Optional

import typer

app = typer.Typer()


@app.command()
def main(prompt: Optional[str] = typer.Argument(..., help="The prompt to use")):
    if prompt:
        typer.echo(f"The prompt is: {prompt}")
    else:
        typer.echo("The prompt is not set")
