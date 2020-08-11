import math
import converter as cv
import numpy as np
from numpy.linalg import inv, det

class Hill:
    def __init__(self):
        self.key = []
        pass
    
    #funkcija šifriranja
    def encrypt(self, plaintext, key, m = 3):
        self.key = key
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
        
        ciphertext = self.calculateCipher(letter_vector, m)
    
        return ciphertext
    
    def decrypt(self, ciphertext, m = 3):
        plaintext = ''
        self.invkey = self.findInverseMatrix()
        plaintext = self.encrypt(ciphertext, self.invkey)
        
        return plaintext
        
    def findInverseMatrix(self):
        #pronadji determinantu
        determinant = round(det(self.key))
        determinant = determinant % 26
        
        #pronadji inverz determinante
        inv_determinant = self.findMultiplicativeInverse(determinant)
        
        #izracunaj matricu 
        adjugate_matrix = self.calculateAdjugateMatrix()
        
        #adjugate_matrix = inv(self.key)
        #adjugate_matrix = np.dot(inv(self.key), inv_determinant)
        
        #promijeni predznake dobivene matrice
        adjugate_matrix[0][1] = -1 * adjugate_matrix[0][1]
        adjugate_matrix[1][0] = -1 * adjugate_matrix[1][0]
        adjugate_matrix[1][2] = -1 * adjugate_matrix[1][2]
        adjugate_matrix[2][1] = -1 * adjugate_matrix[2][1]
        
        #mod 26 dobivenu matricu
        for row in range(3):
            for col in range(3):
                adjugate_matrix[row][col] = round(adjugate_matrix[row][col] % 26)
                print(round(adjugate_matrix[row][col] % 26))
        
        #pomnozi matricu i inverznu determinantu
        adjugate_matrix = np.dot(adjugate_matrix, inv_determinant)
        
        #mod 26
        for row in range(3):
            for col in range(3):
                adjugate_matrix[row][col] = round(adjugate_matrix[row][col] % 26)
        
        return adjugate_matrix
    
    def calculateAdjugateMatrix(self):
        adjugate_matrix = [[0 for x in range(3)] for y in range(3)]
        adjugate_matrix[0][0] = (self.key[1][1] * self.key[2][2]) - (self.key[1][2] * self.key[2][1])
        adjugate_matrix[0][1] = (self.key[0][1] * self.key[2][2]) - (self.key[0][2] * self.key[2][1])
        adjugate_matrix[0][2] = (self.key[0][1] * self.key[1][2]) - (self.key[0][2] * self.key[1][1])
        adjugate_matrix[1][0] = (self.key[1][0] * self.key[2][2]) - (self.key[1][2] * self.key[2][0])
        adjugate_matrix[1][1] = (self.key[0][0] * self.key[2][2]) - (self.key[0][2] * self.key[2][0])
        adjugate_matrix[1][2] = (self.key[0][0] * self.key[1][2]) - (self.key[0][2] * self.key[1][0])
        adjugate_matrix[2][0] = (self.key[1][0] * self.key[2][1]) - (self.key[1][1] * self.key[2][0])
        adjugate_matrix[2][1] = (self.key[0][0] * self.key[2][1]) - (self.key[0][1] * self.key[2][0])
        adjugate_matrix[2][2] = (self.key[0][0] * self.key[1][1]) - (self.key[0][1] * self.key[1][0])
        
        return adjugate_matrix
        
    def findMultiplicativeInverse(self, determinant):
        inv_determinant = -1
        
        for x in range(26):
            if(((determinant * x) % 26) == 1):
                inv_determinant = x
                
        return inv_determinant
        
    #funkcija za izračun šifrata
    def calculateCipher(self, letter_vector, m):
        ciphertext = ''
        vector = []
        buffer = 0
        
        for value in range(len(letter_vector)):
            for col in range(m):
                for row in range(m):
                    #pomnoži blok od m slova s matricom ključa
                    buffer += int((letter_vector[value][row] * self.key[col][row]))
                
                buffer %= 26
                vector.append(buffer)
                buffer = 0
            
            #pretvori izračunate vrijednosti bloka u tekst
            print(vector)
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