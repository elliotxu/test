from tkinter import *

root = Tk()
Lang = ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript']
Lang2 = range(100)
v = StringVar(root)
v.set('Python')
def printOption(event):
    print(v.get())
om = OptionMenu(root, v, *Lang)
om.bind('<Button-1>', printOption)
om.pack()
root.mainloop()