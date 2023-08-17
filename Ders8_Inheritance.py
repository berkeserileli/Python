class Employee():
    def __init__(self,name,surname,ID):
        self.name = name
        self.surname = surname
        self.ID = ID
    def displayInfo(self):
        print(
            "Isim: {}\n"
            "Soyisim: {}\n"
            "ID: {}\n"
            .format(self.name,self.surname,self.ID)
        )

class Manager(Employee):
    def __init__(self,name,surname,ID,personAccounted):
        #self.name = name
        #self.surname = surname
        #self.ID = ID   
        super().__init__(name,surname,ID)        #super() fonksiyonu overriding yapmaya yarıyor. Önüne self parametresi almıyor!    
        self.personAccounted = personAccounted
    def displayInfo(self):
        print(
            "Isim: {}\n"
            "Soyisim: {}\n"
            "ID: {}\n"
            "Maas: {}\n"
            .format(self.name,self.surname,self.ID,self.personAccounted)
        )



manager1 = Manager("Berk","ILELI",201201063,15)
manager1.displayInfo()
employee = Employee("Faruk","Yildiz",123)
employee.displayInfo()