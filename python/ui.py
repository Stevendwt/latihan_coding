import tkinter as tk
from openpyxl import Workbook

def input_data():
    global data
    while True:
        nama = entry_nama.get()
        if nama.lower() == "stop":
            break
        nim = entry_nim.get()
        prodi = entry_prodi.get()
        data.append({"nama": nama, "nim": nim, "prodi": prodi})
        entry_nama.delete(0, tk.END)
        entry_nim.delete(0, tk.END)
        entry_prodi.delete(0, tk.END)

def display_data():
    data_sorted = sorted(data, key=lambda x: x["nim"])
    display_text = ""
    for mahasiswa in data_sorted:
        display_text += f"Nama: {mahasiswa['nama']} NIM: {mahasiswa['nim']} Prodi: {mahasiswa['prodi']}\n"
    label_display.config(text=display_text)

def export_to_excel():
    if not data:
        label_display.config(text="Data kosong")
    else:
        wb = Workbook()
        ws = wb.active
        data_sorted = sorted(data, key=lambda x: x["nim"])
        for index, mahasiswa in enumerate(data_sorted, start=1):
            ws.append([mahasiswa['nama'], mahasiswa['nim'], mahasiswa['prodi']])
        wb.save('prodama.xlsx')
        label_display.config(text="Data berhasil diekspor ke Excel (prodama.xlsx).")

def on_quit():
    root.destroy()

data = []

root = tk.Tk()
root.title("Program Data Mahasiswa")

label_nama = tk.Label(root, text="Nama:")
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

label_nim = tk.Label(root, text="NIM:")
label_nim.grid(row=1, column=0)
entry_nim = tk.Entry(root)
entry_nim.grid(row=1, column=1)

label_prodi = tk.Label(root, text="Prodi:")
label_prodi.grid(row=2, column=0)
entry_prodi = tk.Entry(root)
entry_prodi.grid(row=2, column=1)

button_input = tk.Button(root, text="Input Data", command=input_data)
button_input.grid(row=3, column=0)

button_display = tk.Button(root, text="Tampilkan Data", command=display_data)
button_display.grid(row=3, column=1)

button_export = tk.Button(root, text="Export ke Excel", command=export_to_excel)
button_export.grid(row=4, column=0)

label_display = tk.Label(root, text="", wraplength=300)
label_display.grid(row=5, columnspan=2)

button_quit = tk.Button(root, text="Keluar", command=on_quit)
button_quit.grid(row=6, columnspan=2)

root.mainloop()
