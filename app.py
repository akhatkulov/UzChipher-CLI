#################Librarys for CLI tool####################
import typer
from typing import Optional
import os
from tabulate import tabulate
import inquirer
import time
from yaspin import yaspin
from yaspin.spinners import Spinners

################ My Cryptography Codes #####################
from cipher_codes import * 
from helper import *
################ Start Typer Coding #####################################
def main(x: Optional[str] = typer.Argument('home',help="Section"),mode: Optional[str]= typer.Argument('m--encode',help='Mode') , lang: Optional[str] =  typer.Argument('en',help="Program's Language")):
    os.system('clear')
    if x == "home":
        home_page()
##############################################################################################
        loading_func()
        start_cli()
######################This section about uzbek language  #################################################
    elif x == "hill" and mode == "m--encode" and lang == "uz":
        hill_encode_uz()
    elif x == "hill" and mode == "m--decode" and lang == "uz":
        hill_decode_uz()

    elif x == "morse" and mode == "m--encode" and lang == "uz":
        morse_encode_uz()
    elif x == "morse" and mode == "m--decode" and lang == "uz":
        morse_decode_uz()
    elif x == "caesar" and mode == "m--encode" and lang == "uz":
        caesar_encode_uz()
        
    elif x == "caesar" and mode == "m--decode" and lang == "uz":
        caesar_decode_uz()
    elif x == "mirage" and  mode == "m--encode" and lang == "uz":
        mirage_encode_uz()
    elif x == "mirage" and mode == "m--decode" and lang == "uz":
        mirage_decode_uz()
##################### This section about English ##################################################
    elif x == "hill" and mode == "m--encode" and lang == "en":
        hill_encode_en()


    elif x == "hill" and mode == "m--decode" and lang == "en":
        hill_decode_en()

    elif x == "morse" and mode == "m--encode" and lang == "en":
        morse_encode_en()
    elif x == "morse" and mode == "m--decode" and lang == "en":
        morse_decode_en()
    elif x == "caesar" and mode == "m--encode" and lang == "en":
        caesar_encode_en()
        
    elif x == "caesar" and mode == "m--decode" and lang == "en":
        caesar_decode_en()
    elif x == "mirage" and  mode == "m--encode" and lang == "en":
        mirage_encode_en()
    elif x == "mirage" and mode == "m--decode" and lang == "en":
        mirgae_decode_en()


##################### This section about Russian ##################################################
    elif x == "hill" and mode == "m--encode" and lang == "ru":
        hill_encode_ru()


    elif x == "hill" and mode == "m--decode" and lang == "ru":
        hill_decode_ru()

    elif x == "morse" and mode == "m--encode" and lang == "ru":
        morse_encode_ru()
    elif x == "morse" and mode == "m--decode" and lang == "ru":
        morse_decode_ru()
    elif x == "caesar" and mode == "m--encode" and lang == "ru":
        caesar_encode_ru()
        
    elif x == "caesar" and mode == "m--decode" and lang == "ru":
        caesar_decode_ru()
    elif x == "mirage" and  mode == "m--encode" and lang == "ru":
        mirage_encode_ru()
    elif x == "mirage" and mode == "m--decode" and lang == "ru":
        mirage_decode_ru()

if __name__ == "__main__":
    typer.run(main)
