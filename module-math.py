import math

value = dir(math)                       # math fonksiyonundaki tüm fonksiyonları gösterir
value2 = help(math)                     # math fonksiyonunun help dökümanını gösterir
value3 = help(math.factorial)           # math fonksiyonunun factorial inin dökümanını gösterir
print(value)

a = math.factorial(6)
print(a)

b = math.log(math.e**2,math.e)
print(b)

c = math.floor(5.9)
print(c)

################################

import math as baba               # calendar ı takvim olarak işler

ananas = baba.log10(100)
print(ananas)

################################

def sqrt(x):
    print("x:",x)

# from math import *                      # math. yazmamıza gerek kalmadı (hepsini import eder)
from math import factorial,sqrt         # sadece yazdıklarını import eder
#value = factorial(6)
value = sqrt(9)   # en son math fonksiyonu tanımlandığı için 3 yazar, eğer def i 30. satırın altına koyarsan x: 9 yazar. !!!!!!!!!!!!!!
#value = ceil(9.8)

