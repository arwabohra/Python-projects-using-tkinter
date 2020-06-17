from tkinter import *
import time
import requests
import json

root=Tk()
root.geometry("600x250")
root.title('Live Cricket Score')

match_data=requests.get('http://cricapi.com/api/cricketScore?unique_id=--paste your unique id here--')
json_data=match_data.json()

def times():
	current_score=json_data['stat']
	score.configure(text="Current score :  "+current_score)
	score.after(200,times)

score=Label(root,font=("time",15,"bold"),bg="white")
score.grid(row=2,column=2,pady=25,padx=50)
times()

root.mainloop()

