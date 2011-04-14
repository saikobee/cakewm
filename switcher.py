#!/usr/bin/python2

from pypixel    import *

from const      import *
from util       import *

from window     import Window
from point      import Point

import modes

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

cnt = 0

mode = modes.ARRANGE

def cur_info_helper(cur):
    global cnt

    cnt += 1

    echo(">>>", cnt)
    echo(">>> POS   =", cur.pos)
    echo(">>> GRID  =", cur.grid_pos)
    echo(">>> SIZE  =", cur.size)
    echo(">>> GSIZE =", (cur.gw, cur.gh))
    echo()

def mod_wh(dw, dh):
    global cur

    if cur is None:
        return

    cur.gw = clamp(dw + cur.gw, 1, MAX_COL - cur.col)
    cur.gh = clamp(dh + cur.gh, 1, MAX_ROW - cur.row)

    cur.w = cur.gw * GRID_WIDTH
    cur.h = cur.gh * GRID_HEIGHT

    cur_info_helper(cur)

def mod_cr(dc, dr):
    global cur

    if cur is None:
        return

    cur.col = clamp(dc + cur.col, 0, MAX_COL - cur.gw)
    cur.row = clamp(dr + cur.row, 0, MAX_ROW - cur.gh)

    cur.x = cur.col * GRID_WIDTH
    cur.y = cur.row * GRID_HEIGHT

    cur_info_helper(cur)

def echo(*xs): print ' '.join(map(str, xs))

def new_window():
    global windows
    global cur

    if cur is not None:
        windows.append(cur)

    cur = Window()

def close_window():
    global cur

    cur = None

def change_mode():
    global mode

    if mode is modes.ARRANGE:
        mode = modes.NORMAL
        echo("--- NORMAL MODE")
        echo()
    else:
        mode = modes.ARRANGE
        echo("--- ARRANGE MODE")
        echo()

def dispatch_by_mode(key):
    global mode
    global arrange_binds
    global normal_binds

    def fallback():
        echo("!!!", key, "is not bound in this mode!")

    if mode is modes.ARRANGE:
       arrange_binds.get(key, fallback)()
    else:
       normal_binds.get(key, fallback)()

normal_binds = {
}

arrange_binds = {
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
}


binds.update({
    "q": lambda: dispatch_by_mode("q"),
    "w": lambda: dispatch_by_mode("w"),
    "e": lambda: dispatch_by_mode("e"),

    "a": lambda: dispatch_by_mode("a"),
    "s": lambda: dispatch_by_mode("s"),
    "d": lambda: dispatch_by_mode("d"),

    "z": lambda: dispatch_by_mode("z"),
    "x": lambda: dispatch_by_mode("x"),
    "c": lambda: dispatch_by_mode("c"),

    "h": lambda: dispatch_by_mode("h"),
    "j": lambda: dispatch_by_mode("j"),
    "k": lambda: dispatch_by_mode("k"),
    "l": lambda: dispatch_by_mode("l"),

    "y": lambda: dispatch_by_mode("y"),
    "u": lambda: dispatch_by_mode("u"),
    "b": lambda: dispatch_by_mode("b"),
    "n": lambda: dispatch_by_mode("n"),

    "o": new_window,
    "t": close_window,
    "i": change_mode,
})

for key, fun in binds.iteritems():
    bind(key, fun)

while True:
    for window in windows:
        window.unfocus()
        window.draw()

    if cur is not None:
        cur.focus()
        cur.draw()

    update()
    clear()

pause()
