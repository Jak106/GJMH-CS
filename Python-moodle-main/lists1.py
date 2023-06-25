num = 7
numList = []

for x in range(1, 101):
    numList.append(num * x)

reversedList = numList
reversedList.reverse()

print(f'normal list: {numList} \nreversed list: {reversedList}')