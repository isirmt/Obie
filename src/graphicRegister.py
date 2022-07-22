import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import sys
import datetime
import importcsv
import graphicComplete
import graphicHistory

from colorList import *


def RegisterData(winManager):
    def DataRegist(year, month, date, use, target, cost, mode, comment):
        outputList = [year, month, date, use, cost, str(mode), target, comment]
        csvList, file_path = importcsv.inputlist()
        csvList = importcsv.listappend(outputList, csvList)
        # print(csvList[0][1])
        importcsv.outputlist(csvList, file_path, True)
        winManager.RegRegDown()
        graphicComplete.Complete()

    def LoadCSV():
        if importcsv.csvUpdateCheck() == -1:
            return
        winManager.RegRegDown()
        graphicComplete.Complete()

    def CopyCSV():
        if importcsv.csvDifellentName() == -1:
            return
        winManager.RegRegDown()
        graphicComplete.Complete()

    regWin = tk.Tk()
    if not winManager.RegRegUp(regWin):
        regWin.destroy()
        return
    regWin.title(u"データ登録：Obie")
    regWin.geometry("640x480+"+str(int((regWin.winfo_screenwidth() - 640))) + "+0")
    regWin.configure(bg=appColors["lWhite"])
    regWin.resizable(width=False, height=False)

    footSize = 25
    widthLabel = 20

# ロゴ表示
    titleCanvas = tk.Canvas(
        regWin, width=640, height=40, bg=appColors["banner"])
    titleCanvas.place(x=0, y=0)

# footer
    foot = tk.Canvas(regWin, width=660, height=footSize, bg=appColors["blue"])
    foot.place(x=-10, y=(480-footSize))

    dt = datetime.datetime.now()

    fontTitle = tkFont.Font(
        regWin,
        family="Helve",
        size=30)
    fontLabel = tkFont.Font(
        regWin,
        family="Helve",
        size=12)

    # 変数格納
    year = tk.StringVar()
    month = tk.StringVar()
    day = tk.StringVar()
    use = tk.StringVar()
    target = tk.StringVar()
    money = tk.StringVar()
    moneyMode = tk.StringVar()
    comment = tk.StringVar()

    ssMode = [False]
    ssModeStr = []
    ssModeStr.append(tk.StringVar())
    ssModeStr[0].set("収入")

    def SwitchSS(ssMode, ssModeStr, regWin):
        ssMode[0] = not ssMode[0]
        ssModeStr[0].set("支出" if ssMode[0] else "収入")
        titleName = u"支出" if ssMode[0] else u"収入"
        resultTitile = titleName + u"データ登録：Obie"
        regWin.title(resultTitile)


    titleName = u"支出" if ssMode[0] else u"収入"
    resultTitile = titleName + u"データ登録：Obie"
    regWin.title(resultTitile)

    # ラベル
    menuTitle = tk.Label(regWin, text=u'データ登録', fg='black',
                         bg=appColors["lWhite"], font=fontTitle)
    menuTitle.place(x=230, y=50)

    lYear = tk.Label(
        regWin,
        text=u"年",
        fg=appColors["letter"],
        bg=appColors["lWhite"], font=fontLabel)

    lYear.place(x=100, y=120)

    iYear = tk.Entry(
        regWin,
        textvariable=year,
        font=fontLabel,
        width=widthLabel
    )
    iYear.place(x=150, y=120)
    iYear.insert(tk.END, str(dt.year))

    lMonth = tk.Label(
        regWin,
        text=u"月",
        fg=appColors["letter"],
        bg=appColors["lWhite"], font=fontLabel)

    lMonth.place(x=100, y=145)

    iMonth = tk.Entry(
        regWin,
        textvariable=month,
        font=fontLabel,
        width=widthLabel
    )
    iMonth.place(x=150, y=145)
    iMonth.insert(tk.END, str(dt.month))

    lDate = tk.Label(
        regWin,
        text=u"日",
        fg=appColors["letter"],
        bg=appColors["lWhite"], font=fontLabel)

    lDate.place(x=100, y=170)

    iDate = tk.Entry(
        regWin,
        textvariable=day,
        font=fontLabel,
        width=widthLabel
    )
    iDate.place(x=150, y=170)
    iDate.insert(tk.END, str(dt.day))

    lUse = tk.Label(
        regWin,
        text=u"用途",
        fg=appColors["letter"],
        bg=appColors["lWhite"], font=fontLabel)

    lUse.place(x=100, y=195)

    iUse = tk.Entry(
        regWin,
        textvariable=use,
        font=fontLabel,
        width=widthLabel
    )
    iUse.place(x=150, y=195)
    iUse.insert(tk.END, "何か")

    lTarget = tk.Label(
        regWin,
        text=u"対象",
        fg=appColors["letter"],
        bg=appColors["lWhite"], font=fontLabel)

    lTarget.place(x=100, y=220)

    iTarget = tk.Entry(
        regWin,
        textvariable=target,
        font=fontLabel,
        width=widthLabel
    )
    iTarget.place(x=150, y=220)
    iTarget.insert(tk.END, "母")

    lCost = tk.Label(
        regWin,
        text=u"金額",
        fg=appColors["letter"],
        bg=appColors["lWhite"], font=fontLabel)

    lCost.place(x=100, y=245)

    iCost = tk.Entry(
        regWin,
        textvariable=money,
        font=fontLabel,
        width=widthLabel
    )
    iCost.place(x=150, y=245)
    iCost.insert(tk.END, 33400)

    bMMode = tk.Button(
        regWin,
        text=u"収支切り替え",
        font=fontLabel,
        width=widthLabel-5,
        bg=appColors["yellow"],
        fg=appColors["letter_buttond"],
        height=3,
        cursor="hand2",
        relief="groove",
        command=lambda: SwitchSS(ssMode, ssModeStr, regWin))
    bMMode.place(x=370, y=200)

    lCurrentMode = tk.Label(
        regWin,
        textvariable=ssModeStr[0],
        # text=u"支出",
        fg=appColors["letter"],
        bg=appColors["lWhite"], font=fontLabel)
    lCurrentMode.place(x=150, y=270)

    lComment = tk.Label(
        regWin,
        text=u"ｺﾒﾝﾄ",
        fg=appColors["letter"],
        bg=appColors["lWhite"], font=fontLabel)

    lComment.place(x=100, y=295)

    iComment = tk.Entry(
        regWin,
        textvariable=comment,
        font=fontLabel,
        width=widthLabel
    )
    iComment.place(x=150, y=295)

    # 本登録
    bReg = tk.Button(
        regWin,
        text="入力内容を登録",
        width=widthLabel-5,
        height=3,
        bg=appColors["orange"],
        fg=appColors["letter_buttond"],
        cursor="hand2",
        relief="groove",
        font=fontLabel,
        command=lambda: DataRegist(iYear.get(), iMonth.get(), iDate.get(), iUse.get(), iTarget.get(), iCost.get(), 2 if ssMode[0] else 1, iComment.get()))

    bReg.place(x=370, y=270)

    # CSV登録
    bCSVL = tk.Button(
        regWin,
        text="CSV読み込み/登録",
        width=widthLabel,
        height=3,
        bg=appColors["orange"],
        relief="groove",
        font=fontLabel,
        cursor="hand2",
        fg=appColors["letter_buttond"],
        command=lambda: LoadCSV())

    bCSVL.place(x=100, y=350)

    bCSVS = tk.Button(
        regWin,
        text="CSV書き出し",
        width=widthLabel,
        height=3,
        bg=appColors["orange"],
        relief="groove",
        font=fontLabel,
        cursor="hand2",
        fg=appColors["letter_buttond"],
        command=lambda: CopyCSV())

    bCSVS.place(x=350, y=350)

    bClose = tk.Button(
        regWin,
        text="閉じる",
        width=7,
        height=2,
        bg=appColors["banner"],
        relief="groove",
        font=fontLabel,
        cursor="hand2",
        fg=appColors["letter_buttond"],
        command=lambda: ClickRegClose(winManager))

    bClose.place(x=530, y=0)

    # regWin.protocol("WM_DELETE_WINDOW", ClickRegClose(winManager))
    regWin.protocol("WM_DELETE_WINDOW", lambda: ClickRegClose(winManager))
    regWin.mainloop()


def ClickRegClose(winManager):
    winManager.RegRegDown()
