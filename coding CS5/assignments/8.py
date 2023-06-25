import random as r

visaCount = int(input("How many Visa Electron cards would you like to generate? "))
masterCount = int(input("How many Mastercard cards would you like to generate? "))

visaSequence = [4026, 417500, 4508, 4844, 4913, 4917]
masterSequence = [51, 52, 53, 54, 55]

lengthCount = {
    "visa": [16, 16],
    "mastercard": [16, 19]
}

cards = []

def luhn(numbers: list):
    count, add = 0, 0
    for numPos in range(0, len(numbers)):
        print("------------------------------------------------------")
        print(f"num is {numbers[numPos]}, position is {numPos+1}")
        num = numbers[numPos]
        if numPos % 2 == 0:
            print(f"Multiplying")
            if num * 2 > 9:
                print(f"multiplying, more then 9 => {num*2}")
                for n in str(num*2):
                    count += int(n)
            else:
                print(f"multiplying by 2, less then 9 => {num*2}")
                count += num * 2
        else:
            count += num            
    while (count+add) % 10 != 0:
        add += 1
    numbers.append(add)
    return numbers
    
def generate_cards(manu: list, count: int, length: int):
    n = 0
    res = []
    while n < count:
        nums = [int(n) for n in str(r.choice(manu))]
        while len(nums) < length:
            nums.append(r.randint(0, 9))
        cardNum = ""
        for x in luhn(nums):
            cardNum += str(x)
        res.append(cardNum)
        n += 1
        
    if manu == visaSequence:
        with open("VISA.txt", "w") as f:
            for num in res:
                f.write(num + "\n")
    else:
        with open("Mastercard.txt", "w") as f:
            for num in res:
                f.write(num + "\n")
                
generate_cards(visaSequence, visaCount, r.randint(lengthCount["visa"][0], lengthCount["visa"][1]))
generate_cards(masterSequence, masterCount, r.randint(lengthCount["mastercard"][0], lengthCount["mastercard"][1]))
