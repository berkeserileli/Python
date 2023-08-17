#Soru2
"""class Dosya():

    def __init__(self,fileName):
        with open(fileName,"r",encoding = "utf-8") as f:
            okunan = f.read()
            kelimeler = okunan.split()
            self.R_kelimeler = list()
            
            for i in kelimeler:
                i = i.strip()
                i = i.strip("\n")
                self.R_kelimeler.append(i[0])
            print(self.R_kelimeler)

dosya = Dosya("siir.txt")
"""

#Soru3
"""
class Dosya2():
    def __init__(self,fileName2):
        with open(fileName2,"r",encoding= "utf-8") as f2:
            okunan_ = f2.read()
            kelimeler2 = okunan_.split()
        for eleman in kelimeler2:
            if(("@gmail.com" in eleman or "@yahoo.com" in eleman)):
                print(eleman + "+")
            else:
                print(eleman + "-")

dosya = Dosya2("mailller.txt")
"""




