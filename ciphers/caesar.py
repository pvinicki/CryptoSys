import converter as cv
key = 3

#funkcija šifriranja
def encrypt(plaintext):    
    global key                             
    ciphertext = []
    plaintext = plaintext.lower()
    plaintext = cv.textToNum(plaintext)
    
    for letter in plaintext:
        ciphertext.append((letter + key) % 26)
        
    return cv.numToText(ciphertext)

#funkcija dešifriranja
def decrypt(ciphertext):                            
    plaintext = []
    ciphertext = ciphertext.lower()
    ciphertext = cv.textToNum(ciphertext)

    for letter in ciphertext:
        plaintext.append((letter - key) % 26)
    
    return cv.numToText(plaintext)
    
    
