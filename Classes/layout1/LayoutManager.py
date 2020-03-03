from Layout1 import*
from Layout2 import*
from Layout3 import*


class LayoutManager:

    root = None
    buttonList = []

    def __init__(self,root,buttonList):
        self.root = root
        self.buttonList = buttonList

    def getLay1(self):
        l1= Layout1(self.root, self.buttonList)
        l1.placeButton()

    def getLay2(self):
        l2 = Layout3(self.root, self.buttonList)
        l2.placeButton()

    def getLay3(self):
        l3 = Layout3(self.root, self.buttonList)
        l3.placeButton()