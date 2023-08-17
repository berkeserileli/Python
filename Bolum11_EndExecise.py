
#Ucgen
"""def alanHesapla(tek_boyutlu_hali):
    return tek_boyutlu_hali[0]*tek_boyutlu_hali[1]

listem1 = [(3,4),(10,3),(5,6),(1,9)]
tek_boyutlu_hali = []
for i in listem1:
    tek_boyutlu_hali.extend(i)           #burda extend fonksiyonu listem1 i tek boyutlu dizi haline döndürür çünkü her elemani
                                         #birbirinin arkasina ekler
print(list(map(alanHesapla,listem1)))
"""
#soru2 Ucgen kontrolü
"""def ucgenKontrol(listem2):
    if(abs(listem2[0]-listem2[2]) < listem2[1]< (listem2[0] + listem2[2]) or abs(listem2[1]-listem2[2]) < listem2[0]< (listem2[1] + listem2[2] or abs(listem2[0]-listem2[1]) < listem2[2]< (listem2[0] + listem2[1]))):
        return True
    else:
        return False

listem2 = [(3,4,5),(6,8,10),(3,10,7)]
#for i in listem2:
filtered = list(filter(ucgenKontrol,listem2))
if filtered:
    print(filtered, "ucgen olusturur")
else:
    print("Ucgen olusturmaz!")
"""

#soru3 sayiçiftlerini aırıp toplama
"""from functools import reduce as re
def ciftleri_ayikla(listem3):
        if(listem3 % 2 == 0):
            return True
        else:
            return False

listem3 =  [1,2,3,4,5,6,7,8,9,10]
filtered = list(filter(ciftleri_ayikla,listem3))
print(filtered)

def ciftleri_topla(a,b):
     return a+b

sonuc = re(ciftleri_topla,filtered)
print(sonuc)
"""

#soru4
 
"""isimler = ["Kerim","Tarik","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yilmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
print(list(zip(isimler,soyisimler)))
"""