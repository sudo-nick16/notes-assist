import sqlite3
import pyscreenshot
import os
from datetime import date
from datetime import datetime
from tkinter import *
import webbrowser
import re
from PIL import ImageGrab
from tkinter import messagebox

root = Tk()
root.title("Notes Assist")
icon = PhotoImage(file='./notes.png')
root.iconbitmap('./notes.ico')
#global img
#img = PhotoImage(file='./tre.png')
global label
label = Label(root, bg="black")
label.place(x=0, y=0, relwidth=1, relheight=1)
today = str(date.today())
sube = Label(root, text="Enter  the  Subject", bg="black", border=0, font=("Jokerman", 11), fg="green2")
sube.pack(pady=(34, 0))
fnam = Entry(root, width=16, fg="gray7", bg="white", border=0, font=("Comic Sans MS", 13), justify="center")
fnam.pack(pady=(10, 5))
fnam.focus()

path = os.path.normpath(os.path.expanduser("~/Desktop"))
os.chdir(path)
isnt = os.path.isdir("Notes Assist")
if not isnt:
    os.mkdir("Notes Assist")
    os.chdir("Notes Assist")
else:
    os.chdir("Notes Assist")

isda = os.path.isfile("fnamesdb.db")
if not isda:
    conn = sqlite3.connect('fnamesdb.db')
    c = conn.cursor()
    c.execute("CREATE TABLE fnames(names text)")
    conn.commit()
    conn.close()
else:
    pass


def func():
    ent = fnam.get()
    fnam.delete(0, END)
    conn = sqlite3.connect('fnamesdb.db')
    c = conn.cursor()
    iss = os.path.isdir(str(ent))
    if not iss:
        c.execute("INSERT INTO fnames VALUES(:sub)", {'sub': ent})
        os.mkdir(ent)
        conn.commit()
        conn.close()
        # won't be shown because i suck at positioning the widgets.
        labelinf = Label(root, text=ent + " is added.", width=20, height=1, bg="black", fg="black")
        labelinf.pack()

    else:
        # won't be shown because i suck at positioning the widgets.
        labelinf = Label(root, text=ent + " is already present.", width=30, height=1, bg="black", fg="black")
        labelinf.pack()

count = 0

def next():
    root.withdraw()
    global top
    top = Toplevel()
    top.title("Notes Assist")
    top.iconphoto(False, icon)
    # top.wm_iconbitmap(icon)
    label = Label(top, bg="black")
    label.place(x=0, y=0, relwidth=1, relheight=1)


    def opendir(subn=0):
        pa = v.get()
        global count
        count += 1
        if count > 1:
            os.chdir("../..")
        else:
            pass

        isd = os.path.isdir(pa)
        if isd:
            os.chdir(pa)

        isT = os.path.isdir(today)
        isT1 = os.path.isdir("../" + today)
        if not isT and not isT1:
            os.mkdir(today)
            os.chdir(today)
        else:
            os.chdir(today)

    conn = sqlite3.connect('fnamesdb.db')
    c1 = conn.cursor()
    c1.execute("SELECT names FROM fnames")
    n = c1.fetchall()
    v = StringVar()
    rbframe = Frame(top, bg="black")
    rbframe.pack(padx=0)
    num = 0
    col = 0
    for i in n:
        name = Radiobutton(rbframe, text=i[0], variable=v, bg="black", fg="teal", value=str(i[0]), command=opendir,
                     activebackground="black", activeforeground="white", font=("Jokerman", 10), selectcolor="black")
        if num == 4:
            num = 0
            col += 1
        name.grid(row=num, column=col, pady=5, padx=5)
        num += 1
    conn.commit()
    conn.close()

    def take_ss():
        isT = os.path.isdir("../" + today)
        if not isT:
            pass
        else:
            image = ImageGrab.grab()
            now = str(datetime.now())
            file_name = re.sub(r'[^\w]', ' ', now)
            image.save(file_name + ".png")

    def web():
        webbrowser.open('https://linktr.ee/sudo_nick')

    button2 = Button(top, text="Take  Screenshot", command=take_ss, bg="black", border=2, fg="beige", padx=20, pady=6)
    button2.config(activebackground="gray15", activeforeground="white", font=("Jokerman", 10))
    button2.pack(pady=(11, 5))
    button2.focus()

    ext = Button(top, text="Exit", command=top.quit, justify="center", activebackground="gray15",
                 activeforeground="white")
    ext.config(padx=15, pady=5, bg="black", fg="beige", border=2, relief="raised", font=("Jokerman", 10))
    ext.pack(pady=(5, 8))

    follow = Button(top, text="Creator : @sudo_nick", font=("Segoe Print", 9), bg="gray10", border=0, fg="MEDIUMPURPLE1",
                    activebackground="gray10", activeforeground="yellow", command=web, padx=100)
    follow.pack(pady=(5, 0))

    top.geometry("300x310")
    top.resizable(0, 0)


def web():
    webbrowser.open('https://linktr.ee/sudo_nick')


btn = Button(root, text="Add", command=func, activebackground="gray10", activeforeground="white")
btn.config(padx=20, pady=7, bg="black", fg="beige", border=2, relief="raised", font=("Jokerman", 8))
btn.pack(pady=(15, 4))

nextb = Button(root, text="Next", command=next, justify="center", activebackground="gray10",
               activeforeground="white")
nextb.config(padx=17, pady=5, bg="black", fg="beige", border=2, relief="raised", font=("Jokerman", 8))
nextb.pack(pady=(15, 4))

skip = Button(root, text="Skip", command=next, justify="center", activebackground="gray10",
              activeforeground="white")
skip.config(padx=17, pady=5, bg="black", fg="beige", border=2, relief="raised", font=("Jokerman", 8))
skip.pack(pady=(15, 4))

follow = Button(root, text="Creator : @sudo_nick", font=("Segoe Print", 9), bg="gray10", border=0, fg="MEDIUMPURPLE1",
                activebackground="gray10", activeforeground="yellow", command=web, padx=100)
follow.pack(pady=(11, 0))

root.geometry("300x310")
root.resizable(0, 0)
root.mainloop()
