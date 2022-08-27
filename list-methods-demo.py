names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

# Cenk ismini liste sonuna ekle
names.append("Cenk")

# Sena ismini liste başına ekle
names.insert(0,"Sena")
print(names)

# Deniz isminin indeksi nedir?
result =names.index("Deniz")
print(result)
# Deniz ismini listeden siliniz
names.remove("Deniz")

# Ali listenin bir elemanı mıdır?
result = "Ali" in names
print(result)

# Liste elemanlarını ters çevirin
names.reverse()
print(names)

# Liste elemanlarını alfabetik olarak sıralayın
names.sort()
print(names)

# years listesini büyüklüğüne göre sırala
years.sort()
print(years)

# str= "Chevrolet,Dacia" karakter dizisini listeye çevirin
str = "Chevrolet,Dacia"
result = str.split()
print(result)

#years dizisinin en büyük ve en küçük elemanı nedir?
years.sort()
print(years[0])
print(years[-1])

#years dizisinde kaç tane 1998 vardır
a = years.count(1998)
print(a)

#years dizisinin tüm elemanlarını siliniz
years.clear()
print(len(years))

# kullanıcıdan aldığınız 3 tane marka bilgisini listede saklayınız
markalar = []
for i in range(0,3,1):
    x = input("Marka: ")
    markalar.append(x)
print(markalar)
