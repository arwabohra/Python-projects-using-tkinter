import sys
from tkinter import *
import time

def times():
    current_time=time.strftime('%H:%M:%S')
    clock.config(text=current_time)
    clock.after(200,times)

root=Tk()
root.geometry('500x300')
root.configure(bg='black')
root.title('Digital Clock')
clock=Label(root,font=('Arial Bold',50),bg='black',foreground='white')
clock.grid(row=2,column=2,padx=100,pady=25)
times()

digital_clock=Label(root,text='Digital Clock',font=('Arial Bold',20),bg='black',foreground='white')
digital_clock.grid(row=0,column=2)

notations=Label(root,font=('Arial Bold',20),text='    Hours  Minutes  Seconds',bg='black',foreground='white')
notations.grid(row=3,column=2)

root.mainloop()



