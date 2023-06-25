numList = "-68,-5,36,-97,48,-18,12,20,85,-51,-33,64".split(",")

neg, pos = 0, 0

for num in numList:
    if int(num) < 0:
        neg += int(num)
    else:
        pos += int(num)

print("Sum of non-negative values:", pos)
print("Sum of negative values:", neg)

if abs(neg) > abs(pos):
    print("The sum of negative numbers is greater in the magnitude.")
else:
    print("The sum of positive numbers is greater in the magnitude.")