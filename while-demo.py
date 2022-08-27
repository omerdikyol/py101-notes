sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana bastırın
i = 0
while i<len(sayilar):
    print(sayilar[i])
    i +=1


# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
baslangic = int(input("Başlangıç: "))
bitis = int(input("Bitiş: "))
a= baslangic
while a<=bitis:
    if a%2==1:
        print(a)
    a+=1


# 3- 1-100 arasındaki sayıları azalan bir şekilde yazdırın
i = 100
while i>0:
    print(i)
    i-=1


# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
numbers = []
i =0
while i<5:
    sayi = int(input("sayı: "))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)


# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesine ekleyin
#       -Ürün sayısını kullanıcıya sorun
#       - dictionary listesi yapısı şeklinde olsun
#       -ürün ekleme işlemi bittiğinde ürünü listeleyin
urunler =[]

adet = int(input("Kaç ürün eklemek istersiniz: "))
i = 0
while i <adet:
    name= input("Ürün Adı: ")
    price = input("Ürün Fiyatı: ")
    urunler.append({
        "name":name,
        "price":price
    })
    i+=1
for urun in urunler:
    print(f"Ürün Adı:{urun["name"]} / Ürün Fiyatı: {urun["price"]}")
