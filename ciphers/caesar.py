import converter as cv


class Caesar:
    def __init__(self):
        self.key = 3
        
    #funkcija šifriranja
    def encrypt(self, plaintext):    
        global key                             
        ciphertext = []
        plaintext = plaintext.lower()
        plaintext = cv.textToNum(plaintext)
        
        for letter in plaintext:
            ciphertext.append((letter + self.key) % 26)
            
        return cv.numToText(ciphertext)
    
    #funkcija dešifriranja
    def decrypt(self, ciphertext):                            
        plaintext = []
        ciphertext = ciphertext.lower()
        ciphertext = cv.textToNum(ciphertext)
    
        for letter in ciphertext:
            plaintext.append((letter - self.key) % 26)
        
        return cv.numToText(plaintext)
    
    
