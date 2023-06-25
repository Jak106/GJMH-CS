import random as r

alphabetOld = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

alphabet = [x.lower() for x in alphabetOld]

with open("cc.txt", "r") as f:
    text = f.read()

def basicAlphabet(text:str, shift:int):
    
    encrypted = alphabet[shift-1]
    
    for sign in text:
        if sign in alphabet:
            try:
                encrypted += alphabet[alphabet.index(sign)+shift]
            except:
                encrypted += alphabet[(alphabet.index(sign)+shift) % len(alphabet)]
        else:
            encrypted += sign
    
    return encrypted
                
                
    
    # try:
    #     newList = [alphabet.index(sth.capitalize())+shift for sth in text]
        
    #     for x in newList:
    #         if x < len(alphabet):
    #             encrypted += alphabet[x]
    #         else:
    #             encrypted += alphabet[x % len(alphabet)]
    #     print("encrypted message =", encrypted)
        
    #     sndList = [alphabet[sth-shift] for sth in newList]
    #     decrypted = ""
    #     for x in sndList: decrypted += x
    #     print("decrypted message =", decrypted)
    # except:

#print(basicAlphabet(text, r.randint(1, len(alphabet))))
print(basicAlphabet(text, 2))