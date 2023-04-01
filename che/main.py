from typing import Optional
import openai
import os
import typer

openai.api_key = os.getenv("OPENAI_API_KEY")

app = typer.Typer()


def parse_output(ouput: str):
    typer.echo(ouput)


@app.command()
def main(exe: bool = typer.Option(False), prompt: Optional[str] = typer.Argument("", help="The prompt to use")):  
    if exe:
        # API CALL, EXECUTABLES OR BASH SCRIPTS
        typer.launch("./ccli/videoPlugin.sh")
        return
    
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI Terminal Copilot. Your job is to help users find the right terminal command in a bash shell on Linux. Just output the command the user is looking for, and nothing else. Do not make any comments, nor try to talk to the user in any way. Just output the bash command, iwthout any styling or comments. Don't add line breaks or quotes backticks or anything"},
                {"role": "user", "content": prompt},
            ],
        )

        answer = res["choices"][0]["message"]["content"]

        commands = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are going to receive bash commands, along with other text. I want you to extract those bash commands, and output each one of them, separated by a \\n line break. Add a comment to explain in detail what the commands and their flags do."},
                {"role": "user", "content": answer},
            ],
        )

        command = commands["choices"][0]["message"]["content"]

        typer.echo(answer)

        typer.echo(command)
        
    except openai.error.APIError as e:
        print(f"An API error occurred: {e}")
    except openai.error.AuthenticationError as e:
        print(f"An authentication error occurred: {e}")
    except openai.error.InvalidRequestError as e:
        print(f"An invalid request error occurred: {e}")
    except openai.error.RateLimitError as e:
        print(f"A rate limit error occurred: {e}")
    except openai.error.OpenAIError as e:
        print(f"An unknown error occurred: {e}")