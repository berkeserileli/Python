
#Soru1 kareler classının elemanı içerisinden 5 e kadar olan sayıların karesini alan algoritma
class Kareler():
    def __init__(self,maksimum):
        self.maksimum = maksimum
        self.ilk_sayi = 1
    
    def __iter__(self):
        return self

    def __next__(self):
        if(self.ilk_sayi <=5):
            sonuc = self.ilk_sayi**2
            self.ilk_sayi +=1
        else:
            raise StopIteration
        return sonuc
    
kareler = Kareler(5)
iterator = iter(kareler)
for kare in range(5):
    print(next(kareler))

#Soru2 2 den 1000 e kadar olan asal sayiları döndüren generator
def asal_uret():
    liste = []
    for eleman in range(2, 1001):
        for sbt in range(2, eleman):
            if eleman % sbt == 0:
                break
        else:
            liste.append(eleman)
    yield liste
    
generator = asal_uret()
for value in generator:
    print(value)

    