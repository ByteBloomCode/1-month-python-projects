#veri tipleri , input/output , koşullar
sayi1=float(input("Birinci sayıyı giriniz:"))
operator=input("Yapmak istediğiniz işlemi giriniz(+,-,*,/):")
sayi2=float(input("İkinci sayıyı giriniz:"))

if operator=="+":
    sonuc=sayi1 + sayi2
    print("Sonuç:",sonuc)

elif operator=="-":
    sonuc=sayi1 - sayi2
    print("Sonuç:",sonuc)

elif operator=="*":
    sonuc= sayi1*sayi2
    print("Sonuç:",sonuc)

elif operator=="/":
    if sayi2==0:
        print("Tanımsız")
    else:
        sonuc=sayi1/sayi2
        print("Sonuç:",sonuc)

else: 
    print("Geçersiz işlem")
    print("Lütfen +,-,*,/ işlemlerinden birini giriniz.")
