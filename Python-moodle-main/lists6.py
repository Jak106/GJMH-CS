listCheck = ["hello", 4, ["no", "yes"], True, 6, 8, 10, "definitely int", 5.25]

res = 1

for thing in listCheck:
    if type(thing) == int or type(thing) == float:
        res = res*thing

print(res)