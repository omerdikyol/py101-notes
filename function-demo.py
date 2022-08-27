# 1 - Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

def print_times(word,times):
    print(word * times)

print_times("Patates ",7)


# 2 - Kendine gösterilen sınırsız sayıdaki parametreyi bir listeyi çeviren fonksiyon yazın

def turn_to_list(*params):
    list_1 = []

    for param in params:
        list_1.append(param)

    return list_1

print(turn_to_list(10,20,30,"Kek"))


# 3 - Gönderilen iki sayı arasındaki tüm asal sayıları bulun.

def prime_finder(n1,n2):

    for a in range(n1,n2):
        for b in range(2,n1):
            if  a % b == 0:
                break
        else:
            print(a)

print(prime_finder(5,21))


# 4 - Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde yazan bir fonksiyon yazın.

def divisor_finder(number1):
    list1 = list()
    for a in range(2,number1):
        if number1 % a ==0:
            list1.append(a)

    return list1

print(divisor_finder(20))