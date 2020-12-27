#install python library pyshorteners

import pyshorteners

url = input("Enter the URL you want to shorten: ")
shortner = pyshorteners.Shortener()
a = shortner.tinyurl.short(url)
print(a)