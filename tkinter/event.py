from tkinter import *

root = Tk()

def printCoords(event):
    print(event.x,event.y)

bt1 = Button(root,text='leftmost button')
bt1.bind('<Button-1>',printCoords)

bt2 = Button(root,text='middle button')
bt2.bind('<Button-2>',printCoords)

bt3 = Button(root,text='rightmost button')
bt3.bind('<Button-3>',printCoords)

bt4 = Button(root,text='double click')
bt4.bind('<Double-Button-1>',printCoords)

bt5 = Button(root,text='triple click')
bt5.bind('<Triple-Button-1>',printCoords)

bt1.grid()
bt2.grid()
bt3.grid()
bt4.grid()
bt5.grid()

root.mainloop()

