import math

current_row = 0
current_col = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#funkcija za šifriranja
def encrypt(plaintext):
    ciphertext = ""
    matrix = generateMatrix(plaintext)
    print(matrix)
    buffer = []
    for letter in plaintext:
        for row in range(5):
            for col in range(5):
                if (matrix[row][col] == letter):
                    buffer.append([row, col])
                    
                    if(len(buffer) == 2):
                        ciphertext += encryptPair(matrix, buffer)
                        buffer = []
    
    return ciphertext
                    
def encryptPair(matrix, pair):
    ciphertext = ""
    Arow = pair[0][0]
    Acol = pair[0][1]
    Brow = pair[1][0]
    Bcol = pair[1][1]
    
    if(Arow == Brow):
        #zamijeni sa sljedecim u retku
        #vjerojatno dodati mod 5 za pomicanje stupaca i redaka kako bi se osigurala ciklicnost
        ciphertext += matrix[Arow][Acol + 1]
        ciphertext += matrix[Brow][Bcol + 1]
    elif(Acol == Bcol):
        #zamijeni sa sljedecim u stupcu
        ciphertext += matrix[Arow + 1][Acol]
        ciphertext += matrix[Brow + 1][Bcol]
    else:
        #zamijeni vrhovima kvadrata kojeg formiraju elementi
        if(Arow < Brow):
            ciphertext += matrix[Arow][Bcol]
            ciphertext += matrix[Brow][Acol]
        else:
            ciphertext += matrix[Brow][Acol]
            ciphertext += matrix[Arow][Bcol]
    return ciphertext
    
#funkcija koja stvara matricu šifriranja
def generateMatrix(plaintext):
    matrix = [[0 for x in range(5)] for y in range(5)]      #stvori prazno 2D polje s 25 elemenata
    padding = [x for x in alphabet if x not in plaintext]   #slova abecede koja nisu u otvorenom tekstu
    plaintext = plaintext.lower()
    
    unique_letters = getUniqueLetters(plaintext)
    matrix = fillMatrix(matrix, unique_letters)
    matrix = padMatrix(matrix, padding)
    
    return matrix
  
#funkcija koja stvara listu jedinstvenih slova otvorenog teksta              
def getUniqueLetters(plaintext):
    unique_letters = [];
    
    for letter in plaintext:                            
        if (ord(letter) >= 97 and ord(letter) <= 122):
            if letter not in unique_letters:
                unique_letters.append(letter)
    
    return unique_letters
            
#funkcija koja popunjava matricu jedinstvenim slovima otvorenog teksta
def fillMatrix(matrix, unique_letters):
    global current_row
    global current_col
    flag = True
    counter = 0
    
    for row in range(5):                               
        for col in range(5):
            if (flag != True):
                current_row = row
                current_col = col
                return matrix
            
            matrix[row][col] = unique_letters[counter]
            counter += 1
            
            if (counter == len(unique_letters)):
                flag = False

#funkcija koja dopunjuje matricu slovima abecede
def padMatrix(matrix, padding):
    global current_row
    global current_col
    counter = 0
    startPadding = False
    
    for row in range(5):
        for col in range(5):
            if(row == current_row and col == current_col):
                startPadding = True
                
            if (startPadding == True):
                matrix[row][col] = padding[counter]
                counter += 1
    
    return matrix