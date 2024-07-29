import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import pymysql

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
    #window1.destroy()
    import register_page

def onclick_forgot():
    #window1.destroy()
    import forgot_password

def onclick_exit():
    window1.quit()

splash_screen= Tk()
splash_screen.geometry("990x560+50+40")
splash_screen.title("splash screen")
splash_screen.configure(bg='chocolate1')
p1=PhotoImage(file='titlelogo.png')
splash_screen.iconphoto(False,p1)

#splash_screen.eval('tk::PlaceWindow . center')

#words= Label(splash_screen,text='Splash Screen',font=20)
#words.pack()
bgimage = ImageTk.PhotoImage(file='splash_logo-removebg-preview.png')
bglabel = Label(splash_screen,image=bgimage,bd=0)
bglabel.place(relx=0.5, rely=0.5,anchor=CENTER)


def loginpage():
# GUI window code
    splash_screen.destroy()
    global window1
    window1 = tk.Tk()
    window1.title('Login Page')
    window1.geometry('990x560+50+40')
    #window1.iconbitmap("mainlogo.png")
    #window1.eval('tk::PlaceWindow . center')

    p1=PhotoImage(file='titlelogo.png')
    window1.iconphoto(False,p1)

    

    # create heading title text
    title1=Label(window1,bd=10,relief=RIDGE,text="Be Fit",font=("times new roman",25,"bold"),bg='chocolate1')
    title1.pack(side=TOP,fill=X)



    # create username label and entry
    username_label = Label(window1, text='Username:',font=("times new roman",12))
    username_label.pack()
    global username_entry 
    username_entry = tk.Entry(window1)
    username_entry.pack()

    # create password label and entry
    password_label = Label(window1, text='Password:',font=("times new roman",12))
    password_label.pack()
    global password_entry 
    password_entry = tk.Entry(window1, show='*')
    password_entry.pack()

    message_label = Label(window1, text='')
    message_label.pack()

    # create login button
    login_button = Button(window1, text='Login', command=login)
    login_button.pack()

    # create message label
    
    message_label = Label(window1, text='')
    message_label.pack()

    # for forgot password
    forgot_lable = Label(window1, text='Forgot password?')
    forgot_lable.place(x=50,y=210)

    # create a recover button for forgot password
    forgot_button = Button(window1, text='Recover',bd=0,fg='blue' ,command= onclick_forgot)
    forgot_button.place(x=200,y=210)

    # create message lable for register
    register_lable = Label(window1, text='New here? Register now!')
    register_lable.place(x=50,y=250)

    # create a register button
    register_button = Button(window1, text='Register',bd=0,fg='blue' ,command= onclick_register)
    register_button.place(x=200,y=250)

    exit_button = Button(window1, text='Exit',bd=2 ,command= onclick_exit)
    exit_button.pack()

    bottomrighttriangle = ImageTk.PhotoImage(file='bottomtri.jpg')
    bglabeltriangle = Label(window1,image=bottomrighttriangle)
    bglabeltriangle.place(x=900,y=500)

splash_screen.after(2000,loginpage)
mainloop()