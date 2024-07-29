import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import login_page as lp

# code for function 



def chest():
    #wk1.destroy()
    global chest_window
    chest_window= Toplevel(wk1)
    chest_window.geometry('1920x1080+0+0')
    chest_window.title('Chest Workout')
    #chest_window.attributes('-fullscreen',True)
    chest_window.state('zoomed')

    bgimage = ImageTk.PhotoImage(file='chestwk.jpg')
    bglabel = Label(chest_window,image=bgimage)
    bglabel.place(x=0,y=0)

    back_button=Button(chest_window, text="Retrun to workout tab",width=20,height=2, command=chestback)
    back_button.place(x=1100,y=600)
    

    chest_window.mainloop()

def abs():
    #wk1.destroy()
    global abs1
    abs1= Toplevel(wk1)
    abs1.geometry('1920x1080+0+0')
    abs1.title('Abs Workout')
    abs1.state('zoomed')

    bgimage = ImageTk.PhotoImage(file='abs.jpg')
    bglabel = Label(abs1,image=bgimage)
    bglabel.place(x=0,y=0)

    back_button=Button(abs1, text="Retrun to workout tab",width=20,height=2, command=absback)
    back_button.place(x=1100,y=600)

    abs1.mainloop()

def back():
    #wk1.destroy()
    global back1
    back1= Toplevel(wk1)
    back1.title("Back Workout")
    back1.geometry('1920x1080+0+0')
    back1.state('zoomed')

    bgimage = ImageTk.PhotoImage(file='back.jpg')
    bglabel = Label(back1,image=bgimage)
    bglabel.place(x=0,y=0)
    
    back_button=Button(back1, text="Retrun to workout tab",width=20,height=2, command=backback)
    back_button.place(x=1100,y=600)
    back1.mainloop()

def legs():
    global legswin
    #wk1.destroy()
    legswin= Toplevel(wk1)
    legswin.title("Leg Workout")
    legswin.geometry("1920x1080+0+0")
    legswin.state('zoomed')

    bgimage = ImageTk.PhotoImage(file='legs .jpg')
    bglabel = Label(legswin,image=bgimage)
    bglabel.place(x=0,y=0)

    back_button=Button(legswin, text="Retrun to workout tab",width=20,height=2, command=legsback)
    back_button.place(x=1100,y=600)

    legswin.mainloop()

def biceps():
    #wk1.destroy()
    global bicepswin
    bicepswin= Toplevel(wk1)
    bicepswin.title("Biceps Workout")
    bicepswin.geometry("1920x1080+0+0")
    bicepswin.state('zoomed')

    bgimage = ImageTk.PhotoImage(file="shoulder.jpg")
    bglabel = Label(bicepswin,image=bgimage)
    bglabel.place(x=0,y=0)

    back_button=Button(bicepswin, text="Retrun to workout tab",width=20,height=2, command=bicepsback)
    back_button.place(x=1100,y=600)

    bicepswin.mainloop()

def triceps():
    #wk1.destroy()
    global tricepswin
    tricepswin= Toplevel(wk1)
    tricepswin.title('Triceps Workout')
    tricepswin.geometry("1920x1080+0+0")
    tricepswin.state('zoomed')

    bgimage = ImageTk.PhotoImage(file='triceps.png')
    bglabel = Label(tricepswin,image=bgimage)
    bglabel.place(x=0,y=0)

    back_button=Button(tricepswin, text="Retrun to workout tab",width=20,height=2, command=tricepsback)
    back_button.place(x=1100,y=600)

    tricepswin.mainloop()

def chestback():
    chest_window.destroy()

def absback():
     abs1.destroy()

def backback():
     back1.destroy()

def legsback():
     legswin.destroy()
     
def bicepsback():
    bicepswin.destroy()
     
def tricepsback():
    tricepswin.destroy()

def backmenu():
    wk1.destroy()
    #import main_menu


# code for gui
wk1 = Toplevel(lp.window1)
#wk1 = tk.Tk()

p1=PhotoImage(file='titlelogo.png')
wk1.iconphoto(False,p1)

wk1.title("Workout")
wk1.geometry("1920x1080+0+0")
    
title1=Label(wk1,text="Please select your workout",font=("times new roman",18,"bold"),bd=5,relief=GROOVE,bg="chocolate1")
title1.pack(side=TOP,fill=X)

button1=Button(wk1, text="Chest",width=180,height=2, command= chest)
button1.place(x=10,y=60)

button2=Button(wk1, text="Abs",width=180,height=2, command=abs)
button2.place(x=10,y=130)

button3=Button(wk1, text="Back",width=180,height=2,command=back)
button3.place(x=10,y=200)

button4=Button(wk1, text="Legs",width=180,height=2,command=legs)
button4.place(x=10,y=270)

button5=Button(wk1, text="Biceps",width=180,height=2, command=biceps)
button5.place(x=10,y=340)
    
button6=Button(wk1, text="Triceps",width=180,height=2, command=triceps)
button6.place(x=10,y=410)

button7=Button(wk1, text="Back to main menu",width=180,height=2, command=backmenu)
button7.place(x=10,y=500)
wk1.mainloop()