# (O.o)
sayi = int(input("sayı giriniz : "))

if (sayi==230614)or(sayi==23062014):
    print("<3 :*")
else:
    asalmi=True

    if (sayi==1):
        asalmi = False

    for i in range(2,sayi):
        if (sayi%i == 0 ):
            asalmi=False
            break

    if asalmi:
        print("sayı asal")
    else:
        print("asal değil")

###################################################################

