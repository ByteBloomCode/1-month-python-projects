# bmw, mercedes, opel mazda elemanlarına sahip liste oluştur
liste=("Bmw mercedes opel mazda").split()

# liste kaç elemanlıdır
print(len(liste))

# listenin ilk ve son elemanı nedir
print(liste[0])
print(liste[3])

# mazda değerini toyota ile değiştir
liste[-1]="toyota"
print(liste)

# mercedes listenin bir elemanımıdır
print("mercedes"in liste)

# listenin -2 indeksindeki değer nedir 
print(liste[-2])

# listenin ilk üç elemanını alın
print(liste[0:3])

# listenin son 2 elemanı yerine toyota ve renould ekle
liste[-2:]= ('toyota','renould')
print(liste)

# listenin üzerine audi ve nissan değerlerini ekleyin
x= liste + ["audi","nissan"]
print(x)

# listenin son elemanını silin
del liste[-1]
print(liste)

# liste elemanlarını tersten yazdırın 
print(liste[::-1])


student=['arda','halit',['rümeysa','nehir']]
print(student[-1][1])

print(f"blabla{liste[0]}")











































































