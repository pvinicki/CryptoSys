import converter as cv

#funkcija šifriranja
def encrypt(plaintext, key):                                               
    ciphertext = []
    plaintext = cv.textToNum(plaintext)

    for letter in plaintext:
        ciphertext.append(getEncryptionLetter(letter, key))

    return cv.numToText(ciphertext)

#funkcija dešifriranja
def decrypt(ciphertext, key):                          
    plaintext = []
    ciphertext = cv.textToNum(ciphertext)

    for letter in ciphertext:
        plaintext.append(getDecryptionLetter(letter, key))
        
    return cv.numToText(plaintext)

#funkcija za dešifriranje "grubom silom"
def bruteForce(ciphertext):
    plaintext = []
    buffer = []
    ciphertext = cv.textToNum(ciphertext)
    
    for key in range(1,26):
        for letter in ciphertext:
            buffer.append(getDecryptionLetter(letter, key))
            
        plaintext.append(buffer)
        buffer = []
        
    return cv.multiNumToText(plaintext)
     
#funkcija koja vraća znak šifrata
def getEncryptionLetter(letter, key):                        
    return ((letter + key) % 26)
    

#funkcija koja vraća znak otvorenog teksta
def getDecryptionLetter(letter, key):                       
    return ((letter - key) % 26)
