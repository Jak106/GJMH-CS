numList = [1, 2, 3, 8, 10, 254, 47, '568', 64]

for x in range(0, len(numList)-1):
    if type(numList[x]) == str:
        numList.pop(x)
print(max(numList))