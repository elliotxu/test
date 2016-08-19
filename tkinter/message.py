from tkinter import *

root = Tk()
for i in [LEFT,RIGHT,CENTER]:
    Message(root,text='ABC DEF GHI',justify=i).pack()
root.mainloop()
