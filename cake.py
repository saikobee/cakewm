#!/usr/bin/python2

from pypixel import *

title("cakewm test program")
show()

MAX_COL = 3
MAX_ROW = 3

def clamp(x, a, b):
    if   x < a: return a
    elif x > b: return b
    else:       return x

class Window(object):
    FOCUS_COLOR = WHITE

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
        #if self.focused: rectangle(WHITE,      self.rect)
        if self.focused:
            q = 18; rec1 = ((self.x + q, self.y + q), (self.w - 2*q, self.h - 2*q))
            q =  9; rec2 = ((self.x + q, self.y + q), (self.w - 2*q, self.h - 2*q))
            q =  3; rec3 = ((self.x + q, self.y + q), (self.w - 2*q, self.h - 2*q))

            rectangle(BLACK,      self.rect)
            rectangle(WHITE,           rec3)
            rectangle(BLACK,           rec2)
            rectangle(self.color,      rec1)
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

def select_up():
    cur = Window.current
    row = cur.row - 1
    col = cur.col
    row = max(row, 0)

class Point:
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

cursor = Point(0, 0)

add_row = lambda dr: cursor.inc_x(dr)
add_col = lambda dc: cursor.inc_y(dc)

binds = {
    "h": lambda: add_col(-1),
    "j": lambda: add_row(+1),
    "k": lambda: add_row(-1),
    "l": lambda: add_col(+1),

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

windows = [
    Window(x=10,  y=20,  w=30, h=40, row=0, col=0),
    Window(x=140, y=20,  w=20, h=30, row=0, col=1),
    Window(x=10,  y=150, w=80, h=80, row=1, col=0),

    Window(x=140, y=100, w=80, h=80, row=1, col=1),
    Window(x=250, y=50,  w=80, h=80, row=1, col=2),
    Window(x=300, y=200, w=80, h=80, row=2, col=2),
]

windows = []
dw = WIDTH  / MAX_COL
dh = HEIGHT / MAX_ROW
for row in xrange(MAX_ROW):
    for col in xrange(MAX_COL):
        dx = dw * col
        dy = dh * row
        windows.append(Window(
            x=dx,
            y=dy,
            w=dw,
            h=dh,
            row=row,
            col=col
        ))

while True:
    for window in windows:
        window.unfocus()
        if window.grid_pos == cursor.pos:
            window.focus()

        window.draw()
    update()
    clear()

pause()
