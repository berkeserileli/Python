class araba():                              #eğer classın içerisinde en az 1 tane constructor varsa, class özelliklerini   
    #model = "Peugout"                       #constructorlar ile görmen gerekir.
    #fiyat = 15000
    #beygir = 150
    def __init__(self,model = "Skoda",fiyat= 5000,beygir = 200):
        self.model = model
        self.fiyat = fiyat
        self.beygir = beygir

#araba1 = araba()
araba2 = araba("Opel",20000,100)
#print(araba1.fiyat)
print(araba2.fiyat)
araba3 = araba(fiyat= 30000)
print(araba3.fiyat)
#######################################################################################

class Person():
        def __init__(self,isim,soyisim,numara,diller,maas):
            self.isim = isim
            self.soyisim = soyisim
            self.numara = numara
            self.diller = diller
            self.maas = maas
        
        def bilgileriGoster(self):
            print("----Bilgiler----")
            print(
                "Isim: {}\n"
                "Soyisim: {}\n"
                "Numara: {}\n"
                "Diller: {}\n"
                "Maas: {}\n"
                .format(self.isim,self.soyisim,self.numara,self.diller,self.maas)
            )
            
        def maasYukselt(self,miktar):
            self.maas += miktar
        
        def dilEkle(self,yeniDil):
            self.diller.append(yeniDil)


person1 = Person("Eser","ILELI",201201063,["Phyton","C++"],3500)
person1.bilgileriGoster()
person1.dilEkle("Java")
person1.bilgileriGoster()
person1.maasYukselt(500)
person1.bilgileriGoster()




