from .NammuView import NammuView
from MenuController import MenuController

class NammuController(object):

    def __init__(self):

        self.menuController = MenuController(self)
        self.view = NammuView(self)
        self.view.setJMenuBar(self.menuController.view)
        self.view.display()


    def newFile(self, event):
        """
        1. Check if current file in text area has unsaved changes
            1.1 Prompt user for file saving
                1.1.1 Save file
        2. Clear text area
        3. See GitHub issue: https://github.com/UCL-RITS/nammu/issues/6
        """
        print("NammuController: Creating new file...")

    def openFile(self, event):
        print("NammuController: Opening new file...")

    def saveFile(self, event):
        print("NammuController: Saving new file...")

    def closeFile(self, event):
        print("NammuController: Closing new file...")

    def toolbar(self, event):
        print("NammuController: Toolbar new functions ")

    def __getattr__(self, name):
        print "Undefined: "  + name
