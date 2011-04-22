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

while True:
    for col in cols.items:
        for stack in col.items:
            for window in stack.items:
                window.draw()
    update()
    clear()

pause()
