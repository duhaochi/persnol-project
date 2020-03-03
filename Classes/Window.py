from layout1.LayoutManager import*
from Buttons import*

class Window:
    root = Tk()
    size = "1000x1000"
    lay = 1

    screenHeight = root.winfo_screenheight()
    screenWidth = root.winfo_screenwidth()

    root.geometry(size)


    button = Buttons(root)
    button.creatButtons()
    buttonList = button.buttonList

    LM = LayoutManager(root,buttonList)

    LM.getLay1()


    #layout_1.placeButton()

    @classmethod
    def get_root(cls):
        return cls.root

    root.mainloop()

