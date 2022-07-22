import tkinter as tk


class WinManager:
    def __init__(self):
        self.rootUp = False
        self.regUp = False
        self.hisUp = False
        self.regWin = 0
        self.hisWin = 0
        self.logo = tk.PhotoImage()
        self.modify = []

    def RegModify(self, window):
        self.modify.append(window)

    def DeleteModify(self, window):
        self.modify.remove(window)
        window.destroy()

    def RegLogo(self, img):
        self.logo = img

    def GetLogo(self):
        return self.logo

    def RegRegUp(self, window):
        if self.regUp:
            return False
        else:
            self.regUp = True
            self.regWin = window
            return True

    def RegRegDown(self):
        if self.regUp:
            self.regWin.destroy()
        self.regUp = False

    def RegHisDown(self):
        if self.hisUp:
            self.hisWin.destroy()
        self.hisUp = False

    def RegHisUp(self, window):
        if self.hisUp:
            return False
        else:
            self.hisUp = True
            self.hisWin = window
            return True

    def AllClose(self):
        if self.hisUp:
            self.hisWin.destroy()
            self.hisUp = False
        if self.regUp:
            self.regWin.destroy()
            self.regUp = False
        for item in self.modify:
            item.destroy()
        self.modify.clear()

    def ModClose(self):
        for item in self.modify:
            item.destroy()

        self.modify.clear()
