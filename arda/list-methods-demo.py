names=['Ali','Yağmur','Hakan','Deniz']
years=[1998, 2000, 1998, 1987]

# cenk ismini listenin sonuna ekleyin
names.append("cenk")
print(names)

# sena değerini lisetnin başına ekleyiniz
names.insert(0,'sena')
print(names)


# deniz ismini listeden silelim
names.remove('Deniz') #remove dersen adını yazıcan
print(names)


# deniz ismini listeden silelim
silinen=names.pop(1) #pop dersen index numarasını yazcıan
print(silinen)#popun içini boş bırakırcan sonuncuyu siler 


#cenk isminin indexi nedir
print(names.index('cenk'))


# ali listenin bir elemanımıdır
print("Ali"in names) 

# liste elemanlarını ters çevir
names=names[::-1]
print(names)

# liste elemanlarını ters çevir
names.reverse()
print(names)

# liste elemanlarını alfabetik olarak sırala
names.sort()  #['sena', 'Yağmur', 'Hakan', 'cenk']
print(names)  #['Hakan', 'Yağmur', 'cenk', 'sena']
#Alfabetik olarak sıralaması gerekirdi ama python h büyük yazılmış diye h ye öncelik verdi




#years listesini rakamsal büyüklüğe göre sıralayınız
years.sort()
print(years)

# "chevrolet,dacia" karakter dizisini listeye çevir
print("chevrolet,dacia".split())


# years dizisinin en büyük ve en küçük elemanı nedir
print(max(years),min(years))


# years dizisinde kaç tane 1998 değeri vardır
print(years.count(1998))


# years dizisinin tüm elemanlarını sil
years.clear()
print(years)


# kullanıcıdan aldığın 3 tane marka bilgisini bir listede sakla
markalar=[]
marka=input("markaları giriniz: ")
markalar.append(marka)
marka=input("markaları giriniz: ")
markalar.append(marka)
marka=input("markaları giriniz: ")
markalar.append(marka)

print(markalar)


















