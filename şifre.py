şifre = input("Şifrenizi giriniz:")
liste = list(şifre)
özelKarakter = ["*" , "!" , "/" , "?" , "-"]


if len(şifre) < 8:
    uzunluk1 = 0
else:
    uzunluk1 = 1

if özelKarakter in liste:
    uzunluk2 = 1
else:
    uzunluk2 = 0
if any(harf.isupper() for harf in liste):
    uzunluk3 = 1
else:
    uzunluk3 = 0
if any(harf.islower() for harf in liste):
    uzunluk4 = 1
else:
    uzunluk4 = 0
if any(rakam.isdigit() for rakam in liste):
    uzunluk5 = 1
else:
    uzunluk5 = 0

ortalama = uzunluk1 + uzunluk2 + uzunluk3 + uzunluk4 + uzunluk5

if ortalama > 3:
    print("Şifre güçlü")
else:
    print("Şifre güçsüz")








