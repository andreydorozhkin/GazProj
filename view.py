import model
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.geometry('1300x800')
frame1 = Frame(root); frame1.place(x=0, y=0, width=700, height=650)
figure = plt.Figure(figsize=(5,5), facecolor='white')
canvas = FigureCanvasTkAgg(figure, frame1)
canvas.get_tk_widget().place(x=10,y=10,width=700,height=650)
ax = [figure.add_subplot(1, 1, x+1) for x in range(1)]

#Визуальный метод определния материала
def changeMaterials():
    comboExample["values"] = [ "Сталь", "Аллюминий"]

a=30
b=5
c=0
mass=[]
while c!=a:
    c+=1
    mass=mass+[b]
    b=b+25
X1=710
X2=1150

lbl = Label(root, text="Начальное годовое энергопотребление объектом газификации. (МВт*ч)/год")  
lbl.place(x=X1,y=mass[0])
txt1 = Entry(root,width=20)  
txt1.place(x=X2,y=mass[0])

lbl1 = Label(root, text="Удельные затраты на комплекс сжижения газа. (руб./(МВ*ч)))")  
lbl1.place(x=X1,y=mass[1])  
txt2 = Entry(root,width=20)  
txt2.place(x=X2,y=mass[1])

lbl1 = Label(root, text="Начальное расстояние до населенного пункта. км")  
lbl1.place(x=X1,y=mass[2])  
txt3 = Entry(root,width=20)  
txt3.place(x=X2,y=mass[2])

lbl1 = Label(root, text="Число жителей в снабжаемом городе. тыс. чел.")  
lbl1.place(x=X1,y=mass[3])  
txt4 = Entry(root,width=20)  
txt4.place(x=X2,y=mass[3])

lbl1 = Label(root, text="Допустимые потери давления газопроводе, МПа")  
lbl1.place(x=X1,y=mass[4])  
txt5 = Entry(root,width=20)  
txt5.place(x=X2,y=mass[4])

lbl1 = Label(root, text="Материал газопровода")  
lbl1.place(x=X1,y=mass[5])
comboExample = ttk.Combobox(root, 
                            values=[],
                            postcommand=changeMaterials, width=17)
comboExample.place(x=X2, y=mass[5])


lbl1 = Label(root, text="Усредненное давление газа (абсолютное) в сети. МПф")  
lbl1.place(x=X1,y=mass[6])  
txt7 = Entry(root,width=20)  
txt7.place(x=X2,y=mass[6])

lbl1 = Label(root, text="Удельная стоимость газопровода руб/км")  
lbl1.place(x=X1,y=mass[7])  
txt8 = Entry(root,width=20)  
txt8.place(x=X2,y=mass[7])

lbl1 = Label(root, text="Стоимость ПГ. (руб/(МВт*ч))")  
lbl1.place(x=X1,y=mass[8])  
txt9 = Entry(root,width=20)  
txt9.place(x=X2,y=mass[8])

lbl1 = Label(root, text="Удельная ШГРП (руб/МВт*ч)")  
lbl1.place(x=X1,y=mass[9])  
txt10 = Entry(root,width=20)  
txt10.place(x=X2,y=mass[9])

lbl1 = Label(root, text="Стоимость обслуживания газопровода, (руб/км)/год")  
lbl1.place(x=X1,y=mass[10])  
txt11 = Entry(root,width=20)  
txt11.place(x=X2,y=mass[10])

lbl1 = Label(root, text="Стоимость обслуживания ШГРП (руб/МВт*ч)")  
lbl1.place(x=X1,y=mass[11])  
txt12 = Entry(root,width=20)  
txt12.place(x=X2,y=mass[11])

lbl1 = Label(root, text="Цена цистерны СПГ, руб")  
lbl1.place(x=X1,y=mass[12])  
txt13 = Entry(root,width=20)  
txt13.place(x=X2,y=mass[12])

lbl1 = Label(root, text="Объем цистерны СПГ, м3")  
lbl1.place(x=X1,y=mass[13])  
txt14 = Entry(root,width=20)  
txt14.place(x=X2,y=mass[13])

lbl1 = Label(root, text="Средняя скорость цистерны СПГ, км/ч")  
lbl1.place(x=X1,y=mass[14])  
txt15 = Entry(root,width=20)  
txt15.place(x=X2,y=mass[14])

lbl1 = Label(root, text="Цена резервуара СПГ, руб")  
lbl1.place(x=X1,y=mass[15])  
txt16 = Entry(root,width=20)  
txt16.place(x=X2,y=mass[15])

lbl1 = Label(root, text="Объем резервуара СПГ, м3")  
lbl1.place(x=X1,y=mass[16])  
txt17 = Entry(root,width=20)  
txt17.place(x=X2,y=mass[16])

lbl1 = Label(root, text="Удельная стоимость газификатора, руб/МВт*ч")  
lbl1.place(x=X1,y=mass[17])  
txt18 = Entry(root,width=20)  
txt18.place(x=X2,y=mass[17])

lbl1 = Label(root, text="Стоимость СПГ, руб/ВТ*ч")  
lbl1.place(x=X1,y=mass[18])  
txt19 = Entry(root,width=20)  
txt19.place(x=X2,y=mass[18])

lbl1 = Label(root, text="Удельные затраты на обслуживание объекта по сжижению газа, руб/МВт*ч")  
lbl1.place(x=X1,y=mass[19])  
txt20 = Entry(root,width=20)  
txt20.place(x=X2,y=mass[19])

lbl1 = Label(root, text="Стоимость годового обслуживания цистерны СПГ, руб")  
lbl1.place(x=X1,y=mass[20])  
txt21 = Entry(root,width=20)  
txt21.place(x=X2,y=mass[20])

lbl1 = Label(root, text="Стоимость годового обслуживания резервуара СПГ, руб")  
lbl1.place(x=X1,y=mass[21])  
txt22 = Entry(root,width=20)  
txt22.place(x=X2,y=mass[21])

lbl1 = Label(root, text="Срок службы оборудования ПГ, лет")  
lbl1.place(x=X1,y=mass[22])  
txt23 = Entry(root,width=20)  
txt23.place(x=X2,y=mass[22])

lbl1 = Label(root, text="Срок перехода с СПГ на ПГ, лет")  
lbl1.place(x=X1,y=mass[23])  
txt24 = Entry(root,width=20)  
txt24.place(x=X2,y=mass[23])

lbl1 = Label(root, text="Стоимость демонтажа резервуара СПГ, руб")  
lbl1.place(x=X1,y=mass[24])  
txt25 = Entry(root,width=20)  
txt25.place(x=X2,y=mass[24])

lbl1 = Label(root, text="Коэффициент дисконтирования 1/год")  
lbl1.place(x=X1,y=mass[25])  
txt26 = Entry(root,width=20)  
txt26.place(x=X2,y=mass[25])

lbl1 = Label(root, text="Шаг увеличения энергопотребления, МВт")  
lbl1.place(x=X1,y=mass[26])  
txt27 = Entry(root,width=20)  
txt27.place(x=X2,y=mass[26])

def message_info():
    messagebox.showinfo("Result","Результат в консоли = "+box_result) 
def message_ask():
    messagebox.askquestion("Request!","Нет ошибки, график отрисован?")
def message_error1():
    messagebox.messagebox.showerror("Error","AMOGUS, кто то ввел не число")
def message_error2():
    messagebox.messagebox.showwarning("Error","Где-то ошибка")

btplot1 = Button(root, text='Рассчитать',  # текст кнопки 
                 background="#7F7F7F",     # фоновый цвет кнопки
                 foreground="#F2F2F2",     # цвет текста
                 padx="20",                # отступ от границ до содержимого по горизонтали
                 pady="8",                 # отступ от границ до содержимого по вертикали
                 font="16", command= lambda: model.do_plot())
btplot1.place(x=430, y=650, width=100, height=40)

btplot2=Button(root, text="Сумма первых 2ух полей в бокс",
               background="#7F7F7F",     # фоновый цвет кнопки
                 foreground="#F2F2F2",   # цвет текста
                 padx="20",              # отступ от границ до содержимого по горизонтали
                 pady="8",               # отступ от границ до содержимого по вертикали
                 font="16", command=model.sum)
btplot2.place(x=1, y=650, width=400, height=40)


root.mainloop()
