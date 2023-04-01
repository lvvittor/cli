from typing import Optional
import openai
import os
import typer

openai.api_key = os.getenv("OPENAI_API_KEY")

app = typer.Typer()


@app.command()
def main(prompt: Optional[str] = typer.Argument(..., help="The prompt to use")):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":
                "You are a linux terminal. Users will type commands and you will reply"
                "with what the terminal should show. I want you to only reply with the terminal output"
                "inside one unique code block, and nothing else. do not write explanations. "
                "do not type commands unless i instruct you to do so. when i need to tell you something in english,"
                "i will do so by putting text inside curly brackets {like this}."
                "if you do not have access to the system's resources just output the command that would have been run."
                "never, ever, respond with english words trying to talk to the user. you just output bash commands."},
            {"role": "user", "content": prompt},
        ],
    )

    answer = res["choices"][0]["message"]["content"]

    print(answer)
