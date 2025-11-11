a= int(input("1. kenar:"))
b= int(input("2. kenar:"))
c= int(input("3. kenar:"))
if a+b>c and a+c>b and b+c>a:
    print("Bu kenar uzunlukları ile bir üçgen oluşur.")
else:
    print("Bu kenar uzunlukları ile bir üçgen oluşmaz.")

