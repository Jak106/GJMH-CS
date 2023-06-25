import random

myDictionary = ["train", "bus", "electrobike", "informatics", "guess", "idea", "school", "calendar"]
letterList = []

word = random.choice(myDictionary)

for letter in word:
    letterList.append(letter)

letterList.sort()

alphaWord = ''.join(letterList)

for i in range(1, 6):
    guess = str(input(f'{alphaWord} What is your answer? '))
    if guess == word:
        print("Your guess is correct")
        exit
    else:
        print(f'Your guess was not correct, you have {5-i} tries left')
else:
    print("You are failure")