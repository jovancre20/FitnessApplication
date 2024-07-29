import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import login_page as lp

# code for function 
def recommend():
    dt1.destroy()




# code for gui
dt1 = Toplevel(lp.window1)
#dt1=tk.Tk()
dt1.title("Diet")
dt1.geometry("1100x500+30+30")
title1=Label(dt1,text="Diet Plan",font=("times new roman",18,"bold"),bd=3,relief=GROOVE,bg="chocolate1")
title1.pack(side=TOP,fill=X)

p1=PhotoImage(file='titlelogo.png')
dt1.iconphoto(False,p1)

titleeye= Label(dt1,text="Eyes:",font=('Times New roman',16))
labeleye= Label(dt1,text="Fish, Nuts and legumes, Seeds, Citrus fruits, Leafy green vegetables, Carrots, Sweet potatoes, Eggs, Water",font=('times new roman',14))

titleskin= Label(dt1,text="Skin:",font=('Times New roman',16))
labelskin=Label(dt1,text="Fatty fish, Avocados, Walnuts, Sunflower seeds, Sweet potatoes, Broccoli, Tomatoes, Dark chocolate, Green tea",font=('times new roman',14))

titleheart= Label(dt1,text="Heart:",font=('Times New roman',16))
labelheart=Label(dt1, text="Fresh Herbs, Black Beans, Red Wine, Olive Oil, Walnuts, Almonds, Sweet Potatoes, Oranges, Low-Fat Yogurt, Dark Leafy Greens.",font=('times new roman',14))

titleliver= Label(dt1,text="Liver:",font=('Times New roman',16))
labelliver=Label(dt1,text="Coffee, Grapefruit, Blueberries and cranberries, Beetroot juice, Cruciferous vegetables, Nuts, Olive oil",font=('times new roman',14))

titlehair= Label(dt1,text="Hair:",font=('Times New roman',16))
labelhair= Label(dt1,text="Eggs, Berries, Spinach, Fatty fish, Sweet potatoes, Avocados, Nuts, Beans",font=('times new roman',14))

titleeye.place(x=10,y=50)
labeleye.place(x=10,y=80)

titleskin.place(x=10,y=120)
labelskin.place(x=10,y=150)

titleheart.place(x=10,y=200)
labelheart.place(x=10,y=230)

titleliver.place(x=10,y=280)
labelliver.place(x=10,y=310)

titlehair.place(x=10,y=350)
labelhair.place(x=10,y=380)

dietrec=Button(dt1, text="Back to menu",width=20,height=2,command= recommend)
dietrec.place(x=900,y=440)

dt1.mainloop()