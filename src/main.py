import tkinter as tk
import tkinter.font as tkFont
import datetime

import graphicRegister
import graphicHistory
from graphicStatus import *
from colorList import *
import colorPreset
import JsonManager
from tkinter import messagebox


def main():
    def Reboot():
        cpreset.change_preset(cpreset.get_preset()+1)
        root.configure(bg=appColors["lWhite"])
        titleCanvas.configure(bg=appColors["banner"])
        welcome.configure(fg=appColors["letter"], bg=appColors["lWhite"])
        dateBoxm.configure(fg=appColors["letter"], bg=appColors["lWhite"])
        dateBoxd.configure(fg=appColors["letter"], bg=appColors["lWhite"])
        dateBox.configure(fg=appColors["letter"], bg=appColors["lWhite"])
        menuReg.configure(bg=appColors["orange"],
                          fg=appColors["letter_button"])
        menuHis.configure(bg=appColors["yellow"],
                          fg=appColors["letter_buttond"])
        menuSub.configure(bg=appColors["orange"],
                          fg=appColors["letter_button"])
        menuChange.configure(
            bg=appColors["orange"], fg=appColors["letter_button"])
        bClose.configure(bg=appColors["banner"])
        manuTabClose.configure(
            bg=appColors["orange"], fg=appColors["letter_button"])
        bClose.configure(bg=appColors["banner"])
        foot.configure(bg=appColors["blue"])
        winManager.AllClose()
        # print(cpreset.get_preset())
        jFile['colorPreset'] = cpreset.get_preset()
        JsonManager.save(jFile)

    jFile = JsonManager.load()
    # print(jFile)

    cpreset = colorPreset.color_manager(jFile['colorPreset'])

    root = tk.Tk()
    root.title(u"Obie")
    root.geometry("640x480+"+str(int((root.winfo_screenwidth() - 640) / 2)) + "+"+str(int((root.winfo_screenheight() - 480) / 2)))
    root.configure(bg=appColors["lWhite"])
    root.resizable(width=False, height=False)

    font = tkFont.Font(
        root,
        family="Helve",
        size=30)

    fontLabel = tkFont.Font(
        root,
        family="Menlo",
        size=12)

    fontMonth = tkFont.Font(
        root,
        family="Helve",
        size=17)

    fontDate = tkFont.Font(
        root,
        family="Helve",
        size=24)

    winManager = WinManager()

    footSize = 25

# ロゴ表示
    titleCanvas = tk.Canvas(root, width=640, height=80, bg=appColors["banner"])
    titleCanvas.place(x=0, y=0)
    img = tk.PhotoImage(file="./logo.png", width=135, height=80)
    winManager.RegLogo(img)
    titleCanvas.create_image(325, 40, image=img, anchor=tk.CENTER)

# footer
    foot = tk.Canvas(root, width=660, height=footSize, bg=appColors["blue"])
    foot.place(x=-10, y=(480-footSize))

# ラベル
    # menuTitle = tk.Label(root, text=u'かけいぼ', fg='black',
    #                      bg=appColors["lWhite"], font=font)
    # menuTitle.place(x=250, y=100)
    welcome = tk.Label(root, text="おかえりなさい！Obieへようこそ！",
                       font=fontMonth,
                       fg=appColors["letter"],
                       bg=appColors["lWhite"])
    welcome.place(x=160, y=100)
    dateBoxm = tk.Label(root, text="Today",
                        font=fontMonth,
                        fg=appColors["letter"],
                        bg=appColors["lWhite"])
    dateBoxm.place(x=435, y=200)
    dateBoxd = tk.Label(root, text=datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=9))).strftime("%b"),
        font=fontMonth,
        fg=appColors["letter"],
        bg=appColors["lWhite"])
    dateBoxd.place(x=400, y=239)
    dateBox = tk.Label(root, text=datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=9))).strftime("%d(%a)"),
        font=fontDate,
        fg=appColors["letter"],
        bg=appColors["lWhite"])
    dateBox.place(x=440, y=230)

    menuReg = tk.Button(
        root,
        text="データ登録",
        width=25,
        height=3,
        bg=appColors["orange"],
        fg=appColors["letter_button"],
        font=fontLabel,
        relief="groove",
        cursor="hand2",
        command=lambda: graphicRegister.RegisterData(winManager))

    menuReg.place(x=70, y=200)

    menuHis = tk.Button(
        root,
        text="履歴",
        width=25,
        height=3,
        bg=appColors["yellow"],
        fg=appColors["letter_buttond"],
        font=fontLabel,
        relief="groove",
        cursor="hand2",
        command=lambda: graphicHistory.ListUpHistory(winManager))

    menuHis.place(x=70, y=300)

    menuSub = tk.Button(
        root,
        text="サブスク情報",
        width=25,
        height=3,
        bg=appColors["orange"],
        fg=appColors["letter_button"],
        font=fontLabel,
        relief="groove",
        cursor="hand2",
        command=lambda: messagebox.showerror("まだ実装してないんちょ！", "工事中です"))

    menuSub.place(x=350, y=300)

    menuChange = tk.Button(
        root,
        text="テーマ変更",
        width=12,
        height=2,
        bg=appColors["orange"],
        fg=appColors["letter_button"],
        font=fontLabel,
        relief="groove",
        cursor="hand2",
        command=lambda: Reboot())

    menuChange.place(x=0, y=415)

    manuTabClose = tk.Button(
        root,
        text="タブ閉じる",
        width=12,
        height=2,
        bg=appColors["orange"],
        fg=appColors["letter_button"],
        font=fontLabel,
        relief="groove",
        cursor="hand2",
        command=lambda: winManager.AllClose())

    manuTabClose.place(x=520, y=415)

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
        command=lambda: ClickRootClose(winManager, root))

    bClose.place(x=530, y=0)

    root.protocol("WM_DELETE_WINDOW", lambda: ClickRootClose(winManager, root))
    root.mainloop()


def ClickRootClose(winManager, win):
    winManager.AllClose()
    win.destroy()


if __name__ == "__main__":
    main()
