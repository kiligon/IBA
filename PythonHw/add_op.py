class Log():
    
    def __init__(self, index):
        self.index = index
    
    def __add__(self, b):
        return Log(self.index*b.index)
    
    def __str__(self):
        return("Log({})".format(self.index))
