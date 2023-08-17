import sqlite3

connection = sqlite3.connect("YeniDatabase.db")   #sqlite kütüphanesi ile "kutuphane" isminde bir veritabanı olusturuyorum ve ona bağlanıyorum
file_pointer = connection.cursor()    #eğer böyle bir veritabanı yoksa oluşturulur ve bağlanılır, eğer böyle bir veritabanı varsa bağlanılır


def tablo_olustur():
    file_pointer.execute("CREATE TABLE IF NOT EXISTS Personel(Isim TEXT,Soyisim TEXT,Memleket TEXT)")
    connection.commit()
    
def veri_ekle():
    file_pointer.execute("""INSERT INTO Personel VALUES('Eser','ILELI','Trabzon')""")
    file_pointer.execute("""INSERT INTO  Personel VALUES('Dursun','Korkmaz','Bursa')""")
    file_pointer.execute("""INSERT INTO Personel VALUES('Ahmet','Mithat','Diyarbakir')""")
    file_pointer.execute("""INSERT INTO Personel VALUES('Ayse','Bilgili','Van')""")
    file_pointer.execute("""INSERT INTO Personel VALUES('Firuze','Ceylan','Van')""")
    connection.commit()

def veri_ekle_manuel():
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    memleket = input("Memleket: ")
    file_pointer.execute("INSERT INTO Personel VALUES(?,?,?)",(isim,soyisim,memleket))
    connection.commit()

def veri_sec():
    file_pointer.execute("""SELECT Isim,Soyisim FROM Personel""")
    data = file_pointer.fetchall() #fetchall fonksiyonu, pointerın gösterdiği listenin hepsini demet haline getirir. 
    for i in data:
        print(i)

def veri_sec_2():
    file_pointer.execute("""SELECT* FROM Personel""")
    data2 = file_pointer.fetchall()
    for a in data2:
        print(a)

def veri_sec_3(memleket):
    file_pointer.execute("""SELECT* FROM Personel where Memleket = ?""",(memleket,))
    data3 = file_pointer.fetchall()
    for b in data3:
        print(b)

def veri_guncelle(memleket):
    file_pointer.execute("""UPDATE Personel SET Memleket =? where Memleket=? """,("Van",memleket)) #memleketi, parametre olarak girilen değerlerin tüm özellikleri silinir
    connection.commit()

def veri_sil(isim):
    file_pointer.execute("""DELETE FROM Personel where Isim = ?""",(isim,))   #ismi, parametre olarak girilen değerin tüm özellikleri silinir
    connection.commit()

        

tablo_olustur()
#veri_ekle()
#veri_ekle_manuel()
#veri_sec()
#veri_sec_2()
#veri_sec_3("Van")
#veri_sil("Eser") # İsmi eser olan tüm verileri Personel database inden siler.
veri_guncelle("Balikesir") #memleketi Balikesir olan herkesin memleketi Van olarak güncellendi.
connection.close()








