website="http://www.sadikturan.com"
course="Pyhton kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# course içindeki karakter sayısını bulun
x=len(course)
print("uzunluk:",x)

# website içinden www karakterlerini alın
print(website[7:10])


# website içinden com karakterlerini alın
print(website[-3:])

# course içinden ilk 15 ve son 15 karakteri alın
print(course[:15])
print(course[-15:])

# course içindeki karakterleri tersten yazdırın
print(course[::-1]) 

s="12345"*5
print(s[::5])

name="arda "
surname="ozturk"
age="18"

print("benim adım {} soyadım {} yaşım{}".format(name,surname,age))
print(f"benim adım {name} soyadım {surname} yaşım {age}")


# 'Hello world' ifadesindeki w yu büyük harf yapın
s='Hello world'
print(s[0:6] + "W"+ s[-4:])

# 'abc' ifadesini yan yana 3 defa yazdırın
print("abc"*3)






