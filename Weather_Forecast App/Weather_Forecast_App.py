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

root.mainloop()