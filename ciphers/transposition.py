import math

def encrypt(plaintext, key):
    key= key.split(',')
    for element in key:
        key[key.index(element)] = int(element)
        
    rows = math.ceil(len(plaintext)/len(key))

    transposition_matrix = generateTranspositonMatrix(plaintext, rows, len(key))     
    return generateCiphertext(transposition_matrix, key)

def decrypt(ciphertext, key):
    key= key.split(',')
    for element in key:
        key[key.index(element)] = int(element)
        
    rows = math.ceil(len(ciphertext)/len(key))
    matrix = [[0 for x in range(len(key))] for y in range(rows)]
    plaintext = ""
    buffer = ""
    column_letters = []
    ordered_letters = []
    
    #stvori listu slova ciji su elementi slova stupaca
    for letter in ciphertext:         
        buffer += letter
    
        if (len(buffer) == rows):
            column_letters.append(buffer)
            buffer = "";

    #poredaj stupce slova prema kljucu
    for value in key:
        ordered_letters.append(column_letters[value - 1])
    
    #popuni matricu s ispravnim poretkom slova
    for col in range(len(key)):
        for row in range(rows):
            matrix[row][col] = ordered_letters[col][row]
    
    #iscitaj redove popunjene matrice
    for row in range(rows):
        for col in range(len(key)):
            plaintext += matrix[row][col]
    
    return plaintext
    
def generateTranspositonMatrix(plaintext, rows, cols):
    transposition_matrix = [[0 for x in range(cols)] for y in range(rows)]
    padding = (cols * rows) - len(plaintext)
    counter = 0
    
    for row in range(rows):
        for col in range(cols):
            transposition_matrix[row][col] = plaintext[counter]
            
            counter += 1
            
            if(counter >= len(plaintext)):
                transposition_matrix = addPadding(transposition_matrix, padding, row, col)
                break
            
    return transposition_matrix
            
def addPadding(transposition_matrix, padding, row, col):
    counter = 0
    col += 1
    
    while(padding > 0):
        transposition_matrix[row][col + counter] = 'x'
        
        padding -= 1
        counter += 1
    
    return transposition_matrix

def generateCiphertext(transposition_matrix, key):
    ciphertext = ''
    print(key)
    for num in range(1, len(key)+1):
        index = key.index(num)
        
        for row in transposition_matrix:
            ciphertext += str(row[index])
    
    return ciphertext
        