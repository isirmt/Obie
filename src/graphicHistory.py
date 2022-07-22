from cgitb import text
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import sys
import datetime
import importcsv

from colorList import *
import graphicComplete
import gnuplot
import plottest


def ListUpHistory(winManager):
    regWin = tk.Tk()
    if not winManager.RegHisUp(regWin):
        regWin.destroy()
        return
    regWin.title(u"履歴：Obie")
    regWin.geometry("640x480+0+"+str(int((regWin.winfo_screenheight() - 560))))
    regWin.configure(bg=appColors["lWhite"])
    regWin.resizable(width=False, height=False)

    footSize = 25

# ロゴ表示
    titleCanvas = tk.Canvas(regWin, width=640, height=40, bg="white")
    titleCanvas.place(x=0, y=0)
    # imga = tk.PhotoImage(file="./logo.png", width=135, height=80)
    # titleCanvas.create_image(325, 40, image=winManager.Getlogo(), anchor=tk.CENTER)

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

    rList = [[]]
    csvList, file_path = importcsv.inputlist()
    rList[0] = csvList

    def Reload(gList = rList[0]):
        for i in tree.get_children():
            tree.delete(i)
        # csvList, file_path = importcsv.inputlist()
        rList[0] = gList

        for item in rList[0]:
            if item[5] == "1":
                item[5] = u"収入"
            else:
                item[5] = u"支出"
            if item[7] == "NULL":
                item[7] = ""
        for index, item in enumerate(rList[0]):
            tree.insert(parent="", index="end", iid=index,
                        values=tuple(item), tags=item[5])

    def DrawGraph():
        # print(rList[0])
        plottest.canvas(winManager, rList[0])

    def ItemModify(event):
        def ModifyWindow(record_values, item):
            def DataRegist(year, month, date, use, target, cost, mode, comment):
                outputList = [year, month, date, use,
                              cost, str(mode), target, comment]
                csvList, file_path = importcsv.inputlist()
                try:
                    int(item, 0)
                except ValueError:
                    csvList[0] = outputList
                else:
                    csvList[int(item, 0)] = outputList
                importcsv.outputlist(csvList, file_path, True)
                winManager.DeleteModify(regMod)
                csvList, file_path = importcsv.inputlist()
                Reload(csvList)
                graphicComplete.Complete()

            def DataDelete():
                csvList, file_path = importcsv.inputlist()
                csvList.pop(int(item))
                importcsv.outputlist(csvList, file_path, True)
                winManager.DeleteModify(regMod)
                csvList, file_path = importcsv.inputlist()
                Reload(csvList)
                winManager.ModClose()
                graphicComplete.Complete()
            print(item)
            regMod = tk.Tk()
            winManager.RegModify(regMod)

            regMod.title(u"データ確認・編集：Obie")
            regMod.geometry("640x480")
            regMod.configure(bg=appColors["lWhite"])
            regMod.resizable(width=False, height=False)

            footSize = 25
            widthLabel = 20

        # ロゴ表示
            titleCanvas = tk.Canvas(
                regMod, width=640, height=40, bg=appColors["banner"])
            titleCanvas.place(x=0, y=0)

        # footer
            foot = tk.Canvas(regMod, width=660,
                             height=footSize, bg=appColors["blue"])
            foot.place(x=-10, y=(480-footSize))

            dt = datetime.datetime.now()

            fontTitle = tkFont.Font(
                regMod,
                family="Helve",
                size=30)
            fontLabel = tkFont.Font(
                regMod,
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

            ssMode = [False if record_values[5] == "収入" else True]
            ssModeStr = []
            ssModeStr.append(tk.StringVar())
            ssModeStr[0].set(record_values[5])

            def SwitchSS(ssMode, ssModeStr, regMod):
                ssMode[0] = not ssMode[0]
                ssModeStr[0].set("支出" if ssMode[0] else "収入")
                titleName = u"支出" if ssMode[0] else u"収入"
                resultTitile = titleName + u"データ確認・編集：Obie"
                regMod.title(resultTitile)

            titleName = u"支出" if ssMode[0] else u"収入"
            resultTitile = titleName + u"データ確認・編集：Obie"
            regMod.title(resultTitile)

            # ラベル
            menuTitle = tk.Label(regMod, text=u'データ確認・編集', fg='black',
                                 bg=appColors["lWhite"], font=fontTitle)
            menuTitle.place(x=170, y=50)

            lYear = tk.Label(
                regMod,
                text=u"年",
                fg=appColors["letter"],
                bg=appColors["lWhite"], font=fontLabel)

            lYear.place(x=100, y=120)

            iYear = tk.Entry(
                regMod,
                textvariable=year,
                font=fontLabel,
                width=widthLabel
            )
            iYear.place(x=150, y=120)
            iYear.insert(tk.END, str(record_values[0]))

            lMonth = tk.Label(
                regMod,
                text=u"月",
                fg=appColors["letter"],
                bg=appColors["lWhite"], font=fontLabel)

            lMonth.place(x=100, y=145)

            iMonth = tk.Entry(
                regMod,
                textvariable=month,
                font=fontLabel,
                width=widthLabel
            )
            iMonth.place(x=150, y=145)
            iMonth.insert(tk.END, str(record_values[1]))

            lDate = tk.Label(
                regMod,
                text=u"日",
                fg=appColors["letter"],
                bg=appColors["lWhite"], font=fontLabel)

            lDate.place(x=100, y=170)

            iDate = tk.Entry(
                regMod,
                textvariable=day,
                font=fontLabel,
                width=widthLabel
            )
            iDate.place(x=150, y=170)
            iDate.insert(tk.END, str(record_values[2]))

            lUse = tk.Label(
                regMod,
                text=u"用途",
                fg=appColors["letter"],
                bg=appColors["lWhite"], font=fontLabel)

            lUse.place(x=100, y=195)

            iUse = tk.Entry(
                regMod,
                textvariable=use,
                font=fontLabel,
                width=widthLabel
            )
            iUse.place(x=150, y=195)
            iUse.insert(tk.END, str(record_values[3]))

            lTarget = tk.Label(
                regMod,
                text=u"対象",
                fg=appColors["letter"],
                bg=appColors["lWhite"], font=fontLabel)

            lTarget.place(x=100, y=220)

            iTarget = tk.Entry(
                regMod,
                textvariable=target,
                font=fontLabel,
                width=widthLabel
            )
            iTarget.place(x=150, y=220)
            iTarget.insert(tk.END, str(record_values[6]))

            lCost = tk.Label(
                regMod,
                text=u"金額",
                fg=appColors["letter"],
                bg=appColors["lWhite"], font=fontLabel)

            lCost.place(x=100, y=245)

            iCost = tk.Entry(
                regMod,
                textvariable=money,
                font=fontLabel,
                width=widthLabel
            )
            iCost.place(x=150, y=245)
            iCost.insert(tk.END, record_values[4])

            bMMode = tk.Button(
                regMod,
                text=u"収支切り替え",
                font=fontLabel,
                width=widthLabel-5,
                bg=appColors["yellow"],
                fg=appColors["letter_buttond"],
                height=3,
                cursor="hand2",
                relief="groove",
                command=lambda: SwitchSS(ssMode, ssModeStr, regMod))
            bMMode.place(x=370, y=200)

            lCurrentMode = tk.Label(
                regMod,
                textvariable=ssModeStr[0],
                # text=u"支出",
                fg=appColors["letter"],
                bg=appColors["lWhite"], font=fontLabel)
            lCurrentMode.place(x=150, y=270)

            lComment = tk.Label(
                regMod,
                text=u"ｺﾒﾝﾄ",
                fg=appColors["letter"],
                bg=appColors["lWhite"], font=fontLabel)

            lComment.place(x=100, y=295)

            iComment = tk.Entry(
                regMod,
                textvariable=comment,
                font=fontLabel,
                width=widthLabel
            )
            iComment.place(x=150, y=295)
            iComment.insert(tk.END, str(record_values[7]))

            # 本登録
            bReg = tk.Button(
                regMod,
                text="データを更新",
                width=widthLabel-5,
                height=3,
                bg=appColors["orange"],
                fg=appColors["letter_buttond"],
                cursor="hand2",
                relief="groove",
                font=fontLabel,
                command=lambda: DataRegist(iYear.get(), iMonth.get(), iDate.get(), iUse.get(), iTarget.get(), iCost.get(), 2 if ssMode[0] else 1, iComment.get()))

            bReg.place(x=370, y=270)

            bDelete = tk.Button(
                regMod,
                text="削除",
                width=widthLabel-8,
                height=2,
                bg=appColors["orange"],
                fg=appColors["letter_buttond"],
                cursor="hand2",
                relief="groove",
                font=fontLabel,
                command=lambda: DataDelete())

            bDelete.place(x=0, y=410)

            bClose = tk.Button(
                regMod,
                text="閉じる",
                width=7,
                height=2,
                bg=appColors["banner"],
                relief="groove",
                font=fontLabel,
                cursor="hand2",
                fg=appColors["letter_buttond"],
                command=lambda: winManager.DeleteModify(regMod))

            bClose.place(x=530, y=0)

            # regWin.protocol("WM_DELETE_WINDOW", ClickRegClose(winManager))
            regMod.protocol("WM_DELETE_WINDOW", lambda: winManager.DeleteModify(regMod))
            regMod.mainloop()

        id = tree.focus()
        record_values = tree.item(id, 'values')
        for item in tree.selection():
            ModifyWindow(record_values, item)
        # messagebox.showinfo("まだ実装してないんちょ！", message)
        # print(record_values)

    # ラベル
    menuTitle = tk.Label(regWin, text=u'履歴', fg='black',
                         bg=appColors["lWhite"], font=fontTitle)
    menuTitle.place(x=260, y=50)

    column = ("年", "月", "日", "用途", "金額", "支出", "利用者", "ｺﾒﾝﾄ")

    tree = ttk.Treeview(regWin, columns=column, height=15)
    tree.bind("<<TreeviewSelect>>", ItemModify)

    tree.column('#0', width=0, stretch='no')
    tree.column("年", width=40, stretch='no', anchor="center")
    tree.column("月", width=30, stretch='no', anchor="center")
    tree.column("日", width=30, stretch='no', anchor="center")
    tree.column("用途", width=100, stretch='no')
    tree.column("金額", width=60, stretch='no', anchor="e")
    tree.column("支出", width=40, stretch='no', anchor="center")
    tree.column("利用者", width=60, stretch='no')
    tree.column("ｺﾒﾝﾄ", width=200, stretch='no')

    for item in column:
        tree.heading(item, text=item, anchor="center")

    tree.heading('#0', text='')

    tree.pack(pady=100)
    Reload()

    style = ttk.Style()
    style.configure("Treeview.Heading", rowheight=100,
                    foreground=appColors["letter"], background="white")
    # style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))
    tree.tag_configure(
        u"収入", foreground=appColors["syunyu"], background=appColors["syunyuB"])
    tree.tag_configure(
        u"支出", foreground=appColors["sisyutu"], background=appColors["sisyutuB"])

    serchWord = tk.StringVar()

    def Serch():
        def DataSerch(year, month, date, use, target, costu, costl, comment):
            csvList, file_path = importcsv.inputlist()
            if year != "": csvList = importcsv.csvSort(csvList, 0, int(year))
            if month != "": csvList = importcsv.csvSort(csvList, 1, int(month))
            if date != "": csvList = importcsv.csvSort(csvList, 2, int(date))
            if use != "": csvList = importcsv.csvSort(csvList, 3, use)
            if target != "": csvList = importcsv.csvSort(csvList, 6, target)
            if comment != "": csvList = importcsv.csvSort(csvList, 7, comment)

            if costu != "": csvList = importcsv.csvmoneySort(csvList, int(costu), False)
            if costl != "": csvList = importcsv.csvmoneySort(csvList, int(costl), True)

            csvList.reverse()

            winManager.DeleteModify(regMod)
            Reload(csvList)
            graphicComplete.Complete()

        regMod = tk.Tk()
        winManager.RegModify(regMod)

        regMod.title(u"データ編集：Obie")
        regMod.geometry("640x480+0+0")
        regMod.configure(bg=appColors["lWhite"])
        regMod.resizable(width=False, height=False)

        footSize = 25
        widthLabel = 20

    # ロゴ表示
        titleCanvas = tk.Canvas(
            regMod, width=640, height=40, bg=appColors["banner"])
        titleCanvas.place(x=0, y=0)

    # footer
        foot = tk.Canvas(regMod, width=660,
                            height=footSize, bg=appColors["blue"])
        foot.place(x=-10, y=(480-footSize))

        dt = datetime.datetime.now()

        fontTitle = tkFont.Font(
            regMod,
            family="Helve",
            size=30)
        fontLabel = tkFont.Font(
            regMod,
            family="Helve",
            size=12)

        # 変数格納
        year = tk.StringVar()
        month = tk.StringVar()
        day = tk.StringVar()
        use = tk.StringVar()
        target = tk.StringVar()
        moneyu = tk.StringVar()
        moneyl = tk.StringVar()
        comment = tk.StringVar()

        titleName = ""
        resultTitile = titleName + u"検索：Obie"
        regMod.title(resultTitile)

        # ラベル
        menuTitle = tk.Label(regMod, text=u'検索', fg='black',
                                bg=appColors["lWhite"], font=fontTitle)
        menuTitle.place(x=270, y=50)

        lYear = tk.Label(
            regMod,
            text=u"年",
            fg=appColors["letter"],
            bg=appColors["lWhite"], font=fontLabel)

        lYear.place(x=100, y=120)

        iYear = tk.Entry(
            regMod,
            textvariable=year,
            font=fontLabel,
            width=widthLabel
        )
        iYear.place(x=150, y=120)

        lMonth = tk.Label(
            regMod,
            text=u"月",
            fg=appColors["letter"],
            bg=appColors["lWhite"], font=fontLabel)

        lMonth.place(x=100, y=145)

        iMonth = tk.Entry(
            regMod,
            textvariable=month,
            font=fontLabel,
            width=widthLabel
        )
        iMonth.place(x=150, y=145)

        lDate = tk.Label(
            regMod,
            text=u"日",
            fg=appColors["letter"],
            bg=appColors["lWhite"], font=fontLabel)

        lDate.place(x=100, y=170)

        iDate = tk.Entry(
            regMod,
            textvariable=day,
            font=fontLabel,
            width=widthLabel
        )
        iDate.place(x=150, y=170)

        lUse = tk.Label(
            regMod,
            text=u"用途",
            fg=appColors["letter"],
            bg=appColors["lWhite"], font=fontLabel)

        lUse.place(x=100, y=195)

        iUse = tk.Entry(
            regMod,
            textvariable=use,
            font=fontLabel,
            width=widthLabel
        )
        iUse.place(x=150, y=195)

        lTarget = tk.Label(
            regMod,
            text=u"対象",
            fg=appColors["letter"],
            bg=appColors["lWhite"], font=fontLabel)

        lTarget.place(x=100, y=220)

        iTarget = tk.Entry(
            regMod,
            textvariable=target,
            font=fontLabel,
            width=widthLabel
        )
        iTarget.place(x=150, y=220)

        lCostu = tk.Label(
            regMod,
            text=u"金額↓",
            fg=appColors["letter"],
            bg=appColors["lWhite"], font=fontLabel)

        lCostu.place(x=100, y=245)

        iCostu = tk.Entry(
            regMod,
            textvariable=moneyu,
            font=fontLabel,
            width=widthLabel
        )
        iCostu.place(x=150, y=245)

        lCostl = tk.Label(
            regMod,
            text=u"金額↑",
            fg=appColors["letter"],
            bg=appColors["lWhite"], font=fontLabel)

        lCostl.place(x=100, y=270)

        iCostl = tk.Entry(
            regMod,
            textvariable=moneyl,
            font=fontLabel,
            width=widthLabel
        )
        iCostl.place(x=150, y=270)

        lComment = tk.Label(
            regMod,
            text=u"ｺﾒﾝﾄ",
            fg=appColors["letter"],
            bg=appColors["lWhite"], font=fontLabel)

        lComment.place(x=100, y=295)

        iComment = tk.Entry(
            regMod,
            textvariable=comment,
            font=fontLabel,
            width=widthLabel
        )
        iComment.place(x=150, y=295)

        # 本登録
        bReg = tk.Button(
            regMod,
            text="検索",
            width=widthLabel-5,
            height=3,
            bg=appColors["orange"],
            fg=appColors["letter_buttond"],
            cursor="hand2",
            relief="groove",
            font=fontLabel,
            command=lambda: DataSerch(iYear.get(), iMonth.get(), iDate.get(), iUse.get(), iTarget.get(), iCostu.get(), iCostl.get(), iComment.get()))

        bReg.place(x=370, y=270)

        bClose = tk.Button(
            regMod,
            text="閉じる",
            width=7,
            height=2,
            bg=appColors["banner"],
            relief="groove",
            font=fontLabel,
            cursor="hand2",
            fg=appColors["letter_buttond"],
            command=lambda: winManager.DeleteModify(regMod))

        bClose.place(x=530, y=0)

        # regWin.protocol("WM_DELETE_WINDOW", ClickRegClose(winManager))
        regMod.protocol("WM_DELETE_WINDOW", lambda: winManager.DeleteModify(regMod))
        regMod.mainloop()

    bSerchWindow = tk.Button(
        regWin,
        text="検索",
        width=15,
        height=2,
        bg=appColors["orange"],
        fg="black",
        relief="groove",
        cursor="hand2",
        command=lambda: Serch()
    )
    bSerchWindow.place(x=470, y=50)

    def TypeSort(mode:int):
        csvList, file_path = importcsv.inputlist()
        if mode == 1:
            csvList = importcsv.csvSort(csvList, 5, 1)
            csvList.reverse()
        elif mode == 2:
            csvList = importcsv.csvSort(csvList, 5, 2)
            csvList.reverse()
        else: None
        winManager.ModClose()
        Reload(csvList)

    bSort1 = tk.Button(
        regWin,
        text="収入",
        width=10,
        height=2,
        bg=appColors["orange"],
        fg="black",
        relief="groove",
        cursor="hand2",
        command=lambda: TypeSort(1)
    )
    bSort1.place(x=50, y=50)
    bSort2 = tk.Button(
        regWin,
        text="支出",
        width=10,
        height=2,
        bg=appColors["orange"],
        fg="black",
        relief="groove",
        cursor="hand2",
        command=lambda: TypeSort(2)
    )
    bSort2.place(x=150, y=50)

    bReload = tk.Button(
        regWin,
        text="再読み込み・全表示",
        width=25,
        height=3,
        bg=appColors["orange"],
        fg="black",
        relief="groove",
        cursor="hand2",
        command=lambda: TypeSort(0))
    # command=lambda: graphicRegister.RegisterData(winManager))

    bReload.place(x=100, y=390)

    bCSVS = tk.Button(
        regWin,
        text="統計表示",
        width=25,
        height=3,
        relief="groove",
        cursor="hand2",
        bg=appColors["yellow"],
        fg="black",
        command=lambda: DrawGraph())

    bCSVS.place(x=350, y=390)

    bClose = tk.Button(
        regWin,
        text="閉じる",
        width=7,
        height=2,
        bg="white",
        relief="groove",
        font=fontLabel,
        cursor="hand2",
        fg="black",
        command=lambda: ClickHisClose(winManager))

    bClose.place(x=530, y=0)

    regWin.protocol("WM_DELETE_WINDOW", lambda: ClickHisClose(winManager))
    regWin.mainloop()


def ClickHisClose(winManager):
    winManager.RegHisDown()
