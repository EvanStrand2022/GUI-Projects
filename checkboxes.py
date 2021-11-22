from tkinter import *

def checkIt():
    if check.get() == 0:
        txt.configure(text="NO")
    else:
        txt.configure(text="YES")
main = Tk()

check = IntVar()
check1 = Checkbutton(main, variable=check, onvalue=1, offvalue=0, command=checkIt)
check1.pack()


txt = Label(main, text="Yes")
txt.pack()
#ewe
main.mainloop()