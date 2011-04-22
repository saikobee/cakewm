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

cur = None

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

while True:
    for i, stacks in cols.each():
        for j, stack in stacks.each():
            for k, window in stack.each():
                if (cols.cur, stacks.cur, stack.cur) == (i, j, k):
                    window.focus()
                window.draw()
    update()
    clear()

pause()
