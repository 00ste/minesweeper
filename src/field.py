from random import randint
from cell import Cell

class Field:
    """
    WIDTH, HEIGHT: dimensions
    MINES: the total number of mines on the field

    IN MEMORY:
    [
        [a, d, g, j],
        [b, e, h, k],
        [c, f, i, l]
    ]

    IN THEORY:
    [
        [   [   [
        a,  b,  c,
        d,  e,  f,
        g,  h,  i,
        j,  k,  l
        ]   ]   ]
    ]

    field[x][y]: first index is x coord (col), second index is y coord (row)
    """
    def __init__(self, width, height, mines):
        self.defeat = False
        self.victory = False
        self.mines = 0
        self.revealed = 0
        self.cells = []
        for x in range(width):
            self.cells.append([])
            for y in range(height):
                self.cells[x].append(Cell(0))
    
        # place the mines
        n = 0
        while n < mines:
            rand_x = randint(0, self.width()-1)
            rand_y = randint(0, self.height()-1)
            if self.cells[rand_x][rand_y].set_mine():
                n += 1

        for y in range(self.height()):
            for x in range(self.width()):
                if not self.cell(x, y).is_mine():
                    self.cell(x, y).value = self.count_mines(x, y)
                else:
                    self.mines += 1

    def width(self):
        return len(self.cells)

    def height(self):
        return len(self.cells[0])
    
    def dimension(self):
        return self.width()*self.height()

    def cell(self, x, y):
        if x < 0 or x >= self.width():
            return
        if y < 0 or y >= self.height():
            return
        return self.cells[x][y]
    
    def cell_rel(self, x, y, pos):
        if pos == "ul":                             # CASE A
            if x > 0 and y > 0:
                #return self.cell(x-1, y-1)
                return (x-1, y-1)
        if pos == "u":                              # CASE B
            if y > 0:
                #return self.cell(x, y-1)
                return (x, y-1)
        if pos == "ur":                             # CASE C
            if y > 0 and x < self.width()-1:
                #return self.cell(x+1, y-1)
                return (x+1, y-1)
        if pos == "r":                              # CASE F
            if x < self.width()-1:
                #return self.cell(x+1, y)
                return (x+1, y)
        if pos == "dr":                             # CASE I
            if x < self.width()-1 and y < self.height()-1:
                #return self.cell(x+1, y+1)
                return (x+1, y+1)
        if pos == "d":                              # CASE H
            if y < self.height()-1:
                #return self.cell(x, y+1)
                return (x, y+1)
        if pos == "dl":                             # CASE G
            if y < self.height()-1 and x > 0:
                #return self.cell(x-1, y+1)
                return (x-1, y+1)
        if pos == "l":                              # CASE D
            if x > 0:
                #return self.cell(x-1, y)
                return (x-1, y)
        return "null"
    
    def console_print(self):
        print("width:", self.width(), "height:", self.height())
        for y in range(self.height()):
            print("")
            for x in range(self.width()):
                if self.cell(x,y).hidden:
                    print("#", end=" ")
                elif self.cell(x,y).is_mine():
                    print("@", end=" ")
                else:
                    print(self.cell(x,y).value, end=" ")
    
    def count_mines(self, x, y):
        count = 0        
        positions = ["u", "d", "l", "r", "ul", "ur", "dl", "dr"]
        for i in positions:
            if self.cell_rel(x, y, i) != "null":
                if self.cell(self.cell_rel(x, y, i)[0], self.cell_rel(x, y, i)[1]).is_mine():
                    count = count + 1
        return count

    def reveal(self, x, y):
        if not self.cell(x, y).reveal():        # THE CELL HAS ALREADY BEEN REVEALED
            return
        if self.cell(x, y).is_mine():           # A MINE WAS REVEALED THE GAME IS LOST
            self.defeat = True
            return
        self.revealed += 1                      # count one more revealed safe cell
        if self.revealed == self.dimension()-self.mines:        # IF ALL SAFE CELLS HAVE BEEN REVEALED THE GAME IS WON
            self.victory = True
            return
        if self.cell(x, y).value != 0:          # A CELL WITH A NUMBER WAS REVEALED
            return
        positions = ["u", "d", "l", "r", "ul", "ur", "dl", "dr"]
        for i in positions:
            if self.cell_rel(x, y, i) != "null":
                #print("from", x, y, "trying", i, "which is at", self.cell_rel(x, y, i))
                self.reveal(self.cell_rel(x, y, i)[0], self.cell_rel(x, y, i)[1])
