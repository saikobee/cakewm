#!/usr/bin/python2

from pypixel    import *

from const      import *
from util       import *

from window     import Window
from point      import Point

title("cakewm test program")
show()

cur = None

binds = {}

windows = []

class Cursor(object):
    def __init__(self):
        self.col    = 0
        self.row    = 0
        self.width  = 1
        self.height = 1

cur = Window()

def mod_wh(dw, dh):
    global cur

    cur.w = clamp(dw + cur.w, 1, MAX_COL - cur.col)
    cur.h = clamp(dh + cur.h, 1, MAX_ROW - cur.row)

def mod_cr(dc, dr):
    global cur

    echo("dc, dr =", (dc, dr))
    echo("cur(.col, .row) =", (cur.col, cur.row))

    echo("GRID POS :", cur.grid_pos)
    cur.col = clamp(dc + cur.col, 0, MAX_COL - cur.w)
    cur.row = clamp(dr + cur.row, 0, MAX_ROW - cur.h)
    echo("GRID POS':", cur.grid_pos)

    echo("POS :", cur.pos)
    cur.x = cur.col * GRID_WIDTH
    cur.y = cur.row * GRID_HEIGHT
    echo("POS':", cur.pos)

def echo(*xs): print ' '.join(map(str, xs))

binds.update({
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

def new_window():
    global windows
    global cur

    windows.append(cur)
    cur = Window()

binds["o"] = new_window

for key, fun in binds.iteritems():
    bind(key, fun)

new_window()

while True:
    for window in windows:
        window.unfocus()
        if window is cur:
            window.focus()
        window.draw()

    update()
    clear()

pause()
