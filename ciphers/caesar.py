import converter as cv
key = 3

#funkcija šifriranja
def encrypt(plaintext):    
    global key                             
    ciphertext = []
    plaintext = plaintext.lower()
    plaintext = cv.textToNum(plaintext)
    
    for letter in plaintext:
        ciphertext.append(getEncryptionLetter(letter))
        
    return cv.numToText(ciphertext)

#funkcija dešifriranja
def decrypt(ciphertext):                            
    plaintext = []
    ciphertext = ciphertext.lower()
    ciphertext = cv.textToNum(ciphertext)

    for letter in ciphertext:
        plaintext.append(getDecryptionLetter(letter))
    
    return cv.numToText(plaintext)
    
#funkcija koja vraća znak šifrata
def getEncryptionLetter(letter):                       
    return ((letter + key) % 26)
    
#funkcija koja vraća znak otvorenog teksta
def getDecryptionLetter(letter):     
    return ((letter - key) % 26)
    
