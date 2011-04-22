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
                    ]
                ),
                Stack(
                    cur=0,
                    items=[
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
    for i, stacks in cols.each():
        for j, stack in stacks.each():
            for k, window in stack.each():
                window.unfocus()
                if (cols.cur, stacks.cur, stack.cur) == (i, j, k):
                    window.focus()
                window.draw()
    update()
    clear()

pause()
