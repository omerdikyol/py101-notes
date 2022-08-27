# Bankamatik uygulaması

hesapA = {
    "ad": "Sadık Turan",
    "hesapNo":"13245678",
    "bakiye": 3000,
    "ekHesap": 2000
}

hesapB = {
    "ad": "Ali Turan",
    "hesapNo":"12345678",
    "bakiye": 2000,
    "ekHesap": 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")      # İçi tek tırnak olmazsa hata veriyor !!!!

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz,kalan bakiyeniz:",hesap['bakiye'])

    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:

            ekHesapCheck = input("Ek Hesap Kullanılsın mı? (e/h): ")

            if ekHesapCheck == "e":
                ekhesapKullanim = miktar - hesap["bakiye"]

                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekhesapKullanim

                print("paranızı alabilirsiniz,kalan bakiyeniz:",toplam-miktar)
            if ekHesapCheck == "h":
                print(f"İşlem iptal edilmiştir,{hesap['hesapNo']} nolu hesabınızdaki bakiye: {hesap['bakiye']}")

        else:
            print("Yeterli bakiyeniz bulunmamaktadır.")



def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} lu hesabınızda {hesap['bakiye']} TL bakiyeniz bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL'dir.")

print("***************")

paraCek(hesapA,3000)
bakiyeSorgula(hesapA)
print("*************")
paraCek(hesapA,2000)
bakiyeSorgula(hesapA)