def find_primes(start, end):
    if start > end:
        return "Invalid input, start is bigger then end"
    primes = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, int(num**(0.5))+1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

def natural_factors(n):
    i = 1
    while i <= n:
        if (n % i==0):
            print(i, end=" ")
        i += 1

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            return False
    return True

num = input("What is your number? ")

while "." in num or int(num) <= 0 or is_prime(int(num)):
    print("Not valid")
    num = input("What is your new number? ")
else:
    print("All natural factors are: ")
    natural_factors(int(num))

m = input("\nWhat is your m number? ")
n = input("What is your n number? ")

while "." in m or int(m) <= 0:
    print("Not valid")
    num = input("What is your new m number? ")

while "." in n or int(n) <= 0:
    print("Not valid")
    num = input("What is your new n number? ")
    
print(find_primes(int(m), int(n)))

with open("primes.txt", "w") as f:
    for num in find_primes(int(m), int(n)):
        f.write(str(num) + "\n")
    print("Numbers saved into file")
