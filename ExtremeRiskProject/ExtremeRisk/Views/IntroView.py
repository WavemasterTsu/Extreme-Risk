from BaseView import BaseView

class IntroView(BaseView):
    
    def __init__(self, parent):
        BaseView.__init__(BaseView(self), parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        print "Hello World"
        pass