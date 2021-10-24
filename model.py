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
    x=[0,28,30]
    y=[105,65,0]
    try:
        [view.ax[x].clear() for x in range(1)]
        view.ax[0].plot(x,y)
        view.canvas.draw()
        view.message_ask(["Request!", "Нет ошибки, график отрисован?"]);
    except:
        view.message_error(["Error", "Где-то ошибка"])