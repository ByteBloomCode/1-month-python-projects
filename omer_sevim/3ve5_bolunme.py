a = int(input("bir sayı giriniz: "))

if a%15 == 0:
    print(f"{a} sayısı 3 ve 5 ile tam bölünmektedir.")
elif a%3 == 0:
    print(f"{a} sayısı 3 ile tam bölünmektedir.")
elif a%5 == 0:
    print(f"{a} sayısı 5 ile tam bölünmektedir.")
else:
    print(f"{a} sayısı 3 veya 5 ile tam bölünmemektedir.")