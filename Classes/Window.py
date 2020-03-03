from layout.Layout1 import*
from layout.Layout2 import*
from layout.Layout3 import*
from Buttons import*

class Window:
    root = Tk()
    size = "600x600"

    screenHeight = root.winfo_screenheight()
    screenWidth = root.winfo_screenwidth()

    root.geometry(size)

    button = Buttons(root)
    button.creatButtons()
    buttonList = button.buttonList


    #print len(list2)
    #layout_1 = Layout1(root,buttonList)
    #layout_2 = Layout2(root,buttonList)
    #layout_2.placeButton()

    layout_3 = Layout3(root,buttonList)
    layout_3.placeButton()


    #layout_1.placeButton()

    @classmethod
    def get_root(cls):
        return cls.root

    root.mainloop()

