"""def decorator(asalSayi):
    def wrapper(asal_liste):
        sayilar = asal_liste
        return sayilar
    return wrapper
 """       
"""@decorator"""

def ekstra(fonk):
    def ekstra_ozellik():
        print("Mükemmel Sayilar...")
        for sayi in range(1,1001):
            toplam = 0
            i = 1
            while (i < sayi):
                if (sayi % i == 0):
                    toplam += i
                i +=1
            if (toplam == sayi):
                print(sayi)
        fonk()
                
    return ekstra_ozellik
    
@ekstra       #"ekstra" fonksiyonunun @parametresi ile belirtilmesi; "asal_olanlar" fonksiyonunun, ekstra(asal_olanlar) ifadesine karşılık geldiğini gösterir.  
def asal_olanlar():
    listem = list()
    for sayim in range(2, 1001):
        asal = True
        for a in range(2, sayim):
            if sayim % a == 0:
                asal = False
                break
        if asal:
            listem.append(sayim)
    print(listem)

asal_olanlar()

 