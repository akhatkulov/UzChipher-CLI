import os
import sys 
import inquirer
import typer
import time 
from cipher_codes import *
def start_cli():
    sys.path.append(os.path.realpath("."))

    language = [
        inquirer.List(
            "lang",
            message=f"{typer.style('Choise workspace language',fg=typer.colors.RED)}",
            choices=[f"{typer.style('Uzbek',fg=typer.colors.GREEN)}", f"{typer.style('Russian',fg=typer.colors.GREEN)}", f"{typer.style('English',fg=typer.colors.GREEN)}"],
        ),
    ]

    answers = inquirer.prompt(language)
    language = answers['lang']
    with open('data/lang.txt','w+') as f:
        f.write(answers['lang'])
    with open('data/lang.txt','r+') as f:
            lang = f.read()
            if "Uzbek" in lang:
                time.sleep(0.4)
                typer.secho("Siz endi dasturni o'zbek tilida ishlatishingiz mumkin")
                cipher_type_uz = [
                    inquirer.List(
                    "type",
                message=f"{typer.style('Shifrlash va kodlash usullaridan birini tanlang',fg=typer.colors.RED)}",
            choices=[f"{typer.style('HILL',fg=typer.colors.GREEN)}", f"{typer.style('Sizar',fg=typer.colors.GREEN)}", f"{typer.style('Mirage',fg=typer.colors.GREEN)}",f"{typer.style('Morse',fg=typer.colors.GREEN)}"],
        ),
    ]
    y = inquirer.prompt(cipher_type_uz)
    if "HILL" in y['type']:
        hill_mode = [
            inquirer.List(
                "mode",
            message=f"{typer.style('Rejimni tanlang',fg=typer.colors.RED)}",
            choices = [f"{typer.style('Shifrlash/Kodlash',fg=typer.colors.GREEN)}",f"{typer.style('Shifrdan chiqarish/Koddan chiqarish',fg=typer.colors.GREEN)}"],
                                                                                                  
            ),
        ]

        x = inquirer.prompt(hill_mode)
        if "Shifrlash/Kodlash" in x:
            typer.echo("hello")

