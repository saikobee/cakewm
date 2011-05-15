#!/usr/bin/python2

from pypixel    import *

import util

from binds      import Binds
from cake.wm    import WM

from junk       import display

title("cakewm test program")
show()

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

    "1": the_binds.select_nth_tag(0),
    "2": the_binds.select_nth_tag(1),
    "3": the_binds.select_nth_tag(2),
    "4": the_binds.select_nth_tag(3),
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
