import random as rand
import converter as cv
#ovo NIJE idealna jednokratna biljeznica jer su brojevi kljuca PSEUDO NASUMICNI

#funkcija šifriranja
def encrypt(plaintext):
    ciphertext = []
    key = []
    #pretvori tekst u polje brojeva u rasponu 0-25
    plaintext = cv.textToNum(plaintext)
    
    #za svaku vrijednost otvorenog teksta dodaj pseudonasumican broj u rasponu 0-25
    for value in range(len(plaintext)):
        key.append(rand.randrange(0, 26))
    
    #modularno zborji otvoreni tekst i kljuc
    ciphertext = modularAddition(plaintext, key)
    ciphertext = cv.numToText(ciphertext)
    
    return ciphertext
        
def modularAddition(text, key):
    ciphertext = []
    for value in range(len(text)):
        ciphertext.append((text[value] + key[value]) % 26)
    
    return ciphertext