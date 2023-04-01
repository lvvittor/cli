from typing import Optional
import openai
import os
import platform
import typer
import pyperclip

openai.api_key = os.getenv("OPENAI_API_KEY")

app = typer.Typer()


def is_unix_system():
    return platform.system().lower().startswith("lin") or platform.system().lower().startswith("dar")


# Show terminal options
if is_unix_system():
    from simple_term_menu import TerminalMenu
elif platform.system().lower().startswith("win"):
    import inquirer


@app.command()
def main(exe: bool = typer.Option(False), prompt: Optional[str] = typer.Argument("", help="The prompt to use")):  
    if exe:
        # API CALL, EXECUTABLES OR BASH SCRIPTS
        typer.launch("./ccli/videoPlugin.sh") # Can use the return value of the script to do something
        return
    
    is_user_satisfied = None

    try:
        while is_user_satisfied == None or not is_user_satisfied:
            if (is_user_satisfied == False):
                corrections = input("Indicaciones adicionales: ")
                prompt += f". {corrections}"
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an AI Terminal Copilot. Your job is to help users find the right terminal command in a bash shell on Linux. Just output the command the user is looking for, and nothing else. Do not make any comments, nor try to talk to the user in any way. Just output the bash command, iwthout any styling or comments. Don't add line breaks or quotes backticks or anything. If more than one command is requested, concatenate them with && so that they run one after the other. If the user asks for a command that is not possible, just output 'El comportamiento pedido no es posible de realizar actualmente.' instead of any commands."},
                    {"role": "user", "content": prompt},
                ],
            )

            answer = res["choices"][0]["message"]["content"]
            explanation = None

            is_user_satisfied = True

            typer.echo(answer)
            typer.echo("\n")

            # What to do with the answer

            options = ["Ejecutar", "Copiar", "Explicar", "Corregir", "Salir"]

            menu_entry_index = None

            while menu_entry_index == None or options[menu_entry_index] == "Explicar":
                if is_unix_system():
                    terminal_menu = TerminalMenu(options)
                    menu_entry_index = terminal_menu.show()
                elif platform.system().lower().startswith("win"):
                    questions = [
                        inquirer.List(
                            "menu_entry_index",
                            message="Acción a tomar",
                            choices=options,
                        ),
                    ]
                    answers = inquirer.prompt(questions)
                    menu_entry_index = options.index(answers["menu_entry_index"])

                if menu_entry_index == 0:
                    os.system(answer)
                    typer.echo("\n")
                elif menu_entry_index == 1:
                    print("> copied")
                    pyperclip.copy(answer)
                elif menu_entry_index == 2:
                    if explanation == None:
                        res = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are going to receive bash commands, along with other text. I want you to extract those bash commands, and output each one of them, separated by a \\n line break. Add a comment to explain in detail what the commands and their flags do."},
                                {"role": "user", "content": answer},
                            ],
                        )
                        explanation = res["choices"][0]["message"]["content"]

                    typer.echo(explanation)
                    typer.echo("\n")
                elif menu_entry_index == 3:
                    is_user_satisfied = False
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
