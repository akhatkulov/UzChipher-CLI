import typer
import tabulate
from helper import *
from cipher_codes import *
import time
from tabulate import tabulate


def loading_func():
    with typer.progressbar(range(10))as sp:
        for i in sp:

            time.sleep(0.1)
        time.sleep(0.3)

def hill_encode_uz():
    try:
        hill_txt = typer.prompt("Shiflamoqchi bo'lgan matningizni yuboring")
        hill_code = typer.prompt("Shifringizga parol qo'ying")
        hill_result = typer.style(hillEncrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
        hill_code = typer.style(hill_code,fg=typer.colors.RED)
        hill_table = [
            [f"{typer.style('Asl matn',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
            [f"{typer.style(hill_txt,fg=typer.colors.BLUE)}",f"{hill_code}",f"{hill_result}"],
        ]
        loading_func()
        typer.secho("Sizning matningiz \"HILL\" usulida  shifrlandi",fg=typer.colors.CYAN,bold=True)
        print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))
    except ZeroDivisionError:
        loading_func()
        typer.secho("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
def hill_decode_uz():
        try:
            hill_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            hill_code = typer.prompt("Shifr parolini ayting")
            hill_result = typer.style(hillDecrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Shifrlangan matn',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(hill_txt,fg=typer.colors.BLUE)}",f"{hill_code}",f"{hill_result}"],
            ]
            loading_func()
            typer.secho("Sizning \"HILL\" usulida matningiz shifrdan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))

        except ZeroDivisionError:
            loading_func()
            typer.secho("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
def morse_encode_uz():
        try:
            morse_txt = typer.prompt("Kodlash uchun matningizni yuboring ")
            morse_result = typer.style(text_to_morse(morse_txt),fg=typer.colors.BLUE)
            morse_table = [
                [f"Asl matn",f"Kodlangan matn"],
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            loading_func()
            typer.secho(f"Sizning matningiz \"MORSE\"usulida kodlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
def morse_decode_uz():
        try:
            
            morse_txt = typer.prompt("Koddan chiqarmoqchi bo'lgan matningizni yuboring")
            morse_result = typer.style(morse_to_text(morse_txt),fg=typer.colors.RED)
            morse_table = [
                [f"Kodlangan matn",f"Asl matn"],
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            loading_func()
            typer.secho(f"Sizning matningiz \"MORSE\"usulida koddan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
def caesar_encode_uz():
        try:
            caesar_txt = typer.prompt("Shifrlamoqchi bo'lgan matningizni bering")
            caesar_num = typer.prompt("1dan 27gacha bo'lgan sonlardan birini yuboring")
            caesar_res = typer.style(caesar_encipher(caesar_txt,caesar_num),fg=typer.colors.BLUE)
            caesar_table = [
                [f"{typer.style('Asl matn',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.BLUE)}",f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            loading_func()
            typer.secho("Sizning \"Sizar\" usulida matningiz shifrlandi chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(caesar_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
def caesar_decode_uz():
        try:
            caesar_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            caesar_num = typer.prompt("Shiifrdan chiqarish uchun 1dan 27gacha bo'lgan son yuboring")
            caesar_res = typer.style(caesar_decipher(caesar_txt,caesar_num),fg=typer.colors.BLACK)
            caesar_table = [
                [f"{typer.style('Shifr matni',fg=typer.colors.GREEN)},"f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.BLUE)}",f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            loading_func()
            typer.secho("Sizning \"Sizar\" usulida matningiz shifrdan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(caesar_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
def mirage_encode_uz():
        try:
            mirage_txt = typer.prompt("Shifrlamoqchi bo'lgan matningizni yuboring")
            mirage_res = typer.style(en_mirage(mirage_txt),fg=typer.colors.RED)
            mirage_table = [
                [f"Asl matn",f"Kodlangan matn"],
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            loading_func()
            typer.secho(f"Sizning matningiz \"Mirage\" usulida kodlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
def mirage_decode_uz():
        try:
            mirage_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            mirage_res = typer.style(de_mirage(mirage_txt),fg=typer.colors.RED)
            mirage_table = [
                [f"Asl matn",f"Kodlangan matn"],
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            loading_func()
            typer.secho(f"Sizning matningiz \"Mirage\"usulida koddan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            loading_func()
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
