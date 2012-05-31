import gtk
from MenuItem import MenuItem

class Menu(gtk.MenuBar):
    
    def Create(self):
        objFile = Menu(self)
        objFile.append(MenuItem("New"))
        objFile.append(MenuItem("Load"))
        objFile.append(MenuItem("Save"))
        objFile.append(MenuItem("Exit"))
    
    def __init__(self):
        self.Create()