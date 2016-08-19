from tkinter import *

root = Tk()
lb1 = Label(root,text='Hello')
lb2 = Label(root,text='Grid')

lb1.grid()
lb2.grid(row=0,column=1)

root.mainloop()