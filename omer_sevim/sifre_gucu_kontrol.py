password = input("bir şifre giriniz: ")

score = 0
if 16> len(password) > 8:
    score += len(password)*5

ch = 0
dg = 0
kh = 0
bh = 0
for i in range(0, len(password)):
    
    if i<len(password)-2:
        if password[i] == password[i+1] == password[i+2]:
            score -= 10
    if password[i].isupper():
        score += 10
        bh += 1
    elif password[i].islower():
        kh += 1
    elif password[i].isdigit():
        score += 10
        dg += 1
    elif password[i].isalnum() == False:
        score += 15
        ch += 1

yuzde = score * (1/300)
print(f"şifrenizin zorluk seviyesi yüzde {yuzde}")
print(f"skor: {score}")