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

def hill_encode_ru():
        try:
            hill_txt = typer.prompt("Отправьте текст, который вы хотите зашифровать")
            hill_code = typer.prompt("Установите пароль для вашего пароля")
            hill_result = typer.style(hillEncrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Оригинальный текст',fg=typer.colors.GREEN)}",f"{typer.style('Пароль',fg=typer.colors.GREEN)}",f"{typer.style('Результат',fg=typer.colors.GREEN)}"],
                [f"{typer.style(hill_txt,fg=typer.colors.BLUE)}",f"{hill_code}",f"{hill_result}"],
            ]
            loading_func()
            typer.secho("Ваш текст зашифрован методом «HILL».",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))
        except ZeroDivisionError:
            loading_func()
            typer.secho("Вы допустили ошибку, пожалуйста, обратитесь к руководству пользователя еще раз.",fg=typer.colors.RED)
def hill_decode_ru():
        try:
            hill_txt = typer.prompt("Отправьте текст, который хотите расшифровать")
            hill_code = typer.prompt("Скажи пароль")
            hill_result = typer.style(hillDecrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Шифрованный текст',fg=typer.colors.GREEN)}",f"{typer.style('Пароль',fg=typer.colors.GREEN)}",f"{typer.style('Результат',fg=typer.colors.GREEN)}"],
                [f"{hill_text}",f"{hill_code}",f"{hill_result}"],
            ]
            loading_func()
            typer.secho("Ваш текст расшифрован методом «HILL».",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))

        except ZeroDivisionError:
            loading_func()
            typer.secho("Вы допустили ошибку, пожалуйста, обратитесь к руководству пользователя еще раз.g",fg=typer.colors.RED)
def morse_encode_ru():
        try:
            morse_txt = typer.prompt("Отправьте текст на кодировку")
            morse_result = typer.style(text_to_morse(morse_txt),fg=typer.colors.BLUE)
            morse_table = [
                [f"Оригинальный текст",f"Кодированный текст"],
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            loading_func()
            typer.echo(f"Отправьте текст, который хотите расшифровать",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Вы допустили ошибку, пожалуйста, обратитесь к руководству пользователя еще раз.",fg=typer.colors.RED)
def morse_decode_ru():
        try:
            morse_txt = typer.prompt("Отправьте текст, который хотите расшифровать")
            morse_result = typer.style(morse_to_text(morse_txt),fg=typer.colors.RED)
            morse_table = [
                [f"Кодированный текст",f"Результат"],
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]

            loading_func()
            typer.secho(f"Ваш текст расшифрован методом \"MORZE\".",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Вы допустили ошибку, пожалуйста, обратитесь к руководству пользователя еще раз.",fg=typer.colors.RED)
def caesar_encode_ru():
        try:
            caesar_txt = typer.prompt("Введите текст, который хотите зашифровать")
            caesar_num = typer.prompt("Отправьте одно из чисел от 1 до 27.")
            caesar_res = typer.style(caesar_encipher(caesar_txt,caesar_num),fg=typer.colors.BLUE)
            caesar_table = [
                [f"{typer.style('Оригинальный текст',fg=typer.colors.GREEN)}",f"{typer.style('Пароль',fg=typer.colors.GREEN)}",f"{typer.style('Результат',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.BLUE)},"f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            loading_func()
            typer.secho("Ваш текст расшифрован методом «Сизар».",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Вы допустили ошибку, пожалуйста, обратитесь к руководству пользователя еще раз.",fg=typer.colors.RED)
def caesar_decode_ru():
        try:
            caesar_txt = typer.prompt("Отправьте текст, который хотите расшифровать")
            caesar_num = typer.prompt("Отправьте число от 1 до 27 для расшифровки")
            caesar_res = typer.style(caesar_decipher(caesar_txt,caesar_num),fg=typer.colors.BLACK)
            caesar_table = [
                [f"{typer.style('Шифрованный текст',fg=typer.colors.GREEN)},"f"{typer.style('Пароль',fg=typer.colors.GREEN)}",f"{typer.style('Результат',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.BLUE)}",f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            loading_func()
            typer.secho("Ваш текст расшифрован в вашем методе «Сизар»",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Вы допустили ошибку, пожалуйста, обратитесь к руководству пользователя еще раз.",fg=typer.colors.RED)
def mirage_encode_ru():
        try:
            mirage_txt = typer.prompt("Отправьте текст, который вы хотите зашифровать")
            mirage_res = typer.style(en_mirage(mirage_txt),fg=typer.colors.RED)
            mirage_table = [
                [f"Оригинальный текст",f"Кодированный текст"],
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            loading_func()
            typer.secho(f"Ваш текст закодирован методом «Мираж».",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Вы допустили ошибку, пожалуйста, обратитесь к руководству пользователя еще раз.",fg=typer.colors.RED)
def mirage_decode_ru():
        try:
            mirage_txt = typer.prompt("Отправьте текст, который хотите расшифровать")
            mirage_res = typer.style(de_mirage(mirage_txt),fg=typer.colors.RED)
            mirage_table = [
                [f"Кодированный текст",f"Результат"]
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            loading_func()
            typer.echo(f"Ваш текст был декодирован с помощью программы «Мираж».",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Вы допустили ошибку, пожалуйста, обратитесь к руководству пользователя еще раз.",fg=typer.colors.RED)
