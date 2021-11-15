import model
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
root["bg"] = "white"

frame1 = Frame(root);
frame1.place(x=0, y=0, width=700, height=700)  # 325 height
figure = plt.Figure(figsize=(5, 5), facecolor='white', edgecolor="white")
canvas = FigureCanvasTkAgg(figure, frame1)
canvas.get_tk_widget().place(x=0, y=0, width=700, height=650)
ax = [figure.add_subplot(1, 1, x + 1) for x in range(1)]
ax[0].set_xlabel("Время газификации опорного пункта \nсетевым природным газом t0 лет",
                 fontsize=12, color="black")
ax[0].set_ylabel("Удаленность потребителя от опорного пунка \nэнергоснабжения L, км",
                 fontsize=12, color="black")


# Визуальный метод определния материала
def changeMaterials():
    combo_exsample_gas_material["values"] = ["Сталь", "Полиэтилен"]


# Вывод ошибок
def message_info(message):
    messagebox.showinfo("Внимание!", message)


def message_ask(message):
    messagebox.askquestion("Внимание!", message)


def message_error(message):
    messagebox.showerror("Error!", message)


def generate_coordinat(a, b, c):
    coordinat = []
    while c != a:
        c += 1
        coordinat = coordinat + [b]
        b = b + 25
    return coordinat


def generate_field(name_field, x_label, y_label, x_entry, y_entry):
    lab = Label(root, text=name_field, background="white")
    lab.place(x=x_label, y=y_label)
    text = Entry(root, width=20, background="white")
    text.place(x=x_entry, y=y_entry)
    return text


mass = generate_coordinat(30, 70, 0)
X1 = 775
X2 = 1050

cost_gas = generate_field("Стоимость газа", X1, mass[0], X2, mass[0])
cost_natur_liquided_gas = generate_field("Стоимость СПГ", X1, mass[1], X2, mass[1])
lbl = Label(root, text="Потребность города в КВт", background="white")
lbl.place(x=X1, y=mass[2])
city_need_energy_begin = generate_field("от", 1030, mass[2], X2, mass[2])
city_need_energy_end = generate_field("до", 1030, mass[3], X2, mass[3])

cost_cistern = generate_field("Стоимость автомобильной цистерны", X1, mass[5], X2, mass[5])
volume_cistern = generate_field("Объем автомобильной цистерны", X1, mass[6], X2, mass[6])
# number_cistern = generate_field("Колличество цистерн ", X1, mass[6], X2, mass[6])
# number_cistern.config(state = "readonly")
cost_tank = generate_field("Стоимость хранилища СПГ", X1, mass[8], X2, mass[8])
volume_tank = generate_field("Объем хранилища СПГ", X1, mass[9], X2, mass[9])
# number_tank = generate_field("Колличество хранилищ ", X1, mass[9], X2, mass[9])
# number_tank.config(state = "readonly")
cost_gasifiers = generate_field("Стоимость газификаторов ", X1, mass[11], X2, mass[11])
# cost_laying_high = generate_field("Стоимость прокладки газопровода высокого давления на километр", X1, mass[10], X2, mass[10])
# cost_laying_medium= generate_field("Стоимость прокладки газопровода среднего давления на километр", X1, mass[11], X2, mass[11])
# cost_GRPSH = generate_field("Стоимость ГРПШ", X1, mass[12], X2, mass[12])
# efficiency_GRPSH = generate_field("Производительность ГРПШ", X1, mass[13], X2, mass[13])
# cost_maintenance_GRPSH = generate_field("Стоимость обслуживания ГРПШ", X1, mass[14], X2, mass[14])
# cost_maintenance_gas_pipeline = generate_field("Стоимость обслуживания газопровода", X1, mass[15], X2, mass[15])
factory_distance = generate_field("Расстояние от завода до города", X1, mass[12], X2, mass[12])
gas_material = Label(root, text="Материал газопровода", background="white")
gas_material.place(x=X1, y=mass[13])

combo_exsample_gas_material = ttk.Combobox(root,
                                           values=["Сталь", "Полиэтилен"],
                                           postcommand=changeMaterials, width=17)
combo_exsample_gas_material.place(x=X2, y=mass[13])
text_entry = Text(root, height=8, width=34)
text_entry.insert(1.0, "Колличество хранилищ = " + "\nКолличество цистерн = ")
# text_entry.insert(2.0,"Колличество цистерн = ")
text_entry.configure(state='disabled')
text_entry.place(x=900, y=mass[16])

btplot1 = Button(root, text='Рассчитать',  # текст кнопки 
                 background="#60B9CE",  # фоновый цвет кнопки
                 foreground="black",  # цвет текста
                 padx="20",  # отступ от границ до содержимого по горизонтали
                 pady="8",  # отступ от границ до содержимого по вертикали
                 font='Tahoma 14', command=lambda: model.critical())
btplot1.place(x=X1, y=mass[16], width=150 / 1.5, height=60 / 1.5)

btplot2 = Button(root, text='Очистить',  # текст кнопки 
                 background="#60B9CE",  # фоновый цвет кнопки
                 foreground="black",  # цвет текста
                 padx="20",  # отступ от границ до содержимого по горизонтали
                 pady="8",  # отступ от границ до содержимого по вертикали
                 font='Tahoma 14', command=lambda: model.clear())
btplot2.place(x=X1, y=mass[18], width=150 / 1.5, height=60 / 1.5)

btplot2 = Button(root, text='Тест',  # текст кнопки 
                 background="#60B9CE",  # фоновый цвет кнопки
                 foreground="black",  # цвет текста
                 padx="20",  # отступ от границ до содержимого по горизонтали
                 pady="8",  # отступ от границ до содержимого по вертикали
                 font='Tahoma 14', command=lambda: model.test())
btplot2.place(x=X1, y=mass[20], width=150 / 1.5, height=60 / 1.5)

root.mainloop()
