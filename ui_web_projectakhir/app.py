from flask import Flask, render_template, request
from openpyxl import Workbook
import qrcode
import json

app = Flask(__name__)

data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    pilihan = request.form['pilihan']

    if pilihan == "1":
        prodi = request.form['prodi']
        nama = request.form['nama']
        nim = request.form['nim']
        data.append({"nama": nama, "nim": nim, "prodi": prodi})
    elif pilihan == "2":
        sorted_data = sorted(data, key=lambda x: x["nim"])
        return render_template('display.html', data=sorted_data)
    elif pilihan == "3":
        if not data:
            return "Data kosong"
        else:
            prodi = request.form['prodi']
            wb = Workbook()
            ws = wb.active
            ws.append(['Nama', 'Nim', 'Prodi'])

            data_sort = sorted(data, key=lambda x: x["nim"])
            for mahasiswa in data_sort:
                mahasiswa_data = json.dumps(mahasiswa)
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
                qr.add_data(mahasiswa_data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                img.save(f"{mahasiswa['nim']}_QRCode.png")
                ws.append([mahasiswa['nama'], mahasiswa['nim'], mahasiswa['prodi']])

            wb.save(f"{prodi}.xlsx")
            return f"Data berhasil diekspor ke Excel {prodi}.xlsx."

    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
