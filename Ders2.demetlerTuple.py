# demetlerin listelerden en temel farkı, ELEMANLARININ DEĞİŞTİRİLEMEMESİDİR!

myTuple = (1,2,3,4,5)
print(myTuple)
print(myTuple.index(2))  #index fonksiyonu elemanın kaçıncı indexte olduğumu gösterir int döner ve tuple daki elemanları yazabilirsin sadece!
print(myTuple.count(5))  #count fonksiyonu elemanın demette kaç tane olduğunu gösterir int döner
#myTuple.append(10)       demetlerin 2 tane fonksionu vardır ve ikisi de integer döner.
myStringTuple = (1,"Eser",8.24)
print(myStringTuple.index("Eser"))  #index fonksiyonu STRİNG DEĞER DE ALABİLİR
print(myStringTuple.count("Eser")) #count string değerleri de sayabilir ve integer döner!
