import pandas as pd
import matplotlib.pyplot as plt

veri = {
    'Ay':['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs'],
    'Okunan Kitap Sayısı':[3, 5, 2, 4,6]
}

df = pd.DataFrame(veri)
print(df)

ortalama=df['Okunan Kitap Sayısı'].mean()

print("Aylık ortalama kitap sayısı:" , ortalama )

plt.plot(df['Ay'], df['Okunan Kitap Sayısı'], marker='o', color='purple')
plt.title('Aylara göre okunan kitap sayısı')
plt.xlabel('Ay')
plt.ylabel("Kitap Sayısı")
plt.grid(True)
plt.show()
