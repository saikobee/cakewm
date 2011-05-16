#!/usr/bin/python2

import pypixel

import util

from binds      import Binds
from cake.wm    import WM

from junk       import display

pypixel.title("cakewm test program")
pypixel.show()

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

    "v": the_binds.move_win_nth_col(0),
    "b": the_binds.move_win_nth_col(1),
    "n": the_binds.move_win_nth_col(2),
    "m": the_binds.move_win_nth_col(3),

    "y": the_binds.select_nth_stack(0),
    "u": the_binds.select_nth_stack(1),
    "i": the_binds.select_nth_stack(2),
    "o": the_binds.select_nth_stack(3),

    "1": the_binds.select_nth_tag(0),
    "2": the_binds.select_nth_tag(1),
    "3": the_binds.select_nth_tag(2),
    "4": the_binds.select_nth_tag(3),
    "5": the_binds.select_nth_tag(4),
    "6": the_binds.select_nth_tag(5),
    "7": the_binds.select_nth_tag(6),
    "8": the_binds.select_nth_tag(7),
    "9": the_binds.select_nth_tag(8),

    "q": the_binds.move_win_nth_tag(0),
    "w": the_binds.move_win_nth_tag(1),
    "e": the_binds.move_win_nth_tag(2),
    "r": the_binds.move_win_nth_tag(3),

    "[" : the_binds.select_nth_screen(0),
    "]" : the_binds.select_nth_screen(1),
    "\\": the_binds.select_nth_screen(2),

    "0": the_binds.win_to_nth_screen(0),
    "-": the_binds.win_to_nth_screen(1),
    "=": the_binds.win_to_nth_screen(2),

    ",": the_binds.swap_tag_nth_screen(0),
    ".": the_binds.swap_tag_nth_screen(1),
    "/": the_binds.swap_tag_nth_screen(2),
}

for key, func in keybinds.iteritems():
    # Normal bind
    pypixel.bind(key, func)

    # Debug bind
    def debug_func(key=key, func=func):
        func()
        # util.debug(key + ": " + str(display))
        util.debug(key)
    pypixel.bind(key, debug_func)

while True:
    the_wm.organize()
    pypixel.update()
    pypixel.clear()

pypixel.pause()
