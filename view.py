#Подключение необходимых библиотек

import model # подключение модуля
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.geometry('1300x650')
root.resizable(width=False, height=False) 
root.title("Main Screen")
root["bg"]="white"

figure1 = plt.Figure(figsize=(8,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax1.grid(True, linestyle='--')
ax1.minorticks_on()

#Визуальный метод определния материала
def changeMaterials():
   combo_exsample_gas_material["values"] = ["Сталь", "Полиэтилен"]

#Вывод ошибок в messagebox
def message_info(message):
    messagebox.showinfo("Внимание!",message) 
def message_ask(message):
    messagebox.askquestion("Внимание!",message)
def message_error(message):
    messagebox.showerror("Error!", message)

def generate_coordinat(a, b, c):
    coordinat=[]
    while c!=a:
        c+=1
        coordinat=coordinat+[b]
        b=b+25
    return coordinat

# Метод генерации текстовых и вводных полей
def generate_field(name_field, x_label, y_label, x_entry, y_entry):
    lab = Label(root, text=name_field, background="white")
    lab.place(x=x_label, y=y_label)
    text = Entry(root, width=20, background="white")
    text.place(x=x_entry, y=y_entry)
    return text

# Выборочные координаты
mass=generate_coordinat(30, 70, 0)
X1=775
X2=1110

#Создание полей
cost_gas = generate_field("Стоимость природного газа, руб/м3", X1, mass[0], X2, mass[0])
cost_natur_liquided_gas = generate_field("Стоимость сжиженного природного газа(СПГ), руб/МВт*ч", X1, mass[1], X2, mass[1])
lbl = Label(root, text="Годовой объем потребления, МВт", background="white")
lbl.place(x=X1,y=mass[2])
city_need_energy_begin = generate_field("от", 1090, mass[2], X2, mass[2])
city_need_energy_end = generate_field("до", 1090, mass[3], X2, mass[3])

cost_cistern = generate_field("Стоимость криогенной цистерны, руб", X1, mass[5], X2, mass[5])
volume_cistern = generate_field("Объем криогенной цистерны СПГ, м/куб", X1, mass[6], X2, mass[6])
cost_tank = generate_field("Стоимость хранилища СПГ, руб", X1, mass[8], X2, mass[8])
volume_tank = generate_field("Объем хранилища СПГ, м/куб", X1, mass[9], X2, mass[9])
cost_gasifiers = generate_field("Стоимость газификаторов СПГ, руб ", X1, mass[11], X2, mass[11])
factory_distance=generate_field("Расстояние от завода до города, км", X1, mass[12], X2, mass[12])
gas_material = Label(root, text="Материал газопровода", background="white") 
gas_material.place(x=X1,y=mass[13])

# Создание и размещение combobox-а
combo_exsample_gas_material = ttk.Combobox(root, 
                           values=["Сталь", "Полиэтилен"],
                           postcommand=changeMaterials, width=17)
combo_exsample_gas_material.place(x=X2, y=mass[13])
text_entry=Text(root, height=8, width=34)
text_entry.insert(1.0,"Колличество хранилищ = "+"\nКолличество цистерн = ")
#text_entry.insert(2.0,"Колличество цистерн = ")
text_entry.configure(state='disabled')
text_entry.place(x=900, y=mass[16])

# Создание кнопок
btplot1 = Button(root, text='Рассчитать',  # текст кнопки 
                 background="#60B9CE",     # фоновый цвет кнопки
                 foreground="black",     # цвет текста
                 padx="20",                # отступ от границ до содержимого по горизонтали
                 pady="8",                 # отступ от границ до содержимого по вертикали
                 font='Tahoma 14', command= lambda: model.critical()) #Команда при нажатии
btplot1.place(x=X1, y=mass[16], width=150/1.5, height=60/1.5)

btplot2 = Button(root, text='Очистить',  # текст кнопки 
                 background="#60B9CE",     # фоновый цвет кнопки
                 foreground="black",     # цвет текста
                 padx="20",                # отступ от границ до содержимого по горизонтали
                 pady="8",                 # отступ от границ до содержимого по вертикали
                 font='Tahoma 14', command= lambda: model.clear())
btplot2.place(x=X1, y=mass[18], width=150/1.5, height=60/1.5)

btplot2 = Button(root, text='Тест',  # текст кнопки 
                 background="#60B9CE",     # фоновый цвет кнопки
                 foreground="black",     # цвет текста
                 padx="20",                # отступ от границ до содержимого по горизонтали
                 pady="8",                 # отступ от границ до содержимого по вертикали
                 font='Tahoma 14', command= lambda: model.test())
btplot2.place(x=X1, y=mass[20], width=150/1.5, height=60/1.5)


root.mainloop()

