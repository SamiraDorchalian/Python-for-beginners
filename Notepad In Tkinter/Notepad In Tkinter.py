from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry('600x600')
root.title('Notepad')
root.config(bg='lightblue')
root.resizable(False,False)
#function save_file
def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

#function open_file
def open_file():
    file=filedialog.askopenfile(mode='r',filetypes=[('text files', '*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)
#Button text(save file)
b1=Button(
    master=root,
    width='20',
    height='2',
    bg='#fff',
    text='save_file',
    command=save_file
).place(x=100,y=5)
#Button text(open file)
b2=Button(
    master=root,
    width='20',
    height='2',
    bg='#fff',
    text='open file',
    command=open_file
).place(x=300,y=5)
#Text Part (write - show)
entry=Text(
    master=root,
    height='33',
    width='72',
    wrap=WORD,
)
entry.place(x=10,y=60)

root.mainloop()