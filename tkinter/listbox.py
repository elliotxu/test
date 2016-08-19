from tkinter import *

def printList(event):
    print(lb.get(lb.curselection()))

root = Tk()
lb = Listbox(root)
lb.bind('<Double-Button-1>',printList)
for i in range(10):
    lb.insert(END, str(i*100))
lb.pack()
root.mainloop()

