
file = open("PhytonDosyam1.txt","w")
file.write("BerkEserILELI\n")
file.write("201201063")
file.close()
file = open("PhytonDosyam1.txt","w")
file.write("ULAK Haberlesme\n")
file.close()
file = open("PhytonDosyam1.txt","a",encoding = "utf-8")
file.write("BerkEserİLELİ\n")
file.close()
file = open("PhytonDosyam1.txt","r",encoding = "utf-8")
icerik = file.read()
print("Dosyanin icerigi:\n",icerik)
file.close()
file = open("PhytonDosyam1.txt","a",encoding = "utf-8")
file.write("Mustafa Demirkoparan\n")
file.close()
file = open("PhytonDosyam1.txt","r",encoding = "utf-8")
icerik2 = file.read()
print("Dosyanin icerigi : \n",icerik2)
file.close()

file = open("PhytonDosyam1.txt","r",encoding = "utf-8")
print(file.readline())      #readline fonksiyonu dosyadaki her bir satırı tek tek okur, ve okunan satırları kaydeder.
print(file.readline())      #okunacak satırlar bitince boş döner
print(file.readline())
file.readlines()
file.close() 

with open("D:\KOdlama denemelerim\PhytonDosyam1.txt","r",encoding = "utf-8") as file:  #bu şekilde dosyayı açarsan dosya işi bitincekendi kapanır .close koymana gerek yok!
    for i in file:
        file.readline()
