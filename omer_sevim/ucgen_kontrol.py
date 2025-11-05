a = int(input("bir sayı giriniz: "))
b = int(input("bir sayı daha giriniz: "))
c = int(input("bir sayı daha giriniz: "))

if abs(a-b) < c < a+b:
    print(f"{a}, {b} ve {c} kenar uzunlukları bir üçgen oluşturabilir.")
elif abs(b-c) < a < b+c:
    print(f"{a}, {b} ve {c} kenar uzunlukları bir üçgen oluşturabilir.")
elif abs(c-a) < b < c+a:
    print(f"{a}, {b} ve {c} kenar uzunlukları bir üçgen oluşturabilir.")
else:
    print(f"{a}, {b} ve {c} kenar uzunlukları bir üçgen oluşturamaz.")
