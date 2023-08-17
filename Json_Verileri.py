import json    #JSON, verileri metin tabanlı bir formatta temsil etmek için yaygın olarak kullanılan bir veri değişim formatıdır.

kisi_dict = {
    'isim': 'Eser',
    'yas': 21,
    'cinsiyet': 'Erkek'
}

kisi_json = json.dumps(kisi_dict)     #json.dumps , python veri yapısını json veri yapısına dönüştürür. 
print(kisi_json)      #Pythondaki "kisi_dict" sözlük yapısı, json modülüne dönüştüğünden str türüne dönüşür.
print(type(kisi_json))

with open("person.json","w") as json_filem:
    json.dump(kisi_dict,json_filem)

sahsi_bilgiler = '{"ID":"201201063","Languages":["Python","C++"]}'  #Json verisidir.
python_datam= json.loads(sahsi_bilgiler)
print(python_datam)
print(type(python_datam)) 



