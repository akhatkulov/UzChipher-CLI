#################Librarys for CLI tool####################
import typer
from typing import Optional
import os
from tabulate import tabulate
import inquirer
import time

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

    elif x == "transposition" and mode == "m--encode" and lang == "uz":
        t_p_encrypt_uz()

    elif x == "transposition" and mode == "m--decode" and lang == "uz":
        t_p_decrypt_uz()


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
    elif x == "guide":
        l = [
            inquirer.List(
                "lang",
            message= f"{typer.style('Choise workspace language',fg=typer.colors.RED)}",
            choices=[f'{typer.style("Uzbek",fg=typer.colors.GREEN)}',f'{typer.style("Russian",fg=typer.colors.GREEN)}',f'{typer.style("English",fg=typer.colors.GREEN)}']
        )
    ]

        x = inquirer.prompt(l)

        if "Uzbek" in x["lang"]:
            types = [
                inquirer.List(
                'type',
                message= f"{typer.style('Shifrlash va kodlash usullaridan birini tanlang',fg=typer.colors.RED)}",
                choices=[f'{typer.style("HILL",fg=typer.colors.GREEN)}',f'{typer.style("Morze",fg=typer.colors.GREEN)}',f'{typer.style("Mirage",fg=typer.colors.GREEN)}',f'{typer.style("Sezar",fg=typer.colors.GREEN)}']
            )

        ]
            check = inquirer.prompt(types)
            os.system('clear')

            if "HILL" in check['type']:
                typer.secho("HILL shifri qanday ishlaydi?",fg=typer.colors.CYAN)
                typer.echo("\n")
                typer.secho(f"""Hill shifrlash chiziqli algebraga asoslangan poligrafik almashtirish shifridir. \nU ochiq matnni shifrlangan matnga aylantirish uchun matritsalarni ko'paytirish orqali ishlaydi va aksincha. \nBu erda Hill shifrining qanday ishlashi haqida qisqacha ma'lumot:


{typer.style("Kalit avlodi:",fg=typer.colors.RED)}
Hill shifridagi shifrlash kaliti kvadrat matritsa bo'lib, odatda K sifatida belgilanadi. \nMatritsaning o'lchami kalit ibora yoki kalit so'z uzunligiga bog'liq. Kalit iboradagi har bir harf raqamli qiymatga mos keladi, bu kalit matritsani qurish uchun ishlatiladi.


{typer.style("Shifrlash:",fg=typer.colors.RED)}
Hill shifridan foydalangan holda xabarni shifrlash uchun ochiq matn birinchi navbatda A=0, B=1 va hokazo kabi oddiy xaritalashdan foydalanib, \nraqamli qiymatlarga aylantiriladi. \nKeyin ochiq matn kalit matritsaning o'lchamiga qarab vektorlarga guruhlanadi.\nKeyin har bir vektor alifbo o'lchamidagi kalit matritsa moduliga ko'paytiriladi (odatda ingliz tili uchun 26), natijada shifrlangan matn hosil bo'ladi.


{typer.style("Shifrni ochish:",fg=typer.colors.RED)}
Hill shifridagi shifrni ochish kalit matritsasining teskarisidan foydalanishni o'z ichiga oladi. \n Asl ochiq matnni olish uchun shifrlangan matn alifbo o'lchamidagi kalit matritsa modulining teskari qismiga ko'paytiriladi.

{typer.style("Masalan:",typer.colors.RED)}
Kiritish: Mexroj \n 
Parol: m2008
Narija: emxay
""")
            if "Sezar" in check['type']:
                typer.secho("Sezar shifri qanday ishlaydi?",fg=typer.colors.CYAN)
                typer.secho("Hozirgi Sezar shifri faqatgina lotin harflariga ishlaydi",fg=typer.colors.RED)
                typer.echo("\n")
                typer.secho(f"""Sezar shifrlash, shuningdek, siljish shifrlash sifatida ham tanilgan, oddiy almashtirish shifridir, unda ochiq matndagi har bir harf alifbo bo'ylab ma'lum miqdordagi joylarni pastga yoki yuqoriga siljitadi. Taqdim etilgan qidiruv natijasiga asoslanib, Sezar shifrlash jarayoni qanday ishlashi haqida qisqacha ma'lumot:


{typer.style("Kalit tanlash:",fg=typer.colors.RED)}

O'zgartirish qiymatini tanlang, ya'ni ochiq matndagi har bir harf o'tkaziladigan pozitsiyalar soni.

{typer.style("Xabarlarni shifrlash",fg=typer.colors.RED)}:

To'g'ri matndagi har bir harf tanlangan qiymat bo'yicha siljiydi. Misol uchun, agar siljish qiymati 3 bo'lsa, 'A' 'D', 'B'ga aylanadi; 'E'ga aylanadi va hokazo.

{typer.style("Misol:",fg=typer.colors.RED)}

Agar kalit 'H' va ochiq matn 'HELLO', shifrlash jarayoni 'KHOOR'ga olib keladi.

{typer.style("Shifrni ochish:",fg=typer.colors.RED)}

Xabarning shifrini ochish uchun shifrlangan matndagi har bir harfni teskari yo'nalishda siljitish orqali jarayon shunchaki teskari tomonga o'zgartiriladi.

""")
            if "Morze" in check['type']:
                typer.secho("Morze kodlash tizimi qanday ishlaydi?",fg=typer.colors.CYAN)
                typer.echo("\n")
                typer.secho("""Morze, telegraf kaliti yordamida nuqta va tirelar orqali xabarlar o'girish uchun qurol kodlash tizimi.\n\nBu tizimda har bir harf va raqamga mos keladigan nuqta va tirelar orqali xabarlarni ifodalash uchun qoladi.\n\nMorze kodlash tizimi, telegraf orqali xabarlar o'girishda, har bir harf va raqamga mos nuqta va tirelar orqali xabarlarni ifodalash uchun olinadi.\n\nMisol uchun, "A" harfi uchun nuqta-tire (.-), "B" harfi uchun tire-nuqta-nuqta-nuqta (−...), "C" harfi uchun tire-nuqta-tire-nuqta (−.-.) kabi.\nBu tizimda har bir harf va raqamga mos keladigan nuqta va tirelar orqali xabarlarni ifodalash uchun qoladi.\n\nMorze kodlash tizimi, telegraf orqali xabarlar o'girishda, har bir harf va raqamga mos nuqta va tirelar orqali xabarlarni ifodalash uchun olinadi.\n\nMisol uchun, "A" harfi uchun nuqta-tire (.-), "B" harfi uchun tire-nuqta-nuqta-nuqta (−...), "C" harfi uchun tire-nuqta-tire-nuqta (−.-.) kabi.\nBu tizimda har bir harf va raqamga mos keladigan nuqta va tirelar orqali xabarlarni ifodalash uchun qoladi. """)
                typer.echo("\n")
            if "Mirage" in check['type']:
                typer.secho("Mirage kodlash tizimi qanday ishlaydi?",fg=typer.colors.CYAN)
                typer.echo("\n")
                typer.secho("""Mirage kodlash tizimi sizning matningizdagi raqam va harflar o'rniga o'zining lug'atdigai belgilarni joylashtirib tushunarsiz ko'rinishga keltiradi""")
                typer.echo("\n")
######################################## Russian Section Start ################################################
        if "Russian" in x["lang"]:
            types = [
                inquirer.List(
                'type',
                message= f"{typer.style('Выберите один из методов шифрования и кодирования',fg=typer.colors.RED)}",
                choices=[f'{typer.style("ХОЛМ",fg=typer.colors.GREEN)}',f'{typer.style("Морзе",fg=typer.colors.GREEN)}',f'{typer.style("Мираж",fg=typer.colors.GREEN)}',f'{typer.style("Цезарь",fg=typer.colors.GREEN)}']
            )

        ]
            check = inquirer.prompt(types)
            os.system('clear')
            if "ХОЛМ" in check['type']:
                typer.secho("Как работает шифр ХОЛМ?",fg=typer.colors.CYAN)
                typer.echo("\n")
                typer.secho(f"""Шифр Хилла — это полиграфический перестановочный шифр, основанный на линейной алгебре. \nОн работает путем умножения матриц для преобразования открытого текста в зашифрованный текст и наоборот. \nВот краткое описание того, как работает шифр Хилла:


{typer.style("Генерация ключей:",fg=typer.colors.RED)}
Ключ шифрования в шифре ХОЛМ представляет собой квадратную матрицу, обычно обозначаемую K. \nРазмер матрицы зависит от длины ключевого слова или ключевого слова. Каждой букве ключевой фразы соответствует числовое значение, которое используется для построения ключевой матрицы.


{typer.style("Шифрование:",fg=typer.colors.RED)}
Чтобы зашифровать сообщение с помощью шифра ХОЛМ, открытый текст сначала преобразуется в числовые значения с использованием простых сопоставлений, таких как A=0, B=1 и т. д. \nОткрытый текст затем группируется в векторы в зависимости от размера ключевой матрицы.\nКаждый вектор затем умножается на модуль ключевой матрицы алфавитного размера (обычно 26 для английского языка), в результате чего получается зашифрованный текст.


{typer.style("Расшифровать:",fg=typer.colors.RED)}
Расшифровка шифра ХОЛМ предполагает использование обратной ключевой матрицы. \n Чтобы получить исходный открытый текст, зашифрованный текст умножается на обратную матрицу по модулю размера алфавита.

{typer.style("Например:",typer.colors.RED)}
Ввод: Mexroj \n
Пароль: m2008
Нария: emxay
""")
            if "Цезарь" in check['type']:
                typer.secho("Как работает шифр Цезаря?",fg=typer.colors.CYAN)
                typer.secho("Текущий шифр Цезаря работает только с латинскими буквами.",fg=typer.colors.RED)
                typer.echo("\n")
                typer.secho(f"""Шифр Цезаря, также известный как шифр сдвига, представляет собой простой шифр перестановки, в котором каждая буква открытого текста сдвигается вниз или вверх на определенное количество мест в алфавите. На основе предоставленных результатов поиска приведено краткое описание того, как работает процесс шифрования Caesar:
{typer.style("Выберите клавишу:",fg=typer.colors.RED)}

Выберите значение смещения, то есть количество позиций, на которые нужно переместить каждую букву открытого текста.

{typer.style("Шифровать сообщения",fg=typer.colors.RED)}:

Каждая буква в правильном тексте сдвигается на выбранное значение. Например, если значение сдвига равно 3, «A» становится «D», «B»; становится «E» и так далее.

{typer.style("Пример:",fg=typer.colors.RED)}

Если ключ — «H», а открытый текст — «HELLO», результат процесса шифрования — «KHOOR».

{typer.style("Расшифровать:",fg=typer.colors.RED)}

Процесс просто меняется на обратный путем перемещения каждой буквы зашифрованного текста в противоположном направлении для расшифровки сообщения.
""")
            if "Морзе" in check['type']:
                typer.secho("Как работает система азбуки Морзе?",fg=typer.colors.CYAN)
                typer.echo("\n")
                typer.secho("""Морзе, система кода оружия для передачи сообщений через точки и тире с использованием телеграфного ключа.\n\nВ этой системе остается выражать сообщения с помощью точек и тире, соответствующих каждой букве и цифре.\n\nСистема кода Морзе, телеграфные сообщения o 'во входных данных каждая буква и цифра используются для представления сообщений через точки и тире.\n\nНапример, точка-тире (.-) для "A", тире-точка-точка-точка-точка ( −.. .), например тире-точка-тире-точка (-.-.) для буквы "C".\nЭта система по-прежнему позволяет выражать сообщения с помощью точек и тире, соответствующих каждой букве и цифре.\n\nСистема азбуки Морзе, при отправке сообщений по телеграфу каждая буква и цифра принимаются для выражения сообщения через точки и тире.\n\nНапример, точка-тире (.-) для буквы "А", тире- для буквы "Б" типа точки -точка-точка (-...), тире-точка-тире-точка (-.-.) для буквы "С".\nСистеме остается выражать сообщения с помощью точек и тире, соответствующих каждой букве и цифре. . """)
                typer.echo("\n")
            if "Мираж" in check['type']:
                typer.secho("Как работает система кодирования Мираж?",fg=typer.colors.CYAN)
                typer.echo("\n")
                typer.secho("""Система кодирования Мираж делает ваш текст неясным, заменяя символы из словаря вместо цифр и букв""")
                typer.echo("\n")
################################### English section start #####################
        if "English" in x["lang"]:
            types = [
                inquirer.List(
                'type',
                message= f"{typer.style('Choose one of encryption and encoding methods',fg=typer.colors.RED)}",
                choices=[f'{typer.style("HILL",fg=typer.colors.GREEN)}',f'{typer.style("Morse",fg=typer.colors.GREEN)}',f'{ typer.style("Mirage",fg=typer.colors.GREEN)}',f'{typer.style("Caesar",fg=typer.colors.GREEN)}']
            )

        ]
            check = inquirer.prompt(types)
            os.system('clear')
            if "HILL" in check['type']:
                typer.secho("How does the HILL cipher work?",fg=typer.colors.CYAN)
                typer.echo("\n")
                typer.secho(f"""Hill cipher is a polygraphic permutation cipher based on linear algebra. \nIt works by multiplying matrices to convert plaintext to ciphertext and vice versa. \nHere's a brief explanation of how Hill's cipher works:


{typer.style("Key Generation:",fg=typer.colors.RED)}
The encryption key in a Hill cipher is a square matrix, usually denoted as K. \nThe size of the matrix depends on the length of the keyword or keyword. Each letter in the key phrase corresponds to a numeric value, which is used to construct the key matrix.


{typer.style("Encryption:",fg=typer.colors.RED)}
To encrypt a message using the Hill cipher, the plaintext is first converted into \nnumeric values ​​using simple mappings such as A=0, B=1, etc. \nThe plaintext is then grouped into vectors based on the size of the key matrix.\nEach vector is then multiplied by the modulus of the alphabetic-sized key matrix (typically 26 for English), resulting in a ciphertext.


{typer.style("Decrypt:",fg=typer.colors.RED)}
Decrypting a Hill cipher involves using the inverse of the key matrix. \n To get the original plaintext, the ciphertext is multiplied by the inverse of the matrix modulo the size of the alphabet.

{typer.style("For example:",typer.colors.RED)}
Input: Mexroj \n
Password: m2008
result: emxay
""")
            if "Caesar" in check['type']:
                typer.secho("How does the Caesar cipher work?",fg=typer.colors.CYAN)
                typer.secho("The current Caesar cipher only works with Latin letters",fg=typer.colors.RED)
                typer.echo("\n")
                typer.secho(f"""Caesar cipher, also known as shift cipher, is a simple permutation cipher in which each letter in the plaintext is shifted a certain number of places down or up through the alphabet. Based on the search result provided, Caesar Here's a quick rundown of how the encryption process works:


{typer.style("Select key:",fg=typer.colors.RED)}

Select the displacement value, that is, the number of positions to move each letter in the plaintext.

{typer.style("Encrypt messages",fg=typer.colors.RED)}:

Each letter in the correct text is shifted by the selected value. For example, if the shift value is 3, 'A' becomes 'D', 'B'; becomes 'E' and so on.

{typer.style("Example:",fg=typer.colors.RED)}

If the key is 'H' and the plaintext is 'HELLO', the encryption process results in 'KHOOR'.

{typer.style("Decrypt:",fg=typer.colors.RED)}

The process is simply reversed by moving each letter in the ciphertext in the opposite direction to decrypt the message.

""")
            if "Morse" in check['type']:
                typer.secho("How does Morse code work?",fg=typer.colors.CYAN)
                typer.echo("\n")
                typer.secho("""Morse is a weapon code system for converting messages through dots and dashes using a telegraph key.\n\nThis system remains to represent messages using dots and dashes corresponding to each letter and number.\n\nMorze the coding system used to represent messages in telegraphic messages using dots and dashes corresponding to each letter and number. For example, a dot-dash (.-) for the letter "A", a dash for the letter "B". -dot-dot-dot (−...), such as dash-dot-dash-dot (−.-.) for the letter "C".\nThis system uses dots and dashes to represent messages corresponding to each letter and number. remains.\n\nThe Morse code system is used to represent messages by means of dots and dashes corresponding to each letter and number when transmitting messages by telegraph.\n\nFor example, a dot-dash (.-) for the letter "A", Like dash-dot-dot-dot (−...) for "B", dash-dot-dash-dot (−.-.) for "C".\nA dot corresponds to each letter and number in this system. and it remains to express messages through dashes. """)
                typer.echo("\n")
            if "Mirage" in check['type']:
                typer.secho("How does the Mirage coding system work?",fg=typer.colors.CYAN)
                typer.echo("\n")
                typer.secho("""Mirage's encoding system makes your text look obscure by substituting characters from its dictionary instead of numbers and letters""")
                typer.echo("\n")

if __name__ == "__main__":
    typer.run(main)
