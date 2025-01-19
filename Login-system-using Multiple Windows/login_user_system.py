from tkinter import *
from tkinter import messagebox
import os

def main_screen():
    screen=Tk()
    screen.geometry('1000x680+150+80')
    screen.configure(bg='#d7dae2')
    #icon
    image_icon=PhotoImage(file='login.png')
    screen.iconphoto(False,image_icon)
    screen.title('Login system')
    #Label Titel
    lbl_Title=Label(text='Login System',font=('arial',50,'bold'),fg='black', bg='#d7dae2')
    lbl_Title.pack(pady=50)
    #Border form
    bordercolor=Frame(screen,bg='black',width=800,height=400)
    bordercolor.pack()
    #Form inside
    mainframe=Frame(bordercolor,bg='#d7dae2',width=800,height=400)
    mainframe.pack(padx=20,pady=20)
    #Label Texts
    Label(mainframe,text='Username',font=('arial',30,'bold'),bg='#d7dae2').place(x=100,y=50)
    Label(mainframe,text='Password',font=('arial',30,'bold'),bg='#d7dae2').place(x=100,y=150)

    username=StringVar()
    password=StringVar()
    #Entry inputs
    entry_username=Entry(mainframe,textvariable=username,width=12,bd=2,font=('arial',30))
    entry_username.place(x=400,y=50)
    entry_password=Entry(mainframe,textvariable=password,width=12,bd=2,font=('arial',30),show='*')
    entry_password.place(x=400,y=150)
    #functions
    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    #Buttons
    Button(mainframe,text="login",height='2',width=23,bg='#ed3833',fg='white',bd=0).place(x=100,y=250)
    Button(mainframe,text="Reset",height='2',width=23,bg='#1089ff',fg='white',bd=0,command=reset).place(x=300,y=250)
    Button(mainframe,text="Exit",height='2',width=23,bg='#00bd56',fg='white',bd=0,command=screen.destroy).place(x=500,y=250)

    screen.mainloop()

main_screen()



