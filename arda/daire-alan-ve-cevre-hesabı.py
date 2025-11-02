'''
yariçapi verilen bir dairenin alaninin ve çevresini 
hesaplama
'''

pi=float(3.14)

r=float(input("direnin alanını ve cevresini bulmak için yaricapi giriniz:"))

print("alan:",pi*r**2)
print("cevre:",2*pi*r)

"""
dik kenarları verilen bir üçgenin hipotenüsünü hesaplama

"""


x=input("dik kenarları verilen bir üçgenin hipotenüsünü hesaplamak için 1.dik kenarı giriniz:")
y=input("2.dik kenar:")
hipotenüs=(float(x)**2+float(y)**2)**0.5
print("hipoıtenüs",hipotenüs)



"""
bir kenarı verlilen karenin alanını ve çevresini hesaplama
"""

x=input("karenin alanını ve cevresini hesaplamak için kenarı giriniz :")
alan=float(x)**2
cevre=4*float(x)
print("alan:",alan)
print("cevre:",cevre)  







'''
şimdide silindirin yüzey alanını ve hacmini hesaplayalım

'''

pi=3.14

r=float(input("silindirin yüzey alanını ve hacmini hesaplamak için yarıçapı giriniz:"))

h=input("yüksekliği giriniz")
h=float(h)

hacim=pi*r**2*h

yuzey_alani=pi*r**2*2+2*pi*r*h

print("hacim:",hacim)
print("yüzey alanı:",yuzey_alani)




