import u_26_data

def urunEkle(urunAdi, fiyat):
    u_26_data.urunler.append({
        "id":len(u_26_data.urunler)+1,
        "urunAdi": urunAdi,
        "fiyat": fiyat
    })

def urunGuncelle (id,urunAdi, fiyat):
    for urun in u_26_data.urunler:
        if(urun["id"]== id):
            urun["urunAdi"]= urunAdi
            urun["fiyat"]= fiyat
            break

def urunleriGetir():
    for urun in u_26_data.urunler:
        print(f"id {urun['id']}, ürün adı: {urun['urunAdi']}, fiyat: {urun['fiyat']}")

