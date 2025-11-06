#yalnızca koşulllar ve input/output kullanılan basit versiyon
sifre = "abc123"
giris = input("Lütfen şifrenizi giriniz:")
if giris == sifre:
    print("Şifre doğru, giriş yapılıyor.")
else:
    print("Şifre yanlış, lütfen tekrar deneyiniz.")