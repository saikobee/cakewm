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

col    = 0
row    = 0
width  = 1
height = 1

def mod_wh(dw, dh):
    global row
    global col
    global width
    global height

    width  += dw
    height += dh

    width  = clamp(width,  1, MAX_COL - col)
    height = clamp(height, 1, MAX_ROW - row)

def mod_cr(dc, dr):
    global row
    global col
    global width
    global height

    col += dc
    row += dr

    col = clamp(col, 0, MAX_COL - width)
    row = clamp(row, 0, MAX_ROW - height)

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
        if (col <= window.col < (col + width) and
            row <= window.row < (row + height)):
            print "Selecting window at", window.grid_pos
            window.focus()
        window.draw()

    update()
    clear()

pause()
