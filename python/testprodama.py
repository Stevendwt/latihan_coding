from openpyxl import Workbook
import qrcode
import json

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
    print("[4] Generate Barcode")
    print("[5] Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        print("===== Input Data Mahasiswa ======")
        prodi = input("Input Progam Studi: ")
        while True:
            nama = input("Input nama mahasiswa (ketik 'stop' untuk berhenti): ")
            if nama.lower() == "stop":
                break
            nim = input("Input NIM mahasiswa: ")
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
            wb.save(f"{prodi}.xlsx")
            print(f"Data berhasil diekspor ke Excel {prodi}.xlsx.")
    elif pilihan == "4":
        data_sort = sorted(data, key=lambda x: x["nim"])
        for mahasiswa in data_sort:
                # Menyiapkan data per mahasiswa dalam format JSON
            mahasiswa_data = json.dumps(mahasiswa)

            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(mahasiswa_data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f"{mahasiswa['nama']}_QRCode.png")
    elif pilihan == "5":
        print("====== Goodbye bitch ======")
        exit()
    else:
        print()
