import re

with open("image_input.txt", "r", encoding="utf-8") as f:
    image = f.read().split("\n")

width = len(image[0])
height = len(image)

def process_line(check):
    pixels = re.findall(r"0+|1+", check)
    if pixels[0][0] == "1":
        res = "0 "
    else:
        res = ""
    for pixel in pixels:
        res += str(len(pixel)) + " "
    return res + "\n"

with open("image_compression_output.txt", "a", encoding="utf-8") as f:
    f.write(f'{width} {height}\n')
    for line in image:
        f.write(process_line(line))
        
#Q1: For what kind of line is there going to be only one number in the output file?
#A: This will mark the line where only one of the possible numbers is going to be used.
#Q2: What kind of lines are going to have more than one number in the output file?
#A: Kind of lines where these are both numbers used
#Q3: What's the longest line possible going to look like?
#A: It will have 0 and 1 alternating
#Q4: What image (with the same amount of rows) is going to have the shortest output file?
#A: Where there is only one number used