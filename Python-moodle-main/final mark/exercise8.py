import random

myCards = random.sample(range(1, 10), 5)
yourCards = random.sample(range(1, 10), 5)

print("My cards:", myCards)
print("Your cards:", yourCards)
myCards.sort()
yourCards.sort()

myComb = str(myCards[len(myCards)-1])+str(myCards[len(myCards)-2])
yourComb = str(yourCards[len(yourCards)-1])+str(yourCards[len(yourCards)-2])

print("You can get", myComb)
print("Your opponent can get", yourComb)

if myComb > yourComb:
    print("You have won")
else:
    print("You have lost")
