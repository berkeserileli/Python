a = True
print(type(a))
a = bool(15) #bool -1 yazsan da true döner. Sadece 0 da false dönüyor
print(a)
print("Mehmet"=="Murat")
print("Zula"<"Araba") #Z harfi A dan daha sonra olduğundan false döner
print((1<2) and ("Murat"=="Murat") )
print((1>5)and("Eser"=="Eser"))    #sınırsız and ekleyebiliriz yan yana
print(not 2==2)
print((1>0) or ("Eser"=="Fatih"))

#k = 2
#if (k==2):
     #print("Evet,deger esit")
#print("Bloktan cikis")
#l = int(input("Yasinizi giriniz: "))
#if(l<18):
    #print("Gece kulubune giremezsiniz!")
#else:
     #print("Girdiniz!")

islem = input("Lutfen yapilacak islemi seciniz: ")
if(islem=='a'):
    print("Ilk islem secildi!")
elif(islem =='b'):
    print("ikinci islem secildi!")
else:
    print("Gecersiz islem!")







