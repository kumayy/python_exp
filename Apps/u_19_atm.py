hesapA = {
    "ad" : "D G",
    "hesap no": "1234",
    "bakiye": 1000,
    "ek hesap": 2000
}

hesapB = {
    "ad" : "M B B",
    "hesap no": "5678",
    "bakiye": 2000,
    "ek hesap": 200
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("Para çekebilirsiniz")
    else:
        toplam = hesap["bakiye"]+hesap["ek hesap"]

        if (toplam >= miktar):
            ekHesapKullanımı = input("Ek hesap kullanılsın mı (e/h): ")

            if ekHesapKullanımı == "e":
                ekHesaptanKullanılacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ek hesap"] -=  ekHesaptanKullanılacakMiktar
                
                print("paranızı çekebilirsiniz")

            else:
                print(f"{hesap['hesap no']}nolu hesabınızda yeterli bakiye bulunmamaktadır. Toplam bakiyeniz: {hesap['bakiye']}")
        else:
            print("fakir köpek")        

def bakiyeSorgula(hesap):
    print(f"{hesap['hesap no']} nolu hesapta {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz {hesap['ek hesap']}TL dir.")

paraCek(hesapA,1200)
bakiyeSorgula(hesapA)

print("###########################")

paraCek(hesapA,500)
bakiyeSorgula(hesapA)

print("###########################")

paraCek(hesapA,1500)
bakiyeSorgula(hesapA)


