from BaseView import BaseView

class IntroView(BaseView):
    
    def __init__(self, parent):
        BaseView.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        pass