import typer
import tabulate
from cipher_codes import *
from helper import *
import time
from tabulate import tabulate


def loading_func():
    with typer.progressbar(range(10))as sp:
        for i in sp:

            time.sleep(0.1)
        time.sleep(0.3)

def hill_encode_en():
        try:
            hill_txt = typer.prompt("Send the text you want to encrypt")
            hill_code = typer.prompt("Enter a passwor for encrypt")
            hill_result = typer.style(hillEncrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Original text',fg=typer.colors.GREEN)}",f"{typer.style('Password',fg=typer.colors.GREEN)}",f"{typer.style('Result',fg=typer.colors.GREEN)}"],
                [f"{typer.style(hill_txt,fg=typer.colors.BLUE)}",f"{hill_code}",f"{hill_result}"],
            ]
            loading_func()
            typer.secho("Your text has been encrypted using the \"HILL\" method",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))
        except ZeroDivisionError:
            loading_func()
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
def hill_decode_en():
        try:
            hill_txt = typer.prompt("Send to text you want to decrypt")
            hill_code = typer.prompt("Enter a passwor for decrypt")
            hill_result = typer.style(hillDecrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Cipher text',fg=typer.colors.GREEN)}",f"{typer.style('Password',fg=typer.colors.GREEN)}",f"{typer.style('Result',fg=typer.colors.GREEN)}"],
                [f"{typer.style(hill_txt,fg=typer.colors.BLUE)}",f"{hill_code}",f"{hill_result}"],
            ]
            loading_func()
            typer.secho("Your text has been decrypted using the \"HILL\" method",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))

        except ZeroDivisionError:
            loading_func()
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
def morse_encode_en():
        try:
            morse_txt = typer.prompt("Give me text to encode ")
            morse_result = typer.style(text_to_morse(morse_txt),fg=typer.colors.BLUE)
            morse_table = [
                [f"Original text",f"Coded text"],
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            loading_func()
            typer.secho(f"Your text has been encoded using the \"MORZE\" method",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
def morse_decode_en():
        try:
            morse_txt = typer.prompt("Giv me text to decode")
            morse_result = typer.style(morse_to_text(morse_txt),fg=typer.colors.BLUE)
            morse_table = [
                [f"Coded text",f"Original text"],
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            loading_func()
            typer.secho(f"Your text has been decoded using the \"MORZE\" method",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
def caesar_encode_en():
        try:
            caesar_txt = typer.prompt("Send the text you want to encrypt")
            caesar_num = typer.prompt("Send one of the numbers from 1 to 27")
            caesar_res = typer.style(caesar_encipher(caesar_txt,caesar_num),fg=typer.colors.BLUE)
            caesar_table = [
                [f"{typer.style('Original text',fg=typer.colors.GREEN)}",f"{typer.style('Password',fg=typer.colors.GREEN)}",f"{typer.style('Result',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.BLUE)},"f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            loading_func()
            typer.secho("Your text has been decrypted using the \"Caesar\" method",fg=typer.colors.CYAN,bold=True)
            print(tabulate(caesar_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
def caesar_decode_en():
        try:
            caesar_txt = typer.prompt("Send the text you want to decrypt")
            caesar_num = typer.prompt("Send one number of the number from 1 to 27")
            caesar_res = typer.style(caesar_decipher(caesar_txt,caesar_num),fg=typer.colors.BLUE)
            caesar_table = [
                [f"{typer.style('Cipher Text',typer.colors.GREEN)}",f"{typer.style('Password',fg=typer.colors.GREEN)}",f"{typer.style('Result',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.RED)}",f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            loading_func()
            typer.secho("Your text has been decrypted using the \"Caesar\" method",fg=typer.colors.CYAN,bold=True)
            print(tabulate(caesar_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
def mirage_encode_en():
        try:
            mirage_txt = typer.prompt("Give me text to encode")
            mirage_res = typer.style(en_mirage(mirage_txt),fg=typer.colors.BLUE)
            mirage_table = [
                [f"Original text",f"Coded text"],
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            loading_func()
            typer.secho(f"Your text has been encoded using the \"Mirage\" method",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
def mirage_decode_en():
        try:
            mirage_txt = typer.prompt("Give me text to decode")
            mirage_res = typer.style(de_mirage(mirage_txt),fg=typer.colors.BLUE)
            mirage_table = [
                [f"Coded text",f"Result"],
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            loading_func()
            typer.secho(f"Your text has been decoded using \"Mirage\".",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("You've made a mistake. Check out the user guide",fg=typer.colors.RED)