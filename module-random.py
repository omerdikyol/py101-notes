import random

# print(dir(random))
# help(random)


result = random.random() #0.0 ile 1.0 arasında random ondalıklı sayı
result2 =random.uniform(8,14) #8 ile 14 arasında random ondalıklı sayı
result3 = random.randint(35,37)

print(result,result2,result3)

names = ["ali","yağmur","deniz","cenk","murtaza"]
print(names[random.randint(0,len(names)-1)])

result4 = random.choice(names)
print(result4)


liste = (list(range(10)))                               # vay...
print(liste)
random.shuffle(liste)
print(liste)

liste2 = range(100)
result5 = random.sample(liste2,3)
print(result5)