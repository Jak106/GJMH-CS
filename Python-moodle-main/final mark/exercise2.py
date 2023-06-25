#-6,4,6,1,10,13,1,4,2,-7,0,13,10,13
numList = "-6,4,6,1,10,13,1,4,2,-7,0,13,10,13".split(",")

unique, repeated = [], []

for num in numList:
    if numList.count(num) == 1:
        unique.append(int(num))
    else:
        if int(num) not in repeated:
            repeated.append(int(num))

print("Unique:", unique)
print("Repeated:", repeated)