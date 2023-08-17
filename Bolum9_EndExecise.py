#sadece int olan stringleri bastıran örnek
"""liste = ["345","sadas","324a","14","kemal"]
for a in liste:
    try:
        a = int (a)
        print(a)
        
    except ValueError:
        #pass                     # bu komut ile hatalari pass gecebilirsin, yani komut sisteminde görünmez sadece çiktilar görünür.
        print("Value Error!")
"""

#sadece çift sayilari bastıran örnek
"""try:
    a = int(input("Lutfen sorgulamak istediginiz sayiyi giriniz: "))
    if(a%2 == 0):
        print("Cift")
    else:
        raise ValueError
except ValueError:
    print("Tek sayidir")
"""
        










