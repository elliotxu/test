from tkinter import *

root = Tk()
tl = Toplevel()
tl.title('hello Toplevel')
tl.geometry('400x300')
Label(tl,text='hello label').pack()
root.mainloop()