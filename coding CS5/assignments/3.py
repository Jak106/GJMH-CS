table = [[" "], ["Z", "X", "E"], ["M", "L", "G"], ["W", "K", "I"], ["D", "A", "Q"], ["F", "P", "Y"], ["T", "B", "C"], ["U", "H", "O"], ["S", "J", "R"], ["V", "N"]]

sentence = "AAAAAAA EEEEEEE IIIIIII"#input("What is your sentence: ").upper()
encode = list(sentence)
decode = ""
frequency = {}

for letter in encode:
    pos = 0
    for lst in table:
        if letter in lst:
            try:
                frequency[str(pos)] += 1
            except:
                frequency[str(pos)] = 1
            decode += str(pos)*(lst.index(letter)+1)
        pos += 1
    decode += " "

print(decode)
print([k for k, v in frequency.items() if v == max(frequency.values())])
