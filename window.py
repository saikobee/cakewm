import pypixel
import util
from focusable      import Focusable
from floatingrect   import FloatingRect
from conf           import conf

class Window(FloatingRect, Focusable):
    NUMBER = 0
    NAME = "Win"

    def __str__(self):
        return "%s:%i" % (type(self).NAME, self.number)

    def title(self):
        return "Window %d" % self.number

    def __init__(self, **kwargs):
        super(Window, self).__init__(**kwargs)

        self.color = kwargs.get("color", util.INFINITE_RAINBOW.next())

        self.number = type(self).NUMBER

        type(self).NUMBER += 1

    def draw_fullscreen(self, screen):
        tag = screen.item()
        w = tag.w
        h = tag.h
        x = 0
        y = tag.y_offset

        pypixel.rectangle(self.color, ((x, y), (w, h)))

    def draw(self):
        colr3 = conf.window_unfocused_shadow
        colr2 = conf.window_unfocused_highlight
        colr1 = self.color

        if self.focused:
            colr3 = conf.window_focused_shadow
            colr2 = conf.window_focused_highlight

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
