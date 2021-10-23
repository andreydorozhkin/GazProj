import view
import numpy as np
def sum():
    try:
        num1=int(view.txt1.get())
        num2=int(view.txt2.get())
        box_result=str(num1+num2)
        print(box_result)
        view.message_info(view.message_mass[0], view.message_mass[1]+box_result)    
    except:
        view.message_error(view.message_mass[4], view.message_mass[5])
       

def do_plot():
    x=[0,3,1.5,0,3,4.5,4.5,3.5,4.5,5.5,4.5,4.5,6,6,6,8,8]
    y=[0,6,3,6,0,0,3,6,3,6,3,0,0,6,0,6,0]
    try:
        [view.ax[x].clear() for x in range(1)]
        view.ax[0].plot(x,y)
        view.canvas.draw()
        view.message_ask(view.message_mass[2], view.message_mass[3]);
    except:
        view.message_error(view.message_mass[6], view.message_mass[7])