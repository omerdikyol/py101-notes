# 1 - Girilen iki sayıdan hangisi daha büyüktür?
#a = int(input("a: "))
#b = int(input("b: "))

#result = a>b
#print(f"a: {a} , b: {b}01 'den büyüktür: {result}")


# 2 - Kullanıcıdan 2 vize (%60) ve 1 final(%40) notu alıp ortalama hesaplayınız eğer not 50 nin altındaysa kaldı değilse geçti yazdırın

vize_1 = float(input("1.vize: "))
vize_2 = float(input("2.vize: "))
final = float(input("Final: "))

avr_note = ((vize_2+vize_1)*0.6)+(final*0.4)

print(f"not ortalamanız: {avr_note}. Geçme durumunuz: {avr_note>=50}")


# 3 - girilen bir sayının tek mi çift mi olduğunu yazdırın
num_1= int(input("Bir sayı giriniz."))

print(f"Girdiğiniz Sayı: {num_1},Sayının tek olma durumu: {num_1%2==1}")


# 4 - Girilen sayının pozitif negatif olma durumunu yazın.
num_2= int(input("Bir Sayı Giriniz."))
print(f"Girdiğiniz Sayı: {num_2}.Sayının pozitif olma durumu {num_2>0}")


# 5 - Parola ve email bilgisini isteyip doğruluğunu test edin.

email = "omerdikyol02@gmail.com"
sifre = "abc123"

girilenEmail = input("Mail: ")
girilenSifre = input("Sifre: ")

print(f"""Girdiğiniz Email: {email}
Girdiğiniz Şifre: {sifre}
Email Uyumluluğu: {email==girilenEmail}
Sifre Uyumluluğu: {girilenSifre==sifre}

""")