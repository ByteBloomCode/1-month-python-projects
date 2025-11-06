#Deneme hakkıı aşılınca erişim engeli getiren versiyon
#koşullar , döngüler , sayaç(+=) , input/output
sifre="abc123"
deneme_hakki=3
deneme_sayisi=0
while deneme_sayisi<deneme_hakki:
    giris=input("Lütfen şifrenizi giriniz:")
    if giris==sifre:
        print("Şifre doğru, giriş yapılıyor.")
        break
    else:
        deneme_sayisi+=1
        kalan_hak=deneme_hakki-deneme_sayisi
        print("Şifre yanlış," ,kalan_hak , "hakkınız kaldı.")
if deneme_sayisi==deneme_hakki:
    print("Çok fazla yanlış deneme yaptınız. Erişiminiz engellendi.")