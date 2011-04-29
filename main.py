#!/usr/bin/python2

from pypixel    import *

from util       import *
from const      import *
from window     import Window
from columns    import Columns
from stacks     import Stacks
from stack      import Stack
from window     import Window
from tags       import Tags

title("cakewm test program")
show()

#tags = SIMPLE_TAGS
tags = THREE_COLUMN_TAGS
tags.organize()

binds = {
    "l": tags.go_col_next,
    "h": tags.go_col_prev,

    "j": tags.go_stack_next,
    "k": tags.go_stack_prev,

    "u": tags.go_win_next,
    "y": tags.go_win_prev,

    "o": tags.make_new_win,

    "d": tags.move_win_col_next,
    "a": tags.move_win_col_prev,

    "s": tags.move_win_stack_next,
    "w": tags.move_win_stack_prev,

    "n": tags.make_win_stack_next,
    "m": tags.make_win_stack_prev,

    "b": tags.make_win_col_next,
    "v": tags.make_win_col_prev,
}

for key, func in binds.iteritems():
    bind(key, func)

while True:
    tags.big_looper()

    debug(tags)

    update()
    clear()

pause()
