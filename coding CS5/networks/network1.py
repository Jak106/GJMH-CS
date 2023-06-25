#gets html from site
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://zubersafety.sk')
for line in fhand:
    print(line.decode().strip())