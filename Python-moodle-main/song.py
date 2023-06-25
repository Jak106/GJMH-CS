song = [
    ["first", "A partridge in a pear tree"],
    ["second", "Two turtle-doves"],
    ["third", "Three French hens"],
    ["fourth", "Four calling birds"],
    ["fifth", "Five golden rings (five golden rings)"],
    ["sixth", "Six geese a laying"],
    ["seventh", "Seven swans a swimming"],
    ["eight", "Eight maids a milking"],
    ["ninth", "Nine ladies dancing"],
    ["tenth", "Ten lords a-leaping"],
    ["eleventh", "I sent 11 pipers piping"],
    ["twelfth", "12 drummers drumming"]
]

def showVerse(numArg):
    print(f'On the {song[numArg-1][0]} day of Christmas my true love sent to me')
    if numArg > 1:
        for i in range (numArg-1, -1, -1):
            if i == 0:
                print("And a partridge in a pear tree")
            else:
                print(song[i][1])
    else:
        print(song[0][1])

num = int(input("What verse do you want to show: "))

showVerse(num)