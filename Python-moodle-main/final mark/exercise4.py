numList = [5, 5, 5, 0, 1234, 10, 2, 2, 1]

left, right = 0, 0

for num in numList[0:int((len(numList)-1)/2)]:
    left += num

for num in numList[int((len(numList)-1)/2)+1:]:
    right += num

if left < right:
    print("right")
elif left > right:
    print("left")
else:
    print("balanced")
