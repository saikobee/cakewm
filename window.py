import pypixel
import util
from focusable      import Focusable
from floatingrect   import FloatingRect

class Window(FloatingRect, Focusable):
    NUMBER = 0
    NAME = "Win"

    def __str__(self):
        return "%s:%i" % (type(self).NAME, self.number)

    def __init__(self, **kwargs):
        super(Window, self).__init__(**kwargs)

        self.color = kwargs.get("color", util.INFINITE_RAINBOW.next())

        self.number = type(self).NUMBER

        type(self).NUMBER += 1

    def draw_fullscreen(self, screen):
       w = screen.w
       h = screen.h
       x = 0
       y = 0

       pypixel.rectangle(self.color, ((x, y), (w, h)))

    def draw(self):
        colr3 = pypixel.grey(20)
        colr2 = pypixel.grey(50)
        colr1 = self.color

        if self.focused:
            colr2 = pypixel.grey(70)

        x = self.x
        y = self.y
        w = self.w
        h = self.h
        q = 2; rec1 = ((x + q, y + q), (w - q - q, h - q - q))
        q = 1; rec2 = ((x + q, y + q), (w - q - q, h - q - q))
        pass;  rec3 = self.rect

        pypixel.rectangle(colr3, rec3)
        pypixel.rectangle(colr2, rec2)
        pypixel.rectangle(colr1, rec1)
