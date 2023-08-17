# Iki sayinin ebobunu bulma
"""def ebobuBul(a,b):
    EBOB = 1
    if(a>b):
        for i in range(1,b+1):
             if((b%i==0) and (a%i ==0)):
                EBOB = i
             else:
                continue
    elif(a<b):
         for i in range(1,a+1):
             if((b%i==0) and (a%i ==0)):
                EBOB= i
             else:
                 continue
    else:
        for i in range(1,a+1):
             if((b%i==0) and (a%i ==0)):
                EBOB = i
             else:
                 continue
    print(EBOB)
             

a = int(input("Ilk sayiyi gir: "))
b = int(input("Ikinci sayiyi gir:"))
ebobuBul(a,b)
"""

#Mukemmel sayi
"""def mukemmelSayi(k):
    toplam = 0
    p = 0
    listem=[]
    for i in range(1,k):
        if(k%i==0):
            listem.append(i)
            toplam += listem[p]
            p += 1
    print(listem)
    print(toplam)
    if(toplam != k):
        print("Bu sayi mükemmel sayi degildir!")
    else:
        print("{} mukemmel sayidir!".format(k))


k = int(input("Lutfen bir sayi giriniz: "))
mukemmelSayi(k)
"""

#Iki sayinin ekokunu bulma
"""def ekok_bulma(sayi1,sayi2):
    
    i = 2
    ekok = 1
    while True:
        if (sayi1 % i == 0 and sayi2 % i == 0):
            ekok *= i

            sayi1 //= i
            sayi2 //= i


        elif (sayi1 % i ==  0 and sayi2 % i != 0):
            ekok *= i

            sayi1 //= i


        elif (sayi1 % i != 0 and sayi2 % i == 0):
            ekok *= i

            sayi2 //= i
        else:
            i += 1
        if (sayi1 == 1 and sayi2 == 1):
            break
    return ekok

sayi1 = int(input("Sayi-1:"))
sayi2 = int(input("Sayi-2:"))

print("Ekok:",ekok_bulma(sayi1,sayi2))
"""

