alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

with open("files/cifertext_2.txt" ) as f:
    content = f.read()

shift = alphabet.index(content[0])

action = input("Do you want to decrypt or encrypt?, If Decrypt type 'd'; if encrypt type 'e'\n").lower

res = ""

for letter in content:
    if letter in alphabet:
        if action == "d":
            res += alphabet[(alphabet.index(letter)-shift)%len(alphabet)]
        else:
            res += alphabet[(alphabet.index(letter)+shift)%len(alphabet)]
    else:
        res += letter

print(res)
