morse_code_dict = {
    'A': '.-','B': '-...','C': '-.-.',
    'D': '-..','E': '.','F': '..-.',
    'G': '--.','H': '....','I': '..',
    'J': '.---','K': '-.-','L': '.-..',
    'M': '--','N': '-.','O': '---','P': '.--.',
    'Q': '--.-','R': '.-.','S': '...',
    'T': '-','U': '..-','V': '...-',
    'W': '.--','X': '-..-','Y': '-.--',
    'Z': '--..','0': '-----','1': '.----',
    '2': '..---','3': '...--','4': '....-',
    '5': '.....','6': '-....','7': '--...',
    '8': '---..','9': '----.','.': '.-.-.-',
    ',': '--..--','?': '..--..',"'": '.----.',
    '!': '-.-.--','/': '-..-.','(': '-.--.',
    ')': '-.--.-','&': '.-...',':': '---...',
    ';': '-.-.-.','=': '-...-','+': '.-.-.',
    '-': '-....-','_': '..--.-','"': '.-..-.',
    '$': '...-..-','@': '.--.-.',' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
    return morse_code.strip()

def morse_to_text(morse_code):
    text = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for key, value in morse_code_dict.items():
            if code == value:
                text += key
    return text

# # Example usage
# text = 'HELLO WORLD'
# morse_code = text_to_morse(text)
# print(morse_code)
                                                                                                                                                                                      
# morse_code = '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
# text = morse_to_text(morse_code)
# print(text)

