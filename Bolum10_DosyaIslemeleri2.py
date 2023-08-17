
#with open("PhytonDosyam2.txt","r",encoding = "utf-8") as f:
    #icerik = f.read()

#with open("PhytonDosyam2.txt","w",encoding = "utf-8") as f:
    #f.write("Istiklal Marsi \n"+icerik)
    
#with open("PhytonDosyam2.txt","a",encoding ="utf-8") as f:
    #f.write("\nCatma kurban olayim cehreni ey nazli hilal")

#metinin başına odev1 ifadesini eklemek
"""with open("PhytonDosyam2.txt","r+",encoding = "utf-8") as f:
    icerik = f.read()
    icerik = "Odev-1 \n" + icerik
    f.seek(0)
    f.write(icerik)
"""    
with open("PhytonDosyam2.txt","r+",encoding = "utf-8") as f:
    liste = f.readlines()
    liste.insert(9,"Kahraman irkima bir gul, ne bu siddet bu celal\n")
    liste.insert(0,"Bu bir deneme dosyasidir.\n")
    f.seek(0)
    for i in liste:
        f.write(i)
    