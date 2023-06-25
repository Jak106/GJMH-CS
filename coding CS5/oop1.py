from unittest import result


def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

def getResult(num1, mark, num2):
    if mark == "+":
        return str(int(num1) + int(num2))
    elif mark == "-":
        return str(int(num1) - int(num2))

class Problem:
    def __init__(self, num1, mark, num2):
        self.num1 = num1
        self.mark = mark
        self.num2 = num2
        self.result = getResult(self.num1, self.mark, self.num2)
    
    def linePrint(self):
        if self.result != None:
            longestChar = max([self.num1, self.num2, self.result], key=len)
            self.line1 = "  " + " "*(len(longestChar)-len(self.num1)) + self.num1
            self.line2 = self.mark + " " + " "*(len(longestChar)-len(self.num2)) + self.num2
            self.line3 = "-"*len(longestChar) + "--"
            self.line4 = "  " + " "*(len(longestChar)-len(str(self.result))) + self.result
        else:   
            self.result = "Error: Operator must be '+' or '-."

def arithmetic_arranger(Arg, arg2=False):
    lineList = []
    resultsList = []
    arg = flatten_list(Arg)

    if len(arg) <= 5:
        for problem in arg:
            splitList = problem.split(" ")
            if len(splitList[0]) <= 4 and len(splitList[2]) <= 4:
                obj1 = Problem(splitList[0], splitList[1], splitList[2])
                obj1.linePrint()
                resultsList.append(obj1)
            else:
                return 'Error: Numbers cannot be more than four digits.'
    else:
        return 'Error: Too many problems.'
    
    for x in range(1, len(resultsList)):
        if resultsList[x].result == "Error: Operator must be '+' or '-'.":
            return resultsList[x].result
    
    for x in range(0, len(resultsList)):
        lineList.append(resultsList[x].line1 + "    ")
    for x in range(0, len(resultsList)):
        lineList.append(resultsList[x].line2 + "    ")
    for x in range(0, len(resultsList)):
        lineList.append(resultsList[x].line3 + "    ")

    lineList.insert(len(arg), "\n")
    lineList.insert(len(arg)*2+1, "\n")
    lineList.insert(len(arg)*3+2, "\n")

    if arg2:
        for x in range(len(resultsList)):
            lineList.append(resultsList[x].line4 + "    ")
    lineList.insert(0, "")
    
    return lineList
print(*arithmetic_arranger([['3801 - 2', '123 + 49']], True))