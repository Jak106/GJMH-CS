import random

n, good, bad = 0, 0, 0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            return False
    return True

average = 0
i = 0
while i < 10:
    while n < 100000:
        print(n)
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        if is_prime(num1 + num2):
            good += 1
        else:
            bad += 1
        n += 1
    average += (good/100000)*100
    i += 1
    
print(f"Good: {good}, Bad: {bad}")
print(f"Pravdepodobnost je {round((good/100000)*100, 10)} %")
  
with open("tries.txt", "a") as f:
    f.write(f"\nGood: {good}, Bad: {bad}, Pravdepodobnost je {round((good/1000)*100, 10)} %. Celkova = {average/10} %")
    