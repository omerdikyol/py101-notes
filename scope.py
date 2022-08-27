# global scope
x = "global x"

def function():
    # local scope
    x = "local x"

function()
print(x)

#####################

# global
name = "Çınar"

def changeName(new_name):
    # local
    name = new_name
    print(name)

changeName("Ada")
print(name)

######################

name = "global string"

def greeting():
    # name = "Mert"

    def hello():
        # name = "Mustafa"
        print("hello",name)

    hello()

greeting()

#######################

x = 50
def test():
    global x
    print("x :",x)

    x = 100
    print("changed x to",x)

test()
print(x)