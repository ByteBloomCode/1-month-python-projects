# x, 5-10 arasında ola bir çift sayımı
x=int(input('gireceğiniz sayı 5 le 10 arasında olan bir çift sayımı? '))
y= (x>5 and x<10)  and (x % 2==0 )
print(f'gireceğiniz sayı 5 le on arasında olan bir çifr sayıdır {y}')

# girilen bir sayının 0 100 arasında olup olmadığını kontrol ediniz
öylemi=float(input('girilen sayının 0 la yüz arasında \nolup olmadığını programın bulması için bir sayı giriniz: '))
öylemii= 0<öylemi<100
print('girdiğiniz sayı 0 la 100 arasında',öylemii)


# girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
tek=int(input('girilen bir sayının pozitif çift sayı olup olmadığını anlamak için sayı giriniz '))
tekk=tek>0 and tek%2==0
print('evet girdiğiniz sayı pozitif bir çift sayıdır',tekk)


# e mail ve parola bilgisiyle giriş kontrolü yap
# e mail='arda45361@gmail.com'
# password='124abc'
print("email='arda45361@gmail.com'")
print("password='124abc'")
email='arda45361@gmail.com'
password='124abc'

mail=(input('mailinizi girin: '))
şifre=(input('şifrenizi girin: '))

btk=email==mail and şifre== password
print(f'şifreniz ve mailiniz doğru: {btk} ')


# girilen 3 sayıyı büyüklük olarak karşılaştır
a=float(input('girilen 3 sayıyı büyüklük olarak karşılaştırmak için sayı giriniz a: '))
b=float(input('b: '))
c=float(input('c: '))

t= a>b and a>c
print(f'a en büyük sayıdır {t}')

t= b>c and b>a 
print(f'b en büyük sayıdır {t}')

t=c>a and c>b
print(f'c en büyük sayıdır {t}')

# kullanıcından iki vize (%60) ve 1 final (%40) notunu alıp ortalamasını hesaplayınız
# eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazınız
# a)ortalama 50 olsa bile final notu en az 50 olmalıdır
# b)finalden 80 alındığında ortalamanın önemi olmasın 
# değişken= final1>80 or ortalaması>50 burda ikisinde biri doğruysa true gelicek
vize1=input('alltan alıp almayacağınızı anlamak için 1. vize notunuzu gininiz: ')
vize2=input('2. vize notunuzu gininiz: ')
final1=input('final notunuzu giriniz: ')
vize1=float(vize1)
vize2=float(vize2)
final1=float(final1)
ortalaması=(vize1+vize2)/2*0.6+final1*0.4

ö=ortalaması>50 and final1>=50 

print('öğrenci sınavdan geçti {}'.format(ö))

















