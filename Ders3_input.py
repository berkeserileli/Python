#a = input("Lutfen bir sayi gir: ") #string deger döndürür!
#print(a)
#print(a*3) # burda a nın değeri String olarak dönüyor! o yüden çarılan sayı kadar yazar!
#print(type(a))
#b = int(input("Diger sayiyi giriniz: "))
#print(b*3)
#print("Degeriniz: ",b)

a = int(input("Lutfen ilk sayiyi giriniz: "))
b= int(input("Lutfen ikinci sayiyi giriniz: "))
print("Sonucunuz: ",a+b)

sayi1 = input("Sayi1: ")
sayi2 = input("Sayi2: ")

try:
 Sayi1 = int(sayi1)
 Sayi2 = int(sayi2)
 print(Sayi1,"/",Sayi2,"=",Sayi1/Sayi2)
except ValueError:
    print("Bu durum gecerli degil!")


