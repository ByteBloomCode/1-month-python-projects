import tkinter as tk

sayi_1 = None
r = None
sayi_2 = None

def click_1(i):
    mevcut = ekran.get()
    ekran.delete(0, tk.END)
    ekran.insert(0, mevcut + str(i['text']))

def click_islem(i):
    global r, sayi_1
    sayi_1 = float(ekran.get())
    r = i['text']
    mevcut = ekran.get()
    ekran.delete(0, tk.END)
    ekran.insert(0, mevcut + r)
    ekran.delete(0, tk.END)

def sonuc(i):
    global sayi_1, sayi_2, r
    sayi_2 = float(ekran.get())
    if r == "+":
        sonuc = sayi_1 + sayi_2
    elif r == "-":
        sonuc = sayi_1 - sayi_2
    elif r == "*":
        sonuc = sayi_1 * sayi_2
    elif r == "/":
        sonuc = sayi_1 / sayi_2
    mevcut = ekran.get()
    ekran.delete(0, tk.END)
    ekran.insert(0, sonuc)

def delete(i):
    global sayi_2, sayi_1, r
    sayi_1 = None   
    sayi_2 = None
    r = None
    ekran.delete(0, tk.END)
    




a = tk.Tk(screenName="calculator")
ekran = tk.Entry(a, width=25)
ekran.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)
button_1 = tk.Button(a, text=1, width=5, height=3, command=lambda: click_1(button_1))
button_2 = tk.Button(a, text=2, width=5, height=3, command=lambda: click_1(button_2))
button_3 = tk.Button(a, text=3, width=5, height=3, command=lambda: click_1(button_3))
button_4 = tk.Button(a, text=4, width=5, height=3, command=lambda: click_1(button_4))
button_5 = tk.Button(a, text=5, width=5, height=3, command=lambda: click_1(button_5))
button_6 = tk.Button(a, text=6, width=5, height=3, command=lambda: click_1(button_6))
button_7 = tk.Button(a, text=7, width=5, height=3, command=lambda: click_1(button_7))
button_8 = tk.Button(a, text=8, width=5, height=3, command=lambda: click_1(button_8))
button_9 = tk.Button(a, text=9, width=5, height=3, command=lambda: click_1(button_9))
button_0 = tk.Button(a, text=0, width=5, height=3, command=lambda: click_1(button_0))
button_a = tk.Button(a, text="sil", width=5, height=3, command=lambda: delete(button_a))
button_b = tk.Button(a, text="+", width=5, height=3, command=lambda: click_islem(button_b))
button_c = tk.Button(a, text="-", width=5, height=3, command=lambda: click_islem(button_c))
button_d = tk.Button(a, text="*", width=5, height=3, command=lambda: click_islem(button_d))
button_e = tk.Button(a, text="/", width=5, height=3, command=lambda: click_islem(button_e))
button_f = tk.Button(a, text="=", width=5, height=3, command=lambda: sonuc(button_f))
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_a.grid(row=1, column=3)
button_b.grid(row=2, column=3)
button_c.grid(row=3, column=3)
button_d.grid(row=4, column=2)
button_e.grid(row=4, column=1)
button_f.grid(row=4, column=3)
#entry_kutusu.pack(padx=20, pady=10)

a.mainloop()

