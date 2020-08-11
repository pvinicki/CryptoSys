import math

class Transposition:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.transposition_matrix = []
    
    def encrypt(self, plaintext, key):
        #if(math.ceil(len(plaintext)/len(key)) == 1 ):
        #    return 1
        text = ''
        
        for letter in plaintext:
            if letter not in self.alphabet:
                continue
            else:
                text += letter
                
        rows = math.ceil(len(text)/len(key))
    
        self.generateTranspositonMatrix(text, rows, len(key))  
        
        return self.generateCiphertext(key)
    
    def decrypt(self, ciphertext, key):
        padding = len(ciphertext) % len(key)
        
        if(padding != 0):
            for x in range(len(key) - padding):
                ciphertext += 'x'
            
        print(ciphertext)
        
        rows = math.ceil(len(ciphertext)/len(key))
        matrix = [[0 for x in range(len(key))] for y in range(rows)]

            
        plaintext = ""
        buffer = ""
        column_letters = []
        ordered_letters = []
        
        #stvori listu slova ciji su elementi slova stupaca
        for letter in ciphertext:         
            buffer += letter
        
            if (len(buffer) == rows):
                column_letters.append(buffer)
                buffer = "";
    
        #poredaj stupce slova prema kljucu
        for value in key:
            ordered_letters.append(column_letters[value - 1])
        
        #popuni matricu s ispravnim poretkom slova
        for col in range(len(key)):
            for row in range(rows):
                matrix[row][col] = ordered_letters[col][row]
        
        #iscitaj redove popunjene matrice
        for row in range(rows):
            for col in range(len(key)):
                plaintext += matrix[row][col]
        
        return plaintext
        
    def generateTranspositonMatrix(self, plaintext, rows, cols):
        self.transposition_matrix = [[0 for x in range(cols)] for y in range(rows)]
        print(self.transposition_matrix)
        padding = (cols * rows) - len(plaintext)
        counter = 0

        for row in range(rows):
            for col in range(cols):
                self.transposition_matrix[row][col] = plaintext[counter]
                
                counter += 1
                
                if(counter >= len(plaintext)):
                    self.addPadding(padding, row, col)
                    break
                
                
    def addPadding(self,  padding, row, col):
        counter = 0
        col += 1
        
        while(padding > 0):
            self.transposition_matrix[row][col + counter] = 'x'
            
            padding -= 1
            counter += 1
        
    
    def generateCiphertext(self, key):
        ciphertext = ''
        for num in range(1, len(key)+1):
            index = key.index(num)
            
            for row in self.transposition_matrix:
                ciphertext += str(row[index])
        
        return ciphertext
        