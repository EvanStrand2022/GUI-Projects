from tkinter import *

def initAreaCalc():
  
  def multiplyHeightWidth():
    x = int(calcEntryWidth.get())
    y = int(calcEntryHeight.get())
    z = (x*y)
    calcLabelC.configure(text=z)
  #define title and dimensions
  calc = Tk()
  calc.geometry("430x160")
  calc.title("Area Calculator")
  calc.configure(bg="#2e2e2e")

  #define calculator entry
  calcEntryHeight = Entry(calc, bg="black", fg="limegreen", font=("Courier", 20))
  calcEntryHeight.grid(column=1, row=0)
  calcEntryWidth = Entry(calc, bg="black", fg="limegreen", font=("Courier", 20))
  calcEntryWidth.grid(column=1, row=1)

  #define height label
  calcLabelA = Label(calc, text="Height", font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
  calcLabelA.grid(column=0, row=0)
  #define width label
  calcLabelB = Label(calc, text="Width", font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
  calcLabelB.grid(column=0, row=1)
  #define answer label
  calcLabelC = Label(calc, text="Answer", font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
  calcLabelC.grid(column=0, row=5)

  #define buttons
  calcButton = Button(calc, text="=", font=("Courier", 20), width=7, command=multiplyHeightWidth)
  calcButton.grid(column=1, row=3)  

  #define mainloop
  calc.mainloop()