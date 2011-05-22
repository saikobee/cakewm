from pypixel    import *
from util       import *

from focusable      import Focusable
from floatingrect   import FloatingRect

class Window(FloatingRect, Focusable):
    FOCUS_COLOR = WHITE
    NUMBER = 0

    def __str__(self):
        return "#W:%i" % self.number

    def __init__(self, **kwargs):
        super(Window, self).__init__(**kwargs)

        self.color = kwargs.get("color", THE_RAINBOW.next())

        self.number = type(self).NUMBER

        type(self).NUMBER += 1

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
