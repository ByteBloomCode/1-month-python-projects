

def ehliyet_kontrol():
    try:
        yas = int(input("lütfen yaşınızı giriniz:"))
        if yas >= 18:
            print("yaşınız ehliyet almak için uygun.")
        else:
            bekle = 18-yas
            print(f"Malesef şu anda ehliyet alamazsınız.{bekle} yıl beklemeniz gerekmektedir.")
    except ValueError:
        print("lütfen bir sayı giriniz.")

ehliyet_kontrol()