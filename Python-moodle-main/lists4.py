num1 = int(input("What is your number? "))
nonTrivialNum = []

for x in range(2, int((num1/2)+1), 1):
    if num1 % x == 0:
        nonTrivialNum.append(x)

print(nonTrivialNum)