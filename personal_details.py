import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import pymysql
import login_page as lp

#code for functions
def menu_window():
    if pinfo_age.get()=='' or pinfo_ht.get()=='' or pinfo_wt.get()=='' or text1.get()=='':
        messagebox.showerror('Error','All fields required')
    else:
        try:
                con=pymysql.connect(host='localhost',user='root',password='')
                mycursor=con.cursor()
        except:
                messagebox.showerror('Error','Database connectivity issue, Please try again!')
                return
        try:
                 query='use userdata'
                 mycursor.execute(query)
                 query='create table personal(id int auto_increment primary key not null,Age varchar(3), height varchar(5), weight varchar(5), gender varchar(50))'
                 mycursor.execute(query)
        except:
                 mycursor.execute('use userdata')
    
    query='insert into personal(Age,height,weight,gender) values(%s,%s,%s,%s)'
    mycursor.execute(query,(pinfo_age.get(),pinfo_ht.get(),pinfo_wt.get(),text1.get()))
    con.commit()
    con.close()
    messagebox.showinfo('Confirmation','Your details have been registered successfully!')

    #window3.destroy()
    import main_menu

def ahead_menu():
       import main_menu

#code for gui
window3= Toplevel(lp.window1)
window3.title('Personal Information')
window3.geometry('500x500')

p1=PhotoImage(file='titlelogo.png')
window3.iconphoto(False,p1)

title3=Label(window3,text="Please enter your personal information",font=("times new roman",18,"bold"),bd=5,relief=GROOVE,bg="chocolate1")
title3.pack(side=TOP,fill=X)
    
pinfotext_age=Label(window3, text="Enter your Age:")
pinfo_age=tk.Entry(window3)
pinfotext_age.place(x=40,y=50)
pinfo_age.place(x=200,y=50)

pinfotext_ht=Label(window3, text="Enter your Height:")
pinfo_ht=tk.Entry(window3)
pinfotext_ht.place(x=40,y=80)
pinfo_ht.place(x=200,y=80)

pinfotext_wt=Label(window3, text="Enter your Weight:")
pinfo_wt=tk.Entry(window3)
pinfotext_wt.place(x=40,y=110)
pinfo_wt.place(x=200,y=110)

# create a drop down list for gender
pinfotext_gen=Label(window3, text="Enter your Gender:")
#pinfo_gen=tk.Entry(window3)
pinfotext_gen.place(x=40,y=140)
#pinfo_gen.place(x=200,y=140)

text1 = StringVar()
# Set the value you wish to see by default
text1.set("Choose here")
 
# Create options from the Option Menu
w = OptionMenu(window3, text1, "Male", "Female", "Others")
w.place(x=200,y=140)
    
submit_button = Button(window3, text='Submit', command=menu_window)
submit_button.place(x=100,y=200)

submit_button = Button(window3, text='Go Ahead', command=ahead_menu)
submit_button.place(x=200,y=200)


window3.mainloop()