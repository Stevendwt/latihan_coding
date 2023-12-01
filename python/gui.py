import tkinter as tk
from tkinter import messagebox

def hitung_rata_rata():
    data = entry.get()
    if data == 'stop':
        if len(nilai_list) > 0:
            rata_rata = sum(nilai_list) / len(nilai_list)
            messagebox.showinfo("Rata-rata", f"Rata-rata nilai adalah: {rata_rata}")
        else:
            messagebox.showwarning("Peringatan", "Tidak ada nilai yang dimasukkan.")
    else:
        try:
            nilai = int(data)
            nilai_list.append(nilai)
            entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")

nilai_list = []

root = tk.Tk()
root.title("Program Hitung Rata-rata")

label = tk.Label(root, text="Masukkan nilai angka (ketik 'stop' untuk menghitung rata-rata):")
label.pack()

entry = tk.Entry(root, width=20)
entry.pack()

button = tk.Button(root, text="Hitung", command=hitung_rata_rata)
button.pack()

root.mainloop()
