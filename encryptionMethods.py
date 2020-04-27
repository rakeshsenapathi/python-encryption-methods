from consts import *
import math
import string
import itertools

def encryptText(inputData, encryptType):
    if(encryptType == SHIFT_CIPHER):
        return getShiftCipher(inputData)
    if(encryptType == MONO_ALPHABETIC_CIPHER):
        return getMonoAlphabeticCipher(inputData)
    if(encryptType == PLAY_FAIR_CIPHER):
        return getPlayFairCipher(inputData)
    if(encryptType == HILL_CIPHER):
        return getHillCipher(inputData)
    if(encryptType == POLY_ALPHABETIC_CIPHER):
        return getPolyAlphabeticCipher(inputData)
    if(encryptType == TRANSPOSITION_CIPHER):
        return getTranspositionCipher(inputData)
    else:
        return "Invalid Data, Could not proceed with encryption"


# -------- Hill Cypher Implementation

# Python3 code to implement Hill Cipher 
  
keyMatrix = [[0] * 3 for i in range(3)] 
  
# Generate vector for the message 
messageVector = [[0] for i in range(3)] 
  
# Generate vector for the cipher 
cipherMatrix = [[0] for i in range(3)] 
  
# Following function generates the 
# key matrix for the key string 
def getKeyMatrix(key): 
    k = 0
    for i in range(3): 
        for j in range(3): 
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
  
# Following function encrypts the message 
def encrypt(messageVector): 
    for i in range(3): 
        for j in range(1): 
            cipherMatrix[i][j] = 0
            for x in range(3): 
                cipherMatrix[i][j] += (keyMatrix[i][x] * 
                                       messageVector[x][j]) 
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def getHillCipher(message):
    # Get key matrix from the key string 
    getKeyMatrix(KEY) 
  
    # Generate vector for the message 
    for i in range(3): 
        messageVector[i][0] = ord(message[i]) % 65
  
    # Following function generates 
    # the encrypted vector 
    encrypt(messageVector) 
  
    # Generate the encrypted text  
    # from the encrypted vector 
    CipherText = [] 
    for i in range(3): 
        CipherText.append(chr(cipherMatrix[i][0] + 65)) 
    return(CipherText)

# ------------------ Shift/ Caeser Cypher Problem

#A python program to illustrate Caesar Cipher Technique 
def getShiftCipher(inputData): 
    result = "" 
    # traverse text 
    for i in range(len(inputData)): 
        char = inputData[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + CIPHER_VALUE -65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + CIPHER_VALUE - 97) % 26 + 97) 
  
    return(result)

# --------------------------------------------------

# --------------------------------------------------
def getMonoAlphabeticCipher(message):
    translated = ''
    charsA = LETTERS
    charsB = MONO_ALPHABETIC_KEY

    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol

    return(translated)

# --------------------------------------------------------

# -------------- POLYAPLHABETIC ENCRYPTION ---------------

# This function generates the  
# key in a cyclic manner until  
# it's length isn't equal to  
# the length of original text 
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      
# This function returns the  
# encrypted text generated  
# with the help of the key 
def cipherText(string, key): 
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 
      
# This function decrypts the  
# encrypted text and returns  
# the original text 
def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text))

def getPolyAlphabeticCipher(inputData):
    key = generateKey(inputData, KEY) 
    cipher_text = cipherText(inputData,key) 
    return(cipher_text) 

# ------------ TRANSPOSITION ENCRYPTION ----------------------------
  
# Encryption 
def getTranspositionCipher(msg): 
    cipher = "" 
  
    # track key indices 
    k_indx = 0
  
    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(KEY)) 
  
    # calculate column of the matrix 
    col = len(KEY) 
      
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 
  
    # add the padding character '_' in empty 
    # the empty cell of the matix  
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 
  
    # create Matrix and insert message and  
    # padding characters row-wise  
    matrix = [msg_lst[i: i + col]  
              for i in range(0, len(msg_lst), col)] 
  
    # read matrix column-wise using key 
    for _ in range(col): 
        curr_idx = KEY.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        k_indx += 1
  
    return(cipher)

# --------------- PLAY FAIR CIPHER -----------------------

import string
import itertools

def chunker(seq, size):
    it = iter(seq)
    while True:
       chunk = tuple(itertools.islice(it, size))
       if not chunk:
           return
       yield chunk



def prepare_input(dirty):
    """
    Prepare the plaintext by up-casing it
    and separating repeated letters with X's
    """
    
    dirty = ''.join([c.upper() for c in dirty if c in string.ascii_letters])
    clean = ""
    
    if len(dirty) < 2:
        return dirty

    for i in range(len(dirty)-1):
        clean += dirty[i]
        
        if dirty[i] == dirty[i+1]:
            clean += 'X'
    
    clean += dirty[-1]

    if len(clean) & 1:
        clean += 'X'

    return clean

def generate_table(key):

    # I and J are used interchangeably to allow
    # us to use a 5x5 table (25 letters)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # we're using a list instead of a '2d' array because it makes the math 
    # for setting up the table and doing the actual encoding/decoding simpler
    table = []

    # copy key chars into the table if they are in `alphabet` ignoring duplicates
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    # fill the rest of the table in with the remaining alphabet chars
    for char in alphabet:
        if char not in table:
            table.append(char)

    return table

def getPlayFairCipher(inputData):
    table = generate_table(KEY)
    plaintext = prepare_input(inputData)
    ciphertext = ""

    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            ciphertext += table[row1*5+(col1+1)%5]
            ciphertext += table[row2*5+(col2+1)%5]
        elif col1 == col2:
            ciphertext += table[((row1+1)%5)*5+col1]
            ciphertext += table[((row2+1)%5)*5+col2]
        else: # rectangle
            ciphertext += table[row1*5+col2]
            ciphertext += table[row2*5+col1]

    return(ciphertext)