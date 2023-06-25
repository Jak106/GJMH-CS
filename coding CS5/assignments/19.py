import random

try:
    low = int(input("What is boundary below (including)? "))
    high = int(input("What is boundary above (including)? "))
except:
    print("You have to input number. Please start again")
    exit

while high < low:
    print("You boundary above is less then boundary below. Please be carefull next time.")
    low = int(input("What is boundary below (including)? "))
    high = int(input("What is boundary above (including)? "))

option = input("Do you want to do binary search => B or Random search => R? ").upper()

while option not in "RB":
    print("Answer is either R => random, B => binary. Please choose correct answer.")
    option = input("Do you want to do binary search => B or Random search => R? ").upper()

def binarySearch(bb:int, ba:int):
    print("You are going to have three options:\nE = exactly\nM = more (your number is larger)\nL = less (your number is smaller)\nInput one of those to play game with me when asked.")
    attempt = 0
    guess = int((ba - bb)/2)
    while True:
        attempt += 1
        answer = input(f"My {attempt}. attempt is {guess}. What is your answer? ")
        while answer.upper() not in "EML":
                answer = input(f"My {attempt}. is {guess}. What is your answer (Plese give me answer from options)? ")
        if answer.upper() == "E":
            return f"I am awesome. It only took me {attempt} attempts"
        elif answer.upper() == "M":
            bb = guess
            guess = int(bb + (ba - bb)/2)
        elif answer.upper() == "L":
            ba = guess
            guess = int(bb + (ba - bb)/2)

def randomSearch(bb:int, ba:int):
    print("You are going to have two options:\nC = correct\nW = wrong\nInput one of those to play game with me when asked.")
    used = []
    guess = random.randint(bb, ba)
    while True:
        used.append(guess)
        answer = input(f"My guess is {guess}. Am i correct or wrong? ").upper()
        while answer not in "CW":
            answer = input(f"Please input correct answer, C=correct, W=wrong").upper()
        if answer == "C":
            return f"This is finnaly over, it took me {len(used)} tries"
        if len(used) == ba-bb+1:
            return f"I think you forgot what you am i supposed to be guessing. This game is over."
        guess = random.randint(bb, ba)
        while guess in used:
            guess = random.randint(bb, ba)    

if option == "B":
    print(binarySearch(low, high))
elif option == "R":
    print(randomSearch(low, high))
