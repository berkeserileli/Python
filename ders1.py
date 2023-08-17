a = 4
b = 3
c = a//b   #  tam sayı bölmesidir a nın b ye bölünmesinden kalan bölümü verir.
print(c)   
k = 4
l = 2
d = k**l
print(d)   #üs bulma operatörüdür 4 üssü 2
a= "merhaba"
b = 'naber'
print(a)
print(b)
print(a[1])
print(a[-1]) #en sondaki karakter -1 den başlıyor dikkat et!
y ="Python Ogrenemeye Basladim"
print(y[1:])  
print(y[:3])
print(y[l:k])
print(y[:]) #tüm stringi gösteriyor
print(y[:-1])
print(y[::-1]) #stringi ters döndürüyor
print(y[1:8:2]) # 1. değerden 8. değere kadar 2 şer atlayarak gidiyor 1 dahil 8 dahil değil
g = "Merhaba"
print(g)
#g[3] = l
#print(g[3])
a = "Berk"
b = "Eser"
c = "ILELI"
print(a+b+c)
print(b*3)
l = "berkEser"
print(l + "ileli")
print(int(7/4))
o = "BerkEserILELI"
str(61)
k = o+str(61)
print(len(k))
a = "4asda3rfsdf"
#print(int(a)) her bir karakterin integer olması lazım
k = "142532452354235623562433245125"
print(int(k))
print("berk","eser","ileli")
print(3.7,5.54,8.31,"berkeserILELI")
print("at\navrat\nsilah")
print("Ocak\tSubat\tMart")
print(type(k))
print(12,8,2001,sep = "/")
print("berk","eser","ileli",sep = "\n")
print(*"12, 8 2001")
print(*"eser",sep = "/")
x = 3
y = 4
print("{} ve {} benim en sevdigim sayilardir.{} ise onlarin carpimidir".format(x,y,x*y))
print("{1}{0}{2}".format("eser","baba",61))
print("{:.2f}".format(7.1292))

