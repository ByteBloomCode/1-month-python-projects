a = int(input("bir sayı giriniz: "))
b = int(input("bir sayı daha giriniz: "))
c = int(input("bir sayı daha giriniz: "))

if a<b and c<a or b<a and a<c:
    print(f"{a} sayısı ortancadır.")
elif b<a and c<b or a<b and b<c:
    print(f"{b} sayısı ortancadır.")
else:
    print(f"{c} sayısı ortancadır.")