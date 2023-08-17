import sqlite3
import time

class Sarkilar():
        def __init__(self,sarki_ismi,sanatci,album,produksiyon,sarki_suresi):
            self.sarki_ismi = sarki_ismi
            self.sanatci = sanatci
            self.album = album
            self.produksiyon = produksiyon
            self.sarki_suresi = sarki_suresi

        def __str__(self):
                return "Sarki Ismi: {}\nSanatci: {}\nAlbum: {}\nProduksiyon: {}\nSarki Suresi: {}".format(self.sarki_ismi,self.sanatci,self.album,self.produksiyon,self.sarki_suresi)    
    
        def baglan(self):
                self.connection = sqlite3.connect("Sarkilarim.db")
                self.pointer = self.connection.cursor()
                self.pointer.execute("""CREATE TABLE IF NOT EXISTS Sarkilar("Sarki" TEXT,Sanatci TEXT,Album TEXT,Produksiyon TEXT,"Sarki Suresi" INT)""")
                self.connection.commit()

        def baglantiyiKes(self):
                self.connection.close()

        def sarki_ekle(self):
                self.sarki_ismi = input("Sarki Ismi: ")
                self.sanatci = input("Sanatci: ")
                self.album = input("Album: ")
                self.produksiyon = input("Produksiyon: ")
                self.sarki_suresi = input("Sarki suresi: ")
                self.pointer.execute("""INSERT INTO Sarkilar VALUES(?,?,?,?,?)""",(self.sarki_ismi,self.sanatci,self.album,self.produksiyon,self.sarki_suresi))
                print("Sarki basariyla eklendi!")
                time.sleep(1)
                self.connection.commit()

        def sarki_sil(self,sarki_ismi):
            self.pointer.execute("""DELETE FROM Sarkilar WHERE Sarki =?""",(sarki_ismi,))
            print("Sarki basariyla silindi!")
            self.connection.commit()    
    
        def sarkilari_goster(self):
            self.pointer.execute("SELECT * FROM Sarkilar")
            self.sarkilarim = self.pointer.fetchall()
            for i in self.sarkilarim:
                print(i)
    
        def sarkilari_guncelle(self,sarki_ismi):
            yeni_sarki_ismi = input("Yeni Sarki: ")
            self.pointer.execute("""UPDATE Sarkilar SET Sarki = ? WHERE Sarki = ?""",(yeni_sarki_ismi,sarki_ismi))
            self.connection.commit()


sarkim1 = Sarkilar("Vur","Uzi","Favela","GNG Produksiyon",3.18)
sarkim1.baglan()
#sarkim1.sarki_ekle()
#print(sarkim1)
#sarkim1.sarkilari_guncelle("Sarki")
#sarkim1.sarkilari_goster()
sarkim1.baglantiyiKes()

