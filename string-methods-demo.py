website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"


#1- " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin

a = " Hello World "
a = a.strip()

print(a)

#2- "www.sadikturan.com" içindeki sadikturan bilgileri haricindeki her karakteri silin
result = "www.sadikturan.com".strip("moc.").strip(".www")
print(result)
b = website[11:21]
print(b)

#3- course ın içindeki tüm harfleri küçük yap

c = course.lower()

#4- website içinde kaç a vardır?

d = website.count("a")

print(d)

#5- website www ile başlayıp com ile bitiyor mu?
e = website.startswith("www")
f = website.endswith("com")
print (e,f)

#6 website ın içinde com var mı?
g = website.find(".com")
print(g)

#7 - "course" içindeki karakterlerin hepsi alfabetik mi? (isalpha,isdigit)
h = course.isalpha()
i = course.isdigit()
print(h)
print(i)

#8 - "Contents" ifadesini satırda 50 karakter içine yerleştir sağa ve sola * ekle
j = "Contents"
j = j.center(50,"*")
print(j)

#9- "course" karakter dizisindeki tüm boşlukları - yap
k = course.replace(" ","-")
print(k)

#10 - Hello World karakter dizisinde World yerine There yaz
l = "Hello World"
l = l.replace("World","There")
print(l)

#11 - course karakter dizisini boşluk karakterlerinden ayırın
m = course.split(" ")
print(m)