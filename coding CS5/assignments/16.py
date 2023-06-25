with open("image.txt", "r", encoding="utf-8") as f:
    content = f.read().split("\n")

def process_line(line:list):
    pixels = line.split(" ")
    tryes = 1
    res = ""
    for pixel in pixels:
        if tryes % 2: 
            res += "0" * int(pixel)
        else:
            res += "1" * int(pixel)
        tryes += 1
    
    return res

resolution = content[0].split(" ")
content.pop(0)
image = []

with open("image_decompression_output.txt", "a", encoding="utf-8") as f:
    f.write(f"{resolution[0]} {resolution[1]}\n")
    for imageLine in content:
        f.write(process_line(imageLine) + "\n")