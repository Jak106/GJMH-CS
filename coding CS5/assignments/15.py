import random as r

with open("virus.txt", "r", encoding="utf-8") as f:
    original = f.read().split("\n")
    
print("\n".join(original))

#shuffle original list
if r.randint(0,1):
    r.shuffle(original)
    
res = ""
for line in original:
    line = line.split(" ")
    if r.randint(0, 1): #checks wether to shuffle sentece
        r.shuffle(line)
    for word in line:
        if r.randint(0, 1): #checks wether to reverse word
            res += word[::-1]
        else:
            res += word
        res += " "
    res += "\n"

print(res)

with open("virus_output.txt", "w", encoding="utf-8") as f:
    f.write(res)
    