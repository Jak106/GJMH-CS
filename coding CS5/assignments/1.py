#The line includes the diner's numerical code, a space and the chosen meal
#Each meals is assigned different color value
#g - green, r - red, b - blue, o - orange)

#1. use the text file to determine the total number of meals ordered (3 points),
#2. count the number of individual meal choices and print the findings (the number of meals ordered for each color) (4 points),
#3. determine whether there is a meal (or meals) ordered less than twenty times and if so, print its assigned color (5 points),
#4. notify us when enough diners have ordered each of the meal options (5 points).

import re

def add(search, string):
    global total
    if search in string:
        meals[search] += int(re.findall(r"[0-9]+", string)[0])
        total += int(re.findall(r"[0-9]+", string)[0])

with open("ordered_meals.txt", "r", encoding="utf-8") as f:
    content = f.read()

total = 0

meals = {
    "g": 0,
    "r": 0,
    "b": 0,
    "o": 0,
}

found = re.findall(r"[0-9]+ [orbg]",content)

for meal in found:
    add("g", meal)
    add("r", meal)
    add("b", meal)
    add("o", meal)

for colour in meals:
    print(f"Meal with assigned colour {colour} was ordered {meals[colour]}")
    print(f"Total number of orders is {total}")
    if meals[colour] < 20:
        print(f"Meal with assigned colour {colour} was ordered less than 20 times")

#Q1: What would your program do if the inputted file totally lacks one of the meal options (nobody ordered that particular meal)?
#A: Nothing unussual would happend, program would print it out as 0 orderes

#Q2: How would you need to modify your program so that it would be able to handle more meal options (in case the menu is expanded)?
#A: I would need to add them to dictionary, then add it to the list of functions checking for different meal options