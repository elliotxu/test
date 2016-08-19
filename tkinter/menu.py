from tkinter import *

root = Tk()
menubar = Menu(root)
vLang = StringVar()
def printItem():
    print('vLang=',vLang.get())

filemenu = Menu(menubar,tearoff=0)
for k in ['Python',
             'PHP',
             'CPP',
             'C',
             'Java',
             'JavaScript',
             'VBScript']:
    filemenu.add_radiobutton(label=k,command=printItem,variable=vLang)
menubar.add_cascade(label='Language',menu=filemenu)
root['menu'] = menubar
root.mainloop()


