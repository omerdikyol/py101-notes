"""
# 3 - Email ve parola bilgileri ile giriş kontrolu yapınız.
email = "1"
sifre = "2"

girilene = input("1")
girilens = input("2")

result = (email == girilene) and (sifre == girilens)

print(f"Girilen Email ve Sifre: {email} {sifre} Hesaba giriş: {result}")


# 4 - Girilen 3 sayıyı karşılaştırın
a = int(input("a"))
b = int(input("b"))
c = int(input("c"))

result = (a>b) and (a>c)
print(f"a en büyük sayıdır: {result}")
result = (b>c) and (a>c)
print(f"b en büyük sayıdır: {result}")
result = (c>a) and (c>b)
print(f"c en büyük sayıdır: {result}")

"""
# 5 - kullanıcı 2 vize (%60) 1 final (%40) 50 alsa geçer  / a)ortalama geçse bile final 50 altıysa kalır / b)final 70 ise ortalama manasız

#vize1 = float(input("vize1 "))
#vize2 = float(input("vize2 "))
#final = float(input("final "))

#ortalama  = ((vize1+vize2)/2)*0.6 + (final * 0.4)
#a) result = (ortalama>50) and (final>=50)
#b) result = (ortalama>50) and (final>=70)

#print(f"öğrencinin ortalaması: {ortalama} ve geçme durumu {result}")


#6 - Kişinin,ad,kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül= (kilo/boy uzunluğunun karesi)
# 0-18.4 = Zayıf
# 18.5 - 24.9 = Normal
# 25.0 - 29.9 = Fazla Kilolu
# 30.0 - 34.9 = Obez

name = input("Adınız: ")
kg = float(input("Kilonuz: "))
hg = int(input("Boyunuz: "))

index = (kg/hg)**2
zayif =(0<=index<=18.4)
normal = (18.4<index<=24.9)
fazla_kilo = (24.9<index<=29.9)
obez = (29.9<index<=34.9)

print(f"""Sayın {name} 
Kilo indeksiniz: {index}
Kilo Değerlendirmeniz zayıf: {zayif}
Kilo Değerlendirmeniz normal: {normal}
Kilo Değerlendirmeniz fazla kilo: {fazla_kilo}
Kilo Değerlendirmeniz obez: {obez}
""")