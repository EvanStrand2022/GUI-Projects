from tkinter import *
import pygame

pygame.mixer.init()
def playSound():
    #load in sound track
    pygame.mixer.music.load("legoYoda.mp3")
    #set volume
    pygame.mixer.music.set_volume(0.2)

    #play the sound
    pygame.mixer.music.play(loops=0)

main = Tk()

b = Button(main, text="play sound", command = playSound)
b.pack()

main.mainloop()