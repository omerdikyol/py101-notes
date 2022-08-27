import random
"""

1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
        ** random modülü için python random şeklinde arama yap.
        ** 100 üzerinden puanlama yapın her soru 20 puan.
        ** hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""
hak = int(input("Hak Sayısını Giriniz: "))
rand_number = random.randint(1,100)
sayac = 0
bildiniz = False
while hak>0:
    hak-=1
    sayac +=1
    deneme=int(input("Sayıyı tahmin ediniz: "))
    if hak==1:
        print("Son hakkın iyi kullan.")

    if deneme<rand_number:
        print("Biraz Yukarı.")
    if deneme==rand_number:
        print(f"Bildiniz. Deneme sayınız: {sayac} Toplam puanınız: {100-(100/hak)*(sayac-1)}")
        hak=0
        bildiniz = True
    if deneme>rand_number:
        print("Biraz Aşağı.")
    if hak==0 and bildiniz == False:
        print("Hakkın Kalmadı. Sayı:",rand_number)


print("Uygulama bu kadardı hacı")
