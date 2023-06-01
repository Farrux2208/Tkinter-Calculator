from tkinter import *

# 1 - bosqich

# root = Tk()

# root["bg"] = "black"

# mylabel = Label(root, text="Salom tkinter")
# mylabel2 = Label(root, text="Salom python")
# mylabel.pack()
# mylabel2.pack()





# root.mainloop()


#=======================================================================

##  2-bosqich
# root = Tk()

# # root["bg"] = "black"

# mylabel = Label(root, text="Salom tkinter")
# mylabel2 = Label(root, text="Salom python")
# mylabel3 = Label(root, text="Salom salom")

# mylabel.grid(row=0, column=0)
# mylabel2.grid(row=1, column=1)
# mylabel3.grid(row=2, column=2)


# root.mainloop()


#===============================================================
#  3-bosqich

# root = Tk()

# def mini_kinopka():
# 	chiqadigan_soz = Label(root, text="meni bekor bosding")
# 	chiqadigan_soz.pack()

# mybutton = Button(root, command=mini_kinopka, text="Submit", bg="gray", fg="white", padx=20, pady=15)
# mybutton.pack()


# root.mainloop()

#==============================================================
# 4-bossqich

# root = Tk()

# input1 = Entry(root, bg="black", fg="green", width=150, borderwidth=20)
# input1.pack()

# def meni_kinopkam():
# 	chiqadigan_soz = Label(root, text=input1.get())# text = input1.git()
# 	chiqadigan_soz.pack()
# mybutton = Button(root, text="Submit", command=meni_kinopkam)
# mybutton.pack()
# root.mainloop()

#--------------------------------------

# 4-bosqqich 2-qism


# root =Tk()
# root.title("Kalkulator")

# input1 = Entry(root, width=45, borderwidth=5)
# input1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# button1 = Button(root, text="1", padx=40, pady=20)
# button2 = Button(root, text="2", padx=40, pady=20)
# button3 = Button(root, text="3", padx=40, pady=20)
# button4 = Button(root, text="4", padx=40, pady=20)
# button5 = Button(root, text="5", padx=40, pady=20)
# button6 = Button(root, text="6", padx=40, pady=20)
# button7 = Button(root, text="7", padx=40, pady=20)
# button8 = Button(root, text="8", padx=40, pady=20)
# button9 = Button(root, text="9", padx=40, pady=20)
# button_add = Button(root, text="+", padx=39, pady=20)
# button_equal = Button(root, text="=", padx=91, pady=20)

# button1.grid(row=3, column=0)
# button2.grid(row=3, column=1)
# button3.grid(row=3, column=2)
# button4.grid(row=4, column=0)
# button5.grid(row=4, column=1)
# button6.grid(row=4, column=2)
# button7.grid(row=5, column=0)
# button8.grid(row=5, column=1)
# button9.grid(row=5, column=2)
# button_add.grid(row=6, column=0)
# button_equal.grid(row=6, column=1, columnspan=2)


################################################################
# 5-bosqich

root = Tk()
root.title("Kalkulator")

input1 = Entry(root, width=45, borderwidth=5)
input1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
	string = input1.get()
	input1.delete(0, END)
	input1.insert(0, str(string)+str(number))


def button_clear():
	input1.delete(0, END)



def button_add():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal = "qushish"
	saqlangan_raqam = int(raqamni_olish)
	input1.delete(0, END)

def ayiruv():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal = "ayirish"
	saqlangan_raqam = int(raqamni_olish)
	input1.delete(0, END)

def button_tenglik():
	summa = input1.get()
	input1.delete(0, END)
	if amal == "qushish":
		input1.insert(0,saqlangan_raqam + int(summa))
	if amal == "ayirish":
		input1.insert(0,saqlangan_raqam - int(summa))



button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))


button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_tenglik)
button_clear = Button(root, text="clear", padx=83, pady=20, command=button_clear)
button_minus = Button(root, text="-", padx=140, pady=20, command=ayiruv)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_minus.grid(row=6,  columnspan=3)



root.mainloop()




































root.mainloop()











