from tkinter import *
from tkinter import messagebox
import os

def login():
    user=username.get()
    code=password.get()

    if user == 'samira' and code =='1024':
        root=Toplevel(screen)
        root.title('Bill')
        root.geometry('1000x500')
        root.configure(bg='#d7dae2')
        root.resizable(False,False)
        
        def Reset():
            entry_dosa.delete(0,END)
            entry_cookies.delete(0,END)
            entry_tea.delete(0,END)
            entry_coffee.delete(0,END)
            entry_juice.delete(0,END)
            entry_pancakes.delete(0,END)
            entry_eggs.delete(0,END)
        def Total():
            try: a1=int(dosa.get())
            except: a1=0

            try: a2=int(cookies.get())
            except: a2=0
            
            try: a3=int(tea.get())
            except: a3=0
            
            try: a4=int(coffee.get())
            except: a4=0
            
            try: a5=int(juice.get())
            except: a5=0
            
            try: a6=int(pancakes.get())
            except: a6=0
            
            try: a7=int(eggs.get())
            except: a7=0

            #define cost of each item per quantity
            c1=60*a1
            c2=30*a2
            c3=7*a3
            c4=100*a4
            c5=20*a5
            c6=15*a6
            c7=7*a7
            #label Total
            lbl_total=Label(f2,font=('aria',20,'bold'),text='Total',width=16,fg='lightyellow',bg='black')
            lbl_total.place(x=0,y=50)

            entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg='lightgreen')
            entry_total.place(x=20,y=100)

            totalcost=c1+c2+c3+c4+c5+c6+c7
            string_bill='Rs.',str('%.2f' %totalcost)
            Total_bill.set(string_bill)

        #Label Header
        Label(root,text='BILL MANAGEMENT',bg='black',fg='white',font=('calibri',33),width='300',height='2',).pack()
        # MENU CARD
        f=Frame(master=root,bg='lightgreen',highlightbackground='black',highlightthickness=1,width=300,height=370,)
        f.place(x=10,y=118)
        #Label Menu
        Label(f,text='Menu',font=('Gabriola',40,'bold'),fg='black',bg='lightgreen').place(x=80,y=0)
        #Label Texts 
        Label(f,font=('Lucida Calligraphy',15,'bold'),text='Dosa.......Rs.60/plate',fg='black',bg='lightgreen',).place(x=10,y=80)
        Label(f,font=('Lucida Calligraphy',15,'bold'),text='Cookies.......Rs.30/plate',fg='black',bg='lightgreen',).place(x=10,y=110)
        Label(f,font=('Lucida Calligraphy',15,'bold'),text='Tea.......Rs.7/cup',fg='black',bg='lightgreen',).place(x=10,y=140)
        Label(f,font=('Lucida Calligraphy',15,'bold'),text='Coffee.......Rs.100/cup',fg='black',bg='lightgreen',).place(x=10,y=170)
        Label(f,font=('Lucida Calligraphy',15,'bold'),text='Juice.......Rs.20/glass',fg='black',bg='lightgreen',).place(x=10,y=200)
        Label(f,font=('Lucida Calligraphy',15,'bold'),text='Pancakes.......Rs.15/pack',fg='black',bg='lightgreen',).place(x=10,y=230)
        Label(f,font=('Lucida Calligraphy',15,'bold'),text='Eggs.......Rs.7/egg',fg='black',bg='lightgreen',).place(x=10,y=260)

        #BILL
        f2=Frame(root,bg='lightyellow',highlightbackground='black',highlightthickness=1,width=300,height=370)
        f2.place(x=690,y=118)

        Bill=Label(f2,text='Bill',font=('calibri',20),bg='lightyellow')
        Bill.place(x=120,y=10)

        #ENTRY WORK
        f1=Frame(master=root,bd=5,height=370,width=300,relief=RAISED,)
        f1.pack()

        dosa=StringVar()
        cookies=StringVar()
        tea=StringVar()
        coffee=StringVar()
        juice=StringVar()
        pancakes=StringVar()
        eggs=StringVar()
        Total_bill=StringVar()
        #Label
        lbl_dosa=Label(f1,font=('aria',20,'bold'),text='Dosa',width=12,fg='blue4')
        lbl_cookies=Label(f1,font=('aria',20,'bold'),text='Cookies',width=12,fg='blue4')
        lbl_tea=Label(f1,font=('aria',20,'bold'),text='Tea',width=12,fg='blue4')
        lbl_coffee=Label(f1,font=('aria',20,'bold'),text='Coffee',width=12,fg='blue4')
        lbl_juice=Label(f1,font=('aria',20,'bold'),text='Juice',width=12,fg='blue4')
        lbl_pancakes=Label(f1,font=('aria',20,'bold'),text='Pancakes',width=12,fg='blue4')
        lbl_eggs=Label(f1,font=('aria',20,'bold'),text='Eggs',width=12,fg='blue4')
        lbl_dosa.grid(row=1,column=0)
        lbl_cookies.grid(row=2,column=0)
        lbl_tea.grid(row=3,column=0)
        lbl_coffee.grid(row=4,column=0)
        lbl_juice.grid(row=5,column=0)
        lbl_pancakes.grid(row=6,column=0)
        lbl_eggs.grid(row=7,column=0)

        Entry
        entry_dosa=Entry(f1,font=('aria',20,'bold'),textvariable=dosa,bd=6,width=8,bg='lightpink')
        entry_cookies=Entry(f1,font=('aria',20,'bold'),textvariable=cookies,bd=6,width=8,bg='lightpink')
        entry_tea=Entry(f1,font=('aria',20,'bold'),textvariable=tea,bd=6,width=8,bg='lightpink')
        entry_coffee=Entry(f1,font=('aria',20,'bold'),textvariable=coffee,bd=6,width=8,bg='lightpink')
        entry_juice=Entry(f1,font=('aria',20,'bold'),textvariable=juice,bd=6,width=8,bg='lightpink')
        entry_pancakes=Entry(f1,font=('aria',20,'bold'),textvariable=pancakes,bd=6,width=8,bg='lightpink')
        entry_eggs=Entry(f1,font=('aria',20,'bold'),textvariable=eggs,bd=6,width=8,bg='lightpink')
        entry_dosa.grid(row=1,column=1)
        entry_cookies.grid(row=2,column=1)
        entry_tea.grid(row=3,column=1)
        entry_coffee.grid(row=4,column=1)
        entry_juice.grid(row=5,column=1)
        entry_pancakes.grid(row=6,column=1)
        entry_eggs.grid(row=7,column=1)

        #buttons
        btn_reset=Button(f1, bd=5,fg='black', bg='lightblue',font=('ariel',16,'bold'),width=10,text='Reset',command=Reset)
        btn_reset.grid(row=8,column=0)

        btn_total=Button(f1,bd=5,fg='black',bg='lightblue',font=('ariel',16,'bold'),width=10,text='Total',command=Total)
        btn_total.grid(row=8,column=1)


    elif user=='' and code=='':
        messagebox.showerror('Invalid','Please enter Username and Password')
    elif user=='':
        messagebox.showerror('Invalid','Username is required')
    elif code=='':
        messagebox.showerror('Invalid','The Password field is required')
    elif user!='samira' and code!='1024':
        messagebox.showerror('Invalid','invalid Username and Password')
    elif user!='samira':
        messagebox.showerror('Invalid','Please enter a valid username')
    elif code!='1024':
        messagebox.showerror('Invalid','Please enter a valid Password ')

def main_screen():

    global screen
    global username
    global password

    screen=Tk()
    screen.geometry('1000x680+100+40')
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
    Button(mainframe,text="login",height='2',width=23,bg='#ed3833',fg='white',bd=0,command=login).place(x=100,y=250)
    Button(mainframe,text="Reset",height='2',width=23,bg='#1089ff',fg='white',bd=0,command=reset).place(x=300,y=250)
    Button(mainframe,text="Exit",height='2',width=23,bg='#00bd56',fg='white',bd=0,command=screen.destroy).place(x=500,y=250)

    screen.mainloop()

main_screen()



