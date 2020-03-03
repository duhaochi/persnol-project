from Tkinter import *

class Layout1:
    root = None
    buttonList = []
    k = 0

    def __init__(self,root,bList):
        self.root = root
        self.buttonList = bList

    print buttonList
    def placeButton(self):

        for i in range(3):
            for j in range(3):
                self.buttonList[self.k].grid(row=i, column=j)

                self.k += 1