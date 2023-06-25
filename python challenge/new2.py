import re
import urllib.request
with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8880') as response:
   html = response.read()

newArg = re.findall(r'[0-9]{4}' , str(html))

working = True

while working:
    try:
        with urllib.request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={newArg[0]}') as response:
            html = response.read()
            newArg = re.findall(r'[0-9]+' , str(html))
            print(f"{html}")
    except:
        working = False
        print(newArg)