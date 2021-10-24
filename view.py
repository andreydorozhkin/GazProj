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
ax = [figure.add_subplot(1,1,x+1)for x in range(1)]

#Визуальный метод определния материала
def changeMaterials():
   comboExample["values"] = [ "Сталь", "Аллюминий"]

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
    lab = Label(root, text=name_field)
    lab.place(x=x_label, y=y_label)
    text = Entry(root, width=20)
    text.place(x=x_entry, y=y_entry)
    return text

print(model.liquidation_value(299845.51, 27768000, 4049849.86, 2554200, 1, 30, 40000))
mass=generate_coordinat(30, 5, 0)
X1=710
X2=1150
print(model.critical_distance(9.42, 1720710.28, 0.909, 121.8, 33477498.85, 9.5, 11325.02, 0.9, 12.18, 4864558, 30))
initial_enegry_consum = generate_field("Начальное годовое энергопотребление объектом газификации. (МВт*ч)/год", X1, mass[0], X2, mass[0])
unit_cost_liquefaction_complex = generate_field("Удельные затраты на комплекс сжижения газа. (руб./(МВ*ч)))", X1, mass[1], X2, mass[1])
initial_distance = generate_field("Начальное расстояние до населенного пункта. км", X1, mass[2], X2, mass[2])
inhabitants = generate_field("Число жителей в снабжаемом городе. тыс. чел.", X1, mass[3], X2, mass[3])
acceptable_losses = generate_field("Допустимые потери давления газопроводе, МПа", X1, mass[4], X2, mass[4])
gas_material = generate_field("Материал газопровода", X1, mass[5], X2, mass[5])
average_gas_pressure = generate_field("Усредненное давление газа (абсолютное) в сети. МПф", X1, mass[6], X2, mass[6])
specific_cost_gas_pipeline = generate_field("Удельная стоимость газопровода руб/км", X1, mass[7], X2, mass[7])
cost_natural_gas = generate_field("Стоимость ПГ. (руб/(МВт*ч))", X1, mass[8], X2, mass[8])
specific_SGRP = generate_field("Удельная ШГРП (руб/МВт*ч)", X1, mass[9], X2, mass[9])
cost_gas_pipeline_maintenance = generate_field("Стоимость обслуживания газопровода, (руб/км)/год", X1, mass[10], X2, mass[10])
cost_maintenance_SHGRP = generate_field("Стоимость обслуживания ШГРП (руб/МВт*ч)", X1, mass[11], X2, mass[11])
price_cistern_liquefied_natural_gas = generate_field("Цена цистерны СПГ, руб", X1, mass[12], X2, mass[12])
volume_liquefied_natural_gas_cistern = generate_field("Объем цистерны СПГ, м3.", X1, mass[13], X2, mass[13])
average_cistern_speed = generate_field("Средняя скорость цистерны СПГ, км/ч", X1, mass[14], X2, mass[14])
price_liquefied_natural_gas_tank = generate_field("Цена резервуара СПГ, руб", X1, mass[15], X2, mass[15])
volume_liquefied_natural_gas_tank = generate_field("Объем резервуара СПГ, м3", X1, mass[16], X2, mass[16])
unit_cost_gasifier = generate_field("Удельная стоимость газификатора, руб/МВт*ч", X1, mass[17], X2, mass[17])
cost_liquefied_natural_gas = generate_field("Стоимость СПГ, руб/ВТ*ч", X1, mass[18], X2, mass[18])
unit_maintenance_cost_gas_liquefaction_facility = generate_field("Удельные затраты на обслуживание объекта по сжижению газа, руб/МВт*ч", X1, mass[19], X2, mass[19])
сost_annual_maintenance_liquefied_natural_gas_cistern = generate_field("Стоимость годового обслуживания цистерны СПГ, руб", X1, mass[20], X2, mass[20])
cost_annual_maintenance_liquefied_natural_gas_tank = generate_field("Стоимость годового обслуживания резервуара СПГ, руб", X1, mass[21], X2, mass[21])
service_life_natural_gas_equipment = generate_field("Срок службы оборудования ПГ, лет", X1, mass[22], X2, mass[22])
transition_period_liquefied_natural_gas = generate_field("Срок перехода с СПГ на ПГ, лет", X1, mass[23], X2, mass[23])
cost_dismantling_liquefied_natural_gas_tank = generate_field("Стоимость демонтажа резервуара СПГ, руб", X1, mass[24], X2, mass[24])
discount_coef = generate_field("Коэффициент дисконтирования 1/год", X1, mass[25], X2, mass[25])
step_increasing_energy_consumption = generate_field("Шаг увеличения энергопотребления, МВт", X1, mass[26], X2, mass[26])

comboExample = ttk.Combobox(root, 
                            values=[],
                            postcommand=changeMaterials, width=17)
comboExample.place(x=X2, y=mass[5])


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
