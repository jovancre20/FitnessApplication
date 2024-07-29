import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import pymysql
import login_page as lp

#Function used in registration page

def clearbutton():
            reg_input1.delete(0,END)
            reg_input2.delete(0,END)
            reg_input3.delete(0,END)
            reg_input4.delete(0,END)
            reg_input5.delete(0,END)
            reg_input6.delete(0,END)

def howdy():
        name=reg_input1.get()
        phno=reg_input2.get()
        username=reg_input3.get()
        email=reg_input6.get()
        pass1=reg_input4.get()
        pass2=reg_input5.get()
        if name=='' or phno=='' or username=='' or email=='' or pass1=='' or pass2=='':
            messagebox.showerror("Error","All fields required")
        elif pass1 != pass2:
            messagebox.showerror('Error','Password has been mismatched') 
        elif len(pass1) <=5:
            messagebox.showinfo('Password lenght','Password lenght should be atleast 5 characters')
        else:
              try:
                con=pymysql.connect(host='localhost',user='root',password='')
                mycursor=con.cursor()
              except:
                    messagebox.showerror('Error','Database connectivity issue, Please try again!')
                    return
              try:
                 query='create database userdata'
                 mycursor.execute(query)
                 query='use userdata'
                 mycursor.execute(query)
                 query='create table data(id int auto_increment primary key not null, name varchar(50), phoneno varchar(50), email varchar(50), username varchar(50), password varchar(50))'
                 mycursor.execute(query)
              except:
                 mycursor.execute('use userdata')

        query='select * from data where username=%s'
        mycursor.execute(query,(reg_input3.get()))

        duplicate_username=mycursor.fetchone()
        if duplicate_username != None:
             messagebox.showerror('Error','Username Already exists')

        else:
            query='insert into data(name,phoneno,email,username,password) values(%s,%s,%s,%s,%s)'
            mycursor.execute(query,(reg_input1.get(),reg_input2.get(),reg_input6.get(),reg_input3.get(),reg_input4.get()))
            #mycursor.execute(query,(name,phno,email,username,pass1))
            con.commit()
            con.close()
            messagebox.showinfo('Confirmation','You have been registered successfully!')
            clearbutton()
            window2.destroy()
            import login_page



def window_login():
    window2.destroy()
    import login_page


# GUI of registration page
# create window2
#window2 = Tk()
window2 = Toplevel(lp.window1)
window2.title('Registration Page')
window2.geometry("500x400")

p1=PhotoImage(file='titlelogo.png')
window2.iconphoto(False,p1)

# title page of registration page 
title2=Label(window2,text="Registration",font=("times new roman",20,"bold"),bd=5,relief=GROOVE,bg='chocolate1')
title2.pack(side=TOP,fill=X)


# create what details to input while registration
reg_lable1=tk.Label(window2, text="Enter your name:",font=("times new roman",12))
reg_input1=tk.Entry(window2)
reg_lable1.place(x=40,y=50)
reg_input1.place(x=250,y=50)

reg_lable2=tk.Label(window2, text="Enter your phone number:",font=("times new roman",12))
reg_input2=tk.Entry(window2)
reg_lable2.place(x=40,y=80)
reg_input2.place(x=250,y=80)

reg_lable6=tk.Label(window2, text="Enter your email:",font=("times new roman",12))
reg_input6=tk.Entry(window2)
reg_lable6.place(x=40,y=110)
reg_input6.place(x=250,y=110)

reg_lable3=tk.Label(window2, text="Enter your username:",font=("times new roman",12))
reg_input3=tk.Entry(window2)
reg_lable3.place(x=40,y=140)
reg_input3.place(x=250,y=140)

reg_lable4=tk.Label(window2, text="Enter your password:",font=("times new roman",12))
reg_input4=tk.Entry(window2, show='*')
reg_lable4.place(x=40,y=170)
reg_input4.place(x=250,y=170)

reg_lable5=tk.Label(window2, text="Confirm your password:",font=("times new roman",12))
reg_input5=tk.Entry(window2, show='*')
reg_lable5.place(x=40,y=200)
reg_input5.place(x=250,y=200)
    


#create a register button
register_button = tk.Button(window2, text='Register', command=howdy)
register_button.place(x=100,y=240)
    
#create a button which clears all text fields in registration page
clear_button = tk.Button(window2, text='Clear', command=clearbutton)
clear_button.place(x=200,y=240)


# back to login from register page
backtologin_button = tk.Button(window2, text ="Return to login page", command = window_login, width=20)
backtologin_button.place(x=100,y=300)

bottomrighttriangle = ImageTk.PhotoImage(file='bottomtri-removebg-preview-removebg-preview.png')
bglabeltriangle = Label(window2,image=bottomrighttriangle)
bglabeltriangle.place(relx=1.0, rely=1.0, x=0, y=0, anchor=SE)

    
      
# start of window2
window2.mainloop()
