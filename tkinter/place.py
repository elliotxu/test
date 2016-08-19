from tkinter import *

root = Tk()
root.geometry('800x600')
lb1 = Label(root,text='hello Place',fg='green')
bt1 = Button(root,text='hello Place',fg='red')
#lb.place(relx=1,rely=0.5,anchor=CENTER)
lb1.place(relx=0.5,
          rely=0.5,
          anchor=CENTER)
bt2 = Button(root,text='button in root',fg='yellow')
bt2.place(relx=0.25,
          rely=0.25,
          anchor=W)
bt1.place(in_=lb1,anchor=W)
root.mainloop()