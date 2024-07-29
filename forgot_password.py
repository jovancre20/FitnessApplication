import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import pymysql
import login_page as lp

#function part

def changepass():
    if username_entry.get=='' or password_entry.get=='' or confpassword_entry.get()=='':
        messagebox.showerror('Error','All fields required',parent=window1)
    elif password_entry.get() != confpassword_entry.get():
         messagebox.showerror('Error','Password or confirm password not matched',parent=window1)
    else:
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s'
        mycursor.execute(query,(username_entry.get()))
        row= mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username',parent=window1)
        else:
            query= 'update data set password=%s where username=%s'
            mycursor.execute(query,(password_entry.get(),username_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Successfull','Your Password has been changed successfull! Please try to log in again',parent=window1)
            window1.destroy()
            import login_page
        

def window_login():
    window1.destroy()
    import login_page



#gui part
window1=Toplevel(lp.window1)
window1.geometry('400x400')
window1.title('Reset password')

p1=PhotoImage(file='titlelogo.png')
window1.iconphoto(False,p1)

title1=Label(window1,bd=10,relief=RIDGE,text="Reset Password",font=("times new roman",25,"bold"),bg='chocolate1')
title1.pack(side=TOP,fill=X)


# create username label and entry
username_label = tk.Label(window1, text='Username:',font=("times new roman",12))
username_label.pack()
#global username_entry 
username_entry = tk.Entry(window1)
username_entry.pack()

space1 = Label(window1, text='')
space1.pack()

# create password label and entry
password_label = tk.Label(window1, text='New Password:',font=("times new roman",12))
password_label.pack()
password_entry = tk.Entry(window1, show='*')
password_entry.pack()

space2 = Label(window1, text='')
space2.pack()

confpassword_label = tk.Label(window1, text='Confirm Password:',font=("times new roman",12))
confpassword_label.pack()
confpassword_entry = tk.Entry(window1, show='*')
confpassword_entry.pack()

space3 = Label(window1, text='')
space3.pack()

# create login button
login_button = tk.Button(window1, text='Submit',command=changepass)
login_button.pack()

backtologin_button = tk.Button(window1, text ="Return to login page", command = window_login, width=20)
backtologin_button.place(x=125,y=300)


window1.mainloop()