from selenium import webdriver  ##Selenium is used for login and js lines for scrolling of the screen
from selenium.webdriver.common.keys import Keys
import time
import pyautogui ## pyautogui is used to click on heart button to like the tweet
from tkinter import *

class twitter_bot:
	def __init__(self,username,password):
		self.username=username
		self.password=password
		self.bot=webdriver.Firefox()


	def login(self):
		bot=self.bot
		bot.get('https://twitter.com/')
		time.sleep(5)
		email=bot.find_element_by_name('session[username_or_email]')
		password=bot.find_element_by_name('session[password]')
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(10)


	def like_tweet(self,entry3):
		bot=self.bot
		bot.get('https://twitter.com/search?q='+str(entry3)+'&src=typed_query')
		while True:

			bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
			time.sleep(2)
			pyautogui.click(pyautogui.locateCenterOnScreen('1.png'),duration=2)
			time.sleep(3)

def execute():
	log=twitter_bot(str(entry1.get()),str(entry2.get()))
	log.login()
	log.like_tweet(entry3.get())

window=Tk()
window.geometry("450x250")
window.title('Twitter')
window.configure(bg='Midnight Blue')
emails=Label(window,text="Enter your email here ",font='Arial  12 bold',bg='Midnight blue',foreground='Light Blue')
emails.grid(row=5,column=0)
entry1=Entry(window)
entry1.configure(width=30)
entry1.grid(row=5,column=3,padx=5,pady=10)


password=Label(window,text="Enter your password here ",font='Arial 12 bold',bg='Midnight blue',foreground='Light Blue')
password.grid(row=7,column=0)
entry2=Entry(window)
entry2.configure(width=30)
entry2.grid(row=7,column=3,padx=5,pady=10)


hashtag=Label(window,text="Enter the hashtag ",font='Arial 12 bold',bg='Midnight blue',foreground='Light Blue')
hashtag.grid(row=10,column=0)
entry3=Entry(window)
entry3.configure(width=30)
entry3.grid(row=10,column=3,padx=5,pady=10)

b1=Button(window,text=" GO ",command=execute,width=12,bg='Light Blue',foreground='Midnight blue',font='Arial 12 bold',
		  activebackground='Midnight blue',activeforeground='Light Blue')
b1.grid(row=20,column=3)
window.mainloop()


