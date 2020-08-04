alphabet = 'abcdefghijklmnopqrstuvwxyz'
import converter as cv
letter_matrix = [[0 for x in range(len(alphabet))] for y in range(len(alphabet))]

#funkcija šifriranja
def encrypt(plaintext, key):
    ciphertext = ''
    numKey = []
    letter_matrix = generateLetterMatrix()
    
    plaintext = cv.textToNum(plaintext)
    numKey    = cv.textToNum(key)
    counter = 0

    for letter in plaintext:
        if(counter >= len(key)):
            counter = 0

        ciphertext += letter_matrix[letter][numKey[counter]]
        counter += 1
    
    return ciphertext

#funkcija šifriranja s autoključem
def autokeyEncrypt(plaintext, key):
    ciphertext = ''
    numKey = []
    letter_matrix = generateLetterMatrix()
    
    plaintext = cv.textToNum(plaintext)
    numKey    = cv.textToNum(key)
    
    counter = 0
    
    for letter in numKey:
        ciphertext += letter_matrix[plaintext[counter]][letter]
        counter += 1
        
    position = counter
    counter = 0
    
    while(position < len(plaintext)):
        ciphertext += letter_matrix[plaintext[position]][plaintext[counter]]
        counter += 1
        position += 1
        
    return ciphertext

def autokeyDecrypt(ciphertext, key):
    plaintext = ''
    numKey    = []

    letter_matrix = generateLetterMatrix()
    ciphertext = cv.textToNum(ciphertext)
    numKey     = cv.textToNum(key)
    counter = 0

#funkcija dešifriranja
def decrypt(ciphertext, key):
    plaintext = ''
    numKey    = []

    letter_matrix = generateLetterMatrix()
    ciphertext = cv.textToNum(ciphertext)
    numKey     = cv.textToNum(key)
    counter = 0
    
    #za svaki znak u šifratu
    for cipherletter in ciphertext:                                                      
        if(counter >= len(key)):                
            counter = 0
        
        #pronađi slovo koje uz ključ indeksira polje vigenereovog kvadrata
        #čiji je element odgovarajući znak šifrata. 
        for letter in alphabet: 
            if(cipherletter == alphabet.index(letter_matrix[alphabet.index(letter)][numKey[counter]])):                         
                plaintext += letter
                
        counter += 1
    
    return plaintext

#funkcija koja generira Vigenereov kvadrat s predanom abecedom
def generateLetterMatrix():                 
    starting_position = 0
    
    for i in range(len(letter_matrix)):
        value = starting_position
        
        for j in range(len(letter_matrix[i])):
            
            if(value >= len(alphabet)):
                value = 0
                
            letter_matrix[i][j] = alphabet[value]
            value += 1
            
        starting_position += 1 
    
    #ispis abecede
    for i in range(len(letter_matrix)):
        for j in range(len(letter_matrix[i])):
            print(letter_matrix[i][j], end=" ")
            
        print('\n')
        
    return letter_matrix
            
        
        
