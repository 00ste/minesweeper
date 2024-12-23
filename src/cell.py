from operator import truediv


class Cell:
    def __init__(self, value):
        self.value = value
        self.hidden = True
        self.flagged = False
    
    def is_mine(self):
        return self.value == 9
    
    def set_mine(self):
        if self.value == 9:
            return False
        else:
            self.value = 9
            return True
    
    def reveal(self):
        if not self.hidden:
            return False
        else:
            self.hidden = False
            return True
    
    def flag(self):
        if not self.hidden:
            return False
        else:
            self.flagged = not self.flagged
            return True