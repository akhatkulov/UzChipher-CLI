#################Librarys for CLI tool####################
import typer
from typing import Optional
import os
import pyfiglet
from tabulate import tabulate
################ My Cryptography Codes #####################
from connecter import *

# os.system('clear')
################ Start Typer Coding #####################################
def main(x: Optional[str] = typer.Argument('home',help="Section"),mode: Optional[str]= typer.Argument('m--encode',help='Mode') , lang: Optional[str] =  typer.Argument('en',help="Program's Language")):
    os.system('clear')
    if x == "home":
        print(pyfiglet.figlet_format("UzChipher",font='slant',justify='center',width=150))
        


######################This section about uzbek language  #################################################
    elif x == "hill" and mode == "m--encode" and lang == "uz":
        try:
            hill_txt = typer.prompt("Shiflamoqchi bo'lgan matningizni yuboring")
            hill_code = typer.prompt("Sifringizga parol qo'ying")
            hill_result = typer.style(hillEncrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Asl matn',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(hill_txt,fg=typer.colors.BLUE)}",f"{hill_code}",f"{hill_result}"],
            ]
            typer.secho("Sizning \"HILL\" usulida matningiz shifrlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))
        except ZeroDivisionError:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)


    elif x == "hill" and mode == "m--decode" and lang == "uz":
        try:
            hill_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            hill_code = typer.prompt("Sifr parolini ayting")
            hill_result = typer.style(hillDecrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Shifrlangan matn',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(hill_txt,fg=typer.colors.BLUE)}",f"{hill_code}",f"{hill_result}"],
            ]
            typer.secho("Sizning \"HILL\" usulida matningiz shifrdan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))

        except ZeroDivisionError:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)

    elif x == "morse" and mode == "m--encode" and lang == "uz":
        try:
            morse_txt = typer.prompt("Kodlash uchun matningizni yuboring ")
            morse_result = typer.style(text_to_morse(morse_txt),fg=typer.colors.BLUE)
            morse_table = [
                [f"Asl matn",f"Kodlangan matn"],
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            typer.secho(f"Sizning matningiz \"MORSE\"usulida kodlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
    elif x == "morse" and mode == "m--decode" and lang == "uz":
        try:
            morse_txt = typer.prompt("Koddan chiqarmoqchi bo'lgan matningizni yuboring")
            morse_result = typer.style(morse_to_text(morse_txt),fg=typer.colors.RED)
            morse_table = [
                [f"Kodlangan matn",f"Asl matn"],
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            typer.secho(f"Sizning matningiz \"MORSE\"usulida koddan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
    elif x == "caesar" and mode == "m--encode" and lang == "uz":
        try:
            caesar_txt = typer.prompt("Sifrlamoqchi bo'lgan matningizni bering")
            caesar_num = typer.prompt("1dan 27gacha bo'lgan sonlardan birini yuboring")
            caesar_res = typer.style(caesar_encipher(caesar_txt,caesar_num),fg=typer.colors.BLUE)
            caesar_table = [
                [f"{typer.style('Asl matn',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.BLUE)}"f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            typer.secho("Sizning \"Sizar\" usulida matningiz shifrlandi chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(caesar_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
        
    elif x == "caesar" and mode == "m--decode" and lang == "uz":
        try:
            caesar_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            caesar_num = typer.prompt("Shiifrdan chiqarish uchun 1dan 27gacha bo'lgan son yuboring")
            caesar_res = typer.style(caesar_decipher(caesar_txt,caesar_num),fg=typer.colors.BLACK)
            caesar_table = [
                [f"{typer.style('Shifr matni',fg=typer.colors.GREEN)},"f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.BLUE)}",f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            typer.secho("Sizning \"Sizar\" usulida matningiz shifrdan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(caesar_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
    elif x == "mirage" and  mode == "m--encode" and lang == "uz":
        try:
            mirage_txt = typer.prompt("Shifrlamoqchi bo'lgan matningizni yuboring")
            mirage_res = typer.style(en_mirage(mirage_txt),fg=typer.colors.RED)
            mirage_table = [
                [f"Asl matn",f"Kodlangan matn"]
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            typer.echo(f"Sizning matningiz \"Mirage\" usulida kodlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
    elif x == "mirage" and mode == "m--decode" and lang == "uz":
        try:
            mirage_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            mirage_res = typer.style(de_mirage(mirage_txt),fg=typer.colors.RED)
            mirage_table = [
                [f"Asl matn",f"Kodlangan matn"]
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            typer.echo(f"Sizning matningiz \"Mirage\"usulida koddan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
##################### This section about English ##################################################
    elif x == "hill" and mode == "m--encode" and lang == "en":
        try:
            hill_txt = typer.prompt("Send the text you want to encrypt")
            hill_code = typer.prompt("Enter a passwor for encrypt")
            hill_result = typer.style(hillEncrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Asl matn',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(hill_txt,fg=typer.colors.BLUE)}",f"{hill_code}",f"{hill_result}"],
            ]
            typer.secho("Sizning \"HILL\" usulida matningiz shifrlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))
        except ZeroDivisionError:
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)


    elif x == "hill" and mode == "m--decode" and lang == "en":
        try:
            hill_txt = typer.prompt("Send to text you want to decrypt")
            hill_code = typer.prompt("Enter a passwor for decrypt")
            hill_result = typer.style(hillDecrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Shifr matni',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(hill_txt,fg=typer.colors.BLUE)}",f"{hill_code}",f"{hill_result}"],
            ]
            typer.secho("Sizning \"HILL\" usulida matningiz shifrdan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))

        except ZeroDivisionError:
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)

    elif x == "morse" and mode == "m--encode" and lang == "en":
        try:
            morse_txt = typer.prompt("Give me text to encode ")
            morse_result = typer.style(text_to_morse(morse_txt),fg=typer.colors.BLUE)
            morse_table = [
                [f"Asl matn",f"Kodlangan matn"],
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            typer.secho(f"Sizning matningiz \"MORSE\"usulida kodlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
    elif x == "morse" and mode == "m--decode" and lang == "en":
        try:
            morse_txt = typer.prompt("Giv me text to decode")
            morse_result = typer.style(morse_to_text(morse_txt),fg=typer.colors.RED)
            morse_table = [
                [f"Kodlangan matn",f"Asl matn"],
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            typer.secho(f"Sizning matningiz \"MORSE\"usulida koddan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
    elif x == "caesar" and mode == "m--encode" and lang == "en":
        try:
            caesar_txt = typer.prompt("Send the text you want to encrypt")
            caesar_num = typer.prompt("Send one of the numbers from 1 to 27")
            caesar_res = typer.style(caesar_encipher(caesar_txt,caesar_num),fg=typer.colors.BLUE)
            caesar_table = [
                [f"{typer.style('Asl matn',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.BLUE)}"f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            typer.secho("Sizning \"Sizar\" usulida matningiz shifrlandi chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(caesar_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
        
    elif x == "caesar" and mode == "m--decode" and lang == "en":
        try:
            caesar_txt = typer.prompt("Send the text you want to decrypt")
            caesar_num = typer.prompt("Send one number of the number from 1 to 27")
            caesar_res = typer.style(caesar_decipher(caesar_txt,caesar_num),fg=typer.colors.BLACK)
            caesar_table = [
                [f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            typer.secho("Sizning \"Sizar\" usulida matningiz shifrdan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(caesar_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
    elif x == "mirage" and  mode == "m--encode" and lang == "en":
        try:
            mirage_txt = typer.prompt("Give me text to encode")
            mirage_res = typer.style(en_mirage(mirage_txt),fg=typer.colors.RED)
            mirage_table = [
                [f"Asl matn",f"Kodlangan matn"]
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            typer.echo(f"Sizning matningiz \"Mirage\" usulida kodlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("You've made a mistake. Check out the user guide.",fg=typer.colors.RED)
    elif x == "mirage" and mode == "m--decode" and lang == "en":
        try:
            mirage_txt = typer.prompt("Give me text to decode")
            mirage_res = typer.style(de_mirage(mirage_txt),fg=typer.colors.RED)
            mirage_table = [
                [f"Asl matn",f"Kodlangan matn"]
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            typer.echo(f"Sizning matningiz \"Mirage\"usulida koddan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("You've made a mistake. Check out the user guide",fg=typer.colors.RED)


##################### This section about Russian ##################################################
    elif x == "hill" and mode == "m--encode" and lang == "ru":
        try:
            hill_txt = typer.prompt("Shiflamoqchi bo'lgan matningizni yuboring")
            hill_code = typer.prompt("Sifringizga parol qo'ying")
            hill_result = typer.style(hillEncrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Asl matn',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(hill_txt,fg=typer.colors.BLUE)}",f"{hill_code}",f"{hill_result}"],
            ]
            typer.secho("Sizning \"HILL\" usulida matningiz shifrlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))
        except ZeroDivisionError:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)


    elif x == "hill" and mode == "m--decode" and lang == "ru":
        try:
            hill_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            hill_code = typer.prompt("Sifr parolini ayting")
            hill_result = typer.style(hillDecrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            hill_table = [
                [f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{hill_code}",f"{hill_result}"],
            ]
            typer.secho("Sizning \"HILL\" usulida matningiz shifrdan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))

        except ZeroDivisionError:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)

    elif x == "morse" and mode == "m--encode" and lang == "ru":
        try:
            morse_txt = typer.prompt("Kodlash uchun matningizni yuboring ")
            morse_result = typer.style(text_to_morse(morse_txt),fg=typer.colors.BLUE)
            morse_table = [
                [f"Asl matn",f"Kodlangan matn"]
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            typer.echo(f"Sizning matningiz \"MORSE\"usulida kodlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
    elif x == "morse" and mode == "m--decode" and lang == "ru":
        try:
            morse_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            morse_result = typer.style(morse_to_text(morse_txt),fg=typer.colors.RED)
            morse_table = [
                [f"Kodlangan matn",f"Asl matn"]
                [f"{typer.style(morse_txt,fg=typer.colors.RED)}",f"{morse_result}"]
            ]
            typer.echo(f"Sizning matningiz \"MORSE\"usulida koddan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(morse_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
    elif x == "caesar" and mode == "m--encode" and lang == "ru":
        try:
            caesar_txt = typer.prompt("Sifrlamoqchi bo'lgan matningizni bering")
            caesar_num = typer.prompt("1dan 27gacha bo'lgan sonlardan birini yuboring")
            caesar_res = typer.style(caesar_encipher(caesar_txt,caesar_num),fg=typer.colors.BLUE)
            caesar_table = [
                [f"{typer.style('Asl matn',fg=typer.colors.GREEN)}",f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.BLUE)}"f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            typer.secho("Sizning \"Sizar\" usulida matningiz shifrlandi chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
        
    elif x == "caesar" and mode == "m--decode" and lang == "ru":
        try:
            caesar_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            caesar_num = typer.prompt("Shiifrdan chiqarish uchun 1dan 27gacha bo'lgan son yuboring")
            caesar_res = typer.style(caesar_decipher(caesar_txt,caesar_num),fg=typer.colors.BLACK)
            caesar_table = [
                [f"{typer.style('Shifr matni',fg=typer.colors.GREEN)},"f"{typer.style('Shifr paroli',fg=typer.colors.GREEN)}",f"{typer.style('Natija',fg=typer.colors.GREEN)}"],
                [f"{typer.style(caesar_txt,fg=typer.colors.BLUE)}",f"{typer.style(caesar_num,fg=typer.colors.RED)}",f"{caesar_res}"],
            ]
            typer.secho("Sizning \"Sizar\" usulida matningiz shifrdan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(hill_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
    elif x == "mirage" and  mode == "m--encode" and lang == "ru":
        try:
            mirage_txt = typer.prompt("Shifrlamoqchi bo'lgan matningizni yuboring")
            mirage_res = typer.style(en_mirage(mirage_txt),fg=typer.colors.RED)
            mirage_table = [
                [f"Asl matn",f"Kodlangan matn"]
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            typer.echo(f"Sizning matningiz \"Mirage\" usulida kodlandi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)
    elif x == "mirage" and mode == "m--decode" and lang == "ru":
        try:
            mirage_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            mirage_res = typer.style(de_mirage(mirage_txt),fg=typer.colors.RED)
            mirage_table = [
                [f"Kodlangan matn",f"Natija"]
                [f"{typer.style(mirage_txt,fg=typer.colors.RED)}",f"{mirage_res}"]
            ]
            typer.echo(f"Sizning matningiz \"Mirage\"usulida koddan chiqarildi",fg=typer.colors.CYAN,bold=True)
            print(tabulate(mirage_table,headers="firstrow",tablefmt="psql"))
        except:
            typer.secho("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang",fg=typer.colors.RED)

if __name__ == "__main__":
    typer.run(main)
