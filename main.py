#!/usr/bin/python2

from pypixel    import *

from util       import *
from window     import Window
from columns    import Columns
from stacks     import Stacks
from stack      import Stack
from window     import Window

title("cakewm test program")
show()

binds = {}

cols = Columns(
    cur=0,
    items=[
        Stacks(
            cur=0,
            items=[
                Stack(
                    cur=0,
                    items=[
                        Window(),
                        Window(),
                        Window(),
                    ]
                ),
                Stack(
                    cur=0,
                    items=[
                        Window(),
                        Window(),
                        Window(),
                        Window(),
                        Window(),
                    ]
                ),
            ],
        ),
        Stacks(
            cur=0,
            items=[
                Stack(
                    cur=0,
                    items=[
                        Window(),
                        Window(),
                    ]
                ),
            ]
        ),
    ]
)

cols.organize()

binds = {
    "j": cols.go_next,
    "k": cols.go_prev,
}

for key, func in binds.iteritems():
    bind(key, func)

while True:
    a = cols.cur
    for i, stacks in cols.each():
        b = stacks.cur
        for j, stack in stacks.each():
            c = stack.cur
            for k, window in stack.each():
                window.unfocus()
                if (a, b, c) == (i, j, k):
                    window.focus()
            stack.draw()

    update()
    clear()

pause()
