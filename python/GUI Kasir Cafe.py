from cProfile import label
import string
from tkinter import *
import random
import time
from tkinter import messagebox
from tkinter import filedialog
from turtle import clear;
from PIL import ImageTk, Image 

#Membuat Frame aplikasi
root = Tk()

root.geometry("1275x720+0+0") # menentukan ukuran window aplikasi
root.resizable(0,0)
root.title("De Brunch Cashier") # nama aplikasi

topFrame=Frame(root,bd=10,relief=RIDGE,bg='white') # frame judul
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='De Brunch',font=('Castellar',39,'bold'),fg='#fde4c3',bg='#302a18', bd=15,width=30) #judul aplikasi
labelTitle.grid(row=0,column=10)

root.config(bg='#784c12') # warna dasar / background
# batas Frame aplikasi


# VARIABLE
# Menentukan variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

# variabel menu brunch
e_pancake=StringVar()
e_croissant=StringVar()
e_waffle = StringVar()
e_cinnamonroll = StringVar()
e_burger = StringVar()
e_omelets = StringVar()
e_quiche = StringVar()
e_avocadotoast = StringVar()
e_tomatosoup = StringVar()

# variabel menu minuman
e_applejuice=StringVar()
e_lemontea = StringVar()
e_milktea = StringVar()
e_espresso = StringVar()
e_vanillalatte = StringVar()
e_airmineral = StringVar()
e_fruitysmoothies = StringVar()
e_cappuchinocoffe = StringVar()
e_softdrink = StringVar()

# variabel menu dessert
e_onionring=StringVar()
e_frenchfries = StringVar()
e_friedicecream = StringVar()
e_cheesecake = StringVar()
e_icecream = StringVar()
e_donuts = StringVar()
e_chococupcake = StringVar()
e_saladbuah = StringVar()
e_pudding = StringVar()

# variabel Harga dalam struk
hargadaribrunchvar=StringVar()
hargadariminumanvar=StringVar()
hargadaridessertvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
taxvaluevar=StringVar()

e_pancake.set('0')
e_croissant.set('0')
e_waffle.set('0')
e_cinnamonroll.set('0')
e_burger.set('0')
e_omelets.set('0')
e_quiche.set('0')
e_avocadotoast.set('0')
e_tomatosoup.set('0')

e_applejuice.set('0')
e_lemontea.set('0')
e_milktea.set('0')
e_espresso.set('0')
e_vanillalatte.set('0')
e_airmineral.set('0')
e_fruitysmoothies.set('0')
e_cappuchinocoffe.set('0')
e_softdrink.set('0')

e_onionring.set('0')
e_frenchfries.set('0')
e_friedicecream.set('0')
e_cheesecake.set('0')
e_icecream.set('0')
e_donuts.set('0')
e_chococupcake.set('0')
e_saladbuah.set('0')
e_pudding.set('0')


# FUNGSI
# Awal fungsi perhitungan harga total
tax=(11/100)
def totalcost():
    # mengglobalkan beberapa variable terlebih dahulu
    global hargadaribrunch,hargadariminuman,hargadaridessert,subtotalItems,totaltax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_pancake.get())
        item2=int(e_croissant.get())
        item3=int(e_waffle.get())
        item4=int(e_cinnamonroll.get())
        item5=int(e_burger.get())
        item6=int(e_omelets.get())
        item7=int(e_quiche.get())
        item8=int(e_avocadotoast.get())
        item9=int(e_tomatosoup.get())

        item10=int(e_applejuice.get())
        item11=int(e_lemontea.get())
        item12=int(e_milktea.get())
        item13=int(e_espresso.get())
        item14=int(e_vanillalatte.get())
        item15=int(e_airmineral.get())
        item16=int(e_fruitysmoothies.get())
        item17=int(e_cappuchinocoffe.get())
        item18=int(e_softdrink.get())

        item19=int(e_onionring.get())
        item20=int(e_frenchfries.get())
        item21=int(e_friedicecream.get())
        item22=int(e_cheesecake.get())
        item23=int(e_icecream.get())
        item24=int(e_donuts.get())
        item25=int(e_chococupcake.get())
        item26=int(e_saladbuah.get())
        item27=int(e_pudding.get())

        hargadaribrunch=(item1*28000) + (item2*32000) + (item3*29000) + (item4*28000) + (item5*31000) + (item6*26000) + (item7*38000) \
        + (item8*27000) + (item9*29000)
        hargadariminuman=(item10*20000) + (item11*15000) + (item12*15000) + (item13*22000) + (item14*18000) + (item15*8000) \
        + (item16*22000) + (item17*20000) + (item18*15000)
        hargadaridessert=(item19*18000) + (item20*25000) + (item21*25000) + (item22*28000) + (item23*16000) + (item24*21000) \
        + (item25*23000) + (item26*22000) + (item27*15000)

        hargadaribrunchvar.set(str(hargadaribrunch))
        hargadariminumanvar.set(str(hargadariminuman))
        hargadaridessertvar.set(str(hargadaridessert))

        subtotalItems=hargadaribrunch+hargadariminuman+hargadaridessert
        subtotalvar.set(str(subtotalItems))
       #tax=(11/100)
        taxvaluevar.set(str(tax))
        totaltax= subtotalItems*tax
        
        
        servicetaxvar.set(totaltax)
        
        totalcost=subtotalItems+totaltax
        totalcostvar.set(str(totalcost))

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# Batas fungsi perhitungan harga total

# awal fungsi cetak struk
def struk():
    global billnumber,date
    if hargadaribrunchvar.get() != '' or hargadaridessertvar.get() != '' or hargadariminumanvar.get() != '':
        textStruk.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textStruk.insert(END,'Resep Ref:\t        '+billnumber+'\t         '+date+'\n')
        textStruk.insert(END,'******************\n')
        textStruk.insert(END,'Items:\t\t          Harga Total (Rp)\n')
        textStruk.insert(END,'******************\n')
        if e_pancake.get()!='0':
            textStruk.insert(END,f'pancake\t\t\tRp. {int(e_pancake.get())*27000}\n\n')

        if e_croissant.get()!='0':
            textStruk.insert(END,f'croissant\t\t\tRp. {int(e_croissant.get())*33000}\n\n')

        if e_waffle.get()!='0':
            textStruk.insert(END,f'waffle\t\t\tRp. {int(e_waffle.get())*25000}\n\n')

        if e_cinnamonroll.get() != '0':
            textStruk.insert(END, f'cinnamonroll:\t\t\tRp. {int(e_cinnamonroll.get()) * 22000}\n\n')

        if e_burger.get() != '0':
            textStruk.insert(END, f'burger:\t\t\tRp. {int(e_burger.get()) * 33000}\n\n')

        if e_omelets.get() != '0':
            textStruk.insert(END, f'omelets:\t\t\tRp. {int(e_omelets.get()) * 46000}\n\n')

        if e_quiche.get() != '0':
            textStruk.insert(END, f'quiche:\t\t\tRp. {int(e_quiche.get()) * 38000}\n\n')

        if e_avocadotoast.get() != '0':
            textStruk.insert(END, f'avocado toast:\t\t\tRp. {int(e_avocadotoast.get()) * 27000}\n\n')

        if e_tomatosoup.get() != '0':
            textStruk.insert(END, f'tomato soup:\t\t\tRp. {int(e_tomatosoup.get()) * 22000}\n\n')

        if e_applejuice.get() != '0':
            textStruk.insert(END, f'apple juice:\t\t\tRp. {int(e_applejuice.get()) * 20000}\n\n')

        if e_lemontea.get() != '0':
            textStruk.insert(END, f'lemon tea:\t\t\tRp. {int(e_lemontea.get()) * 15000}\n\n')

        if e_milktea.get() != '0':
            textStruk.insert(END, f'milktea:\t\t\tRp. {int(e_milktea.get()) * 15000}\n\n')

        if e_espresso.get() != '0':
            textStruk.insert(END, f'espresso:\t\t\tRp. {int(e_espresso.get()) * 22000}\n\n')

        if e_vanillalatte.get() != '0':
            textStruk.insert(END, f'vanilla latte :\t\t\tRp. {int(e_vanillalatte.get()) * 18000}\n\n')

        if e_airmineral.get() != '0':
            textStruk.insert(END, f'air mineral:\t\t\tRp. {int(e_airmineral.get()) * 8000}\n\n')

        if e_fruitysmoothies.get() != '0':
            textStruk.insert(END, f'fruity smoothies:\t\t\tRp. {int(e_fruitysmoothies.get()) * 22000}\n\n')

        if e_cappuchinocoffe.get() != '0':
            textStruk.insert(END, f'cappuchino coffe:\t\t\tRp. {int(e_cappuchinocoffe.get()) * 20000}\n\n')

        if e_softdrink.get() != '0':
            textStruk.insert(END, f'softdrink:\t\t\tRp. {int(e_softdrink.get()) * 15000}\n\n')

        if e_onionring.get() != '0':
            textStruk.insert(END, f'onionring:\t\t\tRp. {int(e_onionring.get()) * 18000}\n\n')

        if e_frenchfries.get() != '0':
            textStruk.insert(END, f'frenchfries:\t\t\tRp. {int(e_frenchfries.get()) * 36000}\n\n')

        if e_friedicecream.get() != '0':
            textStruk.insert(END, f'fried ice cream:\t\t\tRp. {int(e_friedicecream.get()) * 15000}\n\n')

        if e_cheesecake.get() != '0':
            textStruk.insert(END, f'cheese cake:\t\t\tRp. {int(e_cheesecake.get()) * 1500}\n\n')

        if e_icecream.get() != '0':
            textStruk.insert(END, f'icecream:\t\t\tRp. {int(e_icecream.get()) * 16000}\n\n')

        if e_donuts.get() != '0':
            textStruk.insert(END, f'donuts:\t\t\tRp. {int(e_donuts.get()) * 21000}\n\n')

        if e_chococupcake.get() != '0':
            textStruk.insert(END, f'choco cupcake:\t\t\tRp. {int(e_chococupcake.get()) * 23000}\n\n')

        if e_saladbuah.get() != '0':
            textStruk.insert(END, f'saladbuah:\t\t\tRp. {int(e_saladbuah.get()) * 18000}\n\n')

        if e_pudding.get() != '0':
            textStruk.insert(END, f'pudding:\t\t\tRp. {int(e_pudding.get()) * 10000}\n\n')

        textStruk.insert(END,'******************\n')
        if hargadaribrunchvar.get()!='Rp 0':
            textStruk.insert(END,f'Harga dari makanan\t\t\tRp. {hargadaribrunch}\n\n')
        if hargadariminumanvar.get() != 'Rp 0':
            textStruk.insert(END,f'Harga dari minuman\t\t\tRp. {hargadariminuman}\n\n')
        if hargadaridessertvar.get() != 'Rp 0':
            textStruk.insert(END,f'Harga dari jajanan\t\t\tRp. {hargadaridessert}\n\n')

        textStruk.insert(END, f'Sub Total\t\t\tRp. {subtotalItems}\n\n')
        textStruk.insert(END, f'Service Tax\t\t\tRp. {totaltax}\n\n')
        textStruk.insert(END, f'Harga total\t\t\tRP. {subtotalItems+totaltax}\n\n')
        textStruk.insert(END,'******************\n')

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# batas fungsi cetak struk

# awal fungsi simpan dalam perangkat
def save():
    if textStruk.get(1.0,END)=='\n':
        pass
    else:
        # HANYA DALAM EXTENSION FILE .txt
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt') 
        if url==None:
            pass
        else:

            bill_data=textStruk.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Informasi','Struk Anda berhasil disimpan')
# Batas fungsi simpan dalam perangkat 

# awal fungsi reset
def reset():
    textStruk.delete(1.0,END)
    e_pancake.set('0')
    e_croissant.set('0')
    e_waffle.set('0')
    e_cinnamonroll.set('0')
    e_burger.set('0')
    e_omelets.set('0')
    e_quiche.set('0')
    e_avocadotoast.set('0')
    e_tomatosoup.set('0')

    e_applejuice.set('0')
    e_lemontea.set('0')
    e_milktea.set('0')
    e_espresso.set('0')
    e_vanillalatte.set('0')
    e_airmineral.set('0')
    e_fruitysmoothies.set('0')
    e_cappuchinocoffe.set('0')
    e_softdrink.set('0')

    e_onionring.set('0')
    e_frenchfries.set('0')
    e_friedicecream.set('0')
    e_cheesecake.set('0')
    e_icecream.set('0')
    e_donuts.set('0')
    e_chococupcake.set('0')
    e_saladbuah.set('0')
    e_pudding.set('0')
    # batas untuk variables

    textpancake.config(state=DISABLED)
    textcroissant.config(state=DISABLED)
    textwaffle.config(state=DISABLED)
    textcinnamonroll.config(state=DISABLED)
    textburger.config(state=DISABLED)
    textomelets.config(state=DISABLED)
    textquiche.config(state=DISABLED)
    textavocadotoast.config(state=DISABLED)
    texttomatosoup.config(state=DISABLED)

    textapplejuice.config(state=DISABLED)
    textlemontea.config(state=DISABLED)
    textmilktea.config(state=DISABLED)
    textespresso.config(state=DISABLED)
    textvanillalatte.config(state=DISABLED)
    textairmineral.config(state=DISABLED)
    textfruitysmoothies.config(state=DISABLED)
    textcappuchinocoffe.config(state=DISABLED)
    textsoftdrink.config(state=DISABLED)

    textonionring.config(state=DISABLED)
    textfrenchfries.config(state=DISABLED)
    textfriedicecream.config(state=DISABLED)
    textcheesecake.config(state=DISABLED)
    texticecream.config(state=DISABLED)
    textdonuts.config(state=DISABLED)
    textchococupcake.config(state=DISABLED)
    textsaladbuah.config(state=DISABLED)
    textpudding.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    hargadariminumanvar.set('')
    hargadaribrunchvar.set('')
    hargadaridessertvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    taxvaluevar.set('')

# batas fungsi reset

# mengaktifkan fungsi entry menu makanan
def pancake():
    if var1.get()==1:
        textpancake.config(state=NORMAL)
        textpancake.delete(0,END)
        textpancake.focus()
    else:
        textpancake.config(state=DISABLED)
        e_pancake.set('0')

def croissant():
    if var2.get()==1:
        textcroissant.config(state=NORMAL)
        textcroissant.delete(0,END)
        textcroissant.focus()
    else:
        textcroissant.config(state=DISABLED)
        e_croissant.set('0')

def waffle():
    if var3.get()==1:
        textwaffle.config(state=NORMAL)
        textwaffle.delete(0,END)
        textwaffle.focus()
    else:
        textwaffle.config(state=DISABLED)
        e_waffle.set('0')

def cinnamonroll():
    if var4.get()==1:
        textcinnamonroll.config(state=NORMAL)
        textcinnamonroll.delete(0,END)
        textcinnamonroll.focus()

    else:
        textcinnamonroll.config(state=DISABLED)
        e_cinnamonroll.set('0')

def burger ():
    if var5.get()==1:
        textburger.config(state=NORMAL)
        textburger.delete(0,END)
        textburger.focus()
    else:
        textburger.config(state=DISABLED)
        e_burger.set('0')

def omelets():
    if var6.get()==1:
        textomelets.config(state=NORMAL)
        textomelets.delete(0,END)
        textomelets.focus()
    else:
        textomelets.config(state=DISABLED)
        e_omelets.set('0')

def quiche():
    if var7.get()==1:
        textquiche.config(state=NORMAL)
        textquiche.delete(0,END)
        textquiche.focus()
    else:
        textquiche.config(state=DISABLED)
        e_quiche.set('0')

def avocadotoast():
    if var8.get()==1:
        textavocadotoast.config(state=NORMAL)
        textavocadotoast.delete(0,END)
        textavocadotoast.focus()
    else:
        textavocadotoast.config(state=DISABLED)
        e_avocadotoast.set('0')

def tomatosoup():
    if var9.get()==1:
        texttomatosoup.config(state=NORMAL)
        texttomatosoup.delete(0,END)
        texttomatosoup.focus()
    else:
        texttomatosoup.config(state=DISABLED)
        e_tomatosoup.set('0')
# batas mengaktifkan entry menu makanan

# mengaktifkan entry menu minuman
def applejuice():
    if var10.get()==1:
        textapplejuice.config(state=NORMAL)
        textapplejuice.delete(0,END)
        textapplejuice.focus()
    else:
        textapplejuice.config(state=DISABLED)
        e_applejuice.set('0')

def lemontea():
    if var11.get()==1:
        textlemontea.config(state=NORMAL)
        textlemontea.focus()
        textlemontea.delete(0, END)
    else:
        textlemontea.config(state=DISABLED)
        e_lemontea.set('0')

def milktea():
    if var12.get()==1:
        textmilktea.config(state=NORMAL)
        textmilktea.delete(0,END)
        textmilktea.focus()
    else:
        textmilktea.config(state=DISABLED)
        e_milktea.set('0')

def espresso():
    if var13.get()==1:
        textespresso.config(state=NORMAL)
        textespresso.delete(0,END)
        textespresso.focus()
    else:
        textespresso.config(state=DISABLED)
        e_espresso.set('0')

def vanillalatte():
    if var14.get()==1:
        textvanillalatte.config(state=NORMAL)
        textvanillalatte.delete(0,END)
        textvanillalatte.focus()
    else:
        textvanillalatte.config(state=DISABLED)
        e_vanillalatte.set('0')

def airmineral():
    if var15.get()==1:
        textairmineral.config(state=NORMAL)
        textairmineral.delete(0,END)
        textairmineral.focus()
    else:
        textairmineral.config(state=DISABLED)
        e_airmineral.set('0')

def fruitysmoothies():
    if var16.get()==1:
        textfruitysmoothies.config(state=NORMAL)
        textfruitysmoothies.delete(0,END)
        textfruitysmoothies.focus()
    else:
        textfruitysmoothies.config(state=DISABLED)
        e_fruitysmoothies.set('0')

def cappuchinocoffe():
    if var17.get()==1:
        textcappuchinocoffe.config(state=NORMAL)
        textcappuchinocoffe.delete(0,END)
        textcappuchinocoffe.focus()
    else:
        textcappuchinocoffe.config(state=DISABLED)
        e_cappuchinocoffe.set('0')

def softdrink(): 
    if var18.get()==1:
        textsoftdrink.config(state=NORMAL)
        textsoftdrink.delete(0,END)
        textsoftdrink.focus()
    else:
        textsoftdrink.config(state=DISABLED)
        e_softdrink.set('0')
# batas mengaktifkan entry minuman

# mengaktifkan entry menu jajanan
def onionring():
    if var19.get()==1:
        textonionring.config(state=NORMAL)
        textonionring.focus()
        textonionring.delete(0,END)
    else:
        textonionring.config(state=DISABLED)
        e_onionring.set('0')

def frenchfries():
    if var20.get()==1:
        textfrenchfries.config(state=NORMAL)
        textfrenchfries.delete(0,END)
        textfrenchfries.focus()
    else:
        textfrenchfries.config(state=DISABLED)
        e_frenchfries.set('0')

def friedicecream():
    if var21.get()==1:
        textfriedicecream.config(state=NORMAL)
        textfriedicecream.delete(0,END)
        textfriedicecream.focus()
    else:
        textfriedicecream.config(state=DISABLED)
        e_friedicecream.set('0')

def cheesecake():
    if var22.get()==1:
        textcheesecake.config(state=NORMAL)
        textcheesecake.delete(0,END)
        textcheesecake.focus()
    else:
        textcheesecake.config(state=DISABLED)
        e_cheesecake.set('0')

def icecream():
    if var23.get()==1:
        texticecream.config(state=NORMAL)
        texticecream.delete(0,END)
        texticecream.focus()
    else:
        texticecream.config(state=DISABLED)
        e_icecream.set('0')

def donuts():
    if var24.get()==1:
        textdonuts.config(state=NORMAL)
        textdonuts.delete(0,END)
        textdonuts.focus()
    else:
        textdonuts.config(state=DISABLED)
        e_donuts.set('0')

def chococupcake():
    if var25.get()==1:
        textchococupcake.config(state=NORMAL)
        textchococupcake.delete(0,END)
        textchococupcake.focus()
    else:
        textchococupcake.config(state=DISABLED)
        e_chococupcake.set('0')

def saladbuah():
    if var26.get()==1:
        textsaladbuah.config(state=NORMAL)
        textsaladbuah.delete(0,END)
        textsaladbuah.focus()
    else:
        textsaladbuah.config(state=DISABLED)
        e_saladbuah.set('0')

def pudding():
    if var27.get()==1:
        textpudding.config(state=NORMAL)
        textpudding.delete(0,END)
        textpudding.focus()
    else:
        textpudding.config(state=DISABLED)
        e_pudding.set('0')


# FRAME KIRI

# Membuat frame kiri untuk menu cafe
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
menuFrame.pack(side=LEFT)

hargaFrame=Frame(menuFrame,bd=9,relief=RIDGE,bg='#050206',pady=12)
hargaFrame.pack(side=BOTTOM)

brunchFrame=LabelFrame(menuFrame,text=' Brunch ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
brunchFrame.pack(side=LEFT)

minumanFrame=LabelFrame(menuFrame,text=' Minuman ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
minumanFrame.pack(side=LEFT)

dessertFrame=LabelFrame(menuFrame,text=' Dessert ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
dessertFrame.pack(side=LEFT)
# batas frame kiri (menu cafe)


# membuat tampilan daftar menu makanan
pancake=Checkbutton(brunchFrame,text=' Pancake ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var1,
                        command=pancake, bg='#f6f6f6')
pancake.grid(row=0,column=0,sticky=W)

croissant=Checkbutton(brunchFrame,text=' Croissant ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var2,
                        command=croissant, bg='#f6f6f6')
croissant.grid(row=1,column=0,sticky=W)

waffle=Checkbutton(brunchFrame,text=' Waffle ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var3,
                        command=waffle, bg='#f6f6f6')
waffle.grid(row=2,column=0,sticky=W)

cinnamonroll=Checkbutton(brunchFrame,text=' Cinnamonroll ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var4,
                        command=cinnamonroll, bg='#f6f6f6')
cinnamonroll.grid(row=3,column=0,sticky=W)

burger=Checkbutton(brunchFrame,text=' Burger ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var5,
                        command=burger, bg='#f6f6f6')
burger.grid(row=4,column=0,sticky=W)

omelets=Checkbutton(brunchFrame,text= ' Omelets ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var6,
                        command=omelets, bg='#f6f6f6')
omelets.grid(row=5,column=0,sticky=W)

quiche=Checkbutton(brunchFrame,text=' Quiche ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var7,
                        command=quiche, bg='#f6f6f6')
quiche.grid(row=6,column=0,sticky=W)

avocadotoast=Checkbutton(brunchFrame,text=' Avocado Toast',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var8,
                        command=avocadotoast, bg='#f6f6f6')
avocadotoast.grid(row=7,column=0,sticky=W)

tomatosoup=Checkbutton(brunchFrame,text=' Tomato Soup ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var9,
                        command=tomatosoup, bg='#f6f6f6')
tomatosoup.grid(row=8,column=0,sticky=W)


# menambahkan fields entri untuk item brunch
textpancake=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_pancake)
textpancake.grid(row=0,column=1)

textcroissant=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_croissant)
textcroissant.grid(row=1,column=1)

textwaffle=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_waffle)
textwaffle.grid(row=2,column=1)

textcinnamonroll=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_cinnamonroll)
textcinnamonroll.grid(row=3,column=1)

textburger=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_burger)
textburger.grid(row=4,column=1)

textomelets=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7, width=8,state=DISABLED,textvar=e_omelets)
textomelets.grid(row=5,column=1)

textquiche=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_quiche)
textquiche.grid(row=6,column=1)

textavocadotoast=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_avocadotoast)
textavocadotoast.grid(row=7,column=1)

texttomatosoup=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_tomatosoup)
texttomatosoup.grid(row=8,column=1)


# membuat tampilan daftar menu minuman
applejuice=Checkbutton(minumanFrame,text='Apple Juice',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var10,
                        command=applejuice, bg='#f6f6f6')
applejuice.grid(row=0,column=0,sticky=W)

lemontea=Checkbutton(minumanFrame,text='Lemon Tea',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var11,
                        command=lemontea, bg='#f6f6f6')
lemontea.grid(row=1,column=0,sticky=W)

milktea=Checkbutton(minumanFrame,text='Milk Tea',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var12,
                        command=milktea, bg='#f6f6f6')
milktea.grid(row=2,column=0,sticky=W)

espresso=Checkbutton(minumanFrame,text='Espresso',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var13,
                        command=espresso, bg='#f6f6f6')
espresso.grid(row=3,column=0,sticky=W)

vanillalatte=Checkbutton(minumanFrame,text='Vanilla Latte',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var14,
                        command=vanillalatte, bg='#f6f6f6')
vanillalatte.grid(row=4,column=0,sticky=W)

airmineral=Checkbutton(minumanFrame,text='Air Mineral',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var15,
                        command=airmineral, bg='#f6f6f6')
airmineral.grid(row=5,column=0,sticky=W)

fruitysmoothies=Checkbutton(minumanFrame,text='Fruity Smoothies',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var16,
                        command=fruitysmoothies, bg='#f6f6f6')
fruitysmoothies.grid(row=6,column=0,sticky=W)

cappuchinocoffe=Checkbutton(minumanFrame,text='Cappuchino Coffe',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var17,
                        command=cappuchinocoffe, bg='#f6f6f6')
cappuchinocoffe.grid(row=7,column=0,sticky=W)

softdrink=Checkbutton(minumanFrame,text='Soft Drink',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var18,
                        command=softdrink, bg='#f6f6f6')
softdrink.grid(row=8,column=0,sticky=W)


# menambahkan fields entri untuk item minuman
textapplejuice=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_applejuice)
textapplejuice.grid(row=0,column=1)

textlemontea=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_lemontea)
textlemontea.grid(row=1,column=1)

textmilktea=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_milktea)
textmilktea.grid(row=2,column=1)

textespresso=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_espresso)
textespresso.grid(row=3,column=1)

textvanillalatte=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_vanillalatte)
textvanillalatte.grid(row=4,column=1)

textairmineral=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_airmineral)
textairmineral.grid(row=5,column=1)

textfruitysmoothies=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_fruitysmoothies)
textfruitysmoothies.grid(row=6,column=1)

textcappuchinocoffe=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_cappuchinocoffe)
textcappuchinocoffe.grid(row=7,column=1)

textsoftdrink=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_softdrink)
textsoftdrink.grid(row=8,column=1)


# membuat tampilan daftar menu dessert
onionring=Checkbutton(dessertFrame,text='Onion Ring',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var19,
            command=onionring, bg='#f6f6f6')
onionring.grid(row=0,column=0,sticky=W)

frenchfries=Checkbutton(dessertFrame,text='French Fries',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var20,
            command=frenchfries, bg='#f6f6f6')  
frenchfries.grid(row=1,column=0,sticky=W)

friedicecream=Checkbutton(dessertFrame,text='Fried Ice Cream',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var21,
            command=friedicecream, bg='#f6f6f6')
friedicecream.grid(row=2,column=0,sticky=W)

cheesecake=Checkbutton(dessertFrame,text='Cheese Cake',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var22,
            command=cheesecake, bg='#f6f6f6')
cheesecake.grid(row=3,column=0,sticky=W)

icecream=Checkbutton(dessertFrame,text='Ice Cream',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var23,
            command=icecream, bg='#f6f6f6')
icecream.grid(row=4,column=0,sticky=W)

donuts=Checkbutton(dessertFrame,text='Donuts',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var24,
            command=donuts, bg='#f6f6f6')
donuts.grid(row=5,column=0,sticky=W)

chococupcake=Checkbutton(dessertFrame,text='Choco Cupcake',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var25,
            command=chococupcake, bg='#f6f6f6')
chococupcake.grid(row=6,column=0,sticky=W)

saladbuah=Checkbutton(dessertFrame,text='Salad Buah',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var26,
            command=saladbuah, bg='#f6f6f6')
saladbuah.grid(row=7,column=0,sticky=W)

pudding=Checkbutton(dessertFrame,text='Pudding',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var27,
            command=pudding, bg='#f6f6f6')
pudding.grid(row=8,column=0,sticky=W)


# menambahkan fields entri untuk item dessert
textonionring = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_onionring)
textonionring.grid(row=0, column=1)

textfrenchfries = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_frenchfries)
textfrenchfries.grid(row=1, column=1)

textfriedicecream = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_friedicecream)
textfriedicecream.grid(row=2, column=1)

textcheesecake = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_cheesecake)
textcheesecake.grid(row=3, column=1)

texticecream = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_icecream)
texticecream.grid(row=4, column=1)

textdonuts = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_donuts)
textdonuts.grid(row=5, column=1)

textchococupcake = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_chococupcake)
textchococupcake.grid(row=6, column=1)

textsaladbuah = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvariable=e_saladbuah)
textsaladbuah.grid(row=7, column=1)

textpudding = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED,textvariable=e_pudding)
textpudding.grid(row=8, column=1)

# FRAME KANAN

# Membuat frame kanan untuk (Struk)
rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

strukFrame=Frame(rightFrame,bd=1,relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()
# Batas frame kanan (Struk)


# membuat label harga dan kolom entrinya
LabelHargadariBrunch=Label(hargaFrame,text='    HARGA DARI BRUNCH', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariBrunch.grid(row=0,column=0)

textHargadariBrunch=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadaribrunchvar)
textHargadariBrunch.grid(row=0,column=1,padx=41)

LabelHargadariMinuman=Label(hargaFrame,text='    HARGA DARI MINUMAN', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariMinuman.grid(row=1,column=0)

textHargadariMinuman=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariminumanvar)
textHargadariMinuman.grid(row=1,column=1,padx=41)

LabelHargadariDessert=Label(hargaFrame,text='  HARGA DARI DESSERT', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariDessert.grid(row=2,column=0)

textHargadariDessert=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadaridessertvar)
textHargadariDessert.grid(row=2,column=1,padx=41)

LabelSubTotal=Label(hargaFrame,text='SUB TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

LabelTax=Label(hargaFrame,text='Pajak'+' '+str(tax*100)+'%', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelTax.grid(row=1,column=2)

textTax=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=servicetaxvar)
textTax.grid(row=1,column=3,padx=41)

LabelHargaTotal=Label(hargaFrame,text='HARGA TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargaTotal.grid(row=2,column=2)

textHargaTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=totalcostvar)
textHargaTotal.grid(row=2,column=3,padx=41)


# Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
buttonTotal= Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonStruk= Button(buttonFrame,text='Struk',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=struk)
buttonStruk.grid(row=0,column=1)

buttonSimpan= Button(buttonFrame,text='Simpan',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=save)
buttonSimpan.grid(row=0,column=2)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='#fefefe',bg='red',bd=3,padx=12,
            command=reset)
buttonReset.grid(row=0,column=4)

# menentukan teks pada frame struk
textStruk=Text(strukFrame,font=('arial',12,'bold'),bd=3,width=36,height=26)
textStruk.grid(row=0,column=0)


root.mainloop()