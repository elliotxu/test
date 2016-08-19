from tkinter import *

root = Tk()
t = Text(root)
t.insert(1.0,'0123456789')
t.insert('2.end','\n')
t.insert(3.5,'ABCDEFGHIJ')
t.pack()
root.mainloop()
