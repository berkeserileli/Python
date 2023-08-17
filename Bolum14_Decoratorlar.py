
#decoratorlar, fonksiyonların çalışma sürelerini ölçmek kontrol etmek, ve fonksiyon içinde herhangi bir exception varsa bunları 
#bunları göstermek amacıyla kullanılır. Temel fonksiyon, fonksiyon parametresi alır ve içerisideki fonksiyonu return eder.
def func(name,*args):
    print("Name: ",name)
    for i in args:
        print(i)


func("name",123,1231,42,43,7,8,9)

bastir = func    # fonksiyonların ismini degistirebiliyoruz
bastir("eser",123,12,32,54,4)
del bastir    #bastiri silince eşitlenen fonksiyon da silinmiyor!
func("kafir",323,4,5)

def func1():
    def func2():
        print("func2 bastirildi")
    func2()
    print("func1 cagirildi")

func1()
#print(func2()) boyle de gorulmez.
#func2() doğrudan görülmez!


def func4(*args):
    def carpim(args):
        k = 1
        for i in args:
            k = k*i
        return k
    print(carpim(args))

func4(3,4,5,3)
####################################################### fonksiyon içinde fonksi.yon tanımlanabiliyor ve aldıgı argümana göre recurse edebiliyor
def islem(islem_adi):
    def carpma(*args):
        sbt = 1
        for i in args:
            sbt *=i
        return sbt
    
    def toplama(*args):
        sbt = 0
        for i in args:
            sbt +=i
        return sbt

    if islem_adi == "toplama": 
        return toplama
    elif islem_adi == "carpma":
        return carpma
    else:
        print("gecersiz islem!")

k = islem("toplama")
print(k(1,2,3,4,5,10))

def ilkfonksiyon():
    print("bu ilk olan")
    def ikincifonk():
        return "bu da 2. fonksiyon"
    print(ikincifonk())
    #print(ikincifonk)   olsa idi, ikinci fonksiyonun adcresi bastırılcaktı!
ilkfonksiyon()
        

import time

def zamanAyir(func):
    def wrapper(sayilar):
        baslangic = time.process_time()
        sonuc = func(sayilar)
        bitis = time.process_time()
        print(func.__name__ + " " + str(baslangic) + "-" + str(bitis)+ "saniye surdu")
        return sonuc
    return wrapper

@zamanAyir
def kupleriHesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i**3)
    return sonuc

@zamanAyir
def kareleriHesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i**2)
    return sonuc

kareleriHesapla(range(1,100,1))    
kupleriHesapla(range(1,100,1))


"""def fonk(fonk1,fonk2):
    def toplamaYap(a,b):
        sonucum = fonk1(a) + fonk2(b)
        return sonucum
    return toplamaYap
@fonk
def fonk1(a):
    return a
@fonk
def fonk2(b):
    return b
""" # bu ifade hatalı, decoratorlar sadece tek parametre alır!

def decorator(fonk):
    def wrapper():
        print("fonksiyon oncesi islemler")
        fonk()
        print("fonksiyon sonrasi islemler")
    return wrapper

@decorator
def fonk():
    print("fonksiyon calisti")

fonk()
#fonksiyon2 = decorator(fonk)
#fonksiyon2()                 #bu yöntemle fonksiyon2 wrapper fonksiyonu gibi çalışır!


#fonk() = decorator(fonk)    bu kisi ayni ifadeyi gösteriyor



