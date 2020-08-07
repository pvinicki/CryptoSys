import DES as des
import binascii
import os
import sys

sys.path.append("../resources")

from strings import caesar

print(caesar)
#text = des.encrypt('patrikvi', 'EAB234CA5B2D3572')
#print(text)
#plaintext = des.decrypt(text, 'EAB234CA5B2D3572')
#print(plaintext)

print(os.path.join(os.getcwd(), "resources"))

