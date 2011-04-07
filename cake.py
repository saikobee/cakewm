#!/usr/bin/python2

from pypixel    import *
from window     import Window
from point      import Point
from const      import *
from util       import *

title("cakewm test program")
show()

class Container(object): pass
box = Container()
box.A = object()
box.B = object()

def select_up():
    cur = Window.current
    row = cur.row - 1
    col = cur.col
    row = max(row, 0)

cursor = Point(0, 0)

add_row = lambda dr: cursor.inc_x(dr)
add_col = lambda dc: cursor.inc_y(dc)

binds = {
#   "h": lambda: add_col(-1),
#   "j": lambda: add_row(+1),
#   "k": lambda: add_row(-1),
#   "l": lambda: add_col(+1),

#   "y": move_left,
#   "u": move_down,
#   "i": move_up,
#   "o": move_right,

#   "b": resize_left,
#   "n": resize_down,
#   "m": resize_up,
#   ",": resize_right,
}

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
            col=col,
            # For 6x6 grid
            #color=hsl2rgb((10 * row + 60 * col, 100, 50))

            # For 10x10 grid
            color=hsl2rgb((5 * row + 30 * col, 100, 50))
        ))

class Cursor(object):
    def __init__(self):
        self.col    = 0
        self.row    = 0
        self.width  = 1
        self.height = 1

cur = Cursor()

def mod_wh(dw, dh):
    global cur

    cur.width  += dw
    cur.height += dh

    cur.width  = clamp(cur.width,  1, MAX_COL - cur.col)
    cur.height = clamp(cur.height, 1, MAX_ROW - cur.row)

def mod_cr(dc, dr):
    global cur

    cur.col += dc
    cur.row += dr

    cur.col = clamp(cur.col, 0, MAX_COL - cur.width)
    cur.row = clamp(cur.row, 0, MAX_ROW - cur.height)

def echo(*xs): print xs

# Screw Python for only have in-place merge
binds = dict(binds, **{
    "q": lambda: mod_wh(-1, -1),
    "w": lambda: mod_wh( 0, -1),
    "e": lambda: mod_wh(+1, -1),

    "a": lambda: mod_wh(-1,  0),
    "s": lambda: mod_wh( 0, +1),
    "d": lambda: mod_wh(+1,  0),

    "z": lambda: mod_wh(-1, +1),
    "x": lambda: mod_wh( 0, +1),
    "c": lambda: mod_wh(+1, +1),

    "h": lambda: mod_cr(-1,  0),
    "j": lambda: mod_cr( 0, +1),
    "k": lambda: mod_cr( 0, -1),
    "l": lambda: mod_cr(+1,  0),

    "y": lambda: mod_cr(-1, -1),
    "u": lambda: mod_cr(+1, -1),
    "b": lambda: mod_cr(-1, +1),
    "n": lambda: mod_cr(+1, +1),
})

for key, fun in binds.iteritems():
    bind(key, fun)

while True:
    for window in windows:
        window.unfocus()
        if (cur.col <= window.col < (cur.col + cur.width) and
            cur.row <= window.row < (cur.row + cur.height)):
            window.focus()
        window.draw()

    update()
    clear()

pause()
