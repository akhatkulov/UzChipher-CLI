def hillEncrypt(text, key):
    # Check text length
    text = ''.join(filter(str.isalpha, text))
    textLength = len(text)

    # Check the length of the key and copy the checktext
    key = ''.join(filter(str.isalpha, key))
    keyLength = len(key)
    keyMatrix = (key * ((textLength // keyLength) + 1))[:textLength]

    # Encrypt the text
    encryptedText = ""
    for i in range(textLength):
        textChar = ord(text[i].lower()) - 97
        keyChar = ord(keyMatrix[i].lower()) - 97
        encryptedChar = chr(((textChar + keyChar) % 26) + 97)
        encryptedText += encryptedChar if text[i].islower() else encryptedChar.upper()

    return encryptedText



def hillDecrypt(text, key):
    # Check text length
    text = ''.join(filter(str.isalpha, text))
    textLength = len(text)

    # Check the length of the key and copy the checktext
    key = ''.join(filter(str.isalpha, key))
    keyLength = len(key)
    keyMatrix = (key * ((textLength // keyLength) + 1))[:textLength]

    # Decrypt the text
    decryptedText = ""
    for i in range(textLength):
        textChar = ord(text[i].lower()) - 97
        keyChar = ord(keyMatrix[i].lower()) - 97
        decryptedChar = chr(((textChar - keyChar + 26) % 26) + 97)
        decryptedText += decryptedChar if text[i].islower() else decryptedChar.upper()

    return decryptedText


