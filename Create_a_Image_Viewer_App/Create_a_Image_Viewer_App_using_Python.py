# pip install image

from tkinter import *
from tkinter import filedialog
import tkinter as tk 
from PIL import Image,ImageTk
import os

root=Tk()

fram=Frame(root)
fram.pack(side=BOTTOM,padx=15,pady=15)

lbl=Label(root)
lbl.pack()

btn1=Button(fram,text='Select Image')
btn1.pack(side=tk.LEFT)

btn2=Button(fram,text='Exit',command=lambda:exit())
btn2.pack(side=tk.LEFT,padx=12)

root.title('Image Viewer')
root.geometry('400x450')
root.mainloop()
