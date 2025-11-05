import tkinter as tk
import random
import os

dosya = "score.txt"

if os.path.exists(dosya):
    f = open(dosya, "r")
    try:
        best = int(f.read())
    except:
        best = 0
    f.close()
else:
    best = 0

puan = 0

def bas():
    global puan, best
    puan = puan + 1
    lbl_puan["text"] = "Skor: " + str(puan)
    if puan > best:
        best = puan
        lbl_best["text"] = "Best: " + str(best)
        f = open(dosya, "w")
        f.write(str(best))
        f.close()
    r = random.randint(1,10)
    if r <= 3:  # %30 ihtimal
        root.destroy()

root = tk.Tk()
root.title("ŞANS")
root.geometry("300x200")

lbl_best = tk.Label(root, text="Best: " + str(best), font=("Arial",14))
lbl_best.pack()

lbl_puan = tk.Label(root, text="Skor: 0", font=("Arial",16))
lbl_puan.pack()

btn = tk.Button(root, text="DOKUN", font=("Arial",18),   background="lightblue", command=bas)
btn.pack(expand=True)


lbl_ekstra = tk.Label(root, text="%30 ihtimal ile ugyulama kapanır")
lbl_ekstra.pack()

root.mainloop()