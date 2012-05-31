import gtk

class MenuItem(gtk.MenuItem):
    
    def Create(self, title):
        super.__init__(title)
    
    def __init__(self, title):
        self.Create(title)