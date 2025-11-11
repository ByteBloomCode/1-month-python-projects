#girilen iki sayının toplamı çift ise EVET, tek ise HAYIR yazdıran program
sayi1=float(input("Birinci sayıyı giriniz:"))
sayi2=float(input("İkinci sayıyı giriniz:"))
toplam=sayi1+sayi2
if toplam%2==0:
    print("EVET")
else:
    print("HAYIR")


