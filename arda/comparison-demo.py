# giliren iki sayıdan hangisi büyüktür
sayı1=int(input('giliren iki sayıdan hangisi büyüktür? 1. sayıyı gir: '))
sayı2=int(input('2. sayıyı gir: '))
büyükmü= sayı1> sayı2
print(f'1. sayı: {sayı1} 2. sayıdan: {sayı2} büyüktür:{büyükmü}')


'''kullanıcıdan 2 vize(%60)ve final (%40 ) notunu alııp ortalamasını hesaplayınız
eğer ortalama 50 üzerindeyse geçti değilse kaldı diyiniz'''

vize1 = float(input('dersten geçtinmi kaldınmı anlamak için 1. vize notunuzu giriniz: '))
vize2 = float(input('2. vize notunuz: '))
final1 = float(input('1. final notunuz: '))

vizelerort= (vize1+vize2)/2
final=final1
geçtimikaldımı=vizelerort*0.6+ final*0.4
x=geçtimikaldımı > 50
print(f'birinci vize notunuz: {vize1} 2. vize notunuz: {vize2} final notunuz{final1} geçtinizmi?: {x}')


# girilen bir sayının tek mi çiftmi olduğunu yazdır
tekçift=int(input('tekmi çiftmi bulmak için sayı girin: '))
y= tekçift%2 == 0  # == mi demek true veya false değeri geliyor.
print(f'girdiğiniz sayı: {tekçift} çifttir: {y}')
print('girdiğiniz sayı: {} çifttir: {}'.format(tekçift,y ))


# girilen sayının negatif pozitif olma durumunu yazdır 
pozitifmi=float(input('sayının negatifmi pozitifmi olduğunu bulmak için sayıyı giriniz: '))
z= pozitifmi > 0 
print('girdiğin sayı pozitif: {}'.format(z))


# parola ve email bilgisini isteyip doğruluğunu kontrol ediniz
# email='arda45361@gmail.com'
# parola='abc123'
parola='abc123'
email='arda45361@gmail.com'

mail=(input('mailinizi giriniz: ')).strip() # strip girdiğin şeyin başını ve sounu silmek için var.
şifre=(input('şifrenizi giriniz: ')).strip()
t=mail=='arda45361@gmail.com'
ö=şifre== 'abc123'
print('şifreniz doğrudur: {1} mailiniz doğrudur: {0} '.format(t,ö))





