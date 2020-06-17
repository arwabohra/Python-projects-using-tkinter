import sqlite3
from tkinter import *

window=Tk()
window.title('Home Screen')
window.geometry('350x300')

def login():

    def login_database():
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * from HOME where Email=? AND Password=?',(e1.get(),e2.get()))
        row=cursor.fetchall()
        conn.close()
        print(row)
        if row!=[]:
            username=row[0][1]
            l3.config(text='User name found with name :'+username)
        else:
            l3.config(text='Username not found')


    window.destroy()
    login_window=Tk()
    login_window.geometry('550x250')
    login_window.title('Login')
    l1=Label(login_window,text='Email-Id',font=('Arial Bold',15))
    l1.grid(row=1,column=1)
    l2=Label(login_window,text='Password',font=('Arial Bold',15))
    l2.grid(row=2,column=1)
    l3=Label(login_window,font=('Arial Bold',15))
    l3.grid(row=3,column=2)

    email_text = StringVar()
    e1 = Entry(login_window, textvariable=email_text, width=25)
    e1.grid(row=1, column=2)
    password_text = StringVar()
    e2 = Entry(login_window, textvariable=password_text, width=25)
    e2.grid(row=2, column=2)

    b1=Button(login_window,text='Login',width=20,command=login_database)
    b1.grid(row=4,column=2)
    login_window.mainloop()

def signup():

    def signup_database():

        conn=sqlite3.connect('test.db')
        cursor=conn.cursor()
        cursor.execute('CREATE table if not exists HOME(Id INTEGER PRIMARY KEY,Name text,Email text,Password text)')
        cursor.execute('INSERT into HOME values(NULL,?,?,?)',(e1.get(),e2.get(),e3.get()))
        l4=Label(signup_window,text='Account Created',font=('Arial Bold',15))
        l4.grid(row=6,column=2)
        conn.commit()
        cursor = conn.execute("SELECT Id, Name, Email, Password from HOME")
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("EMAIL = ", row[2])
            print("PASSWORD = ", row[3], "\n")
        conn.close()

    window.destroy()
    signup_window=Tk()
    signup_window.geometry('400x250')
    signup_window.title('Sign Up')
    l1=Label(signup_window,text='User name',font=('Arial Bold',15))
    l1.grid(row=1,column=1)
    l2=Label(signup_window,text='Email-Id',font=('Arial Bold',15))
    l2.grid(row=2,column=1)
    l3=Label(signup_window,text='Password',font=('Arial Bold',15))
    l3.grid(row=3,column=1)

    name_text=StringVar()
    e1=Entry(signup_window,textvariable=name_text,width=25)
    e1.grid(row=1,column=2)
    email_text = StringVar()
    e2 = Entry(signup_window, textvariable=email_text,width=25)
    e2.grid(row=2, column=2)
    password_text = StringVar()
    e3 = Entry(signup_window, textvariable=password_text,width=25)
    e3.grid(row=3, column=2)

    b1=Button(signup_window,text='Login',width=20,command=signup_database)
    b1.grid(row=4,column=2)

l1=Label(window,text='What do you want to do ?',font=('Arial',20))
l1.grid(row=1,column=2,columnspan=2)

b1=Button(window,text='Login',font=('Arial',16),command=login)
b1.grid(row=2,column=2)

b2=Button(window,text='Signup',font=('Arial',16),command=signup)
b2.grid(row=2,column=3)

window.mainloop()

