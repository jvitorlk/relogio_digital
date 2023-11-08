from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Relógio Digital')

def time():
    string = strftime('%H:%M:%S')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = ('franklin gothic', 200, 'bold'),
            background='black',
            foreground='white')
lbl.pack(anchor='center')
time()
mainloop()