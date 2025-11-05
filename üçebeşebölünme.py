sayi = int(input("Lütfen bir sayı giriniz:"))

if sayi % 3 == 0 and sayi % 5 == 0:
    print("3 ve 5'e tam bölünür")
else:
    print("3 ve 5'e aynı anda tam bölünmez")