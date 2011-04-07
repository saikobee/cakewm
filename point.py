from util   import clamp
from const  import *

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inc_x(self, dx=1):
        self.x += dx
        self.x = clamp(self.x, 0, MAX_COL - 1)

    def inc_y(self, dy=1):
        self.y += dy
        self.y = clamp(self.y, 0, MAX_ROW - 1)

    @property
    def pos(self): return (self.x, self.y)

    def __repr__(self):
        return "(%s, %s)" % self.pos
