def getbit(value, n):
    res = value >> n-1
    mask = 0x01
    return int(res & mask)

assert getbit(0xCA, 1) == 0
assert getbit(0xCA, 2) == 1
assert getbit(0xCA, 3) == 0
assert getbit(0xCA, 4) == 1
assert getbit(0xCA, 5) == 0
assert getbit(0xCA, 6) == 0
assert getbit(0xCA, 7) == 1
assert getbit(0xCA, 8) == 1

def setbit(value, n):
    mask = 0b00000001
    mask = mask << n-1
    return value | mask

assert setbit(0xCA, 1) == 0xCB
assert setbit(0xCA, 2) == 0xCA
assert setbit(0xCA, 3) == 0xCE
assert setbit(0xCA, 4) == 0xCA
assert setbit(0xCA, 5) == 0xDA
assert setbit(0xCA, 6) == 0xEA
assert setbit(0xCA, 7) == 0xCA
assert setbit(0xCA, 8) == 0xCA

def clearbit(value, n):
    mask = 0b00000001
    mask = ~(mask << n-1)
    return value & mask

assert clearbit(0xCA, 1) == 0xCA
assert clearbit(0xCA, 2) == 0xC8
assert clearbit(0xCA, 3) == 0xCA
assert clearbit(0xCA, 4) == 0xC2
assert clearbit(0xCA, 5) == 0xCA
assert clearbit(0xCA, 6) == 0xCA
assert clearbit(0xCA, 7) == 0x8A
assert clearbit(0xCA, 8) == 0x4A

def togglebit(value, n):
    mask = 0b00000001
    mask = mask << n-1
    return value ^ mask

assert togglebit(0xCA, 1) == 0xCB   
assert togglebit(0xCA, 2) == 0xC8 
assert togglebit(0xCA, 3) == 0xCE 
assert togglebit(0xCA, 4) == 0xC2 
assert togglebit(0xCA, 5) == 0xDA 
assert togglebit(0xCA, 6) == 0xEA
assert togglebit(0xCA, 7) == 0x8A
assert togglebit(0xCA, 8) == 0x4A

# def countsetbits(value):
#     return bin(value).count("1")

def countsetbits(val):
    #subtrahand, minuend
    count = 0
    while val != 0:
        subtrahand = val -1
        val = val & subtrahand
        count += 1
    return count

assert countsetbits(0x7C) == 5
assert countsetbits(113) == 4
assert countsetbits(0x713DA4A) == 14

def hammingdistance(val1, val2):
    return countsetbits(val1 ^ val2)

assert hammingdistance(0xDF, 0xAE) == 4
assert hammingdistance(0xFF, 0xDD) == 2
assert hammingdistance(0xFF, 255) == 0

# assert paritybit(0x2E) == 0
# assert paritybit(0x2E, False) == 1
# assert paritybit(0x61) == 1
# assert paritybit(0x61, False) == 0
# assert paritybit(0x5200) == 1
# assert paritybit(0x5200, False) == 0

# assert getbyte(0xFFCCDBE5, 1) == 0xE5
# assert getbyte(0xFFCCDBE5, 2) == 0xDB
# assert getbyte(0xFFCCDBE5, 3) == 0xCC
# assert getbyte(0xFFCCDBE5, 4) == 0xFF
