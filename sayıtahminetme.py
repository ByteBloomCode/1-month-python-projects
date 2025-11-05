import random

print(" 1-100 arası bir sayı tuttum. Bakalım tahmin ettiğim sayıyı deneme hakkın bitmeden bulabilecek misin?")

sayı = random.randint(1,100)
denemeSayısı = 0
maxHata = 5

while denemeSayısı <= maxHata:
    tahmin = int(input("Bir sayı giriniz:"))
    denemeSayısı += 1

    if tahmin > sayı:
        print("Daha küçük bir sayı deneyiniz.")
    elif tahmin < sayı:
        print("Daha büyük bir sayı deneyiniz. ")
    elif tahmin == sayı:
        print(f"Tebrikler sayıyı {denemeSayısı} denemede doğru buldunuz.")
        break

else:
    print(f"Deneme hakkınız bitmiştir. Doğru sayı {sayı}")