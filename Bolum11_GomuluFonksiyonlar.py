# map fonksiyonu 2 parametre alır, ilki tek parametreli fonksiyon ismi, diğer parametre ise liste ismidir
def ikiylecarp(a):
    return a*2 

listem1 = [1,2,3]
sonuc = map(ikiylecarp,listem1)
print(list(sonuc))
print(list(map(lambda x : x**2,(5,6,7,8)))) #map fonksiyonu lambda parametresini de bastırır.

liste1 = [3,4,5,6,9]
liste2 = [2,9,8]
liste3 = [1,5,5,5]
print(list(map(lambda x,y : x*y, liste1,liste2))) #listenin en küçük elemanının gittigi yere kadar islem gider.
print(list(map(lambda x,y,z : x*y*z , liste1 ,liste2,liste3))) #aynı sekilde listelerin aynı indekslerindeki sayıları carpar.

#reduce fonksiyonu, bu da 2 parametre alıyor ilki fonksiyon, diğer parametre ise liste
#burda önemli olan, işlemlerin bastan itibaren 2 şerli olarak yapılması ve 3. indekse etki etmesidir.
from functools import reduce as r
def topla(a,b):
    return a+b

print(r(topla,[1,2,3,4,5]))

#Filter fonksiyonu, bu da 2 parametre alıyor ilk fonksiyon 2.si liste. fakat burda fonksiyon true false dönmeli!

def asal(x):
    i = 2
    if (x ==1):
        i+=1
        return False
    elif(x ==2):
        i+=1
        return True
    else:
        while(i<x):
            if(x%i==0):
                return False
            i +=1
        return True

print(list(filter(asal,range(1,10))))

#zip fonksiyonu, bu 2 tane liste alıyor ve 2 listeyi demetleyip tek liste haline dönüştürüyor aslında yaptığı şu:

list1 = [3,9,7,14,15]
list2 = [3,22,11,44,54,35,67,89]
i = 0
sonuc = []
while(i<len(list1) and i<len(list2)):
    sonuc.append((list1[i],list2[i]))
    i += 1 

print(sonuc)
print(list(zip(list1,list2)))

#any() fonksiyonunda listedeki herhangi bir değer true ise tüm liste true , herhangi bir değer false ise tüm lisete false döner
#all() fonksiyonunda ise her değerin true veya her değerin fals olması lazım, aksi taktirde zıttını döner

liste1 = [False,False,True,True]
print(all(liste1))
print(any(liste1))