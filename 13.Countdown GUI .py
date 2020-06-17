from tkinter import *

window=Tk()
window.title('Countdown GUI')
window.geometry('300x200')

t=0

def set_timer():

    global t
    t=t+int(e1.get())
    return t

def countdown():

    global t
    if t>0:
        l1.config(text=t)
        t=t-1
        l1.after(1000,countdown)
    elif t==0:
        print('End')
        l1.config(text='GO')

l1=Label(window,font=('Arial bold',15))
l1.grid(row=1,column=2)

times=StringVar()
e1=Entry(window,textvariable=times,width="25")
e1.grid(row=3,column=2,padx=50,pady=20,ipady=4)

b1=Button(window,text='SET',font=('Arial bold',14),command=set_timer)
b1.grid(row=4,column=2,padx=20)

b2=Button(window,text='START',font=('Arial bold',14),command=countdown)
b2.grid(row=6,column=2,padx=20)

window.mainloop()
