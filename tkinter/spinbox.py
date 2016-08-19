from tkinter import *

root = Tk()
def printSpin():
    print(sb.get())
sb = Spinbox(root,
             from_=0,
             to=10,
             command=printSpin)
sb.pack()
print(sb['values'])
root.mainloop()