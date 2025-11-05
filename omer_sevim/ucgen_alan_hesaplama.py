a = int(input("bir sayı giriniz: "))
b = int(input("bir sayı daha giriniz: "))
c = int(input("bir sayı daha giriniz: "))

heron = (a + b + c) / 2
alan = (heron * (heron - a) * (heron - b) * (heron - c)) ** 0.5
print(f"üçgenin alanı: {alan}")