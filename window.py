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

        self.color = kwargs.get("color", INFINITE_RAINBOW.next())

        self.number = type(self).NUMBER

        type(self).NUMBER += 1

    def draw(self):
        colr3 = BLACK
        colr2 = GREY
        colr1 = self.color

        if self.focused:
            colr2 = WHITE

        q = 2; rec1 = ((self.x + q, self.y + q), (self.w - 2*q, self.h - 2*q))
        q = 1; rec2 = ((self.x + q, self.y + q), (self.w - 2*q, self.h - 2*q))
        pass;  rec3 = self.rect

        rectangle(colr3, rec3)
        rectangle(colr2, rec2)
        rectangle(colr1, rec1)
