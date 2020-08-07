import converter as cv

#funkcija šifriranja
def encrypt(plaintext, key):                                               
    ciphertext = []
    plaintext = plaintext.lower()
    plaintext = cv.textToNum(plaintext)

    for letter in plaintext:
        ciphertext.append((letter + key) % 26)

    return cv.numToText(ciphertext)

#funkcija dešifriranja
def decrypt(ciphertext, key):                          
    plaintext = []
    ciphertext = ciphertext.lower()
    ciphertext = cv.textToNum(ciphertext)

    for letter in ciphertext:
        plaintext.append((letter - key) % 26)
        
    return cv.numToText(plaintext)

#funkcija za dešifriranje "grubom silom"
def bruteForce(ciphertext):
    plaintext = []
    buffer = []
    ciphertext = cv.textToNum(ciphertext)
    
    for key in range(1,26):
        for letter in ciphertext:
            buffer.append((letter - key) % 26)
            
        plaintext.append(buffer)
        buffer = []
        
    return cv.numArrayToText(plaintext)
     