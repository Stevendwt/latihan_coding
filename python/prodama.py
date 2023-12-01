from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(['Nama', 'Nim', 'Prodi'])

data = []

while True:
    print("====== Program Data Mahasiswa ======")
    print("Pilihan:")
    print("[1] Input Data Mahasiswa")
    print("[2] Tampilkan Data Mahasiswa")
    print("[3] Export Data ke Excel")
    print("[4] Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        print("===== Input Data Mahasiswa ======")
        while True:
            nama = input("Input nama mahasiswa (ketik 'stop' untuk berhenti): ")
            if nama.lower() == "stop":
                break
            nim = input("Input NIM mahasiswa: ")
            prodi = input("Input Progam Studi: ")
            data.append({"nama": nama, "nim": nim, "prodi": prodi})
    elif pilihan == "2":
        print("====== Data Mahasiswa ======")
        data = sorted(data, key=lambda x: x["nim"])
        for mahasiswa in data:
            print("Nama:", mahasiswa['nama'], "NIM:", mahasiswa['nim'], "Prodi:", mahasiswa['prodi'])
    elif pilihan == "3":
        if not data:
            print("====== Data kosong ======")
        else:
            data_sort = sorted(data, key=lambda x: x["nim"])
            for mahasiswa in data_sort:
                ws.append([mahasiswa['nama'], mahasiswa['nim'], mahasiswa['prodi']])
            wb.save('prodama.xlsx')
            print("Data berhasil diekspor ke Excel (prodama.xlsx).")
    elif pilihan == "4":
        exit()
    else:
        print()