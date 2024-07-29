import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import pymysql

import random
import datetime
import sqlite3

# functions code
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username=='' or password=='':
        messagebox.showerror("Error","All fields are required")
    
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue, Please try again!')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(username_entry.get(),password_entry.get()))
        row= mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Your login is successfull')
            import personal_details


def onclick_register():
    window1.destroy()
    import register_page

def onclick_forgot():
    window1.destroy()
    import forgot_password

def onclick_exit():
    window1.quit()

# GUI window code
window1 = tk.Tk()
window1.title('Login Page')
window1.geometry('990x560+50+40')
    
    #bgimage = ImageTk.PhotoImage(file='Sonic.jpg')
    #bglabel = Label(window1,image=bgimage)
    #bglabel.place(x=0,y=0)

# create heading title text
title1=Label(window1,bd=10,relief=RIDGE,text="Be Fit",font=("times new roman",25,"bold"))
title1.pack(side=TOP,fill=X)



# create username label and entry
username_label = tk.Label(window1, text='Username:')
username_label.pack()
#global username_entry 
username_entry = tk.Entry(window1)
username_entry.pack()

# create password label and entry
password_label = tk.Label(window1, text='Password:')
password_label.pack()
global password_entry 
password_entry = tk.Entry(window1, show='*')
password_entry.pack()

# create login button
login_button = tk.Button(window1, text='Login', command=login)
login_button.pack()

# create message label
    
message_label = tk.Label(window1, text='')
message_label.pack()

# for forgot password
forgot_lable = tk.Label(window1, text='Forgot password?')
forgot_lable.place(x=50,y=210)

# create a recover button for forgot password
forgot_button = tk.Button(window1, text='Recover',bd=0,fg='blue' ,command= onclick_forgot)
forgot_button.place(x=200,y=210)

# create message lable for register
register_lable = tk.Label(window1, text='New here? Register now!')
register_lable.place(x=50,y=250)

# create a register button
register_button = tk.Button(window1, text='Register',bd=0,fg='blue' ,command= onclick_register)
register_button.place(x=200,y=250)

exit_button = tk.Button(window1, text='Exit',bd=2 ,command= onclick_exit)
exit_button.pack()

    
window1.mainloop()