from tkinter import *

root = Tk()
lb = Listbox(root)
sl = Scrollbar(root)
sl.pack(side=RIGHT,fill=Y)
lb['yscrollcommand']=sl.set
for i in range(100):
    lb.insert(END,str(i))
lb.see(50)
lb.pack(side=LEFT)
sl['command'] = lb.yview
root.mainloop()