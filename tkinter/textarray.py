from tkinter import *

#Below should pack to class
class MyWindow:
    def __init__(self, wname=""):
        self.root = Tk()
        self.root.title(wname)
        self.text = Text(self.root,font=("Purisa",12))
        self.text.pack()

        self.button=Button(self.root, text ="Button", command=self.prn)
        self.button.pack()
        self.root.mainloop()

    def get_words_list(self, widget):
        """Return list of words"""
        options=widget.get(1.0, END)# get lines into string
        #Remove spaces in list of lines
        return [i.strip() for i in options.splitlines()]

    def prn(self):
        """Testing get_words_list"""
        print(self.get_words_list(self.text))

if __name__ == "__main__":
    w = MyWindow("My window")