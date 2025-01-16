from tkinter import *
from tkinter import messagebox

root= Tk()
root.title('Login')
root.geometry('300x200')

global entry1
global entry2

def login():
    username=entry1.get()
    password=entry2.get()

    if(username == '' and password==''):
        messagebox.showinfo('','Blank Not Allowed')
    elif(username=='Samira' and password=='admin'):
        messagebox.showinfo('','login success')
    else:
        messagebox.showinfo('','incorrect username and password')

Label(
    master=root,
    text='Username',
).place(x=20,y=20)
Label(
    master=root,
    text='Password',
).place(x=20,y=70)

entry1=Entry(
    master=root,
    bd=5
)
entry1.place(x=140,y=20)

entry2=Entry(
    master=root,
    bd=5
)
entry2.place(x=140,y=70)

Button(
    root,
    text="Login",
    command=login,
    height=3,
    width=13,
    bd=6
).place(x=100,y=120)

root.mainloop()