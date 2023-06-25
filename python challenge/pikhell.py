import urllib.request, pickle

with urllib.request.urlopen(f'http://www.pythonchallenge.com/pc/def/banner.p') as response:
    html = pickle.load(response)
    print(f"{html}")

#with open('filename', 'rb') as f:
