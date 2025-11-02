print("Merhaba not hesaplayıcısına hoş geldiniz?\n")

vize = float(input("Vize sınavından aldığınız notu giriniz:"))

final = float(input("Final sınavından aldığınız notu giriniz:"))

ortalama = (vize*0.4) + (final*0.6)

if ortalama >= 60:
    print("Tebrikler dersi geçtiniz.")
elif ortalama < 60:
    print("Maalesef dersten kaldınız :(")
