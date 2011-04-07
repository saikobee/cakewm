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

cmd_q = []
keys = "q w e r t y".split()
for n in xrange(6):
    print "BINDING", keys[n], "TO", n
    def appender(n):
        def inner():
            print "Pressed key '%s'" % keys[n]
            cmd_q.append(n)
        return inner
    binds[keys[n]] = appender(n)
print "OMG THIS IS n:", n

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
            col=col,
            color=hsl2rgb((10 * row + 60 * col, 100, 50))
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

# Screw Python for only have in-place merge
binds = dict(binds, **{
    "q": lambda: mod_wh(-1, -1),
    "w": lambda: mod_wh( 0, -1),
    "e": lambda: mod_wh(+1, -1),

    "a": lambda: mod_wh(-1,  0),
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
            print "Selecting window at", window.grid_pos
            window.focus()
        window.draw()

    update()
    clear()

pause()
