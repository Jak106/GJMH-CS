from random import randint

from rsa import decrypt, encrypt

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def unicodeEnc(text, shift):
    newList = [chr(ord(sth)+shift) for sth in text]
    encrypted = ""
    for x in newList: encrypted += x
    print("encrypted message =", encrypted)
    sndList = [chr(ord(sth)-shift) for sth in newList]
    decrypted = ""
    for x in sndList: decrypted += x
    print("decrypted message =", decrypted)

def basicAlphabet(text, shift):
    try:
        newList = [alphabet.index(sth.capitalize())+shift for sth in text]
        encrypted = ""
        for x in newList:
            if x < len(alphabet):
                encrypted += alphabet[x]
            else:
                encrypted += alphabet[x % len(alphabet)]
        print("encrypted message =", encrypted)
        
        sndList = [alphabet[sth-shift] for sth in newList]
        decrypted = ""
        for x in sndList: decrypted += x
        print("decrypted message =", decrypted)
    except:
        print("You are using unknown letter to english alphabet")

def vigenere(text, word):
    x = 0
    y = 0
    encrypted = ""
    while x < len(text):
        if text[x] in alphabet:
            letterIn = alphabet.index(word[y].capitalize()) + alphabet.index(text[x].capitalize())
            if letterIn <= len(alphabet):
                encrypted += alphabet[letterIn]
            else:
                encrypted += alphabet[letterIn%len(alphabet)]
            y += 1
            if y == len(word):
                y = 0
        else:
            encrypted += text[x]
        x += 1
    print("encrypted message =", encrypted)

    x = 0
    y = 0
    decrypted = ""
    while x < len(encrypted):
        if text[x] in alphabet:
            letterIn = alphabet.index(encrypted[x].capitalize()) - alphabet.index(word[y].capitalize())
            if letterIn <= len(alphabet):
                decrypted += alphabet[letterIn]
            else:
                decrypted += alphabet[letterIn%len(alphabet)]
            y += 1
            if y == len(word):
                y = 0
        else:
            decrypted += text[x]
        x += 1
    print("decrypted message =", decrypted)

def vernam(text):
    key = "WJ SKKVE, DVYK DW PWCVR"
    encrypted = ""
    decrypted = ""
    #for letter in text:
    #    if letter in alphabet:
    #        key += alphabet[randint(0, len(alphabet)-1)]
    #    else:
    #        key += letter
   
    for x in range(0, len(text)):
        if text[x] in alphabet:
            encrypted += alphabet[(alphabet.index(text[x]) + alphabet.index(key[x]))%len(alphabet)]
        else:
            encrypted += text[x]

    for x in range(0, len(text)):
        if text[x] in alphabet:
            decrypted += alphabet[(alphabet.index(encrypted[x]) - alphabet.index(key[x]))%len(alphabet)]
        else:
            decrypted += text[x]
    
    print("Key =", key)
    print("Encrypted message =", encrypted)
    print("Decrypetd message =", decrypted)

t =  f"g fmnc wms bgblr rpylqjyrc gr zw fylb rfyrq ufyr amknsrcpq ypc dmp bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle sqgle qrpglekyicrpylq gq pcamkkclbcb lmu ynnjw ml rfc spj"#input("What message do you want to send? ") #"HI THERE, THIS IS ALICE"
s = 24#int(input("How much do you want to shift? ")) #3
#w = input("Word for Vigenere cipher ") #"BALL"

#print("---------------------- CAESAR UNICODE METHOD -------------------")
#unicodeEnc(t, s)
#print("--------------------- CAESAR ALPHABET METHOD -------------------")
basicAlphabet(t, s)
#print("------------------------ VIGENERE CIPHER -----------------------")
#vigenere(t, w)
#print("------------------------- VERNAM CIPHER ------------------------")
#vernam(t)
