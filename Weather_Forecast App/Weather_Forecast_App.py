# Required modules:
#   pip install pytz 
#   pip install geopy
#   pip install timezonefinder
#   pip install requests 
#   pip install pillow

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title('Weather App')
root.geometry('890x470+300+200')
root.configure(bg='#57adff')
root.resizable(False,False)
#icon
image_icon=PhotoImage(file='Images/logo.png')
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file='Images/Rounded Rectangle 1.png')
Label(root,image=Round_box,bg='#57adff').place(x=30,y=110)

#Label
label1=Label(root,text='Temperature',font=('Helvetica',11),fg='white',bg='#203243')
label1.place(x=50,y=120)

label2=Label(root,text='Humidity',font=('Helvetica',11),fg='white',bg='#203243')
label2.place(x=50,y=140)

label3=Label(root,text='Pressure',font=('Helvetica',11),fg='white',bg='#203243')
label3.place(x=50,y=160)

label4=Label(root,text='Wind Speed',font=('Helvetica',11),fg='white',bg='#203243')
label4.place(x=50,y=180)

label5=Label(root,text='Description',font=('Helvetica',11),fg='white',bg='#203243')
label5.place(x=50,y=200)

root.mainloop()