import pyscreenshot
import os
from datetime import date
from datetime import datetime
from tkinter import *
import re

root = Tk()
root.title("Notes Taker")
root.iconbitmap('./assets/notes.ico')
img = PhotoImage(file='E:/HPro/assets/tre.png')
label = Label(root, image=img)
label.place(x=0, y=0, relwidth=1, relheight=1)

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
rb1 = Radiobutton(root, text='Maths', value=1, variable=i, bg="darkgray")
rb2 = Radiobutton(root, text='CS', value=2, variable=i, bg="#a0a0a0")
rb1.pack(pady=(20,10))
rb2.pack(pady=10)

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


def take_ss():
    makedir()
    image = pyscreenshot.grab()
    now = str(datetime.now())
    file_name = re.sub(r'[^\w]', ' ', now)
    image.save(file_name + ".png")


button2 = Button(root, text="Take Screenshot", command=take_ss, bg="black", border=0, fg="white", padx=20, pady=6)
button2.config(activebackground="gray15", activeforeground="white")
button2.pack(pady=10)

ext = Button(root,text="Exit", command=root.quit, justify="center", activebackground="gray15", activeforeground="white")
ext.config(padx=20, pady=5, bg="black", fg="white", border=0, relief="raised")
ext.pack(pady=(10,5))


root.resizable(0, 0)
root.geometry("300x300+120+120")
root.mainloop()
