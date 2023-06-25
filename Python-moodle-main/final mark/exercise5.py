breath = 10
diveNums = [-3, -6, -2, -6, -2]

for num in diveNums:
    if num < 0:
        breath -= 2
    elif num >= 0:
        breath += 4
    
    if breath > 10:
        breath = 10
    elif breath == 0:
        print("Our hero passed away ...")
        break
else:
    print("Our hero survives!")