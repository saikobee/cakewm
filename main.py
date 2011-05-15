#!/usr/bin/python2

from pypixel    import *

import util
from util       import *

from display    import Display
from screen     import Screen
from tag        import Tag
from column     import Column
from stack      import Stack
from window     import Window
from binds      import Binds

from cake.wm    import WM

title("cakewm test program")
show()

display = \
Display(
    cur=0,
    items=[
        Screen(
            cur=0,
            items=[
                Tag(
                    cur=0,
                    items=[
                        Column(
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
                            ]
                        ),
                        Column(
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
                        Column(
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
                                Stack(
                                    cur=0,
                                    items=[
                                        Window(),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ]
)

the_wm      = WM(display)
the_binds   = Binds(display)


keybinds = {
    "a": the_binds.add_win(),
    "c": the_binds.close_win(),

    "u": the_binds.select_next_win(),
    "y": the_binds.select_prev_win(),

    "h": the_binds.select_nth_col(0),
    "j": the_binds.select_nth_col(1),
    "k": the_binds.select_nth_col(2),
    "l": the_binds.select_nth_col(3),
}

for key, func in keybinds.iteritems():
    # Normal bind
    #bind(key, func)

    # Debug bind
    def debug_func(func=func):
        func()
        util.debug(display)
    bind(key, debug_func)

while True:
    the_wm.organize()
    update()
    clear()

pause()
