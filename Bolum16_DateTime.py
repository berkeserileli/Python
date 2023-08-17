from datetime import datetime
import locale



locale.setlocale(locale.LC_ALL,"")    #Bu fonksiyon kullandığım değişken ve değerleri Türkçe kelimelere çevirir.
print(dir(datetime))
su_an = datetime.now()
print(su_an)
print(su_an.year)  #int döner
print(su_an.month) #int döner
print(su_an.day)   #int döner
print(datetime.ctime(su_an))
print(datetime.strftime(su_an,"%A")) #stfrtime modülü, zamanı spesifikleştirmek için kullanılır." "%A" günün tam adını verir
print(datetime.strftime(su_an,"%B")) #"%B" ayın tam adını verir
print(datetime.strftime(su_an,"%x")) #tam tarh bilgisini döner. GİBİ GİBİ...
print("-------------------------------")
saniye = datetime.timestamp(su_an) #timestamp modülü ,zamanı saniyeye çevirir
print(saniye)
su_an2 = datetime.fromtimestamp(saniye) #fromtimestamp ifadesi, verilen saniyeyi şu anki zamana çevirir 
print(su_an2)

tarih = datetime(2001,8,12)
print(((su_an - tarih).days)//365)

