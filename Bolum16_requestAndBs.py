import requests                     #verisini almak istediğimiz websiteye istek atmamıza yarayacak olan kütüphanedir. 
from bs4  import BeautifulSoup       #BeautifulSoup modülü HTML veya XML dosyalarından veri çekmemizi sağlayan kütpühanedir.
                                    #BU KODDA HER SİTENİN BİLGİSİNİ ALAMAZSINIZ! Çoğu site, botlara karşı önlem alabilmek için,
                                    #response[403] yani erişim engeli hatasını gönderir.BuNUN YERİNE "from urllib.request import Request,urlopen" kütüphanesi ve fonksiyonlarını kullan
#print(dir(BeautifulSoup))
#print(dir(requests))    

url2 =  "https://www.ulakhaberlesme.com.tr/" # Site linki

response2 =  requests.get(url2) # Web sayfamızı çekiyoruz.
#print(response)   #siteye istek attığımızda response[200] ifadesi dönüyorsa siteye bağlanabiliyoruzdur
html_icerigi2 = response2.content  # Web sayfamızın içeriğini alıyoruz.
#print(html_icerigi)       kodu ile değişkenin içerisindeki site bilgilerini karmaşık bir şekilde görebilirsin
soup2 =  BeautifulSoup(html_icerigi2,"html.parser") # Web sayfasını daha düzgün bir görünümde görmemizi sağlar
#print(soup) komutu ile sayfanın komutları alt alta gelir 
print(soup2.prettify()) # Daha güzel bir görüntü için BeautifulSoup kütüphanesindeki prettify() fonksiyonunu kullanıyoruz. 
#print("---------------------------------------------------------------")
#for i in soup2.find_all("div",{"class":"nav-item"}): # "div" etiketine sahip, class'ı nav-item olan verileri çekmemizi sağlar 
    #print(i)
