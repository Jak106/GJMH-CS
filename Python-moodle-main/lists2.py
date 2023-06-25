num = 7
numList = []

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

for x in range(1, 101):
    numList.append(num * x)
    if even(x) == True:
        print(numList[x-1])