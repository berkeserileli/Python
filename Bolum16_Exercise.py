import requests
import json
#from bs4 import BeautifulSoup
#from urllib.request import Request,urlopen

url = "http://data.fixer.io/api/latest?access_key=f2f55b0404a5d451d71342fbfa0dd333&format=1"
#request = Request(url,headers = {"User-Agent":"Mozilla/5.0"})
#content = urlopen(request).read()
#soup = BeautifulSoup(content,"html.parser")

response = requests.get(url)
json_verisi = response.json()
print(json_verisi)
#icerik = response.content
#print(response)
#kaynak = BeautifulSoup(json_verisi,"html.parser")

for key,value in json_verisi.items():  #Json verisi, sözlük yapısına sahip olduğundan;
    print(key,value)