import view
import numpy as np
def sum():
    try:
        num1=int(view.initial_enegry_consum.get())
        num2=int(view.unit_cost_liquefaction_complex.get())
        box_result=str(num1+num2)
        print(box_result)
        view.message_info(["Result","Результат в консоли = "+box_result])    
    except:
        view.message_error(["Error", "AMOGUS, кто то ввел не число"])
       

def do_plot():
    t0=[0,5,10,15,20,25,30]
    l0=[9.48,1.73,0.8,0.532,0.423,0.374,0.35]
    l1=[12.69,2.7,1.48,1.12,0.98,0.912,0.87]
    l2=[38.57,10.55,7.05,5.99,5.54,5.31,5.19]
    if view.comboExample.get()=="100":
        x=t0
        y=l0
        try:
            [view.ax[x].clear() for x in range(1)]
            view.ax[0].plot(x,y, color="red",label="Q=100" )
            view.canvas.draw()
            view.message_ask(["Request!", "Нет ошибки, график отрисован?"]);
        except:
            view.message_error(["Error", "Где-то ошибка"])
    if view.comboExample.get()=="1000":
        x=t0
        y=l1
        try:
            #[view.ax[x].clear() for x in range(1)]
            view.ax[0].plot(x,y,color="green",label="Q=1000")
            view.canvas.draw()
            view.message_ask(["Request!", "Нет ошибки, график отрисован?"]);
        except:
            view.message_error(["Error", "Где-то ошибка"])
    if view.comboExample.get()=="10000":
        x=t0
        y=l2
        try:
            #[view.ax[x].clear() for x in range(1)]
            view.ax[0].plot(x,y,color="blue",label="Q=1000")
            view.canvas.draw()
            view.message_ask(["Request!", "Нет ошибки, график отрисован?"]);
        except:
            view.message_error(["Error", "Где-то ошибка"])

