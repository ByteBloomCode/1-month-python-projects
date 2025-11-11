#15'e bölünebilme kontrolü yapan program
sayi=int(input("Bir sayı giriniz:"))
if sayi%3==0 and sayi%5==0:
    print("Sayı 15'e tam bölünür.")
else:
    print("Sayı 15'e tam bölünmez.")
