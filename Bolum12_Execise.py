class Dosya():

    def __init__(self,dosya_ismi):

        with open(dosya_ismi,"r",encoding = "utf-8") as file:

            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()

            self.sade_kelimeler = list()

            for kelime in kelimeler:
                kelime = kelime.strip()
                kelime = kelime.strip(".")
                kelime = kelime.strip("\n")

                self.sade_kelimeler.append(kelime)
    def kelime_bul(self,aranan):

        konumlar = list()
        say = 1
        for kelime in self.sade_kelimeler:
            if (kelime == aranan ):
                konumlar.append(say)

            say += 1

        if (len(konumlar) == 0):
            print("Dosyada böyle bir kelime bulunmuyor...")
        else:

            print("{} kelimesi dosyada şuralarda geçiyor. \n{}".format(aranan,konumlar))



    def kelime_histogrami(self):

        kelime_frekansi = dict()
        kelime_kümesi = set()

        for kelime in self.sade_kelimeler:
            kelime_kümesi.add(kelime)
            if (kelime in kelime_frekansi):
                kelime_frekansi[kelime] += 1
            else:
                kelime_frekansi[kelime] = 1
        print("Kelimelerin Frekansi........................")
        for i, j in kelime_frekansi.items():
            print("{} kelimesi metinde {} defa geçiyor.".format(i, j))

        print("Tüm Kelimeler")
        for i in kelime_kümesi:
            print(i)
            print("*************************************")


dosya =  Dosya("metin.txt")
print("""****************

Dosya İşlemleri 

1. Tüm kelime frekansini öğren

2. Kelime Ara

Çikmak için 'q' ya basin.

""")
while True:
    işlem = input("İşlem:")

    if (işlem == "q"):
        print("Programdan Çikiliyor....")
        break
    elif (işlem == "1"):
        dosya.kelime_histogrami()
    elif (işlem == "2"):
        kelime = input("Hangi kelimeyi ariyorsunuz ?")
        dosya.kelime_bul(kelime)
    else:
        print("Geçersiz İşlem...")

