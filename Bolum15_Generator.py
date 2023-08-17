#generatorlar, birden fazla değer dönebilir. Değerler "yield" ifadesi ile döner ve tüm yield ifadeleri aynı fonksiyon içerisinde döner!
#generatorlar  



def generator2(): # bu fonksiyon başka bir nesneye aktarılıp döngü içerisine alınabilir.
    return "Return calisti"
    #yield   "Yield calisti"       #geçersiz!

def generator():
    yield "Yield calisti"
    yield "Bu yield da calisti"                     
    return "Return calisti"
#yield döndüren fonksiyonlar return döndürmez! yield döndüren fonksiyonlar return döndürürken hata vermez ama return ifadesini döndürmez!

gen2 = generator2()
gen = generator()

for value2 in gen2:
    print(value2)

for value in gen:
    print(value)
print("--------------")


def katiniUret(sayi_dizisi,kati):
    for eleman in sayi_dizisi:
        yield eleman*kati
    for eleman2 in sayi_dizisi:
        yield eleman2-1

#sonuc = katiniUret([2,4,5,9,12],3)
sayi_dizisi = [3,4,5,6,7]
sonuc = katiniUret(sayi_dizisi,3)
#print(sonuc) ifadesi bu "generator" ın adresini döndürür.Çünkü fonksiyon bittiğinde yield ifadesi oluşmayacaktır.yield ifadesinin oluşması,
#fonksiyonun bir uretece gönderilmesi ile oluşur
#generator = katiniUret(sayi_dizisi,4)
print(list(sonuc))
#iterator =  iter(generator)
iterator = iter(katiniUret(sayi_dizisi,5))
for i in sayi_dizisi:
    print(next(iterator))
print("------------")

class IkininKuvveti():
    def __init__(self,max):
        self.max = max
        self.kuvvet = 0
        
    def __iter__(self):
        return self
    def __next__(self):
        if(self.kuvvet<=self.max):
            sonuc = 2**self.kuvvet
            self.kuvvet +=1
            return sonuc
        else:
            StopIteration
            
ornek1 = IkininKuvveti(5)              
iterator = iter(ornek1)                 #iteration = ornek1.__iter__()
print(next(iterator))                   #print(ornek1.__next__())
print(next(iterator))         #veya     #print(ornek1.__next__())
print(next(iterator))                   #print(ornek1.__next__())
print(next(iterator))                   #print(ornek1.__next__())
print(next(iterator))                   #print(ornek1.__next__())
print(next(iterator))                   #print(ornek1.__next__())

