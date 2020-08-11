import math

class Playfair:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.matrix = [[0 for x in range(5)] for y in range(5)]  
        self.current_row = 0
        self.current_col = 0
        self.flag = True
        
    #funkcija za šifriranja
    def encrypt(self, plaintext):
        ciphertext = ''
        self.flag = True
        
        if(len(plaintext) % 2 != 0):
            plaintext += 'x'

        self.generateMatrix(plaintext)

        buffer = []
        for letter in plaintext:
            for row in range(5):
                for col in range(5):
                    if (self.matrix[row][col] == letter):
                        buffer.append([row, col])
                        
                        if(len(buffer) == 2):
                            ciphertext += self.encryptPair(buffer)
                            buffer = []
                            
            
        print(self.matrix)
        
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ''
        self.flag = False
        
        buffer = []
        for letter in ciphertext:
            for row in range(5):
                for col in range(5):
                    if (self.matrix[row][col] == letter):
                        buffer.append([row, col])
                        
                        if(len(buffer) == 2):
                            plaintext += self.encryptPair(buffer)
                            buffer = []
                            
        return plaintext
                        
    def encryptPair(self, pair):
        ciphertext = ""
        Arow = pair[0][0]
        Acol = pair[0][1]
        Brow = pair[1][0]
        Bcol = pair[1][1]
        
        if(Arow == Brow):
            #zamijeni sa sljedecim u retku
            #vjerojatno dodati mod 5 za pomicanje stupaca i redaka kako bi se osigurala ciklicnost
            if(self.flag):
                ciphertext += self.matrix[Arow][(Acol + 1) % 5]
                ciphertext += self.matrix[Brow][(Bcol + 1) % 5]
                
            else:
                ciphertext += self.matrix[Arow][(Acol - 1) % 5]
                ciphertext += self.matrix[Brow][(Bcol - 1) % 5]
                
        elif(Acol == Bcol):
            #zamijeni sa sljedecim u stupcu
            if(self.flag):
                ciphertext += self.matrix[(Arow + 1) % 5][Acol]
                ciphertext += self.matrix[(Brow + 1) % 5][Bcol]
                
            else:
                ciphertext += self.matrix[(Arow - 1) % 5][Acol]
                ciphertext += self.matrix[(Brow - 1) % 5][Bcol]
                
        else:
            #zamijeni vrhovima kvadrata kojeg formiraju elementi
            if(Arow < Brow):
                ciphertext += self.matrix[Arow][Bcol]
                ciphertext += self.matrix[Brow][Acol]
            else:
                ciphertext += self.matrix[Brow][Acol]
                ciphertext += self.matrix[Arow][Bcol]
                
        return ciphertext
        
    #funkcija koja stvara matricu šifriranja
    def generateMatrix(self, plaintext):
        padding = [x for x in self.alphabet if x not in plaintext]   #slova abecede koja nisu u otvorenom tekstu
        plaintext = plaintext.lower()
        
        unique_letters = self.getUniqueLetters(plaintext)
        self.fillMatrix(unique_letters)
        self.padMatrix(padding)
        
      
    #funkcija koja stvara listu jedinstvenih slova otvorenog teksta              
    def getUniqueLetters(self, plaintext):
        unique_letters = [];
        
        for letter in plaintext:                            
            if (letter in self.alphabet):
                if letter not in unique_letters:
                    unique_letters.append(letter)
        
        return unique_letters
                
    #funkcija koja popunjava matricu jedinstvenim slovima otvorenog teksta
    def fillMatrix(self, unique_letters):
        flag = True
        counter = 0
        
        for row in range(5):                               
            for col in range(5):
                if (flag != True):
                    self.current_row = row
                    self.current_col = col
                    break
                
                self.matrix[row][col] = unique_letters[counter]
                counter += 1
                
                if (counter == len(unique_letters)):
                    flag = False
            
            if(flag != True):
                break
    
    #funkcija koja dopunjuje matricu slovima abecede
    def padMatrix(self, padding):
        counter = 0
        startPadding = False
        
        for row in range(5):
            for col in range(5):
                if(row == self.current_row and col == self.current_col):
                    startPadding = True
                    
                if (startPadding == True):
                    self.matrix[row][col] = padding[counter]
                    counter += 1
        