import random

numList = []
resList = []

while len(numList) < 100:
    numList.append(random.randint(-20, 20))

for x in range(len(numList)-1):
    if numList[x] not in resList:
        resList.append(numList[x])      

print(resList)