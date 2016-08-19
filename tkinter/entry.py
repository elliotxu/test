from tkinter import *

root = Tk()
l1 = Label(root, text='a')
l1.grid(row=0,column=0)
e=StringVar()
e1 = Entry(root, textvariable=e)
e.set('input your value here')
e1.grid(row=0,column=1)
root.mainloop()