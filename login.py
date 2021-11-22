from tkinter import *
import mainMenu

def showPass():
    passEntry.configure(show="")

def hidePass():
    passEntry.configure(show="*")

def checkPass():
    if passEntry.get()=="ChrisPr4tt":
        accessLabel.configure(text="ACCESS GRANTED", fg="limegreen")
        login.destroy()
        mainMenu.initMainMenu()
    else:
        accessLabel.configure(text="ACCESS DENIED", fg="red")

#define login screen
login = Tk()
login.title("Secret Password")
login.geometry("895x210")
login.configure(bg="#2e2e2e")

#define password label
passLabel = Label(login, text="password", font=("Courier", 20), bg="#2e2e2e", fg="limegreen")
passLabel.grid(column=0, row=0)

#define password entry
passEntry = Entry(login, bg="black", fg="limegreen", font=("Courier", 40), show="*", selectbackground="#2e2e2e")
passEntry.grid(column=1, row=0)

#define show button
showButton = Button(login, text="SHOW", font=("Courier", 30), command=showPass, width=10)
showButton.grid(column=0, row=1)

#define hide button
hideButton = Button(login, text="HIDE", font=("Courier", 30), command=hidePass, width=10)
hideButton.grid(column=0, row=2)

#define enter button
enterButton = Button(login, text="LOGIN", font=("Courier", 30), width=10, command=checkPass)
enterButton.grid(column=1, row=1)

#define access granted/access denied label
accessLabel=Label(login, text="", font=("Courier", 30), bg="#2e2e2e", fg="limegreen")
accessLabel.grid(column=1, row=2)

#add mainloop
login.mainloop()