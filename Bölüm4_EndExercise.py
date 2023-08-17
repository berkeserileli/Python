
karar = input("Lutfen seciminizi yapiniz: ")
if(karar=="ucgen"):
    print("Ucgen sectiniz!\nLutfen kenar degerlerini giriniz:")
    a = int(input("Kenar1:"))
    b= int(input("Kenar2: "))
    c = int(input("Kenar3:"))
    if((abs(b-c)<a<(b+c)) and abs(a-b)<c<(a+b) and abs(a-c)<b<(a+c)):
            print("Sectiginiz ucgen gecerlidir!")
            if((a==b==c)):
                print("Eskenar ucgen sectiniz!")
            elif((a==b) or (b==c) or (a==c)):
                print("Ikizkenar Ucgen sectiniz!")
            else:
                print("Cesitkenar ucgen sectiniz!")
    else:
            print("Sectiginiz ucgen gecerli degildir!")
elif(karar == "dortgen"):
     print("Dortgen sectiniz!\n")
     d = int(input("Kenar1:"))
     e = int(input("Kenar2:"))
     f = int(input("Kenar3:"))
     g = int(input("Kenar4:"))
     if(d==e==f==g):
        print("Kare olusturdunuz! ")
     elif(((d==e) and (f==g)) or ((d==f) and (e==g)) or ((d==g) and (e==f))):
        print("Dikdortgen olusturdunuz!")
     else:
        print("Siradan bir dikdortgen olusturdunuz!")
else:
     print("Gecersiz secenek!")








          