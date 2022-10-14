import pygame
from pygame import mixer
import tkinter as tk

class SoundOptions:
    applied = False

    def __init__(self, sound):
        self.volume = 100
        self.currentSound = sound.get_volume()*100
        self.currentMusic = pygame.mixer.music.get_volume() * 100
        self.min = 0
        self.max = 100

    def start(self, sounds):

        window = tk.Tk()
        window.geometry('250x300')
        window.title("Volume")
        icon = tk.PhotoImage(file = "volume.png")
        window.iconphoto(False, icon)
        
        lastMusic = self.currentMusic
        lastSound = self.currentSound

        #Functions --------------------------------------------------

        def applyButtonClick():

            pygame.mixer.music.set_volume(musicSlider.get()/100)

            self.currentSound = soundSlider.get()
            self.currentMusic = musicSlider.get()
            
            for sound in sounds:
                sound.set_volume(soundSlider.get()/100)

        def okayButtonClick():
            if not soundSlider.get() == self.currentSound or not musicSlider.get() == self.currentMusic:
                promptLabel.configure(text = "Please press apply")
            else:
                
                window.destroy()
                return
                
        def cancelButtonClick():
            pygame.mixer.music.set_volume(lastMusic/100)

            for sound in sounds:
                sound.set_volume(lastSound/100)

            
            window.destroy()
            return

        #Frames -----------------------------------------------------
        optionFrame = tk.Frame(window, relief = tk.RAISED, borderwidth = 1)
      

        #Labels -----------------------------------------------------
        musicLabel = tk.Label(optionFrame, text = "Music Volume")
        
        soundEffectLabel = tk.Label(optionFrame, text = "Sound Effects Volume")

        promptLabel = tk.Label(optionFrame, text = "")
               

        #Buttons ----------------------------------------------------
        applyButton = tk.Button(window, text = "Apply", command = applyButtonClick, width = 6)

        okayButton = tk.Button(window, text = "Okay", command = okayButtonClick, width = 6)

        cancelButton = tk.Button(window, text = "Cancel", command = cancelButtonClick, width = 6)

        #Sliders ----------------------------------------------------

        musicSlider = tk.Scale(optionFrame, from_=self.min, to = self.max, orient = tk.HORIZONTAL)
        soundSlider = tk.Scale(optionFrame, from_=self.min, to = self.max, orient = tk.HORIZONTAL)

        musicSlider.set(pygame.mixer.music.get_volume() * 100)
        soundSlider.set(self.currentSound)

        #Placements -------------------------------------------------

        optionFrame.pack(fill = tk.BOTH, expand = True)

        musicLabel.pack()
        musicSlider.pack()
        soundEffectLabel.pack()
        soundSlider.pack()
        promptLabel.pack(side = tk.BOTTOM, pady = 5)

        cancelButton.pack(side = tk.RIGHT, padx = 5, pady = 5)
        okayButton.pack(side = tk.RIGHT, padx = 5, pady = 5)
        applyButton.pack(side = tk.RIGHT, padx = 5, pady = 5)

        #Main

        window.mainloop()


