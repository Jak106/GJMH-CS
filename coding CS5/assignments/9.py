import re

with open("isbn.txt", "r") as f:
    numbers = f.read().split("\n")

valid, invalid = [], []

def fileWrite(filename:str, content:list):
    with open(filename, "w") as f:
        for num in content:
            f.write(f'{num}\n')

def checkNum(number:str):
    count = 0
    if len(number) != 13:
        return False
    for num in range(len(number)):
        if num % 2 != 0:
            count += 3*int(number[num:num+1])
        else:
            count += int(number[num:num+1])
    if count % 10 == 0:
        return True
    else:
        return False

def checkText(text:str):
    if len(text) == 0:
        return True
    elif text == "ISBN":
        return True
    else:
        return False

for isbn in numbers:
    text = re.findall(r'[a-zA-Z]+', isbn)
    marks = re.findall(r'-{2,}', isbn)

    if re.match(r'ISBN-13|ISBN13', isbn) == None:
        nums = ''.join(re.findall(r'[0-9]+', isbn))
    else:
        nums = re.findall(r'[0-9]+', isbn)
        nums.pop(0)
        nums = ''.join(nums)

    if checkText(''.join(text).upper()) and len(marks) == 0 and checkNum(nums):
        valid.append(isbn)
    else:
       invalid.append(isbn)

fileWrite("correct_ISBN.txt", valid)
fileWrite("incorrect_ISBN.txt", invalid)
