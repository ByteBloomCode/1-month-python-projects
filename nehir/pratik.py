import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk
#pandas veri analizi için python da kullanılan en popüler kütüphanelerden biri.
#scikit-learn python da makine öğrenmesi(yapay zeka)modelleri kurmak için kullanılan güçlü bir kütüphanedir.

veri = pd.read_csv("notlar.csv")  #Dosyayı okuyup verileri alıyoruz

#Girdileri ve hedefi ayırıyoruz
x = veri[["Vize" , "Proje" , "Devam"]]  #Girdiler 
y = veri["Final"]                      #Tahmin edilecek değer

#modeli oluştur ve eğit
model = LinearRegression()
model.fit(x, y)

#modeli bir deneyelim
yeni_veri = pd.DataFrame([
                          [60, 80, 90],
                          [45, 70, 85],               #Burda verileri liste içinde liste şeklinde yazmamızın sebebi modelin verileri tablo şeklinde istemesi bu yüzden çift parantez kullandık
                          [30, 50, 60]
                     ], columns=(["Vize", "Proje", "Devam"]))

tahminler = model.predict(yeni_veri)
print(tahminler)

#Arayüzü başlat
pencere = tk.Tk()                                  #Pencereyi oluşturur
pencere.title("Final notu tahmin aracı")           #Pencereye başlık verir
pencere.geometry("350x400")                        #Pencere boyutunu ayarlar
pencere.configure(bg="#801893")                  #Pencere arkaplan rengini ayarlar

#Giriş Kutuları ve etiketler
etiket_stil = {"font": ("Helvetica", 12), "bg":"#f0f4f8", "fg": "#333"}
girdi_stil = {"font": ("Helvetica", 11)}

tk.Label(pencere, text="Vize Notu", **etiket_stil).pack(pady=5)
entry_vize = tk.Entry(pencere, **girdi_stil)
entry_vize.pack()

tk.Label(pencere, text="Proje Notu", **etiket_stil).pack(pady=5)
entry_proje = tk.Entry(pencere, **girdi_stil)
entry_proje.pack()

tk.Label(pencere, text="Devam Notu", **etiket_stil).pack(pady=5)
enrty_devam = tk.Entry(pencere, **girdi_stil )
enrty_devam.pack()

#Sonuç Etiketi
sonuc_label = tk.Label(pencere, text="Tahmin sonucu burada görünecek", font=("Helvetica", 12, "italic"), bg="#f0f4f8" , fg="#00695C")
sonuc_label.pack(pady=20)

#Tahmin fonksiyonu
def tahmin_et():
    try:
        vize = float(entry_vize.get())
        proje = float(entry_proje.get())
        devam = float(enrty_devam.get())
        yeni_veri = pd.DataFrame([[vize, proje, devam]], columns=["Vize", "Proje", "Devam"])
        tahmin = model.predict(yeni_veri)
        sonuc_label.config(text=f"Tahmini Final Notu: {round(tahmin[0], 2)}")
    except:
        sonuc_label.config(text="Geçersiz giriş!Lütfen sayısal değerler girin.")

#Buton ekleme
tk.Button(pencere, text="Tahmin Et", command=tahmin_et, bg="#4CAF50" , fg="white" , font=("Helvetica", 12), padx=10, pady=5).pack(pady=10)

#Arayüzü çalıştırma
pencere.mainloop()








