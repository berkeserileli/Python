import math
print(dir(math)) #dir fonksiyonu import edilen modülün fonksiyonlarını gösterir

print(math.factorial(4))
#help(math) # modulün içindeki fonksiyonların ne is yaptıgını gosterir

import math as mat    #kütüphanenin ismini degistirmeye yarar.
print(mat.fabs(-5))

#from math import *  #math kütüphanesindeki tüm fonksiyonları kullanmaya yarar. Yani bu kütüphane içinden bir fonksiyon çağırdığımızda math.func()şeklinde çağırmasak ta olur
from math import*
print(factorial(7))

