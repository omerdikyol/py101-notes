#name = "Sadık Turan"

#for letter in name:
#    if letter =="r":
#        break           # r ye geldiği an "break" çalışır ve döngü durur

#    if letter =="k":
#        continue          # k ya geldiği zaman es geçip devam etti.
#    print(letter)



x=0
while x<5:
    print(x)
    x+=1
print("*"*10)
y=0
while y<5:
    if y==2:
        break
    print(y)
    y+=1
print("*"*10)
z=0
while z<5:
    z += 1
    if z==2:
        continue
    print(z)

print("*"*10)
# 1-100 arası tek sayılar

a = 0

while a<=100:
    a=a+1
    if a%2==0:
        continue
    print(a)