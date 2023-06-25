#Sieve of Eranthostenes
#prvocisla => odmocnina; n/2

n = int(input("What is your number: "))

numList = list(range(2, n+1))

for x in range(1, int(n/2)):
    for y in range(2, int(n/2)):
        try:
            numList.remove(int(numList[x]*y))
        except:
            continue

print(numList)
