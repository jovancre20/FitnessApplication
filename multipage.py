from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.ttk import *
import os

window3= tk.Tk()
window3.title('Main Menu')
window3.geometry("500x500")
window3.iconbitmap("char.png")

def bro():
    window3.quit()

"""
canvas=Canvas(window3, width=500, height=500)
canvas.pack()

img= ImageTk.PhotoImage(Image.open("char.png"))
canvas.create_image(200,100,image=img)

but=Button(window3,text="hold")
but.place(x=100,y=130)"""

image1 = ImageTk.PhotoImage(Image.open("char.png"))
label= Label(window3, image=image1)
label.place(x=100,y=50)

but1=Button(window3, text="Workout", command = bro)
but1.place(x=100,y=130)

image2 = ImageTk.PhotoImage(Image.open("ni1.png"))
label= Label(window3, image=image2)
label.place(x=300,y=50)

but2=Button(window3, text="Diet", command = bro)
but2.place(x=300,y=130)

image3 = ImageTk.PhotoImage(Image.open("ni2.png"))
label= Label(window3, image=image3)
label.place(x=300,y=200)

but3=Button(window3, text="yoga", command = bro)
but3.place(x=300,y=130)



window3.mainloop()
