import pyscreenshot
import os
from datetime import date
from datetime import datetime
from tkinter import *
import re

root = Tk()

today = str(date.today())
path = os.path.normpath(os.path.expanduser("~/Desktop"))
os.chdir(str(path))
isM = os.path.isdir("Maths")
isCS = os.path.isdir("CS")
if not isM:
    os.mkdir("Maths")
if not isCS:
    os.mkdir("CS")

i = IntVar()
rb1 = Radiobutton(root, text='Maths', value=1, variable=i)
rb2 = Radiobutton(root, text='CS', value=2, variable=i)
rb1.pack()
rb2.pack()
def makedir():
    if (i.get() == 1):
        os.chdir("Maths")
    if (i.get() == 2):
        os.chdir("CS")
    isT = os.path.isdir(today)
    if not isT:
        os.mkdir(today)
        os.chdir(today)
        label_1 = Label(root, text="Directory Created", width=15, height=4)
        label_1.pack()
    else:
        os.chdir(today)
        label_1 = Label(root, text="Directory Already Present", width=20, height=4)
        label_1.pack()

button1 = Button(root, text="Make a directory for today", command=makedir)
button1.pack()
def take_ss():
    # To capture the screen
    image = pyscreenshot.grab()
    # To rename the ss
    now = str(datetime.now())
    file_name = re.sub(r'[^\w]', ' ', now)
    # To save the screenshot
    image.save(file_name + ".png")


button2 = Button(root, text="Take Screenshot", command=take_ss)
button2.pack()

root.geometry("300x300+120+120")
root.mainloop()
