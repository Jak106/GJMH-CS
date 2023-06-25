import re, zipfile

with zipfile.ZipFile("channel.zip", "r") as f:
    content = f.extractall("channelUnziped")
    
newFile = "channelUnziped/29.txt"

working = True

while working:
    try:
        with open(newFile, 'r') as f:
            for line in f:
                num = re.findall(r'[0-9]+', line)[0]
                newFile = f'channelUnziped/{num}.txt'
                print(newFile.comment)
    except:
        working = False

print("------------------------------------------------")
with open(newFile, 'r') as f:
    for line in f:
        print(line)
