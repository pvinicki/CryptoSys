
def textToNum(text, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    text = text.lower()
    num_array = []
    for letter in text:
        if letter not in alphabet:
            continue
        num_array.append(alphabet.index(letter))
    
    return num_array

def numToText(numarray, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    text = ''
    for value in numarray:
        text += alphabet[value]
        
    return text

def multiNumToText(numarray, alphabet = 'abcdefghijklmnopqrstuvwxyz' ):
    text = []
    buffer = ''
    for row in range(len(numarray)):
        for col in range(len(numarray[0])):
            buffer += (alphabet[numarray[row][col]])
        
        text.append(buffer)
        buffer = ''
        
    
    return ' '.join(text)
            