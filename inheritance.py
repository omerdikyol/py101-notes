# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)


class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_am_i(self):
        print("U r Heisenberg")

    def eat(self):
        print("Ay iit.")


class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)           # ?
        self.branch = branch
    def who_am_i(self):
        print(f"I am a {self.branch} teacher.")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)# 16.satırdaki print 11.satırdaki printin basılmasını engeller.Onun çözümü de bu.
        self.studentNumber = number
        print("Student Created")


    def who_am_i(self):
        print("I am a student.")
    def hello(self):
        print("I am a student.")



p1 = Person("Ali","Yılmaz")
s1 = Student("Patates","Tuzcu","1331")
t1 = Teacher("Halil","Gürbüz","Physics")

print(p1.firstName,p1.lastName)
print(s1.firstName,s1.lastName,s1.studentNumber)

p1.who_am_i()
s1.who_am_i()

s1.eat()
p1.who_am_i()  # Gördüğünüz gibi 28. satırı yazmadı

s1.hello()

t1.who_am_i()
