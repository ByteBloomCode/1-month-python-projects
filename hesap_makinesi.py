
def toplama(x,y):
    return x + y 

def cikarma(x,y):
    return x - y

def carpma(x,y):
    return x * y

def bolme(x,y):
    if y == 0:
        return "Hata: Sıfıra bölme yapılamaz ! "
    return x / y 
def hesap_makinesi():
    print("--- Basit python hesap makinesi ---")
    print("Yapılacak İşlemi Seçin:")
    print("1. Toplama (+)")
    print("2. Çıkarma (-)")
    print("3. Çarpma")
    print("4. Bölme (/)")

    secim = input("seçiminizi girin(1/2/3/4): ")

    if secim not in ( '1' , '2' , '3' , '4' ):
        print("Geçersiz Seçim ! Lütfen 1,2,3,4'ten birini girin")
        return
    try:
        sayi1 = float(input("ilk sayıyı girin: "))
        sayi2 = float(input("ikinci sayıyı girin: "))
    except ValueError:
        print("hata: Lütfen geçerli sayısaldeğerler girin.")
        return
    sonuc = None

    if secim == '1':
        sonuc = toplama(sayi1,sayi2)
        islem_sembolu = '+'
    elif secim == '2':
        sonuc = cikarma (sayi1,sayi2)
        islem_sembolu = '-' 
    elif secim == '3':
        sonuc = carpma (sayi1,sayi2)
        islem_sembolu = '*'
    elif secim == '4':
      sonuc = bolme (sayi1,sayi2)
    islem_sembolu = '/'
    if sonuc is not None and "Hata" not in str(sonuc):
        print(f"\nsonuc:")
        print(f"{sayi1} {islem_sembolu} {sayi2} = {sonuc}")
    elif "Hata" in str(sonuc):
        print(f"\n{sonuc}")

hesap_makinesi()

