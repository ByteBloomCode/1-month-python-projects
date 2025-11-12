import math
print("Bilimsel hesap makinasına hoşgeldiniz.")
işlem = ["+" , "-" , "*" , "/" , "log" , "sin" , "cos" , "tan" , "cot" , "sqrt"]

while True:
    try:
        soru = input("Lütfen yapmak istediğiniz işlemi seçin: + , - , * , / , log , sin , cos , tan , cot , sqrt\nİşlem:")
        if soru in işlem:
            break
        else:
            print("Geçersiz işlem girdiniz. Lütfen geçerli işlemlerden birini giriniz!")
    except Exception as e:
        print("Bir hata oluştu" , e)
        
    

if soru in ["log" , "sin" , "cos" , "tan" , "cot" , "sqrt"]:
    while True:
        try:
            sayi1 = float(input("İşlem yapmak istediğiniz sayıyı giriniz:"))
            break
        except ValueError:
            print("Geçersiz giriş. Lütfen sadece sayı giriniz!")
else:
    while True:
        try:
            sayi1 = float(input("İşlem yapmak istediğiniz ilk sayıyı giriniz:"))
            break
        except ValueError:
            print("Geçersiz sayı. Lütfen geçerli bir sayı giriniz!")
    while True:
        try:
            sayi2 = float(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz:"))
            break
        except ValueError:
            print("Geçersiz sayı. Lütfen geçerli bir sayı giriniz!")


if soru == "+":
    print("Sonuç:", sayi1 + sayi2)
elif soru == "-":
    print("Sonuç:" , sayi1 - sayi2)
elif soru == "*":
    print("Sonuç:" , sayi1 * sayi2)
elif soru == "/":
    if sayi2 != 0:
        print("Sonuç:" , sayi1 / sayi2)
    else:
        print("Hata: Sıfıra bölüm tanımsızdır.")
elif soru == "log":
    if sayi1 > 0:
        print("Sonuç:" , math.log(sayi1))
    else:
        print("Hata:Logaritma için sayı pozitif olmalıdır.")
elif soru == "sqrt":
    if sayi1 >= 0:
        print("Sonuç:" ,  math.sqrt(sayi1))
    else:
        print("Hata: Negatif sayıların karekökü tanımsızdır.")
elif soru == "sin":
    print("Sonuç:" , math.sin(math.radians(sayi1)))
elif soru == "cos":
    print("Sonuç:" , math.cos(math.radians(sayi1)))
elif soru == "tan":
    print("Sonuç:" , math.tan(math.radians(sayi1)))
elif soru == "cot":
    try:
        tan_deger = math.tan(math.radians(sayi1))
        if tan_deger != 0:
            print("Sonuç:" , 1 / tan_deger)
        else:
            print("Hata: Tan değeri sıfır olduğundan cot değeri hesaplanamaz.")
    except Exception as e:
        print("Beklenmeyen bir hata oluştu:" , e)




            
                        
       

        



 





      
    
