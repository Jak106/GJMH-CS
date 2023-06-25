import re

from numpy import average

newList = []

with open("pollen.txt") as f:
    lines = f.readlines()

for x in lines:
    newList.append(re.sub("\n", "", x))

totalLoc = int(newList[0])
newList.pop(0)

for x in range (1, len(newList), 2):
    newList.insert(x, newList[x].split(" "))
    newList.pop(x+1)

#problem A ------------------
def problemA(city):
    cityIndex = newList.index(city)
    concentration1 = int(newList[cityIndex+1][0])
    concentration2 = int(newList[cityIndex+1][1])
    return (concentration1 + concentration2) / 2

#problem B -------------------
def problemB():
    totalCon = 0
    for x in range(1, len(newList), 2):
        totalCon += int(newList[x][0]) + int(newList[x][1])

    return totalCon/totalLoc

#problem C -------------------
def problemC():
    top = 0
    for x in range(0, len(newList), 2):
        if problemA(newList[x]) > top:
            top = problemA(newList[x])
    return top

#problem D -------------------
def problemD():
    top = 100
    for x in range(0, len(newList), 2):
        if problemA(newList[x]) < top:
            top = problemA(newList[x])
    return top

print(problemD())