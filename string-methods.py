message = " Hello there. My name is Sadık Turan"

# message = message.upper()    ## Hepsi büyük harf

# message = message.lower()    ## Hepsi küçük harf

# message = message.title()    ## her kelimenin ilk harfi büyük

# message = message.capitalize() ## Sadece ilk harf büyük

# message = message.strip()        ## Baş ve sondaki boşluk gider

# message = message.split()  ## Kelimelerden dizi oluşturur.Bir kelimeyi seçip üzerinde daha rahat işlem yapılmasını sağlar

# print(message[2])  ## Üstteki kod ile diziye çevirdik bu da 3.elemanı gösterir(My)

# message = message.split(".")   ## Noktalardan itibaren ayırır  İÇİNE NE YAZARSAN ONDAN AYIRIYOR YANİ

# message = "*".join(message) ## Ayrılan stringi birleştirir.Baştaki tırnak arasına ne yazarsan birleştirdiği yerlerin arasına onu koyar

# message = message.find("Sadık") ## Kelimeyi arar.Gösterdiği sayı da kelimeyi bulduğu ilk string.

# isFound = message.startswith("H")   # H ile mi başlıyor diyo işte aga
# isFound2 = message.endswith("H")   # H ile mi bitiyor diyo işte aga
# print(isFound)
# print(isFound2)

# message = message.replace("Sadık","Umer")  # Birinciyi bulur siler yerine ikinciyi yazar adı Umer Turan artık adamın

# message = message.replace("ç","c").replace("ö","o").replace("ü","u")  ## vay be...

# message = message.center(100,"*") ### 100 karakterlik alan oluşturur message ı ortaya yerleştirir.İkincisi ise boşluklar yerine bir şey koyabilmek için

print(message)