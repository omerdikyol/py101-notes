import moduleyapmak

result1 = help(moduleyapmak)
result2 = help(moduleyapmak.func)

result3 = moduleyapmak.number
result4 = moduleyapmak.numbers
result5 = moduleyapmak.person["name"]

result6 = moduleyapmak.func(741)

print(result3,result4,result5,result6)


p = moduleyapmak.Person()
p.speak()

# terminal aç
# python
# import sys
# sys path
# python dosyalarının konumlarını gösterir
# C:\\Users\\omerd\\AppData\\Local\\Programs\\Python\\Python39\\lib <----- modüllerin olduğu klasör