from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.geometry('1300x800')
frame = Frame(root)
frame.pack()

def do_plot(x, y):
    [ax[x].clear() for x in range(1)]
    ax[0].plot(x,y)
    canvas.draw()

frame1 = Frame(root); frame1.place(x=0, y=0, width=700, height=650)
figure = plt.Figure(figsize=(5,5), facecolor='yellow')
canvas = FigureCanvasTkAgg(figure, frame1)
canvas.get_tk_widget().place(x=10,y=10,width=700,height=650)
ax = [figure.add_subplot(1, 1, x+1) for x in range(1)]

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
print(mass)
lbl = Label(root, text="Начальное годовое энергопотребление объектом газификации. (МВт*ч)/год")
lbl.place(x=X1,y=mass[0])
txt = Entry(root,width=20)
txt.place(x=X2,y=mass[0])

lbl1 = Label(root, text="Удельные затраты на комплекс сжижения газа. (руб./(МВ*ч)))")
lbl1.place(x=X1,y=mass[1])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[1])

lbl1 = Label(root, text="Начальное расстояние до населенного пункта. км")
lbl1.place(x=X1,y=mass[2])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[2])

lbl1 = Label(root, text="Число жителей в снабжаемом городе. тыс. чел.")
lbl1.place(x=X1,y=mass[3])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[3])

lbl1 = Label(root, text="Допустимые потери давления газопроводе, МПа")
lbl1.place(x=X1,y=mass[4])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[4])

lbl1 = Label(root, text="Материал газопровода")
lbl1.place(x=X1,y=mass[5])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[5])

lbl1 = Label(root, text="Усредненное давление газа (абсолютное) в сети. МПф")
lbl1.place(x=X1,y=mass[6])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[6])

lbl1 = Label(root, text="Удельная стоимость газопровода руб/км")
lbl1.place(x=X1,y=mass[7])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[7])

lbl1 = Label(root, text="Стоимость ПГ. (руб/(МВт*ч))")
lbl1.place(x=X1,y=mass[8])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[8])

lbl1 = Label(root, text="Удельная ШГРП (руб/МВт*ч)")
lbl1.place(x=X1,y=mass[9])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[9])

lbl1 = Label(root, text="Стоимость обслуживания газопровода, (руб/км)/год")
lbl1.place(x=X1,y=mass[10])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[10])

lbl1 = Label(root, text="Стоимость обслуживания ШГРП (руб/МВт*ч)")
lbl1.place(x=X1,y=mass[11])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[11])

lbl1 = Label(root, text="Цена цистерны СПГ, руб")
lbl1.place(x=X1,y=mass[12])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[12])

lbl1 = Label(root, text="Объем цистерны СПГ, м3")
lbl1.place(x=X1,y=mass[13])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[13])

lbl1 = Label(root, text="Средняя скорость цистерны СПГ, км/ч")
lbl1.place(x=X1,y=mass[14])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[14])

lbl1 = Label(root, text="Цена резервуара СПГ, руб")
lbl1.place(x=X1,y=mass[15])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[15])

lbl1 = Label(root, text="Объем резервуара СПГ, м3")
lbl1.place(x=X1,y=mass[16])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[16])

lbl1 = Label(root, text="Удельная стоимость газификатора, руб/МВт*ч")
lbl1.place(x=X1,y=mass[17])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[17])

lbl1 = Label(root, text="Стоимость СПГ, руб/ВТ*ч")
lbl1.place(x=X1,y=mass[18])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[18])

lbl1 = Label(root, text="Удельные затраты на обслуживание объекта по сжижению газа, руб/МВт*ч")
lbl1.place(x=X1,y=mass[19])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[19])

lbl1 = Label(root, text="Стоимость годового обслуживания цистерны СПГ, руб")
lbl1.place(x=X1,y=mass[20])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[20])

lbl1 = Label(root, text="Стоимость годового обслуживания резервуара СПГ, руб")
lbl1.place(x=X1,y=mass[21])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[21])

lbl1 = Label(root, text="Срок службы оборудования ПГ, лет")
lbl1.place(x=X1,y=mass[22])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[22])

lbl1 = Label(root, text="Срок перехода с СПГ на ПГ, лет")
lbl1.place(x=X1,y=mass[23])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[23])

lbl1 = Label(root, text="Стоимость демонтажа резервуара СПГ, руб")
lbl1.place(x=X1,y=mass[24])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[24])

lbl1 = Label(root, text="Коэффициент дисконтирования 1/год")
lbl1.place(x=X1,y=mass[25])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[25])

lbl1 = Label(root, text="Шаг увеличения энергопотребления, МВт")
lbl1.place(x=X1,y=mass[26])
txt1 = Entry(root,width=20)
txt1.place(x=X2,y=mass[26])

btplot1 = Button(root, text='Построить 1', command= lambda: do_plot([0,1,2],[5,3,7]))
btplot1.place(x=100, y=670, width=70, height=20)
btplot2 = Button(root, text='Построить 2', command= lambda: do_plot([8,2,1],[4,9,3]))
btplot2.place(x=200, y=670, width=70, height=20)

# ax = [figure.add_subplot(2, 2, x+1) for x in range(4)]



root.mainloop()