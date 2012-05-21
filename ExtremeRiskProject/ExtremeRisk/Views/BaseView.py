import Tkinter

class BaseView(Tkinter.Tk):   
     
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        pass