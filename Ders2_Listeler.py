myList = ["ali",3,4,5,8.82,"Faruk"]
print(myList[4])
print(myList)
List = list("BerkEserILELI")    #her bir karakteri char olarak listeleştirir.
print(List) 
List2 = ["4","5","6","7"]
#List2 = list("4","5","6","7") kodu hata veriyor cünkü list fonksiyonu içine giren string tek argüman olmalı! list("4567") şeklinde
print(List2)
fruits = ["orange","strawberry","Grapes","melon"]
fruits.append("banana") #append fonksiyonu sadece tek bir argüman ekleyebilir! append("banana","apple") olmaz!
fruits.append(15)
fruits.pop() #pop fonksiyonu sadece 1 eleman kaldırır
fruits.pop()
fruits.pop()
fruits.remove("strawberry") #remove fonksiyonu sadece 1 parametre kaldırır!  seçili elemanı kaldırmak istiyorsan bunu kullan
print(fruits)
myFruits = fruits.copy()
print(myFruits)
listA = ["BERK"]
listB = ["ESER"]
listC = ["ILELI"]
ListResult = listA + listB + listC
print(ListResult)
listB.extend(listC)
listA.extend(listB)
print(listA)
print(listA*3)   #LİSTELER STRİNGLERDE AYNI ÖZELLİKLERE SAHİPTİR! [::2] ŞEKLİNDE ELEMANLARI DA BJULABİLİRSİN
listA.append(61)
print(listA)
listNumber = [1,23,4,44,2,5]
listNumber.sort()
print(listNumber)
listWord = ["Ahmet","Hakan","Fatih"]
listWord.sort()
print(listWord)
listEx1 = [4,5,6]
listEx2 = [1,23,7]
listEx3 = [2,8,12]
listCombined = [listEx1,listEx2,listEx3]
print(listCombined[1][2])
#print(listCombined.index[1])
#print(listCombined.count[5])    bu metodalar sadece demetlere özgündür!
listWord.insert(0,"Can") #insert fonksiyonu 2 parametre alır, ilk parametre listenin hangi elemanına erişeceğini gösterir. Diğer parametre ekleyeceği elemanı listenin belirlenen yerimne ekler.
print(listWord)