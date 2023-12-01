from tkinter import *

tampilan = Tk()
tampilan.geometry("1275x720+0+0")
tampilan.resizable(0,0)
tampilan.title("Covert Temperatur") # nama aplikasi

topFrame=Frame(tampilan,bd=10,relief=RIDGE,bg='white') # frame judul
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Covert Temperatur',font=('Castellar',39,'bold'),fg='#fde4c3',bg='#302a18', bd=15,width=30) #judul aplikasi
labelTitle.grid(row=0,column=10)
var1=IntVar()
tampilan.config(bg='#784c12')
def convert_temperature():
    print('.......konversi suhu.......')
    print("ce. Celcius")
    print("fa. Fahrenheit")
    print("ke. Kelvin")
    print("re. Reamur")
    pilihan = str(input('Pilih skala suhu (ce/fa/ke/re): '))

menuFrame=Frame(tampilan,bd=10,relief=RIDGE,bg='black')
menuFrame.pack(side=LEFT)

convert_temperature=Checkbutton(menuFrame,text='convert temperatur',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var1,
                        bg='#f6f6f6')
convert_temperature.grid(row=0,column=0,sticky=W)
tampilan.mainloop()