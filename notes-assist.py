import sqlite3
import pyscreenshot
import os
from datetime import date
from datetime import datetime
from tkinter import *
import webbrowser
import re

root = Tk()
root.title("Notes Assist")
root.iconbitmap('./assets/notes.ico')
global img
img = PhotoImage(file='./assets/tre.png')
global label
label = Label(root, image=img)
label.place(x=0, y=0, relwidth=1, relheight=1)
today = str(date.today())
sube = Label(root, text="Enter the Subject", bg="#585858", border=0, font=("Arial",11),fg="gray2")
sube.pack(pady=(55,0))
fnam = Entry(root, width=16, fg="black", bg="#585858", border=0.5, font=7, justify="center")
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
        labelinf = Label(root, text=ent + " is added.", width=20, height=1, bg="#a0a0a0", fg="black")
        labelinf.pack(pady=10)

    else:
        labelinf = Label(root, text=ent + " is already present.", width=30, height=1, bg="#a0a0a0", fg="black")
        labelinf.pack(pady=10)


def next():
    root.withdraw()
    global top
    top = Toplevel()
    top.title("Notes Assist")
    top.wm_iconbitmap("E:/HPro/assets/notes.ico")
    label = Label(top, image=img)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    def opendir():
        pa = v.get()
        isd = os.path.isdir(pa)
        if isd:
            os.chdir(pa)

        isT = os.path.isdir(today)
        isT1 = os.path.isdir("../"+today)
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
    for i in n:
        name = Radiobutton(top, text=i[0], variable=v, bg="#585858", fg="black", value=str(i[0]), command=opendir,
                           activebackground="gray40", font=("Arial",10))
        name.pack(pady=(10, 5))

    conn.commit()
    conn.close()

    def take_ss():
        image = pyscreenshot.grab()
        now = str(datetime.now())
        file_name = re.sub(r'[^\w]', ' ', now)
        image.save(file_name + ".png")


    def web():
        webbrowser.open('https://linktr.ee/sudo_nick')


    button2 = Button(top, text="Take Screenshot", command=take_ss, bg="black", border=0, fg="white", padx=20, pady=6)
    button2.config(activebackground="gray15", activeforeground="white")
    button2.pack(pady=(10, 5))

    ext = Button(top, text="Exit", command=top.quit, justify="center", activebackground="gray15",
                 activeforeground="white")
    ext.config(padx=20, pady=5, bg="black", fg="white", border=0, relief="raised")
    ext.pack(pady=(10, 5))

    follow = Button(root, text="Follow Me : @sudo_nick", font=("Arial", 9), bg="gray10", border=0, fg="white",
                    activebackground="gray10", activeforeground="white", command=web)
    follow.pack()

    top.geometry("300x310")
    top.resizable(0, 0)

def web():
    webbrowser.open('https://linktr.ee/sudo_nick')


btn = Button(root, text="Add", command=func, activebackground="gray15", activeforeground="white")
btn.config(padx=20, pady=7, bg="black", fg="white", border=0, relief="raised")
btn.pack(pady=(15, 5))

nextb = Button(root, text="Next", command=next, justify="center", activebackground="gray15",
               activeforeground="white")
nextb.config(padx=17, pady=5, bg="black", fg="white", border=0, relief="raised")
nextb.pack(pady=(15, 5))

skip = Button(root, text="Skip", command=next, justify="center", activebackground="gray15",
               activeforeground="white")
skip.config(padx=17, pady=5, bg="black", fg="white", border=0, relief="raised")
skip.pack(pady=(15, 5))

footer = Frame(root, bg="gray10")
footer.place(x=0, y=285, relwidth=1, relheight=1)

follow = Button(root, text="Follow Me : @sudo_nick", font=("Arial",9), bg="gray10", border=0,fg="white",
                activebackground="gray10", activeforeground="white", command=web)
follow.pack(pady=(19,6),ipadx=9, ipady=10)

root.geometry("300x310")
root.resizable(0, 0)
root.mainloop()
