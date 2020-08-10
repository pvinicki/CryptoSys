import math
import converter as cv

class Hill:
    def __init__(self):
        pass
    
    #funkcija šifriranja
    def encrypt(self, plaintext, key, m = 3):
        ciphertext = ''
        letter_vector = []
        buffer = []
        
        #pretvori otvoreni tekst u niz brojeva
        plaintext = cv.textToNum(plaintext)
        
        plaintext = self.padPlaintext(plaintext, m)
        
        for value in plaintext:
            buffer.append(value)
            
            #Stvori 2D polje koje se sastoji od m-elementnih polja
            if(len(buffer) == m):
                letter_vector.append(buffer)
                buffer = []
        
        ciphertext = self.calculateCipher(letter_vector, key, m)
    
        return ciphertext
    
    #funkcija za izračun šifrata
    def calculateCipher(self, letter_vector, key, m):
        ciphertext = ''
        vector = []
        buffer = 0
        
        for value in range(len(letter_vector)):
            for col in range(m):
                for row in range(m):
                    #pomnoži blok od m slova s matricom ključa
                    buffer += (letter_vector[value][row] * key[col][row])
                
                buffer %= 26
                vector.append(buffer)
                buffer = 0
            
            #pretvori izračunate vrijednosti bloka u tekst
            ciphertext += cv.numToText(vector)
            print(ciphertext)
            vector = []
    
        return ciphertext
            
    def padPlaintext(self, plaintext, m):
        remainder = len(plaintext) % m
        if(remainder != 0):
            for value in range (m -  remainder):
                plaintext.append(23)
                
        return plaintext