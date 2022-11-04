from tkinter import *
from back import *


def Btn_table():
    window2 = Tk()

    getarrI = ent_arrayI.get()
    arrayIstr = getarrI.split(', ')
    arrayIint = [int(i) for i in arrayIstr]
    getarrK = ent_arrayK.get()
    arrayKstr = getarrK.split(', ')

    for i in range(0, len(arrayIint)):
        for j in range(5):
            if i == 0 and j == 0:
                Label(window2, text='I').grid(row=i, column=0, padx=20)
                Label(window2, text='K').grid(row=i, column=1, padx=20)
                Label(window2, text='Eht').grid(row=i, column=2, padx=20)
                Label(window2, text='EHT').grid(row=i, column=3, padx=20)
                Label(window2, text='delt').grid(row=i, column=4, padx=20)
            if i != 0:
                if j == 0:
                    Label(window2, text=arrayIstr[i - 1]).grid(row=i, column=j)
                if j == 1:
                    Label(window2, text=arrayKstr[i - 1]).grid(row=i, column=j)
                if j == 2:
                    Label(window2, text=("%.5f" % a[i - 1])).grid(row=i, column=j)
                if j == 3:
                    Label(window2, text=("%.5f" % b[i - 1])).grid(row=i, column=j)
                if j == 4:
                    Label(window2, text=("%.5f" % eps_x[i - 1])).grid(row=i, column=j)


def Btn_start():
    getarrI = ent_arrayI.get()
    arrayIstr = getarrI.split(', ')
    arrayIint = [int(i) for i in arrayIstr]

    getarrK = ent_arrayK.get()
    arrayKstr = getarrK.split(', ')
    arrayKint = [int(i) for i in arrayKstr]

    getvalK = ent_valK.get()
    valKstr = getvalK.split(', ')
    valKint = [int(i) for i in valKstr]

    getvalI = ent_valI.get()
    valIstr = getvalI.split(', ')
    valIint = [float(i) for i in valIstr]

    if chk_stateD.get() == 1:
        dynamic(chk_stateEl.get(), chk_stateKy.get())

    if chk_stateC.get() == 1:
        convergence(arrayIint, arrayKint, valIint[0], valKint[0], chk_stateEl.get(), chk_stateKy.get())


window1 = Tk()
window1.geometry('740x200')

lbl_arrayI = Label(window1, text="Массив значений i :")
lbl_arrayI.grid(row=0, column=0, pady=10)

ent_arrayI = Entry(window1)
ent_arrayI.grid(row=0, column=1)
ent_arrayI.insert(0, '5, 20, 80, 320')

lbl_arrayK = Label(window1, text="Массив значений k :")
lbl_arrayK.grid(row=1, column=0, pady=10)

ent_arrayK = Entry(window1)
ent_arrayK.grid(row=1, column=1)
ent_arrayK.insert(0, '300, 1200, 4800, 19200')

lbl_valI = Label(window1, text="Коэффициент x(x*pi*R) :")
lbl_valI.grid(row=3, column=0, pady=10)

ent_valI = Entry(window1)
ent_valI.grid(row=3, column=1)
ent_valI.insert(0, '0.25')

lbl_valK = Label(window1, text="Значение t :")
lbl_valK.grid(row=4, column=0, pady=10)

ent_valK = Entry(window1)
ent_valK.grid(row=4, column=1)
ent_valK.insert(0, '70')

lbl_option = Label(window1, text="Выбор опций :")
lbl_option.grid(row=0, column=2, pady=10, padx=20)

chk_stateD = IntVar()
chk_dynamic = Checkbutton(text="динамика числинного решения", variable=chk_stateD)
chk_dynamic.grid(row=0, column=3, padx=10)

chk_stateC = IntVar()
chk_conv = Checkbutton(text="сходимость", variable=chk_stateC)
chk_conv.grid(row=0, column=4)

chk_stateEl = IntVar()
chk_dynamic = Checkbutton(text="Елисеев", variable=chk_stateEl)
chk_dynamic.grid(row=1, column=3, padx=10)

chk_stateKy = IntVar()
chk_conv = Checkbutton(text="Курицын", variable=chk_stateKy)
chk_conv.grid(row=1, column=4)

btn = Button(window1, text='Start', command=Btn_start)
btn.grid(row=6, column=3)
btn_table = Button(window1, text='table', command=Btn_table)
btn_table.grid(row=6, column=4)
window1.mainloop()
