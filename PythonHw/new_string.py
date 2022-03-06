class New_str(str):
    
    def is_repeatance(self, s):
        if type(s) != str:
            return False
        else:
            return len(self) == self.count(s)*len(s)
    
    def is_palindrom(self):
        return self.lower() == self.lower()[::-1]
