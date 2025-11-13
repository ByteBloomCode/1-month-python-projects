şifre=input("şifrenizi giriniz:")
import string 
özel_karakterler= string.punctuation
rakamlar= string.digits
puan=0
sayaç=0

for char in şifre:
    if char in özel_karakterler:
        sayaç+=1
if sayaç>=2:
    print("şifreniz güçlü")

else:   
   if any (char.islower() for char in şifre):
    puan+=1

   
   if any (char.isupper() for char in şifre):
    puan+=1

   if any (char in rakamlar for char in şifre):
    puan+=1

   if any (char in özel_karakterler for char in şifre):
    puan+=1

   if len(şifre)>=8:
    puan+=1





if sayaç<2:
 if puan<=5 and puan>=3: 
    print("şifreniz güçlü")
 else:print("şifreniz zayıf")











    






