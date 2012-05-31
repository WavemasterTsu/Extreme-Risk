from Contracts.States import GlobalState, ConfigurationState, PlayState

# Controller consists of a CurrentState and a CurrentSubState
# These two variables will pinpoint the exact state the program is in    
    
class StateController:    
    
    def __init__(self):
        self.CurrentState = GlobalState.Initial
    
    def ChangeState(self, objNewState):
        
        if(self.ValidateStateChange(objNewState)):
            self.CurrentState = objNewState
            self.ChangeViewByState(objNewState)
    
    def ChangeSubState(self, objNewSubState):
        
        if(self.ValidateSubStateChange(objNewSubState)):
            self.CurrentSubState = objNewSubState
            self.ChangeViewBySubState(objNewSubState)
    
    def ValidateStateChange(self, objNewState):

        if(objNewState == GlobalState.Configuration):
            if(self.CurrentState == GlobalState.Initial):
                return True
            else:
                return False
            
        if(objNewState == GlobalState.Initial):
            if(self.CurrentState == GlobalState.Exit):
                return True
            else:
                return False
            
        if(objNewState == GlobalState.Play):
            if(self.CurrentState == GlobalState.Configuration):
                return True
            else:
                return False
        pass
    
    def ValidateSubStateChange(self):
        pass
    
    # views changed by state are application level views
    def ChangeViewByState(self, objNewState):
        pass
    
    # views changed by sub-state are view level views
    def ChangeViewBySubState(self, objNewSubState):
        pass