"""
Soru:Girilen bir sayının asal olup olmadığını bulun.
"""

number = int(input("Bir sayı giriniz: "))

if number ==1:
    print("1 asal değildir.")

for i in range(2,number//2):

    if number % i !=0:
        print(f"{number}, {i} sayısına bölünemez.")
        i +=1

    if number % i ==0 and i!= number:
        print(f"{number}, {i} sayısına bölünebilir.Böylece asal değildir")
        break

    if i==number:
        print(f"{number} sadece kendisine ve 1'e bölünebilir.Yani asaldır.")

