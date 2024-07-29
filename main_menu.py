import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import login_page as lp

#code for functions
def workout():
    #window33.destroy()
    import workout
    

def diet():
    #window33.destroy()
    import diet

def yoga():
    #window33.destroy()
    import yoga

def logout():
    window33.destroy()
    #import login_page


#code for gui
window33= Toplevel(lp.window1)
window33.title('Main Menu')
window33.geometry('990x560+50+40')

p1=PhotoImage(file='titlelogo.png')
window33.iconphoto(False,p1)

#title
title3=Label(window33,text="Welcome!",font=("times new roman",18,"bold"),bd=5,relief=GROOVE,bg="chocolate1")
title3.pack(side=TOP,fill=X)

title4=Label(window33,text="Select your choice",font=("times new roman",18,"bold"))
title4.pack(side=TOP,fill=X)

global image1
image1 = ImageTk.PhotoImage(Image.open("workout logo.png"))
label= Label(window33, image=image1)
label.place(x=80,y=110)

but1=Button(window33, text="Workout", command = workout, width=35)
but1.place(x=80,y=350)

global image2
image2 = ImageTk.PhotoImage(Image.open("diet logo.jpg"))
label= Label(window33, image=image2)
label.place(x=390,y=110)

but2=Button(window33, text="Diet", command = diet, width=30)
but2.place(x=390,y=350)

global image3
image3 = ImageTk.PhotoImage(Image.open("yoga logo.jpg"))
label= Label(window33, image=image3)
label.place(x=650,y=110)


but3=Button(window33, text="yoga", command = yoga, width=30)
but3.place(x=650,y=350)

logut_button=Button(window33,text="Logout",command=logout, width=10)
logut_button.place(x=900,y=500)

window33.mainloop()
