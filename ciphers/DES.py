import math
from ciphers.config.descfg import (initialPermutation, initialPerm, finalPermutation, compressionDBox, expansionDBox, straightDBox, S1, S2, S3, S4, S5, S6, S7, S8, key_shift)
sboxes = [S1, S2, S3, S4, S5, S6, S7, S8]
flag = True

def encrypt(plaintext, key, isText, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    flag = True
    ciphertext = ''
    buffer = ''
    roundKeys = generateRoundKeys(key)
    print('roundkeys encrypt: ')
    print(roundKeys)
    print('\n')
    
    #napravi listu blocks u koju dodas sve blokove i onda procesirat
    if(isText):
        for letter in plaintext:
            if letter not in alphabet:
                continue
            else:
                buffer += letter
                
            if(len(buffer) == 8):
                block = textToBin(buffer)
                
                block = permuteBlock(block)
                ciphertext += processBlock(block, roundKeys, flag)
                buffer = ''
    else:
        
        for letter in plaintext:
            
            buffer += letter
            
            if(len(buffer) == 16):
                print(buffer)
                block = hexToBin(buffer)
                
                block = permuteBlock(block)
                ciphertext += processBlock(block, roundKeys, flag)
                buffer = ''
    
    print("encrypted block: " + ciphertext)
    ciphertext = hex(int(ciphertext, 2))[2:]
    return ciphertext

def permuteBlock(block):
    buffer = ''
    
    for element in initialPerm:
        buffer += block[element - 1]
        
    return buffer
    
#zasto ne radi ?
def decrypt(ciphertext, key, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    flag = False
    plaintext = ''
    buffer = ''
    blocks = []
    roundKeys = generateRoundKeys(key)
    roundKeys = list(reversed(roundKeys))
    print('roundkeys decrypt: ')
    print(roundKeys)
    print('\n')
    
    ciphertext = bin(int(ciphertext, 16))[2:].zfill(64)
    
    for element in ciphertext:
        buffer += element
        
        if(len(buffer) == 64):
            blocks.append(buffer)
            buffer = ''
    
    for element in blocks:
        element = permuteBlock(element)
        plaintext += processBlock(element, roundKeys, flag)
        print("decrypted block: " + plaintext)
    
    plaintext= hex(int(plaintext, 2))[2:]
    return plaintext
    
    
def processBlock(block, roundKeys, flag):
    lbl = ''
    rbl = ''
    temp = ''
    encrypted_block = ''
    
    for n in range(32):
        lbl += block[n]

    for n in range(32, 64):
        rbl += block[n]     
        
    for n in range(16):
        result = feistelRound(lbl, rbl, roundKeys[n])
        lbl = result[0]
        rbl = result[1]
    
    temp = rbl + lbl
        
    #inverzna permutacija
    for element in finalPermutation:
        encrypted_block += temp[element-1]
    
    return encrypted_block
            
def feistelRound(lbl, rbl, key):
    temp = rbl
    result = []
    
    rbl = roundFunction(rbl, key)
    
    #xor lijeve i desne polovice
    lbl = int(lbl, 2)
    rbl = int(rbl, 2)
    
    rbl = rbl ^ lbl
    rbl = bin(rbl)[2:].zfill(32)
    

    #zamjena
    lbl = temp
    
    result.append(lbl)
    result.append(rbl)
    
    return result
    
def roundFunction(block, key):
    expblock = ''
    sblocks = []
    sresult  = ''
    rbl = ''
    
    #ekspanzija
    for element in expansionDBox:
        expblock += block[element-1]
    
    #XOR s ključem
    expblock = int(expblock, 2)
    key      = int(key, 2)
    
    expblock = expblock ^ key
    expblock = bin(expblock)[2:].zfill(48)
    
    #razdvajanje na 6 bitne blokove
    buffer = ''
    for element in expblock:
        buffer += element
        
        if(len(buffer) == 6):
            sblocks.append(buffer)
            buffer = ''

            
    #supstitucija
    for n in range(8):
        row = int((sblocks[n][0] + sblocks[n][5]), 2)
        col = int((sblocks[n][1] + sblocks[n][2] + sblocks[n][3] + sblocks[n][4]), 2)
        sresult += bin(sboxes[n][row][col])[2:].zfill(4)
    
    
    for element in straightDBox:
        rbl += sresult[element-1]
        
    return rbl
        
    
        
def hexToBin(text):
    bin_block = bin(int(text, 16))[2:].zfill(64)
    #bin_block = bin_block.split(' ')
    
    return bin_block

def textToBin(text):
    bin_block = ''.join(format(ord(x), 'b') for x in text)[2:].zfill(64)

    
    return bin_block

        
def generateRoundKeys(key):
    roundKeys  = []
    temp = []
    permuted_key = ''
     
    key = bin(int(key, 16))[2:].zfill(64)
    
    #inicijalna permutacija
    for element in initialPermutation:
        permuted_key += key[element-1]
        
    temp = getShiftedKeys(permuted_key)
    
    #stvaranje kljuceva za pojedinu rundu
    for n in range(16):
        buffer = ''
        
        for element in compressionDBox:
            buffer += temp[n][element - 1]
            
        roundKeys.append(buffer)

    return roundKeys

def getShiftedKeys(permuted_key):
    temp = []
    lh = ''
    rh = ''
     
    #lijeva polovica kljuca
    for n in range(28):
        lh += permuted_key[n]
        
    #desna polovica kljuca
    for n in range(27, 56):
        rh += permuted_key[n]
        
    
    #pomicanje bitova kljuceva ulijevo
    for element in key_shift:
        lh = int(lh, 2)
        rh = int(rh, 2)
        lh = rotateLeft(lh, element)
        rh = rotateLeft(rh, element)
        
        temp.append(lh + rh)
     
    return temp

        
def rotateLeft(bits, n):
    temp = '1111111111111111111111111111'    
    temp = int(temp, 2)
    
    fillBits  = int(bin(bits >> (28 - n))[2:].zfill(28),2)
    leftShift = int(bin(temp & bits << n)[2:].zfill(28),2)
    
    return bin(leftShift | fillBits)[2:].zfill(28)
        
    