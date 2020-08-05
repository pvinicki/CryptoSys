import math
initialPermutation = [58, 50, 42, 34, 26, 18, 10, 2,
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
                  8,  9, 19, 11, 12, 13,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 31, 31, 32,  1]

straightDBox = [16,  7, 20, 21, 29, 12, 28, 17,
                 1, 15, 23, 26,  5, 18, 31, 10,
                 2,  8, 24, 14, 32, 27,  3,  9,
                19, 13, 30,  6, 22, 11,  4, 25]

#napisat s kutije i sve s kutije staviti u sboxes polje
S1 = []

key_shift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def encrypt(plaintext, key, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    ciphertext = ''
    buffer = ''
    roundKeys = generateRoundKeys(key)
    
    for letter in plaintext:
        if letter not in alphabet:
            continue
        
        buffer += letter
        
        if(len(buffer) == 8):
            block = getBlock(buffer)
            ciphertext += processBlock(block, roundKeys)
            buffer = ''
            
def processBlock(block, roundKeys):
    lbl = ''
    rbl = ''
    temp = ''
    result = ''
    
    for n in range(32):
        lbl += block[n]

    for n in range(32, 64):
        rbl += block[n]     
        
    for n in range(16):
        result = feistelRound(lbl, rbl, roundKeys[n])
        lbl = result[0]
        rbl = result[1]
    
    #krajnja zamjena
    temp = rbl + lbl
    
    #inverzna permutacija
    for element in finalPermutation:
        result += temp[element]
            
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
        col = int((sblocks[n][1] + sblocks[n][2] + sblocks[n][3] + sblocks[n][4]))
        sresult += bin(sboxes[n][row][col])[2:].zfill(4)
        
    for element in straightDBox:
        rbl += sresult[element]
        
    return rbl
        
    
        
def getBlock(text):
    bin_block = ''.join(format(ord(x), 'b').zfill(8) for x in text)
    #bin_block = bin_block.split(' ')
    
    return bin_block

        
def generateRoundKeys(key):
    roundKeys   = []
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
            buffer += temp[n][element]
            
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
    temp = '1111111111111111111111111111111111111111111111111111111111111111'    
    temp = int(temp, 2)
    
    return bin((temp & (bits << n)) | int(bin((bits >> (64 - n)))[2:].zfill(64), 2))[2:]
    #key = bin((temp & (key << 2)) | int(bin((key >> (6 - 2)))[2:].zfill(6),2))[2:]
        
    