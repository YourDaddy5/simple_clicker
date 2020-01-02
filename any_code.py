from tkinter import *
import time

time_count = 10
count = 0

window = Tk()
window.title("Кликер ")
window.geometry('400x250')
lbl = Label(window, text="", font=('American Captain',50))
lbl.grid(column=0, row=0)


def clicked():
    global count
    lbl.configure(text = count)

    if clicked:
        count +=1

def nul():
    global count
    lbl.configure(text = count ==0)
    if clicked:
        count = 0


btn = Button(window,text = "Кликни сюда",fg = "red",bg ="black",command = clicked)
btn.grid(column=1 , row=2)


btn_sbros = Button(window,text = "Сбросить счёт",fg = "red",bg ="black",command = nul)

btn_sbros.grid(column=5,row=2)


window.mainloop()