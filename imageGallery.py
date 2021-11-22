#column = x, row = y
from tkinter import *

def initImageGallery():
#x = 0

    image = Tk()
    image.title("Image Gallery")
    image.geometry("600x700")
    image.configure(bg="#2e2e2e")

    #define image label
    imageLabelA = Label(image, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
    imageLabelA.grid(column=0, row=0)
      
    imageLabelB = Label(image, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
    imageLabelB.grid(column=0, row=0)
      
    imageLabelC = Label(image, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
    imageLabelC.grid(column=0, row=0)
      
    imageLabelD = Label(image, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
    imageLabelD.grid(column=0, row=0)
      
    imageLabelE = Label(image, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
    imageLabelE.grid(column=0, row=0)
      
    imageLabelF = Label(image, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
    imageLabelF.grid(column=0, row=0)
      
    imageLabelG = Label(image, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
    imageLabelG.grid(column=0, row=0)
      
    imageLabelH = Label(image, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
    imageLabelH.grid(column=0, row=0)
      
    imageLabelI = Label(image, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
    imageLabelI.grid(column=0, row=0)
      
    imageLabelJ = Label(image, font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
    imageLabelJ.grid(column=0, row=0)
      

    #define images
    myImageA = PhotoImage(file="Trollge.png")
    imageLabelA.configure(image=myImageA)
    imageLabelA.grid()

    myImageB = PhotoImage(file="JermaSus.png")
    imageLabelB.configure(image=myImageB)
    imageLabelB.grid()

    myImageC = PhotoImage(file="amongUsDrip.png")
    imageLabelC.configure(image=myImageC)
    imageLabelC.grid()

    myImageD = PhotoImage(file="Evan the Hedgehog.png")
    imageLabelD.configure(image=myImageD)
    imageLabelD.grid()

    myImageE = PhotoImage(file="Lego Yoda.png")
    imageLabelE.configure(image=myImageE)
    imageLabelE.grid()

    myImageF = PhotoImage(file="Community.png")
    imageLabelF.configure(image=myImageF)
    imageLabelF.grid()

    myImageG = PhotoImage(file="Crime Against Humanity.png")
    imageLabelG.configure(image=myImageG)
    imageLabelG.grid()

    myImageH = PhotoImage(file="PEEPEEPOOPOO.png")
    imageLabelH.configure(image=myImageH)
    imageLabelH.grid()

    myImageI = PhotoImage(file="")
    imageLabelI.configure(image=myImageI)
    imageLabelI.grid()

    myImageJ = PhotoImage(file="")
    imageLabelJ.configure(image=myImageJ)
    imageLabelJ.grid()

    #define NEXT and LAST buttons
    nextButton = Button(image, text="NEXT", font=("Courier", 30), width=10)
    nextButton.grid(column=5, row=2)
    lastButton = Button(image, text="LAST", font=("Courier", 30), width=10)
    lastButton.grid(column=0, row=0)

    #if x == 0:
    #imageLabel.configure(image=myImageA)

    image.mainloop()

    #if x == 0:
    #imageLabel.configure(image=myImageA)



    #imageLabel = Label(image)
