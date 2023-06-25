from operator import indexOf


with open('D:/Program Files (x86)/Github/Python-moodle/final mark/numbers.txt') as f:
    numList = f.readline().split(",")

num = str(input("What number do you want? "))
availPos = []

while num in numList:
    availPos.append(numList.index(num)+len(availPos))
    numList.pop(numList.index(num))

print("It is present at positions", availPos)