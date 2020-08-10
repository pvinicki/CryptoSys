import converter as cv


class Vigenere():
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.letter_matrix = [[0 for x in range(len(self.alphabet))] for y in range(len(self.alphabet))]
        
    #funkcija šifriranja
    def encrypt(self, plaintext, key):
        ciphertext = ''
        numKey = []
        self.generateLetterMatrix()
        
        plaintext = cv.textToNum(plaintext)
        numKey    = cv.textToNum(key)
        counter = 0
    
        for letter in plaintext:
            if(counter >= len(key)):
                counter = 0
    
            ciphertext += self.letter_matrix[letter][numKey[counter]]
            counter += 1
        
        return ciphertext
    
    #funkcija šifriranja s autoključem
    def autokeyEncrypt(self, plaintext, key):
        ciphertext = ''
        numKey = []
        self.generateLetterMatrix()
        
        plaintext = cv.textToNum(plaintext)
        numKey    = cv.textToNum(key)
        
        counter = 0
        
        for letter in numKey:
            ciphertext += self.letter_matrix[plaintext[counter]][letter]
            counter += 1
            
        position = counter
        counter = 0
            
        while(position < len(plaintext)):
            ciphertext += self.letter_matrix[plaintext[position]][plaintext[counter]]
            counter += 1
            position += 1
            
        return ciphertext
    
    def autokeyDecrypt(self, ciphertext, key):
        plaintext = ''
        numKey    = []
    
        self.generateLetterMatrix()
        ciphertext = cv.textToNum(ciphertext)
        numKey     = cv.textToNum(key)
        
        counter = 0
        
        for index in numKey:
            for letter in self.alphabet: 
                if(ciphertext[counter] == self.alphabet.index(self.letter_matrix[self.alphabet.index(letter)][index])):                         
                    plaintext += letter
                    
            counter += 1
            
        position = counter
        counter = 0
        
        while(position < len(ciphertext)):
            for letter in self.alphabet: 
                if(ciphertext[position] == self.alphabet.index(self.letter_matrix[self.alphabet.index(letter)][self.alphabet.index(plaintext[counter])])):                         
                    plaintext += letter
            
            position += 1
            counter += 1
        
        return plaintext
    
    #funkcija dešifriranja
    def decrypt(self, ciphertext, key):
        plaintext = ''
        numKey    = []
    
        self.generateLetterMatrix()
        
        ciphertext = cv.textToNum(ciphertext)
        numKey     = cv.textToNum(key)
        counter = 0
        
        #za svaki znak u šifratu
        for cipherletter in ciphertext:                                                      
            if(counter >= len(key)):                
                counter = 0
            
            #pronađi slovo koje uz ključ indeksira polje vigenereovog kvadrata
            #čiji je element odgovarajući znak šifrata. 
            for letter in self.alphabet: 
                if(cipherletter == self.alphabet.index(self.letter_matrix[self.alphabet.index(letter)][numKey[counter]])):                         
                    plaintext += letter
                    
            counter += 1
        
        return plaintext
    
    #funkcija koja generira Vigenereov kvadrat s predanom abecedom
    def generateLetterMatrix(self):                 
        starting_position = 0
        
        for i in range(len(self.letter_matrix)):
            value = starting_position
            
            for j in range(len(self.letter_matrix[i])):
                
                if(value >= len(self.alphabet)):
                    value = 0
                    
                self.letter_matrix[i][j] = self.alphabet[value]
                value += 1
                
            starting_position += 1 
        
        #ispis abecede
        for i in range(len(self.letter_matrix)):
            for j in range(len(self.letter_matrix[i])):
                print(self.letter_matrix[i][j], end=" ")
                
            print('\n')
            
            
        
        
