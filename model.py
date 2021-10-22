import view
import numpy as np
def suum():
    try:
        view.num1=int(view.txt1.get())
        view.num2=int(view.txt2.get())
        view.box_result=str(view.num1+view.num2)
        print(view.box_result)
        view.messagebox.showinfo("Result","Результат в консоли = "+view.box_result)      
    except:
        view.messagebox.showerror("Error","AMOGUS, кто то ввел не число")
       
x=[0,3,1.5,0,3,4.5,4.5,3.5,4.5,5.5,4.5,4.5,6,6,6,8,8]
y=[0,6,3,6,0,0,3,6,3,6,3,0,0,6,0,6,0]
def do_plot():
    try:
        #[ax[x].clear() for x in range(1)]
        #ax[0].plot(x,y)
        #view.canvas.draw()
        view.messagebox.askokcancel("Нет ошибки, график отрисован?")
    except:
        view.messagebox.showwarning("Где-то ошибка")