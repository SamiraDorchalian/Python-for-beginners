#pip install pyttsx3
import tkinter as tk
from tkinter import *
import pyttsx3 #pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

engine=pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

root=Tk()

textv=StringVar()

obj=LabelFrame(
    master=root,
    text='Text to speech',
    font=20,
    bd=1
)
obj.pack(fill='both',expand='yes',padx=10,pady=10)

lbl=Label(
    master=obj,
    text='Text',
    font=30
)
lbl.pack(side=tk.LEFT,padx=5)

text=Entry(
    master=obj,
    textvariable=textv,
    font=30,
    width=25,
    bd=5
)
text.pack(side=tk.LEFT,padx=10)

btn=Button(
    master=obj,
    text='Speak',
    font=20,
    bg='black',
    fg='white',
    command=speaknow,
)
btn.pack(side=tk.LEFT,padx=10)

root.title('Text To Speech')
root.geometry('400x200')
root.resizable(False,False) #resizable() method is used to allow Tkinter root window to change it’s size according to the users need as well we can prohibit resizing of the Tkinter window.
                            #So, basically, if user wants to create a fixed size window, this method can be used.
root.mainloop()