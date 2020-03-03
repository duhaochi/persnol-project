from Tkinter import*


class Buttons:
    buttonList = []
    root = None
    size = 44
    font = "Courier"

    def __init__(self,root):
        self.root = root

    def creatButtons(self):
        for i in range(10):
            self.buttonList.append(Button(self.root, text=str(i), borderwidth=5, font=(self.font, self.size),
                            command=lambda a=i: self.click(i)))


    def click(num):
        pass

    #creatButtons()