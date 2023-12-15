import os
import sys 
import inquirer
import typer
import time 
from cipher_codes import *
from helper import *
from parts import * 

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
    if "Uzbek" in language:
        time.sleep(0.4)
        typer.secho("Siz endi dasturni o'zbek tilida ishlatishingiz mumkin")
        cipher_type_uz = [
        inquirer.List(
            "type",
            message=f"{typer.style('Shifrlash va kodlash usullaridan birini tanlang',fg=typer.colors.RED)}",
        choices=[f"{typer.style('HILL',fg=typer.colors.GREEN)}", f"{typer.style('Sizar',fg=typer.colors.GREEN)}", f"{typer.style('Mirage',fg=typer.colors.GREEN)}",f"{typer.style('Morse',fg=typer.colors.GREEN)}"],
        ),
    ]
        uz = inquirer.prompt(cipher_type_uz)
        if "HILL" in uz['type']:
            hill_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Rejimni tanlang',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Shifrlash/Kodlash',fg=typer.colors.GREEN)}",f"{typer.style('Shifrdan chiqarish/Koddan chiqarish',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(hill_mode)
            if "Shifrlash/Kodlash" in x['mode']:
                hill_encode_uz()
            elif "Shifrdan chiqarish/Koddan chiqarish" in x['mode']:
                hill_decode_uz()
        if "Mirage" in uz['type']:
            Mirage_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Rejimni tanlang',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Shifrlash/Kodlash',fg=typer.colors.GREEN)}",f"{typer.style('Shifrdan chiqarish/Koddan chiqarish',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(Mirage_mode)
            if "Shifrlash/Kodlash" in x['mode']:
                mirage_encode_uz()
            elif "Shifrdan chiqarish/Koddan chiqarish" in x['mode']:
                mirage_decode_uz()
        if "Morse" in uz['type']:
            Morse_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Rejimni tanlang',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Shifrlash/Kodlash',fg=typer.colors.GREEN)}",f"{typer.style('Shifrdan chiqarish/Koddan chiqarish',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(Morse_mode)
            if "Shifrlash/Kodlash" in x['mode']:
                morse_encode_uz()
            elif "Shifrdan chiqarish/Koddan chiqarish" in x['mode']:
                morse_decode_uz()
        if "Sizar" in uz['type']:
            Caeasar_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Rejimni tanlang',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Shifrlash/Kodlash',fg=typer.colors.GREEN)}",f"{typer.style('Shifrdan chiqarish/Koddan chiqarish',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(Caeasar_mode)
            if "Shifrlash/Kodlash" in x['mode']:
                caesar_encode_uz()
            elif "Shifrdan chiqarish/Koddan chiqarish" in x['mode']:
                caesar_decode_uz()
########################################################################Section Russian Language Start #########################
    if "Russian" in language:
        time.sleep(0.4)
        typer.secho("Теперь вы можете использовать программу на русском языке.")
        cipher_type_ru = [
        inquirer.List(
            "type",
            message=f"{typer.style('Выберите один из методов шифрования и кодирования',fg=typer.colors.RED)}",
        choices=[f"{typer.style('ХОЛМ',fg=typer.colors.GREEN)}", f"{typer.style('Сизар',fg=typer.colors.GREEN)}", f"{typer.style('Мираж',fg=typer.colors.GREEN)}",f"{typer.style('Морзе',fg=typer.colors.GREEN)}"],
        ),
    ]
        ru = inquirer.prompt(cipher_type_ru)
        if "ХОЛМ" in ru['type']:
            hill_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Выберите режим',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Шифрование/Кодирование',fg=typer.colors.GREEN)}",f"{typer.style('Расшифровать/декодировать',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(hill_mode)
            if "Шифрование/Кодирование" in x['mode']:
                hill_encode_uz()
            elif "Расшифровать/декодировать" in x['mode']:
                hill_decode_uz()
        if "Мираж" in ru['type']:
            Mirage_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Выберите режим',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Шифрование/Кодирование',fg=typer.colors.GREEN)}",f"{typer.style('Расшифровать/декодировать',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(Mirage_mode)
            if "Шифрование/Кодирование" in x['mode']:
                mirage_encode_uz()
            elif "Расшифровать/декодировать" in x['mode']:
                mirage_decode_uz()
        if "Морзе" in uz['type']:
            Morse_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Выберите режим',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Шифрование/Кодирование',fg=typer.colors.GREEN)}",f"{typer.style('Расшифровать/декодировать',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(Morse_mode)
            if "Шифрование/Кодирование" in x['mode']:
                morse_encode_uz()
            elif "Расшифровать/декодировать" in x['mode']:
                morse_decode_uz()
        if "Сизар" in ru['type']:
            Caeasar_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Выберите режим',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Шифрование/Кодирование',fg=typer.colors.GREEN)}",f"{typer.style('Расшифровать/декодировать',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(Caeasar_mode)
            if "Шифрование/Кодирование" in x['mode']:
                caesar_encode_uz()
            elif "Расшифровать/декодировать" in x['mode']:
                caesar_decode_uz()
######################## English Section Start ##########################################
    if "English" in language:
        time.sleep(0.4)
        typer.secho("You can now use the program in English")
        cipher_type_en = [
        inquirer.List(
            "type",
            message=f"{typer.style('Choose one of the encryption and encoding methods',fg=typer.colors.RED)}",
        choices=[f"{typer.style('HILL',fg=typer.colors.GREEN)}", f"{typer.style('Caesar',fg=typer.colors.GREEN)}", f"{typer.style('Mirage',fg=typer.colors.GREEN)}",f"{typer.style('Morse',fg=typer.colors.GREEN)}"],
        ),
    ]
        en = inquirer.prompt(cipher_type_en)
        if "HILL" in en['type']:
            hill_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Select the mode',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Encryption/Encoding',fg=typer.colors.GREEN)}",f"{typer.style('Decrypt/Decode',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(hill_mode)
            if "Encryption/Encoding" in x['mode']:
                hill_encode_en()
            elif "Decrypt/Decode" in x['mode']:
                hill_decode_en()
        if "Mirage" in en['type']:
            Mirage_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Select the mode',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Encryption/Encoding',fg=typer.colors.GREEN)}",f"{typer.style('Decrypt/Decode',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(Mirage_mode)
            if "Encryption/Encoding" in x['mode']:
                mirage_encode_en()
            elif "Decrypt/Decode" in x['mode']:
                mirage_decode_en()
        if "Morse" in en['type']:
            Morse_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Select the mode',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Encryption/Encoding',fg=typer.colors.GREEN)}",f"{typer.style('Decrypt/Decode',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(Morse_mode)
            if "Encryption/Encoding" in x['mode']:
                morse_encode_en()
            elif "Decrypt/Decode" in x['mode']:
                morse_decode_en()
        if "Caesar" in en['type']:
            Caeasar_mode = [
                inquirer.List(
                    "mode",
                message=f"{typer.style('Select the mode',fg=typer.colors.RED)}",
                choices = [f"{typer.style('Encryption/Encoding',fg=typer.colors.GREEN)}",f"{typer.style('Decrypt/Decode',fg=typer.colors.GREEN)}"],
                                                                                                  
                ),
            ]

            x = inquirer.prompt(Caeasar_mode)
            if "Encryption/Encoding" in x['mode']:
                caesar_encode_en()
            elif "Decrypt/Decode" in x['mode']:
                caesar_decode_en()
