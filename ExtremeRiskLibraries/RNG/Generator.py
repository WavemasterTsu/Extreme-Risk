import random

class Generator():

    # int roll(int) Method    
    @staticmethod
    def roll(maxValue):

        random.seed(None)
        
        if maxValue is None or maxValue is not int:
            maxValue = 6
            
        return random.randint(0, maxValue)
    # End roll Method