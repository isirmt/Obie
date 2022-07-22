import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from colorList import *
import datetime
import importcsv as ic
import gnuplot

#
# GUI設定
#


def canvas(winManager, DB):
    root = tk.Tk()
    winManager.RegModify(root)
    root.resizable(width=False, height=False)
    root.title("グラフ描画")

    root.geometry("640x480")  # ウインドウサイズ（「幅x高さ」で指定）

    fontLabel = tkFont.Font(root, family="Helve", size=12)

    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas.create_text(
        40,
        460,
        text="Complete!",
        anchor=tk.CENTER,
    )
    width = 540
    height = 380
    canvas.create_rectangle(
        50, 50, 590, 430,
    )

    bClose = tk.Button(
        root,
        text="閉じる",
        width=7,
        height=2,
        bg=appColors["banner"],
        relief="groove",
        font=fontLabel,
        cursor="hand2",
        fg=appColors["letter_buttond"],
        command=lambda: winManager.DeleteModify(root))  # これで閉じるコマンド

    bClose.place(x=530, y=0)

    # csvList,file = ic.inputlist()

    Y = DB
    for i in Y:
        if i[5] == "支出":
            i[4] = int(int(i[4])*(-1))
        else:
            i[4] = int(i[4])

    dt1 = datetime.datetime(int(Y[0][0]), int(Y[0][1]), int(Y[0][2]))
    dt2 = datetime.datetime(int(Y[len(Y)-1][0]),
                            int(Y[len(Y)-1][1]), int(Y[len(Y)-1][2]))

    daterange = dt1-dt2
    daterange = daterange.days

    flist = gnuplot.daylist(Y)
    ls = []
    for i in range(daterange):
        now = dt2 + datetime.timedelta(days=i)
        ls.append([now, 0])
        total = 0
        for item in flist:
            listDay = datetime.datetime(
                int(item[0]), int(item[1]), int(item[2]))
            timedelta = now - listDay
            if (timedelta.days == 0):
                total += item[3]
        ls[i][1] = total

    max = 0
    min = 0
    for i in ls:
        if max < i[1]:
            max = i[1]
        if min > i[1]:
            min = i[1]

    if max < 0:
        max *= 0.8
    else:
        max /= 0.8

    if min > 0:
        min *= 0.8
    else:
        min /= 0.8

    heightrange = (max-min)

    width = 540
    height = 380

    print(daterange/5)

    for id, item in enumerate(ls):
        if id == 0:
            continue
        yesterday = datetime.datetime(
            ls[id-1][0].year, ls[id-1][0].month, ls[id-1][0].day)
        now = datetime.datetime(ls[id][0].year, ls[id][0].month, ls[id][0].day)
        dyesterday = yesterday - dt2
        dnow = now - dt2
        canvas.create_line(
            50+width/daterange*dyesterday.days,
            50+height-height*(int(ls[id-1][1])-min)/heightrange,
            50+width/daterange*dnow.days,
            50+height-height*(int(ls[id][1])-min)/heightrange
        )
        if id % (int(daterange / 5)) == 0 or id == 1:
            canvas.create_text(
                50+width/daterange*dyesterday.days,
                60+height,
                text=str(yesterday.strftime("%Y/%m/%d"))
            )
    for i in range(6):
        canvas.create_text(45,
                           50+height-i*height/5,
                           text=str(int(0.2*i*heightrange + min)),
                           anchor=tk.E)
    canvas.create_text(45,
                       50+height-height*(0-min)/heightrange,
                       text="0",
                       anchor=tk.E)
    root.mainloop()
