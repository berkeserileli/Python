def not_hesapla(satir):

    satir = satir[:-1]      #satırın sonundaki \n ifadesini kaldırır.

    liste = satir.split(",") #satırdaki her bir stringi virgülle böler ve liste elemanı haline getirir.

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------------> " + harf + "\n"

with open("dosya.txt","r",encoding= "utf-8") as filem:
    eklenecekler_listesi = []
    kalanlar_listesi = []
    gecenler_listesi = []
    for i in filem:
        sonuc = not_hesapla(i)
        eklenecekler_listesi.append(sonuc)
        if "FF" in sonuc or "FD" in sonuc:             
            kalanlar_listesi.append(sonuc)
        else:
            gecenler_listesi.append(sonuc)


with open("notlar.txt","w",encoding="utf-8") as filem:
        for i in eklenecekler_listesi:
            filem.write(i)
with open("kalanlar.txt","w",encoding = "utf-8") as filem:
        for i in kalanlar_listesi:
            filem.write(i)
with open("gecenler.txt","w",encoding = "utf-8") as filem:
        for i in gecenler_listesi:
             filem.write(i)







