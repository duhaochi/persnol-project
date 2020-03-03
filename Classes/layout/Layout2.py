from Tkinter import*
from Window import*
import math



class Layout2:
    win_x = 400
    win_y = 400
    root = None
    buttonList = []
    buttonCoor = []

    def __init__(self,root,bList):
        self.root = root
        self.buttonList = bList


    # use the x and y to place button
    def placeButton(self):
        self.buttonList[1].place(x=100,y=100)


    # find the exact x and y for button placement
    # a list of xy is stored in a list
    def getCoordinate(self,length):
        self.buttonCoor.append()