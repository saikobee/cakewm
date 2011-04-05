#!/usr/bin/python2

from pypixel import *

title("cakewm test program")
show()

class Window(object):
    def __init__(self, **kwargs):
        self.size = kwargs.get("size", (0, 0))
        self.pos  = kwargs.get("pos",  (0, 0))

        self.rect = kwargs.get("rect", ((0, 0), (0, 0)))

        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)

        self.w = kwargs.get("w", 10)
        self.h = kwargs.get("h", 10)

        self.row = kwargs.get("row", 0)
        self.col = kwargs.get("col", 0)

        self.focused = False

        hsl = (random(360), 100, 50)
        self.color = hsl2rgb(hsl)

    def draw(self):
        if self.focused: rectangle(WHITE,      self.rect)
        else:            rectangle(self.color, self.rect)

    def focus(self):
        self.focused = True

    def unfocus(self):
        self.focused = False

    def focus_toggle(self):
        self.focused = not self.focused

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
    def rect(self):
        return (self.pos, self.size)

    @rect.setter
    def rect(self, rect):
        self.pos, self.size = rect

def select_up():
    cur = Window.current
    row = cur.row - 1
    col = cur.col
    row = max(row, 0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inc_x(self, dx=1): self.x += dx
    def inc_y(self, dy=1): self.y += dy

    @property
    def pos(self): return (self.x, self.y)

cursor = Point(0, 0)

add_row = lambda dr: cursor.inc_x(dr)
add_col = lambda dc: cursor.inc_y(dc)

binds = {
    "h": lambda: add_row(-1),
    "j": lambda: add_col(-1),
    "k": lambda: add_col(+1),
    "l": lambda: add_row(+1),

#   "y": move_left,
#   "u": move_down,
#   "i": move_up,
#   "o": move_right,

#   "b": resize_left,
#   "n": resize_down,
#   "m": resize_up,
#   ",": resize_right,
}

for key, fun in binds.iteritems():
    bind(key, fun)

windows = []
windows.append(Window(
    x=10,   y=20,
    w=30,   h=40,
    row=0,  col=0
))
windows.append(Window(
    x=90,   y=20,
    w=20,   h=30,
    row=0,  col=1
))
windows.append(Window(
    x=10,   y=150,
    w=80,   h=80,
    row=1,  col=0
))

while True:
    for window in windows:
        window.unfocus()
        if window.pos == cursor.pos:
            window.focus()

        window.draw()
        print "(COL, ROW) = (", cursor.x, ",", cursor.y, ")"
        update()

pause()
