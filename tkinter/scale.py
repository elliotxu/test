from tkinter import *


def printScale(text):
    print('text=',text)
    print('v=',v.get())

root = Tk()
v = StringVar()
Scale(root,
      from_=0,
      to=100,
      resolution=0.0001,
      orient=HORIZONTAL,
      digits=8,
      variable=v,
      command=printScale,
      label='choice'
      ).pack()
print(v.get())
root.mainloop()