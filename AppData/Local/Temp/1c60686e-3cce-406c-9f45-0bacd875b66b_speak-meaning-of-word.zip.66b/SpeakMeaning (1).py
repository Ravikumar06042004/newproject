#Importing modules
from tkinter import *
import pyttsx3
from PyDictionary import PyDictionary

def speak(audio):
    # Having the initial constructor of pyttsx3
    # and having the sapi5 in it as a parameter
    engine = pyttsx3.init('sapi5')

    # Calling the getter and setter of pyttsx3
    voices = engine.getProperty('voices')

    # Method for the speaking of the the assistant
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
def meaning():
    dic = PyDictionary()
    # Taking the string input
    query = str(text.get())
    word = dic.meaning(query)
    res=''
    for state in word:
        res+=(str(word[state][0]))+'\n'
        spokenText.set(res)
        speak("the meaning  is" + str(word[state])) 
        
#Creating the window 
wn = Tk() 
wn.title("DataFlair Dictionary")
wn.geometry('700x500')
wn.config(bg='SlateGray1')

#Creating the variables to get the word and set the correct word
text=StringVar(wn)
spokenText =StringVar(wn)

#The main label
Label(wn, text='DataFlair - Speak the Meaning',bg='SlateGray1',
  fg='gray30', font=('Times', 20,'bold')).place(x=100, y=10)

#Getting the input of word from the user
Label(wn, text='Please enter the word',bg='SlateGray1',font=('calibre',13,'normal'), anchor="e", justify=LEFT).place(x=20, y=70)

Entry(wn,textvariable=text, width=35,font=('calibre',13,'normal')).place(x=20,y=110)

#Label to show the correct word
queryLabel = Label(wn, textvariable=spokenText, bg='SlateGray1',anchor="e",font=('calibre',13,'normal'), justify=LEFT,wraplengt=500).place(x=20, y=130)
spokenText.set("Which word do u want to find the meaning sir/madam")
speak("Which word do u want to find the meaning sir or madam")

#Button to do the spell check
Button(wn, text="Speak Meaning", bg='SlateGray4',font=('calibre', 13),
   command=meaning).place(x=230, y=350)

#Runs the window till it is closed by the user
wn.mainloop()
