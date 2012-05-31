import gtk
from Controls import Menu

class BaseView(gtk.Window):
    
    def __init__(self):
        super(BaseView, self).__init__()
        self.connect("destroy", gtk.main_quit)
        self.set_position(gtk.WIN_POS_CENTER)
        self.InitializeBase()
    
    def InitializeBase(self):
        self.config(menu=objMenu)
        self.show()
        gtk.main()