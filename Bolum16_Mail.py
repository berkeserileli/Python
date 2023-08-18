#NOT: Bu islemin gerçeklesebilmesi için gmail ayalarından "güvenliği düşük uygulamaların erişimine izin ver" butonunu seçmeniz gerekir. Eğer smtp.gmail.com kullanılacak ise
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = ".....@hotmail.com" #ben
mesaj["To"] = ".....@gmail.com" #göndereceğim kişi
mesaj["Subject"] = "Smtp Mail Gönderme"

yazi = "Bu mail sana geldiyse islem basarilidir."
mesaj_govdesi = MIMEText(yazi,"plain") #MIMETEXT sınıfı ile yazıcağımız verilleri ekliyoruz
mesaj.attach(mesaj_govdesi)

try:
    sunucu = smtplib.SMTP("smtp.outlook.com",587) #SMTP(Simple Mail Transfer Protocol) protokolü, e posta gönderme işlemlerini
#gerçekleştirmek için SMTP sunucusuna bağlanmayı, kimlik doğrulaması yapmayı ve e posta göndermeyi sağlar. 465 ve 587 portları kullanılır
    sunucu.ehlo() #SMTP protokolü ile iletişimi kurar.

    sunucu.starttls() #TLS, e postalarınızın şifrelenmesini sağlayan güvenli bir protokoldur. mesajların güvenliğini sağlıyoruz

    sunucu.login(".........@hotmail.com","sifre") #ben ve şifrem

    sunucu.sendmail("........@hotmail.com",".......@gmail.com",mesaj.as_string()) #ilk parametre maili gönderen kişiyi, ikinci parametre mail alan kişiyi belirtir.

    print("Mail Basariyla Gönderildi....")

    sunucu.close()

except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()
    










