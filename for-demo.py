sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesinde hangi sayılar 3'ün katıdır?
for i in sayilar:
    if i%3==0: print(i,"3'ün katıdır")


# 2- Sayilar listesindeki sayıların toplamı kaçtır?
sum = 0
for i in sayilar:
    sum += i
print("Sayıların toplamı:",sum)


# 3- Sayilar listesindeki tek sayıların karesini alınız
sum = 0
for i in sayilar:
    if i%2==1:
        sum += i**2
print("Tek Sayıların Karesi Toplamı:",sum)

###
sehirler = ["Kocaeli","İstanbul","Ankara","İzmir","Rize"]

# 4- Şehirlerden Hangileri en fazla 5 karakterlidir ?
for i in sehirler:
    if len(i)<=5:
        print(i)

###
urunler =[
    {"name":"samsung S6","price":"3000"},
    {"name":"samsung S7","price":"4000"},
    {"name":"samsung S8","price":"5000"},
    {"name":"samsung S9","price":"6000"},
    {"name":"samsung S10","price":"7000"}
]

# 5- Ürünlerin Fiyatları toplamı nedir?
sum = 0
for i in urunler:
    sum +=int(i["price"])
print("Ürünlerin fiyatları toplamı:",sum)


# 6- Ürünlerin fiyatı en fazla 5000 lira olan ürünleri gösteriniz.
print("Fiyatı en fazla 5000 TL olan ürünler:")
for i in urunler:
    if (int(i["price"])) <= 5000:
        print(i["name"])