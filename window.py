from pypixel    import *
from const      import *

class Window(object):
    FOCUS_COLOR = WHITE

    def __init__(self, **kwargs):
        self.size = kwargs.get("size", (0, 0))
        self.pos  = kwargs.get("pos",  (0, 0))

        self.rect = kwargs.get("rect", ((0, 0), (0, 0)))

        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)

        self.w = kwargs.get("w", WIDTH  / MAX_COL)
        self.h = kwargs.get("h", HEIGHT / MAX_ROW)

        self.gw = kwargs.get("gw", 1)
        self.gh = kwargs.get("gh", 1)

        self.row = kwargs.get("row", 0)
        self.col = kwargs.get("col", 0)

        self.focused = False

        hsl = (random(360), 100, 50)
        rgb = hsl2rgb(hsl)
        self.color = kwargs.get("color", rgb)

    def draw(self):
        #if self.focused: rectangle(WHITE,      self.rect)
        if self.focused:
            q = 18; rec1 = ((self.x + q, self.y + q), (self.w - 2*q, self.h - 2*q))
            q =  9; rec2 = ((self.x + q, self.y + q), (self.w - 2*q, self.h - 2*q))
            q =  3; rec3 = ((self.x + q, self.y + q), (self.w - 2*q, self.h - 2*q))

            rectangle(BLACK,      self.rect)
            rectangle(WHITE,           rec3)
            rectangle(BLACK,           rec2)
            rectangle(self.color,      rec1)
            #rectangle(self.color, self.rect)
        else:
            q = 3
            rect = ((self.x + q, self.y + q), (self.w - 2*q, self.h - 2*q))
            rectangle(self.color, rect)
            #rectangle(self.color, self.rect)

    def focus(self):        self.focused = True
    def unfocus(self):      self.focused = False
    def focus_toggle(self): self.focused = not self.focused

    @property
    def size(self):
        return (self.w, self.h)

    @size.setter
    def size(self, size):
        self.w, self.h = size

    @property
    def pos(self):
        return (self.x, self.y)

    @pos.setter
    def pos(self, pos):
        self.x, self.y = pos

    @property
    def grid_pos(self):
        return (self.row, self.col)

    @grid_pos.setter
    def grid_pos(self, grid_pos):
        self.row, self.col = grid_pos

    @property
    def rect(self):
        return (self.pos, self.size)

    @rect.setter
    def rect(self, rect):
        self.pos, self.size = rect
