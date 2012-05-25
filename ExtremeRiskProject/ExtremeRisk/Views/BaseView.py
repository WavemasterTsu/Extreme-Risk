import Tkinter

class BaseView(Tkinter.Tk):   
             
    def CreateMenu(self):
        objMenu = Tkinter.Menu(self)
        
        objFileMenu = Tkinter.Menu(objMenu, tearoff=0)
        objFileMenu.add_command(label="New")
        objFileMenu.add_command(label="Load")
        objFileMenu.add_command(label="Save")
        objFileMenu.add_command(label="Exit")
        
        objMenu.add_cascade(label="File", menu=objFileMenu)
        
        return objMenu
    
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.InitializeBase()
        self.initialize();
    
    def InitializeBase(self):
        objMenu = self.CreateMenu()
        self.config(menu=objMenu)