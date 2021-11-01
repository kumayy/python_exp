# (O.o)
import random

sayi = random.randint(1,100)

hak = int(input("kaç canınız olsun? : "))
can=hak
can_say = 0

while can > 0:
    can-=1
    can_say +=1
    tahmin= int(input("Seç bakalım: "))

    if sayi == tahmin:
        print(f"kralsın {can_say}. denemede bildin. Puanın: {100-(100/hak)*(can_say-1)}")
        break
    elif sayi>tahmin:
        print("Daha yüksek bir sayı gir")
    else:
        print("Daha düşük bir sayı gir")

    if can == 0:
        print(f"Öldün çık. \nSeçtiğim sayı '{sayi}'idi")

