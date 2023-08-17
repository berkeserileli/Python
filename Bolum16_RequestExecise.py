import requests
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
#sitem1 = requests.get("https://www.imdb.com/chart/top")
#print(sitem1)
url = "https://www.imdb.com/chart/top"
req = Request(url,headers = {"User-Agent":"Mozilla/5.0"})
icerik = urlopen(req).read()

soup = BeautifulSoup(icerik, "html.parser")

for i in soup.find_all("div",{"class":"ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-14dd939d-7 fjdYTb cli-title"}):
    print(i.text)   #almak istedigim filmlerin ismini yazdırır
    
film_ismi = soup.find_all("div",{"class":"ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-14dd939d-7 fjdYTb cli-title"})
rating = soup.find_all("span",{"class":"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"})

for isim,rating in zip(film_ismi,rating):
    print(isim.text," ",rating.text)
   