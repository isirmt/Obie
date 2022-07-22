from colorList import *

class color_manager:
    def __init__(self, id = 1):
        self.id = id
        self.idMax = 4
        self.change_preset(self.id)

    def get_preset(self):
        return self.id

    def change_preset(self, id):
        self.id = id
        if self.id > self.idMax:
            self.id = 1
        if self.id == 1:
            appColors["blue"] = "#083D77"
            appColors["lWhite"] = "#EBEBD3"
            appColors["yellow"] = "#F4D35E"
            appColors["orange"] = "#EE964B"
            appColors["mikan"] = "#F95738"
            appColors["letter"] = "black"
            appColors["letter_button"] = "white"
            appColors["letter_buttond"] = "black"
            appColors["banner"] = "white"
        elif self.id == 2:
            appColors["blue"] = "#C9C9C9"
            appColors["lWhite"] = "#C5E0D8"
            appColors["yellow"] = "#CEABB1"
            appColors["orange"] = "#B5FFE9"
            appColors["mikan"] = "#BDF0E1"
            appColors["letter"] = "#444545"
            appColors["letter_button"] = "#444545"
            appColors["letter_buttond"] = "#444545"
            appColors["banner"] = "#D3D0CB"
        elif self.id == 3:
            appColors["blue"] = "#3772FF"
            appColors["lWhite"] = "#DBF4AD"
            appColors["yellow"] = "#E2EF70"
            appColors["orange"] = "#70E4EF"
            appColors["mikan"] = "#F038FF"
            appColors["letter"] = "black"
            appColors["letter_button"] = "black"
            appColors["letter_buttond"] = "black"
            appColors["banner"] = "white"
        elif self.id == 4:
            appColors["blue"] = "#21A179"
            appColors["lWhite"] = "#F0F0F0"
            appColors["yellow"] = "#81AE9D"
            appColors["orange"] = "#FB9F89"
            appColors["mikan"] = "#F038FF"
            appColors["letter"] = "#1E1E24"
            appColors["letter_button"] = "#1E1E24"
            appColors["letter_buttond"] = "#1E1E24"
            appColors["banner"] = "white"