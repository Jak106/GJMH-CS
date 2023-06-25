nums = [9222, 5873, -5623, 9074, 3481, -2922, -1633, -853, 485]
newList = []

for num in nums:
    if num >= 0:
        newList.append(int(str(num)[::-1]))
    else:
        newList.append(int("-" + str(abs(num))[::-1]))

print(newList)