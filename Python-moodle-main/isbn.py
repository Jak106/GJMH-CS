import re
import urllib.request as r
import json

from requests.api import request

isbnNum = str(input("Input ISBN number: "))

isbnList = re.findall("\d", isbnNum)
isbnRes = ''.join(isbnList)

api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

resp = r.urlopen(api + isbnRes)
bookData = json.load(resp)
volumeInfo = bookData["items"][0]["volumeInfo"]
print(f"Title: {volumeInfo['title']}\nAuthor: {volumeInfo['authors']}\nPage Count: {volumeInfo['pageCount']}")