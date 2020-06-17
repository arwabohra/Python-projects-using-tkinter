import os
from tkinter import *
from tkinter.filedialog import *
import pygame
from mutagen.easyid3 import EasyID3

window=Tk()
window.geometry('700x500')
window.title('Music Player')

pygame.mixer.init()
n=0

def start_stop():
    global n
    n=n+1
    if n==1:
        song_name=songs_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)
    elif (n%2)==0:
        pygame.mixer.music.pause()
    elif (n%2)!=0:
        pygame.mixer.music.unpause()

def previous_song():
    global n
    n -= 1

    songs_listbox.set(songs_list[n])
    pygame.mixer.music.load(songs_list[n])
    pygame.mixer.music.play()
    if songs_list[n]==len(songs_list):
        songs_list[n]=songs_list[n-1]
        pygame.mixer.music.load(songs_list[n])
        pygame.mixer.music.play()

    ##updatelabel()

def next_song():
    global n
    n += 1
    songs_listbox.set(songs_list[n])
    pygame.mixer.music.load(songs_list[n])
    pygame.mixer.music.play()


l1=Label(window,text='MUSIC PLAYER',font=('Arial Bold',20))
l1.grid(row=1,column=1)

b1=Button(window,text='||',width=10,command=start_stop)
b1.grid(row=6,column=2)

b1=Button(window,text='<',width=10,command=previous_song)
b1.grid(row=6,column=1)

b1=Button(window,text='>',width=10,command=next_song)
b1.grid(row=6,column=3)

songs_list=os.listdir()
songs_listbox=StringVar(window)
songs_listbox.set('Select Songs')
menu=OptionMenu(window,songs_listbox,*songs_list)
menu.grid(row=25,column=2)


window.mainloop()



