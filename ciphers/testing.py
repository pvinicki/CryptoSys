import DES as des
import binascii
import os
import sys

from caesar import Caesar

cs = Caesar('abcdefghijklmnopqrstuvwxyz')
text = cs.encrypt('patrik')

print(text)

#text = des.encrypt('patrikvi', 'EAB234CA5B2D3572')
#print(text)
#plaintext = des.decrypt(text, 'EAB234CA5B2D3572')
#print(plaintext)


