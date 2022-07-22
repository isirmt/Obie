from cgitb import text
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import sys
import datetime
import importcsv

from colorList import *


def Complete():
    regWin = tk.Tk()
    regWin.title(u"Complete!：Obie")
    regWin.geometry("360x360+"+str(regWin.winfo_screenwidth() - 500)+"+"+str(regWin.winfo_screenheight() - 500))
    regWin.configure(bg=appColors["lWhite"])
    regWin.resizable(width=False, height=False)

    footSize = 25

    dt = datetime.datetime.now()

    fontTitle = tkFont.Font(
        regWin,
        family="Helve",
        size=30)
    fontLabel = tkFont.Font(
        regWin,
        family="Helve",
        size=12)


    # ラベル
    # menuTitle = tk.Label(regWin, text=u'履歴', fg='black',
    #                      bg=appColors["lWhite"], font=fontTitle)
    # menuTitle.place(x=260, y=50)

    canvas = tk.Canvas(regWin, bg=appColors["yellow"])
    canvas.pack(fill = tk.BOTH, expand = True)

    canvas.create_oval(60,60,300,300,fill=appColors["orange"], outline=appColors["yellow"])
    canvas.create_oval(90,90,270,270,fill=appColors["yellow"], outline=appColors["yellow"])
    canvas.create_text(180,180,text="Complete!", anchor=tk.CENTER, font=fontTitle, fill=appColors["letter"])

    regWin.after(3000, lambda: regWin.destroy()) 

    regWin.mainloop()
