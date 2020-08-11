import math
initialPermutation = [57, 49, 41, 33, 25, 17,  9,
                       1, 58, 50, 42, 34, 26, 18,
                      10,  2, 59, 51, 43, 35, 27,
                      19, 11,  3, 60, 52, 44, 36,
                      63, 55, 47, 39, 31, 23, 15,
                       7, 62, 54, 46, 38, 30, 22,
                      14,  6, 61, 53, 45, 37, 29,
                      21, 13,  5, 28, 20, 12,  4]

initialPerm       = [58, 50, 42, 34, 26, 18, 10, 2,
                      60, 52, 44, 36, 28, 20, 12, 4,
                      62, 54, 46, 38, 30, 22, 14, 6,
                      64, 56, 48, 40, 32, 24, 16, 8,
                      57, 49, 41, 33, 25, 17,  9, 1,
                      59, 51, 43, 35, 27, 19, 11, 3,
                      61, 53, 45, 37, 29, 21, 13, 5,
                      63, 55, 47, 39, 31, 23, 15, 7]

finalPermutation = [40,  8, 48, 16, 56, 24, 64, 32,
                    39,  7, 47, 15, 55, 23, 63, 31,
                    38,  6, 46, 13, 54, 22, 62, 30,
                    37,  5, 45, 13, 53, 21, 61, 29,
                    36,  4, 44, 12, 52, 20, 60, 28,
                    35,  3, 43, 11, 51, 19, 59, 27,
                    34,  2, 42, 10, 50, 18, 58, 26,
                    33,  1, 41,  9, 49, 17, 57, 25]

compressionDBox = [14, 17, 11, 24,  1,  5,  3, 28,
                   15,  6, 21, 10, 23, 19, 12,  4,
                   26,  8, 16,  7, 27, 20, 13,  2,
                   41, 52, 31, 37, 47, 55, 30, 40,
                   51, 45, 33, 48, 44, 49, 39, 56,
                   34, 53, 46, 42, 50, 36, 29, 32]

expansionDBox = [32,  1,  2,  3,  4,  5,
                  4,  5,  6,  7,  8,  9,
                  8,  9, 10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32,  1]

straightDBox = [16,  7, 20, 21, 29, 12, 28, 17,
                 1, 15, 23, 26,  5, 18, 31, 10,
                 2,  8, 24, 14, 32, 27,  3,  9,
                19, 13, 30,  6, 22, 11,  4, 25]

#napisat s kutije i sve s kutije staviti u sboxes polje
S1 = [[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
      [ 0, 15,  7,  4, 14,  2, 13, 10,  3,  6, 12, 11,  9,  5,  3,  8],
      [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
      [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]]

S2 = [[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
      [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
      [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
      [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]]

S3 = [[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
      [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
      [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
      [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]]

S4 = [[ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
      [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
      [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
      [ 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]]

S5 = [[ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
      [13, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
      [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
      [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]]

S6 = [[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
      [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
      [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
      [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7, 10,  0,  8, 13]]

S7 = [[ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
      [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
      [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
      [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]]

S8 = [[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
      [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11, 10, 14,  9,  2],
      [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 10, 15,  3,  5,  8],
      [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  9,  3,  5,  6, 11]]

sboxes = [S1, S2, S3, S4, S5, S6, S7, S8]
key_shift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
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
    #key = bin((temp & (key << 2)) | int(bin((key >> (6 - 2)))[2:].zfill(6),2))[2:]
        
    