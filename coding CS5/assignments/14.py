#this solution is a bit too complicated then it was required due to my decision to change course of solution during coding
import re

with open("expressions.txt", "r") as f:
    lines = f.read().split("\n") 

def find_count(bracket:str, line:str, markup:str):
    matches = re.finditer(bracket, line)
    brackets[markup] = []
    for match in matches:
        brackets[markup].append(match.span()[0])
    return brackets

def compare_count(type1:list, type2:list):
    if len(type1) == len(type2):
        return True
    else:
        return False

def closure(line:str):
    bracks = re.findall("\(|\)", line)
    if bracks[0] == ")" or bracks[-1] == "(":
        return False
    else:
        return True

#to add more types it is important to add them in touples
types = [("circle_forward_bracket", "circle_back_bracket")]
correct, incorrect = 0, 0

for line in lines:
    brackets = {}
    find_count("\(", line, types[0][0])
    find_count("\)", line, types[0][1])
    if compare_count(brackets[0][0], brackets[0][1]) and closure(line):
        with open("correct.txt", "a") as f:
            f.write(line)
        correct += line
    else:
        with open("incorrect.txt", "a") as f:
            f.write(line)
        correct += line

#if i would want to join in other types of brackets it wouldn't be too hard in this case
#first thing i would need to do is to add new markup types of brackets into types variable
#second thing i would need to add find_count function with these types of brackets
#third thing would be to slightly modify closure function to accomodate other types of brackets
#after that i believe it would work

#P.S. at first i wanted to make the function more easily modifiable hovewer i was not sure what datatype to use to accomodate types of brackets