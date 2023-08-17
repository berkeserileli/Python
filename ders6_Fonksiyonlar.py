def toplama(a,b,c):
    #print("Toplama islemi yapiyorum!")
    return a+b+c
c = toplama(10,20,30)
print(c) #c ifadesi print edildiğinde fonksiyonun içine de girilir!

def selamVer(isim):
    print("Selam",isim)
selamVer("Eser")

def selamla(isim = "Faruk"):
    print("Selam", isim)
selamla()
selamla("Ozgur")

def displayInfo(name = "BerkEser", ID = "201201063", years = 9,served= 0):
    print("Name: ",name, "ID ",ID, "Year:",years,"Served:",served)
displayInfo(served = 35)
displayInfo()

def numbers(*a):
    toplam  =0
    for i in a:
        toplam +=i
    print(toplam)
numbers(10,40,23,123,15)
#numbers("Kazim","Ayse","Fatma","Erdi")

##########################################################################################
global d
d = 3
def globalYap():
    #global d
    d = 6
    print(d)
d =5
def globalYap2():
    #global d
    d = 7
    print(d)
globalYap()
print(d)    #değeri global yapmak, fonksiyon dışında da etkili!!!!!
globalYap2()
###########################################################################################

def tersCevir(s):
    return s[::-1]
print(tersCevir("Eser"))

Ters = lambda b : b[::-1] #lambda fonksiyonu, içerisine koyulan ifadeye islem yapar!
print(Ters("Fatih"))

tekSayi = lambda tek:tek % 2 !=0
print(tekSayi(16))



