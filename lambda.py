def square(num): return num ** 2


numbers = [1, 3, 5, 9]

"""
result = square(2)
print(result)
"""

"""
for item in map(square,numbers):      ## map = içindeki fonksiyonu yazdığın listedeki her eleman için çalıştırır.
    print(item)
"""

"""
result2 = list(map(square, numbers))
print(result2)
"""
"""
result3 = list(map(lambda num: num ** 2,numbers))    ## Lambda sayesinde isimsiz bir fonksiyonu anında oluşturup çalıştırdık.
print(result3)
"""

"""
square2 = lambda num: num ** 2                      ## Lambda ile direkt fonksiyon oluşturduk
print(list(map(square2,numbers)))
print(square2(7))
"""

"""
def check_even(num): return num % 2 == 0


numbers2 = [1, 3, 7, 9, 4, 10, 8, 5]

result4 = list(filter(check_even, numbers2))           ##  fonksiyonu çalıştırıp numbers2 listesini filtreleyip sağlayanları yeni bir listeye attık.
print(result4)


print(check_even(numbers2[5]))
"""