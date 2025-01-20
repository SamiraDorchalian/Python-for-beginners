#pip install tkPDFViewer

from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os

root=Tk()
root.geometry('630x700+400+100')
root.title('PDF viewer')
root.configure(bg='white')

def browseFile():
    filename=filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title='select pdf file',
        filetypes=(
            ('PDF File','.pdf'),
            ('PDF File','.PDF'),
            ('All file','.txt')
        )
    )

Button(
    master=root,
    text='open',
    command=browseFile,
    width=40,
    font='arial 20',
    bd=4
).pack()

root.mainloop()