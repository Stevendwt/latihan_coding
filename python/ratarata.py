def rata_rata(x):
    total = sum(x)/len(x)
    print(total)

list = []

while True:
    data = input('masukan nilai angka: ')
    if data == 'stop':
        rata_rata(list)
        break
    else:
        list.append(int(data))
