#!/usr/bin/python2

from pypixel import *

title("cakewm test program")
show()

class Window(object):
    def __init__(self, **kwargs):
        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)

        self.w = kwargs.get("w", 10)
        self.h = kwargs.get("h", 10)

        self.row = kwargs.get("row", 0)
        self.col = kwargs.get("col", 0)

def select_up():
    cur = Window.current
    row = cur.row - 1
    col = cur.col
    row = max(row, 0)

binds = {
    "h": select_left,
    "j": select_down,
    "k": select_up,
    "l": select_right,

    "y": move_left,
    "u": move_down,
    "i": move_up,
    "o": move_right,

    "b": resize_left,
    "n": resize_down,
    "m": resize_up,
    ",": resize_right,
}

for key, fun in binds.iteritems():
    bind(key, fun)

pause()
