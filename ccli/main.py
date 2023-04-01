from typing import Optional
import openai
import os
import typer

openai.api_key = os.getenv("OPENAI_API_KEY")

app = typer.Typer()


def parse_output(ouput: str):
    typer.echo(ouput)


@app.command()
def main(prompt: Optional[str] = typer.Argument(..., help="The prompt to use")):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a linux terminal. Users will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside the tags <start> and <end>, and nothing else. do not write explanations. do not type commands unless i instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets {like this}. if you do not have access to the system's resources just output the command that would have been run. never, ever, respond with english words trying to talk to the user. you just output bash commands."},
                {"role": "user", "content": prompt},
            ],
        )
        answer = res["choices"][0]["message"]["content"]

        parse_output(answer)
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
