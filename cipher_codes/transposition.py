from math import ceil

def tp_encrypt(plaintext: str, num: int) -> str:
    res = [''] * num
    for i in range(num):
        c_i = i
        while c_i < len(plaintext):
            res[i] += plaintext[c_i]
            c_i += num
    return "|"+''.join(res)+"|"

def tp_decrypt(ciphertext: str, num: int) -> str:
    x_rows = num
    y_columns = ceil(len(ciphertext) / num)
    dummy = (x_rows * y_columns) - len(ciphertext)
    
    res = [''] * x_rows
    i = 0
    column = 0
    row = 0
    
    for symbol in ciphertext:
        res[column]+=symbol 
        column+=1

        if (column == y_columns) or (column == x_rows -1 and row >= x_rows - dummy):
            column = 0
            row+=1
    
    return ''.join(res)
