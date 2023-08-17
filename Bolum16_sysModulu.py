import sys  
print(dir(sys))


myList = [2,4,3,45,14,26]

for i in myList:
    if i != 45:
            print(i)
    else:
         #sys.exit()
         print("eser")  #görülmedi!

print("İslem tamamlandi")   #Yani sys.exit() komutu ,geldiği satırda programı bitirir!
#sys.stdout.write("Berk Eser") print() komutudur.

#print(sys.argv) #girilen dosyaları bir listede tutar
def cik():
    print('Cikis...')
    #sys.exit()

if len(sys.argv) < 2:
    print('Gerekli parametreleri girmediniz!')
    cik()

elif len(sys.argv) > 2:
    print('Çok fazla parametre girdiniz!')
    cik()

elif sys.argv[1] in ['-v', '-V']:
    print('Program sürümü: 0.8')

else:
    mesaj = 'Girdiğiniz parametre ({}) anlasilamadi!'
    print(mesaj.format(sys.argv[1]))
    cik()
#sys.argv komutunu çalıstırmak için "python (acilacak dosya)" şeklinde terminale yazilmalidir.



