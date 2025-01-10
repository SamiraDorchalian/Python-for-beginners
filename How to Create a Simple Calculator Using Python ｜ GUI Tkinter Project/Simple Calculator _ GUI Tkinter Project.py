import tkinter
from tkinter import *

root=Tk()
root.title('Simple Calculatoe')
root.geometry('570x600+100+200')
root.resizable(False,False)
root.configure(bg='#17161b')


label_result= Label(
    master=root,
    height=2,
    font=('arial',30)
)
label_result.pack()
# sign : 'C' & '/' & '%' & '*'
Button(
    master=root,
    text='C',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#3697f5'
).place(x=10,y=100)
Button(
    master=root,
    text='/',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=150,y=100)
Button(
    master=root,
    text='%',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=290,y=100)
Button(
    master=root,
    text='*',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=430,y=100)
# numbers : '7' & '8' & '9' sign : '-'
Button(
    master=root,
    text='7',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=10,y=200)
Button(
    master=root,
    text='8',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=150,y=200)
Button(
    master=root,
    text='9',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=290,y=200)
Button(
    master=root,
    text='-',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=430,y=200)
# numbers : '4' & '5' & '6' sign : '+'
Button(
    master=root,
    text='4',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=10,y=300)
Button(
    master=root,
    text='5',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=150,y=300)
Button(
    master=root,
    text='6',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=290,y=300)
Button(
    master=root,
    text='+',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=430,y=300)
# numbers : '1' & '2' & '3' & '0'
Button(
    master=root,
    text='1',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=10,y=400)
Button(
    master=root,
    text='2',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=150,y=400)
Button(
    master=root,
    text='3',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=290,y=400)
Button(
    master=root,
    text='0',
    width=11,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=10,y=500)
# sign '.' & '='
Button(
    master=root,
    text='.',
    width=5,
    height=1,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#2a2d36'
).place(x=290,y=500)
Button(
    master=root,
    text='=',
    width=5,
    height=3,
    font=('arial', 30, 'bold'),
    bd=1,
    fg='#fff',
    bg='#fe9037'
).place(x=430,y=400)

root.mainloop()