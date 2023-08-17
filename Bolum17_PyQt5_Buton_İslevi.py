from PyQt5 import QtWidgets,QtGui
import sys

class Uygulama(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.func()    #Constructor içerisinde sınıfın fonksiyonu çağırılıyor.

    def func(self):
        self.resim_icerigi = QtWidgets.QLabel()
        self.resim_icerigi.setPixmap(QtGui.QPixmap("C:/Users/BERK ESER/OneDrive/Masaüstü/kuş resmi.jpg"))
        self.resim_icerigi.show()
        
        
        self.yaziAlani = QtWidgets.QLabel("Hiç tiklanmadi")
        self.buton = QtWidgets.QPushButton("Tikla")
        self.sayici = 0
        
        self.textAlani = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdir = QtWidgets.QPushButton("Yazdir")



        dikey_yerlesim = QtWidgets.QVBoxLayout() 
        dikey_yerlesim.addWidget(self.buton)
        dikey_yerlesim.addWidget(self.yaziAlani)
        dikey_yerlesim.addStretch()

        
        dikey_yerlesim.addWidget(self.textAlani)
        dikey_yerlesim.addWidget(self.temizle)
        dikey_yerlesim.addWidget(self.yazdir)
        dikey_yerlesim.addWidget(self.resim_icerigi)
        dikey_yerlesim.addStretch(1) 
       

        yatay_yerlesim = QtWidgets.QHBoxLayout()
        yatay_yerlesim.addStretch()
        yatay_yerlesim.addLayout(dikey_yerlesim)
        yatay_yerlesim.addStretch()
        self.setLayout(yatay_yerlesim)

        
        self.buton.clicked.connect(self.click)
        self.temizle.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)
        self.show()
    
    def click(self):
        sender = self.sender()    #Olayın hangi nesene tarafından tetiklendiğini belirlemek için kullanılır.
        if sender.text() == "Temizle":
            self.textAlani.clear() 
        elif sender.text() == "Yazdir":
            print(self.textAlani.text())
        elif sender.text() == "Tikla":
            self.sayici +=1
            self.yaziAlani.setText(str(self.sayici) + " kere tiklandi")
            if self.sayici % 10 ==0:
                self.yaziAlani.setText("Tebrikler")
        else:
            print("Gecersiz islem!")
        
    
uygulama = QtWidgets.QApplication(sys.argv)
uygulayici = Uygulama()
uygulayici.setWindowTitle("Program1")
sys.exit(uygulama.exec_())


