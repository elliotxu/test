from tkinter import *
from tkinter.simpledialog import *


root = Tk()
dlg = SimpleDialog(root,
                   text='hello SimpleDialog',
                   buttons=['Yes','No','cancel'],
                   default=0)
print(dlg.go())
root.mainloop()

