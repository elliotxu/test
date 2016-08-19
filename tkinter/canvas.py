from tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
cv.create_rectangle(10,10,110,110,outline='red',
                    stipple='gray12',
                    fill='green')
cv.pack()
root.mainloop()