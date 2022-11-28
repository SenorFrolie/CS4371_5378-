#This document contains the encryption and decryption functions that will be used 
# to encrypt source, destination, and data fields, 
def Encrypt(inputText):
    N = 7
    D = 1
    inputT = str(inputText)[::-1]
    encryptedText = ''
    shift = N
    for i in range(len(inputT)):
        if ( (N + ord(inputT[i])) > 126):
            shift -= (126 - ord(inputT[i]))
            shift = shift%92
            encryptedText += chr(33+shift)
            shift = N
        else:
            encryptedText += chr(N + (ord(inputT[i]) ))
    return encryptedText

def Decrypt(inputText):
    N = 7
    D = -1
    inputT = str(inputText)[::-1]
    encryptedText = ''
    shift = N
    for i in range(len(inputT)):
        if ( (ord(inputT[i])- N) < 34):
            shift += (34 - ord(inputT[i]))
            shift = shift%92
            encryptedText += chr(127-shift)
            shift = N
        else:
            encryptedText += chr((ord(inputT[i]) - N))
    return encryptedText