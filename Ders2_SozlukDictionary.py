

myDictionary = {'ILERI':1,'SAG':2,'SOL':3,'ASAGI':4}
print(myDictionary["ILERI"])
myDictionary["CAPRAZ"] = 5   #sözlüklere ekleme yapabiliriz bir sınırı yok!
print(myDictionary)
myDictionary["ILERI"] += 1
print(myDictionary)
Dictionary1 = {"Doctor":{"doctor1":1,"doctor2":2,"doctor3":3},"Nurse":{"nurse1":4,"nurse2":5,"nurse3":6}}
print(Dictionary1["Doctor"]["doctor1"])
print(Dictionary1) #values fonksiyonu sözlüğün değerlerini döner
print(myDictionary.values()) #sadece : nın sağındaki degerleri alıyor!
numberDictionary = {10:1,20:2,30:3,40:4}
print(myDictionary.keys()) # : nın solundaki degerleri döner
print(numberDictionary.keys())
print(myDictionary.items())
print(numberDictionary)
Student = {
    "Name:":"Eser",
    "Surname:":"ILELI",
    "ID:":"201201063"
}
name = Student.get("Name:")
surname = Student.get("Surname:")
ID = Student.get("ID:")
print(name)
print(surname)
print(ID)
