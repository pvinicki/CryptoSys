import DES as des
import binascii
import os
import sys

text = des.encrypt('0123456789ABCDEF', '133457799BBCDFF1')
print(text)

result = des.decrypt(text, '133457799BBCDFF1')
print(result)

#print(bin(int('123', 16))[2:].zfill(12))
#decrypted = des.decrypt(text, 'EAB234CA5B2D3572')
#print(decrypted)

#bits = '1011'
#temp = '1111'    
#temp = int(temp, 2)
#bits = int(bits, 2)

#fillBits = int(bin(bits >> 3)[2:].zfill(4),2)
#leftShift = int(bin(temp & bits << 1)[2:].zfill(4),2)

#result = bin((temp & bits << 1) | int(bin((bits >> (3)))[2:].zfill(4), 2))[2:]
#result = bin((temp & (bits << 1)) | int(bin((bits >> (4 - 1)))[2:].zfill(4), 2))[2:]

#print(leftShift)
#print(fillBits)

#print(bin(leftShift | fillBits)[2:].zfill(4))

