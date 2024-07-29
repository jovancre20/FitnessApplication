from tkinter import * 
from PIL import ImageTk



splash_screen= Tk()
splash_screen.geometry("200x200")

splash_screen.eval('tk::PlaceWindow . center')

words= Label(splash_screen,text='Splash Screen',font=20)
words.pack()

def comp():
    global wind2
    splash_screen.destroy()
    wind2= Tk()
    wind2.geometry("400x400")
    wind2.title('hello')

    bgimage = ImageTk.PhotoImage(file='chestwk.jpg')
    bglabel = Label(wind2,image=bgimage)
    bglabel.place(x=0,y=0)

    bgimage2 = ImageTk.PhotoImage(file='char.png')
    bglabe2 = Label(wind2,image=bgimage)
    bglabe2.place(x=0,y=0)


splash_screen.after(1000,comp)
mainloop()