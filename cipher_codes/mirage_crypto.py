mirage_elements = {
    "◤": "Q","⍚": "W","♚": "E",
    "≥": "R",">": "T","-": "Y",
    "<": "U","⊺": "I","Y": "O",
    "z": "P","♝": "A","≤": "S",
    "♛": "D","∞": "F","♕": "G",
    "△": "H","⋮": "J","=": "K",
    "≠": "L","+": "Z","√": "X",
    "♥️": "C","±": "V","♜": "B",
    "x": "N","卐": "M","♖": "Ш",
    "♗": "Ch","♘": "Ng","♔'": "O",
    "㈤": "'","㈢": "-"
}
# ≤♝≠y♔'卐
def de_mirage(text):
    text = text.upper()
    mirage_result = ""
    for i in text.upper():

        if i in mirage_elements:
            mirage_result+=mirage_elements[i];
    return mirage_result;
def en_mirage(text):
    text = text.upper()
    mirage_result = ""
    for i in text:
        for key, value in mirage_elements.items():
            if i == value:
                mirage_result+=key;
    return mirage_result;

