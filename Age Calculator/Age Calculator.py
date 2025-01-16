from tkinter import *
from datetime import date

root =Tk()
root.geometry('800x600')
root.resizable(False,False)
root.title('Age Calculator')
#image
photo=PhotoImage(file='age.png')
myimage=Label(image=photo)
myimage.pack(padx=15,pady=15)
#text
Label(
    text='Name',
    font=23,
).place(x=200,y=250)
Label(
    text='Year',
    font=23,
).place(x=200,y=300)
Label(
    text='Month',
    font=23,
).place(x=200,y=350)
Label(
    text='Day',
    font=23,
).place(x=200,y=400)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(
    master=root,
    textvariable=nameValue,
    width=30,
    bd=3,
    font=20
)
nameEntry.place(x=300,y=250)

yearEntry=Entry(
    master=root,
    textvariable=yearValue,
    width=30,
    bd=3,
    font=20
)
yearEntry.place(x=300,y=300)

monthEntry=Entry(
    master=root,
    textvariable=monthValue,
    width=30,
    bd=3,
    font=20
)
monthEntry.place(x=300,y=350)

dayEntry=Entry(
    master=root,
    textvariable=dayValue,
    width=30,
    bd=3,
    font=20
)
dayEntry.place(x=300,y=400)

root.mainloop()