# pip install pillow

import PIL
from PIL import Image
from tkinter.filedialog import *

import PIL.Image

file_path=askopenfilename()
img=PIL.Image.open(file_path)
myHeight,myWidth=img.size

img=img.resize((myHeight,myWidth),PIL.Image.LANCZOS)
save_path=askopenfilename()
img.save(save_path+'images.png')