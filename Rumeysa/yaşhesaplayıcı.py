#koşullar , input/output
print("Yaş Hesaplayıcıya Hoşgeldiniz.")
print("Lütfen şu anki yaşınızı hesapalamak için klavyeden h, farklı bir yıldaki yaşınızı hesapamak için f girin.")
secim=input("Seçiminiz:")

if secim=="h":
    yil1=int(input("Lütfen doğduğunuz yılı girin:"))
    yil2=int(input("Lütfen şu anki yılı girin:"))
    yas=yil2-yil1
    print("Şu anki yaşınız:",yas)

elif secim=="f":
    yil1=int(input("Lütfen doğduğunuz yılı girin:"))
    yil2=int(input("Lütfen yaşınızı hesaplamak istediğiniz yılı girin:"))
    yas=yil2-yil1
    print("Girdiğiniz yıldaki yaşınız:",yas)

else:
    print("Geçersiz seçim yaptınız. Lütfen sadece h veya f giriniz.")