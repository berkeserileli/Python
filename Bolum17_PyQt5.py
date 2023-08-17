from PyQt5 import QtWidgets,QtGui         #QtWidgets, QApplication sınıfını da içerir.QtGui kütüphanesi grafik işleme için; Qpixmap,QImage,QPainter grafik işlemleri yapan kütüphaneyi de içerir.
#yukarıki satırda, "from PyQt5.QtWidgets import Qapplication şeklide de çağırabilirdik"
import sys

def Pencere():

    uygulama = QtWidgets.QApplication(sys.argv) #Arayüz oluşturuluyor. Arayüz oluşturuluken en temel yapılması gerekendir. #sys.argvs komut satırı işlemleri alıcaksa kullanılabilir [] yerine
    pencere = QtWidgets.QWidget()   #Arayüzü görüntülemek için pencere objesi oluşturuluyor.
    pencere.setWindowTitle("Ilk Uygulama") #Oluşturulan arayüzün başlığını koyar
    #buton = QtWidgets.QPushButton(pencere)
    tus1 = QtWidgets.QPushButton("Tamam")    #olusan tus nesnesinin üstüne text yazmaya yarar. 
    tus2 = QtWidgets.QPushButton("İptal")
    tus3 = QtWidgets.QPushButton("İcerigi goster")
    tus4 = QtWidgets.QPushButton("Programdan Cik")
    yerlestir = QtWidgets.QVBoxLayout() #Yatay kutular oluşturmaya yarar.
    yerlestir.addStretch()  #LayOut kütüphanelerinde bulunan bu fonksiyon, oluşturulan butonların arasında belirli bir mesafe olmasını sağlar.
    yerlestir.addWidget(tus1) #nesnenin bir programda bir parça olacağını belirtir
    yerlestir.addWidget(tus2)
    yerlestir2 = QtWidgets.QHBoxLayout() #Dikey kutular oluşturmaya yarar.
    yerlestir2.addStretch() #Olusan kutuların arasındaki boslukları düzenler
    yerlestir2.addWidget(tus3)
    yerlestir2.addWidget(tus4)
    pencere.setLayout(yerlestir) #olusturulan butonların arayüzde görünmesini sağlar.
    yerlestir.addLayout(yerlestir2)
    icerik = QtWidgets.QLabel(pencere) #Qlabel sınıfı, arayüz oluşturan objeyi parametre olarak alır ve bu objeye yapılacak işlemleri Qlabel kütüphanesini kullanabilecek olan başka bir nesne oluşturur ve ona atar.  
    icerik.setText("Oncelikle herkese selam :)")
    icerik2 = QtWidgets.QLabel(pencere)
    icerik.setGeometry(100,100,500,500) #Arayüzün boyutunu belirler, setGeometry(x,y,width,height) 4 parametre alır. 
    icerik2.setPixmap(QtGui.QPixmap("C:/Users/BERK ESER/OneDrive/Masaüstü/kuş resmi.jpg"))#QPixmap kütüphanesi, QtGui kütüphanesinin içindedir.
    icerik.move(300,300)
    icerik2.setGeometry(20,20,500,550)
    icerik2.show()
    pencere.show() #Kullanıcının pencereyi görebilmesini sağlar
    #buton.setText("Press") #Butonun üzerine text yazar.
    #buton.move(10,10) #Olusan butonun x,y koordinatlarındaki hareketini sağlar.
    #buton.show() #Butonun kullanıcı ekranında görünmesini sağlar.
    sys.exit(uygulama.exec_())  #Program "X" e basıldığında bitirilir. sys.exit() olmadığı durumda uygulama sürekli çalışır.
    

Pencere()




