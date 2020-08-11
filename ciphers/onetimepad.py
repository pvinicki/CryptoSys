import random as rand
import converter as cv
#ovo NIJE idealna jednokratna biljeznica jer su brojevi kljuca PSEUDO NASUMICNI

class OneTimePad:
    def __init__(self):
        pass
    
    #funkcija šifriranja
    def encrypt(self, plaintext):
        ciphertext = []
        result = []
        key = []
        #pretvori tekst u polje brojeva u rasponu 0-25
        plaintext = cv.textToNum(plaintext)
        
        #za svaku vrijednost otvorenog teksta dodaj pseudonasumican broj u rasponu 0-25
        for value in range(len(plaintext)):
            key.append(rand.randrange(0, 26))
        
        #modularno zborji otvoreni tekst i kljuc
        ciphertext = self.modularAddition(plaintext, key)
        ciphertext = cv.numToText(ciphertext)
        
        result.append(ciphertext)
        result.append(cv.numToText(key))
        
        return result
            
    def modularAddition(self, text, key):
        ciphertext = []
        for value in range(len(text)):
            ciphertext.append((text[value] + key[value]) % 26)
        
        return ciphertext