def gcd(a,b):
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b
        
print(gcd(89, 9))
print(gcd(100, 30))
