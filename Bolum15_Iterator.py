#Iteratorlar, üzerinde gezinilebilecek bir objedir, bu obje her seferinde bir eleman döner. Listeler"[]" üzerinde dolaşabilir.

listem1 = [3,7,12,5]
#print(dir(listem1))    kullandığım listenin fonksiyonlarını görebilirim, bu listenin fonksiyoları arasında "iter" metodu da var.

iterator = iter(listem1)   # iterator objesi oluşturuldu
print(next(iterator)) #3
"""print(next(iterator)) #7
print(next(iterator)) #12
print(next(iterator)) #5
#aslında dizi içerisinde gezinmiş olduk
print("----------------")
for eleman in listem1:
    print(eleman)
#burda python ın gördüğü ise:
print("----------------")
iterator2 = iter(listem1)
while True:
    try:
        print(next(iterator2))
    except:
        StopIteration
        break
#print(next(listem2))    #demetler üzerinde iterator oluşturulmaz!
print("----------------")
class Esya():
    def __init__(self,esyaListesi):
        self.esyaListesi = esyaListesi
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index +=1
        if(self.index < len(self.esyaListesi)):
            return self.esyaListesi[self.index]
        else:
            self.index -=1
            raise StopIteration
        
esyam1 = Esya(["Buzdolabi","Firin","Tencere","Bileklik"])
iteratorum = iter(esyam1)
while True:
        try:
            print(next(iteratorum))
        except:
            StopIteration
"""