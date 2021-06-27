import tkinter as tk
from tkinter import ttk
import os
import sys

window = tk.Tk()
window.geometry("500x300")
window.title("Form")
window.resizable(False, False)
window.configure(background="#525150")

background_image = tk.PhotoImage(file='img/bg.png')
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

photo = tk.PhotoImage(file='img/logo.png')
tk.Label(window, image=photo).place(x=0, y=0)

title = tk.Label(text="Menu di scelta", fg="#CBCACA", bg="#257523", font=("Georgia", 20)).place(x=170, y=0)


# Define the working of the button
def terrain_command():
    window.destroy()
    os.system('python Inserimento_terreni.py')


def disease_command():
    window.destroy()
    os.system('python kb_main.py')


# Import the image using PhotoImage function
click_terrain = tk.PhotoImage(file='img/terrain.png')
click_disease = tk.PhotoImage(file='img/disease.png')

# Let us create a label for button event
img_terrain = tk.Label(image=click_terrain)
img_disease = tk.Label(image=click_disease)

# Let us create a dummy button and pass the image
terrain_button = tk.Button(window, image=click_terrain, command=terrain_command,
                           borderwidth=0).place(x=100, y=90)
disease_button = tk.Button(window, image=click_disease, command=disease_command,
                           borderwidth=0).place(x=100, y=170)

if __name__ == '__main__':
    window.mainloop()
