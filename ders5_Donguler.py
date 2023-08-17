#A = [1,2,3,4,5]
#print(6 in A)     #in ifadesi aratılan degeri listede arar ve dogru ise true dödürür. Dondurme şekli booldur.

#myList1 = [3,4,5,6,8.24,9.997]
#for myValue in myList1:
    #print(myValue)
#myList2 = ("Fatih","Ece","Buse","Kerim","Fazil")
#for expected in myList2:
    #print(expected)

#myList3 = (4,5,6,12,20,2)
#toplam = 0
#for eleman in myList3:
     #toplam = toplam + eleman
     #print("Toplam {}, Eleman{}".format(toplam,eleman))

#myList4 = [5,6,8,12,13]
#for eleman in myList4:
    #if(eleman % 2 ==0):
        #print(eleman)
    #else:
        #continue

#a = "BerkEserILELI"
#for eleman in a:
    #print(eleman)  #elemanı char olarak tek tek bastırır.

#myList5 = [(12,15),(19,"Berk"),(3.17,"Fatih")]
#for (i,j) in myList5:
    #print("{},{}".format(i,j))

#myList6 = {"BerkEser":"ILELI",175:77,"Pyhton":"C++"}
#for eleman in myList6.keys():
    #print(eleman)

#index = 0
#myList7 = [2,3,4,12,32,53]
#while(index < len(myList7)):
    #print("Index: ",index,"Value: ",myList7[index])
    #index+=1

#range(0,5)
#print(*range(0,5))  #range ifadesinin başına hep yıldız koy ki aradaki değerleri göstersin!
#print(range(0,5))
#print(*range(1,10,2)) 1 den 10 a kadar olan sayıları yazar ama 2 şer atlayarak, (1,3,5,7,9)

#for i in range(1,10,2):   bu da aynı sonucu verir!
    #print(i)

#myList7 = {3,4,5,7,8,10}
#for i in myList7:
     #if (i == 8):
        #break    #break TÜM döngülerden çıkar.
     #else:
        #print("i: ",i)

#myList8 = [3,5,77,68,84]
#myList9 = [i for i in myList8]
#print(myList9)
#myList9.append(10)
#myList10 = list()
#for i in myList9:    #FOR döngüsü içerisine atılan i değişkeni dizinin sonuna kadar gider!
    #myList10.append(i)
    
#print(myList10)

#myList11 = {(3,4),(7,12),(8,20)}
#myList13 = {i*j for(i,j) in myList11}
#myList12 = sorted(i*j for (i,j) in myList11) #elemanları sorted fonksiyonu içerisine atarak sıralar!
#print(myList12)
#print(myList13)
#myList14 = list()
#for i in myList12:
    #myList14.append(i)
#print(myList14)

#myList15 = [["ESER","FATIH","BURCU"],["KASIM","BURAK","CANSU"],["CANSEL","EZGI","FIKRET"]]
#myList16 = list()
#for i in myList15:
  #for x in i:
    #myList16.append(x)
    
#print(myList16)
    
myList17 = [[12,43,54,1,2,7,],[0,99,876,23,34],[4,9],["Berk",4.77]]
myList18 = list()
for  k in myList17:
   for x in k:
    myList18.append(x)
print(myList18)
myList19 = [x for k in myList17 for x in k]
print(myList19)







