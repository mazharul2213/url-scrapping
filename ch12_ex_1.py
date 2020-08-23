#URL Scrapping program
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

lst = list()
count = 0

#handling ssl error certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#sending request for datq
url = input("Enter - ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_643358.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#data scrapping
tags = soup('span')
for tag in tags:
    #print(tag.get('span class="comments"', None))
    #print(tag)
    #print("content:", tag.contents[0])
    data = tag.contents[0]
    num = lst.append(int(data))
    count = count + 1
print("Count ", count)
print("Sum ", sum(lst))
