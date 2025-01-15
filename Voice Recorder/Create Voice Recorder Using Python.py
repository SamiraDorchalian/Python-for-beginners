from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry('600x700+400+80')
root.resizable(False,False)
root.title('Voice Recorder')
root.configure(background='#4a4a4a')

#icon
image_icon=PhotoImage(file="Remove.png")
root.iconphoto(False,image_icon)
#logo
photo=PhotoImage(file='Remove.png')
myimage=Label(
    image=photo,
    background='#4a4a4a'
)
myimage.pack(padx=5, pady=5)
#name
Label(
    text='Voice Recorder',
    font='arial 30 bold',
    background='#4a4a4a',
    fg='white'
).pack()
#entry box
duration=StringVar()
entry=Entry(
    master=root,
    textvariable=duration,
    font='arial 30',
    width=15
).pack(pady=10)

root.mainloop()