print(bin(4))   
print(hex(35))
#sum() fonksiyonunda degiskenlerin liste veya demet içerisinde gönderilmesi gerekir. sum(3,4) yerine (sum[3,4]) yazılmalıdır!
print(sum((3,4)))
print(max(34,5,1,-5))
print(min(34,5,1,-5))
print("phyTon".upper())
print("PhytTOn".lower())
print("Merhabalar Ben Berk".replace(" ",""))
print("Phyton".startswith("Phy"))    #startswith ve endswith fonksiyonları string karakter alır ve true false döndürür
print("Ulak".endswith("ka"))
print("ada kapisi".count("si"))  #count fonksiyonu string içerisindeki ifadeyi arar ve kaç tane olduğunu integer döner! parametre alır
print("adakapisi".count("i",6))  #6.indexten itibaren stringte arıyor ve aynısını bulduğu kadar döndürüyor
print("peder".find("a")) #find() fonksiyonu string parametre alıyor ve aranan elemanın kaçıncı indexte olduğunu integer olarak dönüyor
                         #eğer string içerisinde ifadeyi bulamazsa -1 döner
print("Fatif".find("a"))

#######################KÜMELER##########################################

X = {1,2,3,4,5}   #BİR KÜMEDİR, liste ve demette ki gibi içinde for ile dönebilirsin
X.add(6)
print(X)
X.add(3)   # eğer aynı eleman varsa kümeye eklenmiyor!
print(X)
X.add("eser")
print(X)
X.discard("eser")
print(X)
kume1= {1,2,45,64,23}
kume2 ={3,7,11,45,2,1}
kume1.intersection_update(kume2)
print(kume1)




