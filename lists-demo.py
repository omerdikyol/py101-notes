# "Bmw,Mercedes,Opel,Mazda" elemanlarına sahip bir liste oluşturunuz
liste = ["Bmw","Mercedes","Opel","Mazda"]

# Liste kaç elemanlıdır?
result = len(liste)

# Listenin ilk ve son elemanı nedir?
ilk = liste[0]
son = liste[-1]

# Mazda değerini Toyota ile değiştirin
liste[-1] = "Toyota"
print(liste)

# Mercedes listenin bir elemanı mıdır ?
ismercedes = "Mercedes" in liste

# Listenin -2 indeksindeki değer nedir?
result = [-2]

# Listenin ilk 3 Elemanını alın
liste2 = liste[0:3]
print(liste2)

# Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
liste[-2:] = ("Toyota","Renault")
print(liste)

# Listenin üzerine audi ve nissan ekle
liste = liste + ["Audi","Nissan"]
#liste.append("Audi")
#liste.append("Nissan")
print(liste)

# istenin son elemanını silin
del liste[-1]
print(liste)

# Listenin elemanlarını tersten yazdırın
liste = liste[::-1]
print(liste)

# Aşağıdaki verileri bir liste içinde saklayınız

    #studentA: Yiğit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan 1998, (80,70,90)

stddef = ["studentA","studentB","studentC"]
names = [ "Yiğit Bilgi","Sena Turan","Ahmet Turan"]
dates = [2010,1999,1998]
rndmnumbers= ["(70,60,70)","(80,80,70)","(80,70,90)"]

#studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
#studentB = ["Sena","Turan",1999,[(80,80,70)]]
#studentC = ["Ahmet","Turan",1998,[(80,70,90)]]


#Verileri yazdır


for i in range(len(stddef)):
    print(stddef[i],names[i],",",dates[i],rndmnumbers[i],"\n ")

#print(studentA)
#print(studentB)
#print(studentC)




