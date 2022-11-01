import turtle
from random import randint
from tkinter import messagebox

#CONFIGURASI AWAL
ts = turtle.getscreen()
ts.bgcolor("green")
turtle.pencolor("black")
turtle.pensize(2)
turtle.colormode(255)
turtle.title("Candi Warna-Warni")
turtle.hideturtle()
turtle.speed('fastest') 

#INPUT 1
#Membuat input jumlah bata lapisan paling bawah dan memvalidasinya 
#agar nilainya selalu bilangan bulat positif dan nilainya tidak melebihi nilai max/min
check_input = False
while not check_input :
    MIN_LAPISAN_BAWAH = 1
    MAX_LAPISAN_BAWAH = 25

    lapisan_paling_bawah = turtle.textinput("Input","Jumlah batu bata pada lapisan paling bawah : ")
    if lapisan_paling_bawah.isnumeric():       
        if int(lapisan_paling_bawah) > MAX_LAPISAN_BAWAH :
            messagebox.showwarning("Too large",f"The allowed maximum value is {MAX_LAPISAN_BAWAH}.\nPlease try again.")
        elif int(lapisan_paling_bawah) < MIN_LAPISAN_BAWAH:
            messagebox.showwarning("Too small",f"The allowed minimum value is {MIN_LAPISAN_BAWAH}.\nPlease try again.")
        else:
            lapisan_paling_bawah = int(lapisan_paling_bawah)
            check_input = True
    else:
        messagebox.showwarning("Invalid Input","Input must be a positive integer")
        
#INPUT 2
#Membuat input jumlah bata lapisan atas dan memvalidasinya 
# agar nilainya selalu bilangan bulat positif dan tidak melebihi nilai max/min
check_input = False
while not check_input :
    MIN_LAPISAN_ATAS = 1
    max_lapisan_atas = lapisan_paling_bawah 

    lapisan_paling_atas = turtle.textinput("Input","Jumlah batu bata pada lapisan paling atas : ")
    if lapisan_paling_atas.isnumeric():
        if int(lapisan_paling_atas) > max_lapisan_atas :
            messagebox.showwarning("Too large",f"The allowed maximum value is {max_lapisan_atas}.\nPlease try again.")
        elif int(lapisan_paling_atas) < MIN_LAPISAN_ATAS:
            messagebox.showwarning("Too small",f"The allowed minimum value is {MIN_LAPISAN_ATAS}.\nPlease try again.")
        else:
            lapisan_paling_atas = int(lapisan_paling_atas)
            check_input = True
    else:
        messagebox.showwarning("Invalid Input","Input must be a positive integer")

#INPUT 3 
#Membuat input panjang satu bata dan memvalidasinya 
#agar nilainya berupa float dan tidak melebihi nilai max/min
check_input = False
while not check_input :
    MIN_PANJANG = 1
    MAX_PANJANG = 35

    panjang_bata = turtle.numinput("Input","Panjang satu buah batu bata (dalam pixel) : ",minval = MIN_PANJANG,maxval = MAX_PANJANG)
    if MIN_PANJANG <= panjang_bata <= MAX_PANJANG :
        check_input = True

#INPUT 4
#Membuat input lebar satu bata dan memvalidasinya
#agar nilainya berupa float dan tidak melebihi nilai max/min
check_input = False
while not check_input :
    MIN_LEBAR = 1
    MAX_LEBAR = 25

    lebar_bata = turtle.numinput("Input","Lebar satu buah batu bata (dalam pixel) : ",minval = MIN_LEBAR,maxval = MAX_LEBAR)
    if MIN_LEBAR <= lebar_bata <= MAX_LEBAR :
        check_input = True

#MENGGAMBAR CANDI

#Informasi titik mulai membangun candi
turtle.penup()
koordinat_x = -(panjang_bata * lapisan_paling_bawah / 2)
koordinat_y = -(lebar_bata * (lapisan_paling_bawah + 1 - lapisan_paling_atas) / 2)
koordinat_write = koordinat_y - 30
turtle.goto(koordinat_x,koordinat_y)

#Mengatur Dimensi Window yang ditampilkan
tinggi_window = int(lebar_bata * (lapisan_paling_bawah + 1 - lapisan_paling_atas) + 150)
lebar_window  = int(panjang_bata * lapisan_paling_bawah + 150)
MIN_TINGGI_WINDOW = 640
MIN_LEBAR_WINDOW  = 640

if lebar_window < MIN_LEBAR_WINDOW :
    lebar_window = MIN_LEBAR_WINDOW
if tinggi_window < MIN_TINGGI_WINDOW :
    tinggi_window = MIN_TINGGI_WINDOW
turtle.setup(width=lebar_window,height=tinggi_window,startx=None,starty=0)

#Proses menggambar candi dan menghitung jumlah bata
lapisan_bata_sekarang = lapisan_paling_bawah
jumlah_bata = 0

while lapisan_bata_sekarang >= lapisan_paling_atas:
    for i in range(lapisan_bata_sekarang):
        turtle.pendown()
        if lapisan_bata_sekarang == lapisan_paling_bawah or lapisan_bata_sekarang == lapisan_paling_atas or i == 0 or i == lapisan_bata_sekarang -1 :
            turtle.fillcolor("#BC4A3C")
        else :
            turtle.fillcolor(randint(0,255),randint(0,255),randint(0,255))
        turtle.begin_fill()
        turtle.forward(panjang_bata)
        turtle.left(90)
        turtle.forward(lebar_bata)
        turtle.left(90)
        turtle.forward(panjang_bata)
        turtle.left(90)
        turtle.forward(lebar_bata)
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(panjang_bata)
    
    jumlah_bata += lapisan_bata_sekarang
    lapisan_bata_sekarang -= 1
    koordinat_x += panjang_bata/2
    koordinat_y += lebar_bata
    turtle.goto(koordinat_x,koordinat_y)

#MENAMPILKAN JUMLAH BATA
turtle.goto(0,koordinat_write)
turtle.write(arg = f"Candi warna-warni dengan {jumlah_bata} bata",align= "center",font = ('Arial', 20, 'bold'))
turtle.exitonclick()