import wolframalpha
import wikipedia
from tkinter import *
import speech_recognition as sr

while True:
    r=sr.Recognizer()  ##Taking input from user using speech recognition library

    with sr.Microphone() as source:
        print('Listening🔊🔊....')
        audio=r.listen(source)

        try:
            print('Recognizing...')
            text=r.recognize_google(audio)  ##Converting audio into text form
            print('You said : ' +text)
            if text=='STOP':
                break
            else :
                window=Tk()
                window.title('Personal Assistant')
                window.geometry('500x500')

                try:
                    app_id='YAX9ER - 936J5U9W64'
                    client=wolframalpha.Client(app_id)
                    res = client.query(text)
                    answer=next(res.results).text
                    print("Answer from Wolfram|Alpha : ")
                    print(answer)

                    label1=Label(window,justify=LEFT,compound=CENTER,padx=10,text=answer,font=('Times New Roman Bold',5))
                    label1.pack()
                    window.after(5000,lambda : window.destroy())
                    mainloop()
                except Exception as e:
                    print("No results from Wolfram|Alpha. Trying wikipedia...")
                    answer=wikipedia.summary(text)
                    print("Answer from Wikipedia : ")
                    print(answer)

                    label1=Label(window,justify=LEFT,compound=CENTER,padx=10,text=answer,font='times 15 bold')
                    label1.pack()
                    window.after(500000,lambda : window.destroy())
                    mainloop()
        except Exception as e:
            print(e)
            answer='Sorry we cannot hear you'
            print(answer)






