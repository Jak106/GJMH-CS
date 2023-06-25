import random

with open("vocab_learning.txt", "r", encoding="utf-8") as file:
    translate = file.read().split("\n")

language = input("Select one of the options for translation\na) english -> slovak\nb) slovak -> english\n")
testnum = int(input(f"How many words would you like to translate (max is {int(len(translate)/2)}): "))

while testnum > len(translate):
    testnum = int(input(f"You selected too many words, please set lower number (max is {int(len(translate)/2)}): "))

def setwords(nums):
    correct = 0
    incorrect = 0
    incorrectwords = []
    for num in nums:
        translation = str(input(f'What is your translation for word "{translate[num]}": '))
        if language == "a":
            if translation == translate[num-1]:
                print("Correct!")
                correct += 1
            else:
                print("Incorrect!")
                incorrect += 1
                incorrectwords.append(translate[num])
                incorrectwords.append(translate[num-1])
        elif language == "b":
            if translation == translate[num+1]:
                print("Correct!")
                correct += 1
            else:
                print("Incorrect!")
                incorrect += 1
                incorrectwords.append(translate[num])
                incorrectwords.append(translate[num+1])
    print(f"Correct: {correct}, Incorrect: {incorrect}")
    return incorrectwords

numbers = []
if language == "a": #english -> slovak; slovak [0], english [1]
    for x in range(testnum):
        num = random.randint(0, len(translate))
        while num in numbers or num % 2 == 0:
            num = random.randint(0, len(translate)-1)
        numbers.append(num)
elif language == "b":
    for x in range(testnum):
        num = random.randrange(0, len(translate))
        while num in numbers or num % 2 != 0:
            num = random.randint(0, len(translate)-1)
        numbers.append(num)

with  open("wrong_answers.txt", "w", encoding="utf-8") as f:
    for word in setwords(numbers):
        f.write(f"{word}\n")
