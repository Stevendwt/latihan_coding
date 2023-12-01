def convert_temperature():
    print('.......konversi suhu.......')
    print("ce. Celcius")
    print("fa. Fahrenheit")
    print("ke. Kelvin")
    print("re. Reamur")

    pilihan = str(input('Pilih skala suhu (ce/fa/ke/re): '))

    if pilihan == 'ce':
        print('.......Celcius.......')
        celc = float(input('Input nilai suhu celsius ='))
        pilihan2 = str(input('Pilih skala suhu (fa/ke/re): '))
        convert_from_celsius(celc, pilihan2)

    elif pilihan == 'fa':
        print('.......Fahrenheit.......')
        fahr = float(input('Input nilai suhu Fahrenheit ='))
        pilihan2 = str(input('Pilih skala suhu (ce/ke/re): '))
        convert_from_fahrenheit(fahr, pilihan2)

    elif pilihan == 'ke':
        print('.......Kelvin.......')
        kelv = float(input('Input nilai suhu Kelvin ='))
        pilihan2 = str(input('Pilih skala suhu (fa/ce/re): '))
        convert_from_kelvin(kelv, pilihan2)

    elif pilihan == 're':
        print('.......Reamur.......')
        ream = float(input('Input nilai suhu Reamur ='))
        pilihan2 = str(input('Pilih skala suhu (fa/ce/ke): '))
        convert_from_reamur(ream, pilihan2)

    else:
        print("Pilihan tidak valid")
        convert_temperature()

def convert_from_celsius(celc, target_scale):
    if target_scale == 'fa':
        fahr = (9 / 5 * celc) + 32
        print(celc, 'derajat Celcius =', fahr, 'derajat Fahrenheit')
    elif target_scale == 'ke':
        kelv = celc + 273.15
        print(celc, 'derajat Celcius =', kelv, 'derajat Kelvin')
    elif target_scale == 're':
        ream = celc * (4 / 5)
        print(celc, 'derajat Celcius =', ream, 'derajat Reamur')
    else:
        print('Pilihan tidak valid')
        convert_temperature()

def convert_from_fahrenheit(fahr, target_scale):
    if target_scale == 'ce':
        celc = ((fahr - 32) * 5 / 9)
        print(fahr, 'derajat Fahrenheit =', celc, 'derajat Celcius')
    elif target_scale == 'ke':
        kelv = ((fahr - 32) * 5 / 9 + 273.15)
        print(fahr, 'derajat Fahrenheit =', kelv, 'derajat Kelvin')
    elif target_scale == 're':
        ream = (4 / 9 * (fahr - 32))
        print(fahr, 'derajat Fahrenheit =', ream, 'derajat Reamur')
    else:
        print('Pilihan tidak valid')
        convert_temperature()

def convert_from_kelvin(kelv, target_scale):
    if target_scale == 'fa':
        fahr = ((kelv - 273.15) * 9 / 5 + 32)
        print(kelv, 'derajat Kelvin =', fahr, 'derajat Fahrenheit')
    elif target_scale == 'ce':
        celc = (kelv - 273.15)
        print(kelv, 'derajat Kelvin =', celc, 'derajat Celcius')
    elif target_scale == 're':
        ream = (4 / 5 * (kelv - 273.15))
        print(kelv, 'derajat Kelvin =', ream, 'derajat Reamur')
    else:
        print('Pilihan tidak valid')
        convert_temperature()

def convert_from_reamur(ream, target_scale):
    if target_scale == 'ce':
        celc = ((5 / 4) * ream)
        print(ream, 'derajat Reamur =', celc, 'derajat Celcius')
    elif target_scale == 'ke':
        kelv = ((5 / 4 * ream) + 273)
        print(ream, 'derajat Reamur =', kelv, 'derajat Kelvin')
    elif target_scale == 'fa':
        fahr = ((ream * 9 / 4) + 32)
        print(ream, 'derajat Reamur =', fahr, 'derajat Fahrenheit')
    else:
        print('Pilihan tidak valid')
        convert_temperature()

# Start the program
convert_temperature()