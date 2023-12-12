#################Librarys for CLI tool####################
import typer
from typing import Optional
import os
import pyfiglet

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
            typer.secho(f"{hill_result} sizning matningiz \n{hill_code} parolida shifrlandi")
        except ZeroDivisionError:
            typer.echo("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")


    elif x == "hill" and mode == "m--decode" and lang == "uz":
        try:
            hill_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            hill_code = typer.prompt("Sifr parolini ayting")
            hill_result = typer.style(hillDecrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            typer.secho(f"{hill_result} sizning matningiz \n{hill_code} parolida shifrdan chiqarildi")
        except ZeroDivisionError:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")

    elif x == "morse" and mode == "m--encode" and lang == "uz":
        try:
            morse_txt = typer.prompt("Shifrlash uchun matningizni yuboring ")
            morse_result = typer.style(text_to_morse(morse_txt),fg=typer.colors.RED)
            typer.echo(f"Sizning matningi shifrlandi:\n{morse_result}")
        except:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
    elif x == "morse" and mode == "m--decode" and lang == "uz":
        try:
            morse_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            morse_result = typer.style(morse_to_text(morse_txt),fg=typer.colors.RED)
            typer.echo(f"Sizning matningiz shifrdan chiqaridi:\n{morse_result}")
        except:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
    elif x == "caesar" and mode == "m--encode" and lang == "uz":
        try:
            caesar_txt = typer.prompt("Sifrlamoqchi bo'lgan matningizni bering")
            caesar_num = typer.prompt("1dan 27gacha bo'lgan sonlardan birini yuboring")
            caesar_res = typer.style(caesar_encipher(caesar_txt,caesar_num),fg=typer.colors.RED)
            typer.echo(f"Sizning matningiz {caesar_num} raqami ostida shifrlandi\n{caesar_res}")
        except:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
        
    elif x == "caesar" and mode == "m--decode" and lang == "uz":
        try:
            caesar_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            caesar_num = typer.prompt("Shiifrdan chiqarish uchun 1dan 27gacha bo'lgan son yuboring")
            caesar_res = typer.style(caesar_decipher(caesar_txt,caesar_num),fg=typer.colors.RED)
            typer.echo(f"Sizning matningiz {caesar_num} raqami orqali shifrdan chiqarildi\n{caesar_res}")
        except:
            typer.echo("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
    elif x == "mirage" and  mode == "m--encode" and lang == "uz":
        try:
            mirage_txt = typer.prompt("Shifrlamoqchi bo'lgan matningizni yuboring")
            mirage_res = typer.style(en_mirage(mirage_txt),fg=typer.colors.RED)
            typer.echo(f"Sizning matningiz shifrlandi\n{mirage_res}")
        except:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
    elif x == "mirage" and mode == "m--decode" and lang == "uz":
        try:
            mirage_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            mirage_res = typer.style(de_mirage(mirage_txt),fg=typer.colors.RED)
            typer.echo(f"Sizning matningiz shifrdan chiqarildi\n{mirage_res}")
        except:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
##################### This section about English ##################################################
    elif x == "hill" and mode == "m--encode" and lang == "en":
        try:
            hill_txt = typer.prompt("Send me the text you want to encrypt")
            hill_code = typer.prompt("Set a password for your encrypt")
            hill_result = typer.style(hillEncrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            typer.secho(f"{hill_result}Your text has been set this password: \n{hill_code}")
        except ZeroDivisionError:
            typer.echo("You made a mistake, back to the introduction!")


    elif x == "hill" and mode == "m--decode" and lang == "en":
        try:
            hill_txt = typer.prompt("Send me the text that you want to decrypt: ")
            hill_code = typer.prompt("Enter the password: ")
            hill_result = typer.style(hillDecrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            typer.secho(f"{hill_result} Your text has been decrypted at password \n{hill_code}")
        except ZeroDivisionError:
            typer.echo("You made a mistake, back to the introduction!")

    elif x == "morse" and mode == "m--encode" and lang == "en":
        try:
            morse_txt = typer.prompt("Send me the text that you want to decrypt: ")
            morse_result = typer.style(text_to_morse(morse_txt),fg=typer.colors.RED)
            typer.echo(f"Your text has been decrypted:\n{morse_result}")
        except:
            typer.echo("You made a mistake, back to the introduction")
    elif x == "morse" and mode == "m--decode" and lang == "en":
        try:
            morse_txt = typer.prompt("Send me the text that you want to decrypt: ")
            morse_result = typer.style(morse_to_text(morse_txt),fg=typer.colors.RED)
            typer.echo(f"Your text has been decrypted:\n{morse_result}")
        except:
            typer.echo("You made a mistake, back to the introduction")
    elif x == "caesar" and mode == "m--encode" and lang == "en":
        try:
            caesar_txt = typer.prompt("Send me the text you want to encrypt")
            caesar_num = typer.prompt("Send me the number fro 1 to 27")
            caesar_res = typer.style(caesar_encipher(caesar_txt,caesar_num),fg=typer.colors.RED)
            typer.echo(f"Your text has been encrypted at the number {caesar_num} \n{caesar_res}")
        except:
            typer.echo("You made a mistake, back to the introduction!")
        
    elif x == "caesar" and mode == "m--decode" and lang == "en":
        try:
            caesar_txt = typer.prompt("Send me the text you want to decrypt")
            caesar_num = typer.prompt("For decrypting send me the number from 1 to 27: ")
            caesar_res = typer.style(caesar_decipher(caesar_txt,caesar_num),fg=typer.colors.RED)
            typer.echo(f"Your text has been decrypted at the number {caesar_num} \n{caesar_res}")
        except:
            typer.echo("You made a mistake, back to the introduction!")
    elif x == "mirage" and  mode == "m--encode" and lang == "en":
        try:
            mirage_txt = typer.prompt("Send me the text you want to encrypt")
            mirage_res = typer.style(en_mirage(mirage_txt),fg=typer.colors.RED)
            typer.echo(f"Your text has been encrypted \n{mirage_res}")
        except:
            typer.echo("You made a mistake, back to the introduction!")
    elif x == "mirage" and mode == "m--decode" and lang == "en":
        try:
            mirage_txt = typer.prompt("Send me the text that you want to decrypt")
            mirage_res = typer.style(de_mirage(mirage_txt),fg=typer.colors.RED)
            typer.echo(f"Your text has been decrypted \n{mirage_res}")
        except:
            typer.echo("You made a mistake, back to the introduction!")


##################### This section about Russian ##################################################
    elif x == "hill" and mode == "m--encode" and lang == "en":
        try:
            hill_txt = typer.prompt("Shiflamoqchi bo'lgan matningizni yuboring")
            hill_code = typer.prompt("Sifringizga parol qo'ying")
            hill_result = typer.style(hillEncrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            typer.secho(f"{hill_result} sizning matningiz \n{hill_code} parolida shifrlandi")
        except ZeroDivisionError:
            typer.echo("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")


    elif x == "hill" and mode == "m--decode" and lang == "en":
        try:
            hill_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            hill_code = typer.prompt("Sifr parolini ayting")
            hill_result = typer.style(hillDecrypt(hill_txt,hill_code),fg=typer.colors.BLUE)
            hill_code = typer.style(hill_code,fg=typer.colors.RED)
            typer.secho(f"{hill_result} sizning matningiz \n{hill_code} parolida shifrdan chiqarildi")
        except ZeroDivisionError:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")

    elif x == "morse" and mode == "m--encode" and lang == "en":
        try:
            morse_txt = typer.prompt("Shifrlash uchun matningizni yuboring ")
            morse_result = typer.style(text_to_morse(morse_txt),fg=typer.colors.RED)
            typer.echo(f"Sizning matningi shifrlandi:\n{morse_result}")
        except:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
    elif x == "morse" and mode == "m--decode" and lang == "en":
        try:
            morse_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            morse_result = typer.style(morse_to_text(morse_txt),fg=typer.colors.RED)
            typer.echo(f"Sizning matningiz shifrdan chiqaridi:\n{morse_result}")
        except:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
    elif x == "caesar" and mode == "m--encode" and lang == "en":
        try:
            caesar_txt = typer.prompt("Sifrlamoqchi bo'lgan matningizni bering")
            caesar_num = typer.prompt("1dan 27gacha bo'lgan sonlardan birini yuboring")
            caesar_res = typer.style(caesar_encipher(caesar_txt,caesar_num),fg=typer.colors.RED)
            typer.echo(f"Sizning matningiz {caesar_num} raqami ostida shifrlandi\n{caesar_res}")
        except:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
        
    elif x == "caesar" and mode == "m--decode" and lang == "en":
        try:
            caesar_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            caesar_num = typer.prompt("Shiifrdan chiqarish uchun 1dan 27gacha bo'lgan son yuboring")
            caesar_res = typer.style(caesar_decipher(caesar_txt,caesar_num),fg=typer.colors.RED)
            typer.echo(f"Sizning matningiz {caesar_num} raqami orqali shifrdan chiqarildi\n{caesar_res}")
        except:
            typer.echo("siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
    elif x == "mirage" and  mode == "m--encode" and lang == "en":
        try:
            mirage_txt = typer.prompt("Shifrlamoqchi bo'lgan matningizni yuboring")
            mirage_res = typer.style(en_mirage(mirage_txt),fg=typer.colors.RED)
            typer.echo(f"Sizning matningiz shifrlandi\n{mirage_res}")
        except:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")
    elif x == "mirage" and mode == "m--decode" and lang == "en":
        try:
            mirage_txt = typer.prompt("Shifrdan chiqarmoqchi bo'lgan matningizni yuboring")
            mirage_res = typer.style(de_mirage(mirage_txt),fg=typer.colors.RED)
            typer.echo(f"Sizning matningiz shifrdan chiqarildi\n{mirage_res}")
        except:
            typer.echo("Siz xatoga yo'l qo'ydingin foydalanish qo'llanmasini qayta qarang")



if __name__ == "__main__":
    typer.run(main)
