sayi=float(input("10-50 aralığında bir sayı girin:"))
if sayi>10 and sayi<20:
    print("sayı 10 ile 20 arasındadır.")
elif sayi>20 and sayi<30:
    print("sayı 20 ile 30 arasındadır")
elif sayi>30 and sayi<40:
    print("sayı 30 ile 40 aralığındadır.")
elif sayi>40 and sayi<50:
    print("sayı 40 ile 50 arasındadır.")
elif sayi==10 or sayi==20 or sayi==30 or sayi==40 or sayi==50:
    print("sayı sınır değerlerindedir.")
else:
    print("sayı 10-50 aralığında değildir.")


