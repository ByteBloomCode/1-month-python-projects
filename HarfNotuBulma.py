# Koşullar ve mantıksal operatörler
print ("Harf Notu Bulma Programına Hoşgeldiniz")
not1=float(input("Lütfen notunuzu giriniz:"))
if not1>=85 and not1<=100:
    print("Harf Notunuz:AA")
elif not1>=80 and not1<=84:
    print("Harf Notunuz:BA")
elif not1>=75 and not1<=79:
    print("Harf Notunuz:BB")
elif not1>=70 and not1<=74:
    print("Harf Notunuz:CB")
elif not1>=60 and not1<=69:
    print("Harf Notunuz:CC")
elif not1>=55 and not1<=59:
    print("Harf Notunuz:DC")
elif not1>=50 and not1<=54:
    print("Harf Notunuz:DD")
elif not1>=40 and not1<=49:
    print("Harf Notunuz:FD")
elif not1>=0 and not1<=39:
    print("Harf Notunuz:FF")