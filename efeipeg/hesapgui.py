import tkinter as tk

guncel_ifade = ""

def buton_tikla(sembol):
    global guncel_ifade
    guncel_ifade = guncel_ifade + str(sembol)
    ekran_metni.set(guncel_ifade)

def sonucu_goster():
    global guncel_ifade
    sonuc = str(eval(guncel_ifade))
    ekran_metni.set(sonuc)
    guncel_ifade = sonuc

def sil():
    global guncel_ifade
    guncel_ifade = ""
    ekran_metni.set("")

ana_pencere = tk.Tk()
ana_pencere.title("Hesap Makinesi")
ana_pencere.geometry("300x400")
ana_pencere.resizable(False, False)

ekran_metni = tk.StringVar()

ekran = tk.Entry(ana_pencere, textvariable=ekran_metni, font=('arial', 20), bd=10, width=14, justify='right')
ekran.grid(row=0, column=0, columnspan=4, pady=10)

btn_7 = tk.Button(ana_pencere, text=' 7 ', height=2, width=5, command=lambda: buton_tikla(7))
btn_7.grid(row=1, column=0, pady=5)

btn_8 = tk.Button(ana_pencere, text=' 8 ', height=2, width=5,background="purple", command=lambda: buton_tikla(8))
btn_8.grid(row=1, column=1, pady=5)

btn_9 = tk.Button(ana_pencere, text=' 9 ', height=2, width=5, command=lambda: buton_tikla(9))
btn_9.grid(row=1, column=2, pady=5)

btn_bol = tk.Button(ana_pencere, text=' / ', height=2, width=5, command=lambda: buton_tikla('/'))
btn_bol.grid(row=1, column=3, pady=5)

btn_4 = tk.Button(ana_pencere, text=' 4 ', height=2, width=5, command=lambda: buton_tikla(4))
btn_4.grid(row=2, column=0, pady=5)

btn_5 = tk.Button(ana_pencere, text=' 5 ', height=2, width=5, command=lambda: buton_tikla(5))
btn_5.grid(row=2, column=1, pady=5)

btn_6 = tk.Button(ana_pencere, text=' 6 ', height=2, width=5,background="gray", command=lambda: buton_tikla(6))
btn_6.grid(row=2, column=2, pady=5)

btn_carp = tk.Button(ana_pencere, text=' * ', height=2, width=5, command=lambda: buton_tikla('*'))
btn_carp.grid(row=2, column=3, pady=5)

btn_1 = tk.Button(ana_pencere, text=' 1 ', height=2, width=5, background="red", command=lambda: buton_tikla(1))
btn_1.grid(row=3, column=0, pady=5)

btn_2 = tk.Button(ana_pencere, text=' 2 ', height=2,   background="blue", width=5, command=lambda: buton_tikla(2))
btn_2.grid(row=3, column=1, pady=5)

btn_3 = tk.Button(ana_pencere, text=' 3 ', height=2, width=5, command=lambda: buton_tikla(3))
btn_3.grid(row=3, column=2, pady=5)

btn_cikar = tk.Button(ana_pencere, text=' - ', height=2, width=5, command=lambda: buton_tikla('-'))
btn_cikar.grid(row=3, column=3, pady=5)

btn_0 = tk.Button(ana_pencere, text=' 0 ', height=2, width=5, command=lambda: buton_tikla(0))
btn_0.grid(row=4, column=0, pady=5)

btn_nokta = tk.Button(ana_pencere, text=' . ', height=2, width=5, command=lambda: buton_tikla('.'))
btn_nokta.grid(row=4, column=1, pady=5)

btn_temizle = tk.Button(ana_pencere, text=' C ', height=2, width=5, command=sil)
btn_temizle.grid(row=4, column=2, pady=5)

btn_topla = tk.Button(ana_pencere, text=' + ', height=2, width=5, command=lambda: buton_tikla('+'))
btn_topla.grid(row=4, column=3, pady=5)

btn_esittir = tk.Button(ana_pencere, text=' = ', height=2, width=26, command=sonucu_goster)
btn_esittir.grid(row=5, column=0, columnspan=4, pady=5)

ana_pencere.mainloop()
