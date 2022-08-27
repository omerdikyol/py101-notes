# class

class Person:
    #pass # Yer tutucu, boş bıraksak bile hata vermemesini sağlar.

    # class attributes
    address = "no information"

    # constructor (yapıcı method)
    def __init__(self, name, year):                 # person class'ı çalıştığı an init de çalışır

        # object attributes
        self.name = name
        self.birthyear = year
        print("init methodu çalıştı.")



    # instance methods
    def intro(self):
        print("Hello There, I am",self.name)

    def calculateAge(self):
        return 2020 - self.birthyear



# object(instance)
p1 = Person("Ali", 1989)
p2 = Person(name = "Ayşe", year = 2002)       # Üstteki ile aynı ama daha okunaklı bele

# instance method'u çalıştırma
p1.intro()
p2.intro()



#updating
p1.name = "Murtaza"
p1.address = "Şebinkarahisar"


#accessing object attributes
print(f"for p1= name: {p1.name}, year: {p1.birthyear}, adress: {p1.address}, age: {p1.calculateAge()}")
print(f"for p2= name: {p2.name}, year: {p2.birthyear}, adress: {p2.address}, age: {p2.calculateAge()}")

print(p1)
print(type(p1))

print(p2)
print(type(p2))

print(p1 == p2)




class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self,yaricap=1):
        self.yaricap = yaricap


    # Methods

    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * self.yaricap**2
    

c1 = Circle() # Yarıçap = 1
c2 = Circle(5)

print(f"c1'in alanı: {c1.alan_hesapla()}, c1'in çevresi: {c1.cevre_hesapla()}")
print(f"c2'in alanı: {c2.alan_hesapla()}, c1'in çevresi: {c2.cevre_hesapla()}")