import gtk
from BaseView import BaseView

class IntroView(BaseView):
    
    def btnPlay_Click(self):
        print "Extreme Risk Started"
    
    def __init__(self):
        BaseView.__init__(self)
        self.Initialize()
        
    def Initialize(self):
        btnPlay = gtk.Button(self, text=u"Start Extreme Risk!", command=self.btnPlay_Click)
        btnPlay.grid(column=0, row=0, padx=20, pady=20)
        self.set_size_request(200, 400)
        pass