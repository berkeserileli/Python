
#print("Oyuncu kaydetme Programi\n")
#ad = input("Oyuncu adini giriniz: ")
#soyad = input("Oyuncu soyadi giriniz: ")
#list1  = [ad,soyad]
#print("Bilgiler basariyla kaydedildi!\n")
#print("Oyuncu adi:{} \n Oyuncu soyadi:{}\n".format(list1[0],list1[1]))

import math
#Ikinci dereceden denklem köklerini bulma
print("Ikinci dereceden denklemin köklerini bulma programi")
a = int(input("Lutfen ilk baskatsayiyi gir: "))
b= int(input("Ikinci katsayi: "))
c= int(input("Ucuncu katsayi: "))

delta = (b*2)-(4*a*c)
kok1 = (-b)+(pow(delta,(1/2)))/(2*a)
kok2 = ((-b)-(math.sqrt(delta)))/(2*a)
print("Ilk deger: ",kok1)
print("Ikinci deger: ",kok2)





