import random

sayi = random.randint(1, 51)
#print(sayi)

user = int(input("Bil bakalım hangi sayıyı tuttum? \n Cevap: "))
sonuc = False
while sonuc == False:
    if sayi == user:
        print("aferin la gardaş. Bildin valla...")
        sonuc = True
    elif sayi <= user:
        user = int(input("in dayı in biraz daha: "))
        sonuc = False
    elif sayi >= user:
        user = int(input("çık  dayı çık biraz daha: "))
        sonuc = False
    
