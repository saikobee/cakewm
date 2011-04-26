#!/usr/bin/python2

from pypixel    import *

from util       import *
from window     import Window
from columns    import Columns
from stacks     import Stacks
from stack      import Stack
from window     import Window
from tags       import Tags

title("cakewm test program")
show()

tags = Tags(
    cur=0,
    items=[
        Columns(
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
                            ]
                        )
                    ]
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
    ]
)

tags.organize()

binds = {
    "l": tags.go_col_next,
    "h": tags.go_col_prev,

    "j": tags.go_stack_next,
    "k": tags.go_stack_prev,

    "u": tags.go_win_next,
    "y": tags.go_win_prev,

    "o": tags.make_new_window,

    "d": tags.move_window_col_next,
    "a": tags.move_window_col_prev,
}

for key, func in binds.iteritems():
    bind(key, func)

while True:
    tags.big_looper()

    update()
    clear()

pause()
