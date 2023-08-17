
class Person():
    pass

person1 = Person()
print(person1)      #Person sınıfında nesne oluşturuldu
del person1         #bu durumda "del" seçilen nesneyi silecektir!
#print(person1)     Hata verir çünkü artık nesne silinmiştir.

class Kitap():
    def __init__(self,kitapAdi,sayfaSayisi,yazar):
        self.kitapAdi = kitapAdi
        self.sayfaSayisi = sayfaSayisi
        self.yazar = yazar
    def __str__(self):
        return "Isim: {}\n Sayfa Sayisi: {}\n Yazar: {}\n".format(self.kitapAdi,self.sayfaSayisi,self.yazar)
    def __len__(self):
        return self.sayfaSayisi

kitap1 = Kitap("Araba Sevdasi",300,"Recaizade")
print(len(kitap1))
print(str(kitap1))