website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan sona Python Programlama Rehberiniz (40 saat)"

#course içerisinde kaç karakter?

print(len(course))

# website içerisinden www karakterlerini alın

print(website[7:10])

# website içerisinden com karakterini alın

print(website[-3:len(website)])
print(website[22:25])

# course içerisinden ilk 15 ve son 15 karakteri alın

print(course[:15])
print(course[-15:])

# course içerisindekileri ters yazdırın

print(course[::-1])


name,surname,age,job = "Bora","Yılmaz",32,"mühendis"

print("Benim Adım {} {} ,Yaşım {} ve mesleğim {}".format(name,surname,age,job))

# Hello world --> Hello World

a ="Hello world"
print (a[0:6] + "W" + a[-4:])

# 3 kere abc yazdır
print ("abc"*3)