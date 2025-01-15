# pip install textblob

import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title('Spelling checker')
root.geometry('700x400') #Width & Height
root.config(background='#dae6f6')

#Label Text
heading=Label(
    master=root,
    text='Spelling checker',
    font=('Trebuchet MS',30,'bold'),
    bg='#dae6f6',
    fg='#364971'
)
heading.pack(pady=(50,0))
#Input Text
entry_text=Entry(
    master=root,
    justify='center',
    width=30,
    font=('poppins',25),
    bg='white',
    border=2
)
entry_text.pack(pady=10)
entry_text.focus()
#Button
button=Button(
    master=root,
    text='Check',
    font=('arial',20,'bold'),
    fg='white',
    bg='red',
)
button.pack()
#Label spell
spell=Label(
    master=root,
    font=('poppins',20),
    bg='#dae6f6',
    fg='#364971',
)
spell.place(x=350,y=250)

root.mainloop()