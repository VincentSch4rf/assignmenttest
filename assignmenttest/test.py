import reprlib

class Test:
    
    def __init__(self, name):
        self.name = name
        self.repr = reprlib.Repr()
        self.repr.maxlist = 10
        self.repr.maxstring = 20        
    
    def test(self):
        return True, ''