import os

print(dir(os))
dosyalar = os.listdir()
for dosya in dosyalar:
    if dosya.endswith(".py"):
        print(dosya)

print("-------------------")
print(os.listdir())
print(os.listdir("/KOdlama denemelerim"))
print("--------------")
#veya
for i in os.listdir():
    print(i)
print("------------------------")
print(os.getcwd())  #getcwd() dosyamın bulunduğu konumu gösterir.
print(os.chdir("C:/Program Files/Common Files/DESIGNER")) #linuxtaki cd komutu gibi davranıyor.
print(os.getcwd()) #bulunduğun konumu gösterdim, değişti.
print(os.listdir()) #şimdi ise içinde bulunduğum dosyaya gittim.
#os.mkdir("C:/PythonOsModülü/deneme1") # belirlenen yerde bir klasör oluşturuldu
#os.rmdir("C:/PythonOsModülü/deneme1") #belirlenen yerdeki klasörü siliyor
dosyalar2 = os.listdir("C:")
os.chdir("C:/")
print(os.getcwd())
os.listdir()
print(os.walk("C:\Riot Games\Riot Client")) #os modulünün walk() fonksiyonu, dosya dizinindeki tüm dosyaları döner fakat bir generator olduğu için döngü içerisinde döndürebilirsin
for i in os.walk("C:\Riot Games\Riot Client"):
    for k in i:
        print(i)
