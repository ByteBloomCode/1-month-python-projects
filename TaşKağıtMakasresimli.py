import random
import time
secenekler = ["taş", "kağıt", "makas"]
kullanıcı_puan=0
bilgisayar_puan=0
print("Taş, Kağıt, Makas oyununa hoş geldiniz!")

while True:
   secim=input("Lütfen seçim yapınız (taş/kağıt/makas): ").lower()
   secim_bilg=random.choice(secenekler)
   if secim not in secenekler:
      print("Geçersiz seçim! Lütfen taş, kağıt veya makas seçeneklerinden birini giriniz.")
      continue
   print("Seçiminiz:",secim)
   print("Bilgisayarın seçimi:",secim_bilg)
   if secim==secim_bilg:
    print("Berabere!")
   elif (secim=="taş" and secim_bilg=="makas") or (secim=="kağıt" and secim_bilg=="taş") or (secim=="makas" and secim_bilg=="kağıt"):
       print("Kazandınız.")
       kullanıcı_puan += 1
   else:
    print("Kaybettiniz.")
    bilgisayar_puan += 1
   time.sleep(1)
   print("Puan Durumu - Siz:", kullanıcı_puan, "Bilgisayar:", bilgisayar_puan)

   if kullanıcı_puan==5:
      print("Tebrikler! Oyunu kazandınız.")
      break
   elif bilgisayar_puan==5:
      print("Oyunu kaybettiniz.")
      break





