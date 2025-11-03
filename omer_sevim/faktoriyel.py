
def faktoriyel_hesapla():
    
    try:
        sonuc = 1
        sayi = int(input("faktöriyelini öğrenmek istediğiniz sayıyı giriniz: "))
        while not sayi == 1:
            sonuc = sonuc*sayi
            sayi = sayi - 1
            if sayi == 1:
                print(sonuc)
        


    except ValueError:
        print("bir sayı giriniz.")

faktoriyel_hesapla()