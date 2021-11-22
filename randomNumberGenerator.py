from tkinter import *
import random

def initRandomNumberGenerator():
      
      def diceRollOneThroughSix():
            (random.randrange(0, 7))
            rngLabelB.configure(text=(random.randrange(0, 7)))
      #define title and dimensions
      rng = Tk()
      rng.geometry("600x600")
      rng.title("Random Number Generator")
      rng.configure(bg="#2e2e2e")


      #define buttons
      randomNumberGeneratorButton = Button(rng, text="Roll", font=("Courier", 30), width=10,  command=diceRollOneThroughSix)        
      randomNumberGeneratorButton.grid(column=1, row=1)

      #define label
      rngLabelA = Label(rng, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
      rngLabelA.grid(column=0, row=0)
      
      #define answer label
      rngLabelB = Label(rng, text="Answer", font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
      rngLabelB.grid(column=0, row=5)

      #define mainloop
      rng.mainloop()