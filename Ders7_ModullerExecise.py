import random
import time
rastgele = random.randint(1,10)
tahmin_hakki = 10
while True:
    tahmin = int(input("Lutfen tahmin ettiginiz sayiyi giriniz"))
    if(tahmin<rastgele):
        print("Kontrol ediliyor...")
        time.sleep(1)
        print("Lutfen daha buyuk bir sayi giriniz!: ")
        tahmin_hakki -=1
        if(tahmin_hakki == 0):
           print("Tahmin hakkiniz bitmistir!")
           break
        else:
            continue
    elif(tahmin>rastgele):
        print("Kontrol ediliyor...")
        time.sleep(1)
        print("Lutfen daha kucuk br deger giriniz!")
        tahmin_hakki -=1
        if(tahmin_hakki ==0):
            print("Tahmin hakkiniz bitmistir!")
            break
        else:
            continue
    else:
        print("Kontrol ediliyor...")
        time.sleep(1)
        print("Tebrikler sayiyi dogru tahmin ettiniz! : ",tahmin)
        break