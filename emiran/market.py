#----GEREKLİ KÜTÜPHANELER----
from time import sleep
from random import choices
import string 


#----ÜRÜNLERİN SÖZLÜĞÜ----
envanter= {}


#----KULLANICILAR SÖZLÜĞÜ----
giris = {}


#----ÜRÜN BİLGİLERİ----
def urunler_bilgileri(ad: str, fiyat: float, stok_miktarı: int) -> dict:
    urun_dict = {
    "urun_adi": ad,
    "fiyat" : fiyat,
    "stok_miktarı":stok_miktarı
    }
    return urun_dict


#----SERİ NO OLUŞTURMA----
def seri_no(uzunluk = 8):
    karakterler =   string.ascii_uppercase + string.digits
    rastgele_karakter = choices(karakterler, k = uzunluk)
    seri_nom = "".join(rastgele_karakter)
    return seri_nom


#----TAM SAYI KONTROL ETME----
def tamsayi_kontrol(verilen:str):
        if verilen.isdigit():
             return int(verilen)        
        else:
            print("Lütfen geçerli bir miktar giriniz.")
            sleep(1)
            return None
        

#----ONDALIKLI SAYI KONTROL ETME----
def ondalikli_kontrol(verilen: str):
     verilen = verilen.strip()

     if not verilen:
          print("Lütfen boş bırakmayınız.")
          sleep(1)
          return None
     try:
          deger = float(verilen)
          return deger
     except ValueError:
          print("Lütfen geçerli bir miktar giriniz.")
          sleep(1)
          return None


#----ÜRÜN OLUŞTURMA----
def urunolusturma():
    isim = input("Eklemek istediğiniz ürünün adını giriniz: ")
    while True:
        giris_stok = input("Ürün miktarı giriniz: ")
        stok = tamsayi_kontrol(giris_stok)
        if stok is not None:
               break 
        
    while True:         
        giris_fiyat = input("Ürünün fiyatını giriniz: ")
        fiyat = ondalikli_kontrol(giris_fiyat)
        if fiyat is not None:
             break  
    urunun_serino = seri_no()
    yeni_urun = urunler_bilgileri(ad=isim, fiyat=fiyat, stok_miktarı=stok)
    envanter[urunun_serino] = yeni_urun
    print("Ürün Kaydedildi!")
    print(f"Eklenen ürünün seri numarası {urunun_serino}")
    sleep(1)


#----KULLANICI ADI VE ŞİFRE YETERLİLİĞİ----
def strength(userpass: str):
    puan = 0
    userpass = userpass.strip()
    ozel_karakterler = string.punctuation
    if len(userpass) >= 8:
         puan += 20
    if any(i.isdigit() for i in userpass):
         puan += 20
    if any(i.isupper() for i in userpass):
         puan += 20
    if any(i in ozel_karakterler for i in userpass):
         puan += 20 
     
    if puan > 40:
         return userpass
         

    
#----KAYIT OLMA----
def register():
    kullaniciadi = input("Lütfen istediğiniz kullanıcı adını giriniz: ").strip()

    if not kullaniciadi:
        print("Kullanıcı adı boş olamaz.")
        return

    if kullaniciadi in giris:
        print("Bu kullanıcı adı zaten alınmış! Başka bir ad deneyin.")
        return

    if len(kullaniciadi) < 3:
        print("Kullanıcı adı en az 3 karakter olmalıdır.")
        return

    sifre = input("Lütfen istediğiniz şifreyi giriniz: ").strip()
    
 
    guclu_mu = strength(sifre)
    
    if guclu_mu is not None:
        if kullaniciadi != sifre:
          giris[kullaniciadi] = sifre 
          print("Başarıyla Kayıt Olundu!")
        else: 
             print("Kullanıcı adınız ile şifreniz aynı olamaz.")
    else:
        print("Seçtiğiniz şifre yeteri kadar güçlü değil.")

#----GİRİŞ YAPMA----
def login():
     kullanici = input("Lütfen kullanıcı adınızı giriniz: ").strip()
     sifre = input("Lütfen şifrenizi giriniz: ").strip()
     if kullanici in giris:
          if giris[kullanici] == sifre:
               print("Hoşgeldiniz yönlendiriliyorsunuz...")
               sleep(2)
               return True
          else:
               print("Kullanıcı adınız veya şifreniz hatalı.")
               return False
     else:
          print("Böyle bir kullanıcı bulunamadı.")
          return False   

def main(): 
     while True:
          print("=" * 30)
          sleep(.2)
          print("1. Giriş Yap")
          sleep(.2)
          print("2. Kayıt Ol")
          sleep(.2)
          print("3. Çıkış")
          sleep(.2)

          secim = input("Lütfen yapmak istediğiniz işlemi seçiniz. (1-3): ")
          if secim == "1":
               if login():
                    while True:
                         print("YÖNETİCİ PANELİ")
                         sleep(.2  )
                         print("1. Ürün Ekle")
                         sleep(.2)
                         print("2. Envanteri Görüntüle")
                         sleep(.2)
                         print("3. Çıkış Yap(Ana Menü)")
                         sleep(.2)
                         islem = input("Lütfen yapmak istediğiniz işlemi seçiniz. (1-3): ")
                         if islem == "1":
                              sleep(.2)
                              urunolusturma()
                              sleep(.2)
                         elif islem == "2":
                              sleep(.2)
                              print("GÜNCEL STOK")
                              sleep(.2)
                              if not envanter:
                                   print("Envanter boş.")
                              else:
                                   for serino, detay in envanter.items():
                                        print(f"Seri Numarası: {serino} | Ürün: {detay["urun_adi"]} | Fiyat: {detay["fiyat"]} | Stok: {detay["stok_miktarı"]}")
                                   sleep(2)
                         elif islem == "3":
                              print("Ana menüye dönülüyor...")
                              sleep(1)
                              break
                         else:
                              print("Lütfen geçerli bir işlem numarası giriniz: ")

          elif secim == "2":
               register()
          
          elif secim == "3":
               print("Çıkış Yapılıyor... ")
               sleep(.2)
               break
          else:
               print("Lütfen geçerli bir işlem numarası giriniz.")

#----PROGRAMI BAŞLAT----
main()
                              
# ŞUANDA HERKES İSTEDİĞİ GİBİ ÜRÜN EKLEYEBİLİYOR  3 FARKLI YETKİ OLACAK. 1. EN GENEL YÖNETİCİ HANGİ KULLANICILARIN ADMİN YETKİSİNE SAHİP OLUP OLMAYACAĞINI O SEÇECEK. ADMİN, STOKTA EKLEME ÇIKARMA YAPABİLECEK USER İSE O EŞYALARI ALACAK EĞER STOKTA YOKSA ALAMAYACAK TABİ VE İSTEK LİSTESİNE EKLEYEBİLECEK EĞER STOK YOKSA VE BU BİLDİRİM OLARAK ADMİNLERE VE YÖNETİCİYE GİDECEKLER Kİ STOK EKLESİNLER.
