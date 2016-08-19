from tkinter import *

root = Tk()
ws = []
ps = PanedWindow(orient=VERTICAL)
ps.pack(fill=BOTH,expand=1)
for w in [Label,Button,Checkbutton,Radiobutton]:
    ws.append(w(ps,text='hello'))
for w in ws:
    ps.add(w)
ps.paneconfig(Label(ps,text='world'),after=ws[0])
root.mainloop()
