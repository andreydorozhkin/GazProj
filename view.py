import model
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.geometry('1300x800')
root["bg"]="white"
frame1 = Frame(root); frame1.place(x=-15, y=-15, width=700, height=650)
figure = plt.Figure(figsize=(5,5), facecolor='white', edgecolor="white")
canvas = FigureCanvasTkAgg(figure, frame1)
canvas.get_tk_widget().place(x=10,y=10,width=700,height=650)
ax = [figure.add_subplot(1,1,x+1)for x in range(1)]


#Визуальный метод определния материала
def changeMaterials():
   combo_exsample_gas_material["values"] = ["Сталь", "Полиэтилен"]

#Вывод ошибок
def message_info(message):
    messagebox.showinfo(message[0],message[1]) 
def message_ask(message):
    messagebox.askquestion(message[0],message[1])
def message_error(message):
    messagebox.showerror(message[0], message[1])

def generate_coordinat(a, b, c):
    coordinat=[]
    while c!=a:
        c+=1
        coordinat=coordinat+[b]
        b=b+25
    return coordinat

def generate_field(name_field, x_label, y_label, x_entry, y_entry):
    lab = Label(root, text=name_field, background="white")
    lab.place(x=x_label, y=y_label)
    text = Entry(root, width=20, background="white")
    text.place(x=x_entry, y=y_entry)
    return text

mass=generate_coordinat(30, 5, 0)
X1=710
X2=1150


cost_gas = generate_field("Стоимость газа", X1, mass[0], X2, mass[0])
cost_natur_liquided_gas = generate_field("Стоимость СПГ", X1, mass[1], X2, mass[1])
city_need_energy = generate_field("Потребность города в КВТ", X1, mass[2], X2, mass[2])
cost_cistern = generate_field("Стоимость автомобильной цистерны", X1, mass[3], X2, mass[3])
volume_cistern = generate_field("Объем автомобильной цистерны", X1, mass[4], X2, mass[4])
number_cistern = generate_field("Колличество цистерн ", X1, mass[5], X2, mass[5])
cost_tank = generate_field("Стоимость хранилища СПГ", X1, mass[6], X2, mass[6])
volume_tank = generate_field("Объем хранилища СПГ", X1, mass[7], X2, mass[7])
number_tank = generate_field("Колличество хранилищ )", X1, mass[8], X2, mass[8])
cost_gasifiers = generate_field("Стоимость газификаторов ", X1, mass[9], X2, mass[9])
cost_laying_high = generate_field("Стоимость прокладки газопровода высокого давления на километр", X1, mass[10], X2, mass[10])
cost_laying_medium= generate_field("Стоимость прокладки газопровода среднего давления на километр", X1, mass[11], X2, mass[11])
cost_GRPSH = generate_field("Стоимость ГРПШ", X1, mass[12], X2, mass[12])
efficiency_GRPSH = generate_field("Производительность ГРПШ", X1, mass[13], X2, mass[13])
cost_maintenance_GRPSH = generate_field("Стоимость обслуживания ГРПШ", X1, mass[14], X2, mass[14])
cost_maintenance_gas_pipeline = generate_field("Стоимость обслуживания газопровода", X1, mass[15], X2, mass[15])
factory_distance=generate_field("Расстояние от завода до города", X1, mass[16], X2, mass[16])
gas_material = Label(root, text="Материал газопровода", background="white") 
gas_material.place(x=X1,y=mass[17])

combo_exsample_gas_material = ttk.Combobox(root, 
                           values=["Сталь", "Полиэтилен"],
                           postcommand=changeMaterials, width=17)
combo_exsample_gas_material.place(x=X2, y=mass[17])



btplot1 = Button(root, text='Рассчитать',  # текст кнопки 
                 background="#72D0F2",     # фоновый цвет кнопки
                 foreground="black",     # цвет текста
                 padx="20",                # отступ от границ до содержимого по горизонтали
                 pady="8",                 # отступ от границ до содержимого по вертикали
                 font='Tahoma 20', command= lambda: model.do_plot())
btplot1.place(x=X1, y=mass[19], width=150, height=60)

btplot2 = Button(root, text='Очистить',  # текст кнопки 
                 background="#72D0F2",     # фоновый цвет кнопки
                 foreground="black",     # цвет текста
                 padx="20",                # отступ от границ до содержимого по горизонтали
                 pady="8",                 # отступ от границ до содержимого по вертикали
                 font='Tahoma 20', command= lambda: model.clear())
btplot2.place(x=X1, y=mass[22], width=150, height=60)

btplot3 = Button(root, text='Critical',  # текст кнопки 
                 background="#72D0F2",     # фоновый цвет кнопки
                 foreground="black",     # цвет текста
                 padx="20",                # отступ от границ до содержимого по горизонтали
                 pady="8",                 # отступ от границ до содержимого по вертикали
                 font='Tahoma 20' )#command = critical())
btplot3.place(x=X1, y=mass[25], width=150, height=60)


root.mainloop()
