from tkinter import *
import areaCalc
import randomNumberGenerator
import madLib
import imageGallery

def initMainMenu():
    mainMenu = Tk()
    
    def openAreaCalc():
        areaCalc.initAreaCalc()

    def openRandomNumberGenerator():
        randomNumberGenerator.initRandomNumberGenerator()

    #define main menu dimensions and title
    mainMenu.geometry("800x800")
    mainMenu.title("Main Menu")
    mainMenu.configure(bg="#2e2e2e")

    #define entry to area calculator
    areaCalcButton = Button(mainMenu, text="Area Calculator", bg="#2e2e2e", fg="darkgrey", font=("courier", 20), width=15, activebackground="black", activeforeground="darkgrey", command=openAreaCalc)
    areaCalcButton.grid(column=0, row=1)

    #define entry to random number generator
    randomNumberGeneratorButton = Button(mainMenu, text="Random Number Generator", bg="#2e2e2e", fg="darkgrey", font=("courier", 20), width=25, activebackground="black", activeforeground="darkgrey", command=openRandomNumberGenerator)
    randomNumberGeneratorButton.grid(column=1, row=1)


    mainMenu.mainloop()