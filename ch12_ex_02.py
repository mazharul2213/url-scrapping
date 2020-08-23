#URL Scrapping program
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

lst = list()

#handling ssl error certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#sending request for data
url = input("Enter URL: ")
if len(url) < 1:
    url = " http://py4e-data.dr-chuck.net/known_by_Sohera.html"

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input("Enter count: "))
position = int(input("Enter position: ")) - 1

while count >= 0 :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup("a")
    print("Retriving: ", url)
    url = tags[position].get("href", None)
    count = count - 1