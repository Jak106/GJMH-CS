#this code outputs middle of the string
text = str(input("Input your string: "))

if len(text) >= 3:    
    if len(text)%2 == 0:
        splitS = text[:len(text)//2]
        splitE = text[len(text)//2:]
        print(splitS[len(splitS)-2:] + (splitE[0:2]))
    else:
        splitS = text[:len(text)//2]
        splitE = text[len(text)//2:]
        print(splitS[len(splitS)-1:] + (splitE[0:2]))
else:
    print("This string is not long enough")