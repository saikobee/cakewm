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
    "p": the_binds.add_win(),
    "`": the_binds.close_win(),

    "a": the_binds.select_next_win(),
    "s": the_binds.select_prev_win(),

    "d": the_binds.move_win_next(),
    "f": the_binds.move_win_prev(),

    "y": the_binds.select_nth_stack(0),
    "u": the_binds.select_nth_stack(1),
    "i": the_binds.select_nth_stack(2),
    "o": the_binds.select_nth_stack(3),

    "z": the_binds.move_win_nth_stack(0),
    "x": the_binds.move_win_nth_stack(1),
    "c": the_binds.move_win_nth_stack(2),
    "v": the_binds.move_win_nth_stack(3),

    "h": the_binds.select_nth_col(0),
    "j": the_binds.select_nth_col(1),
    "k": the_binds.select_nth_col(2),
    "l": the_binds.select_nth_col(3),

    "b": the_binds.move_win_nth_col(0),
    "n": the_binds.move_win_nth_col(1),
    "m": the_binds.move_win_nth_col(2),
    ",": the_binds.move_win_nth_col(3),

    "1": the_binds.select_nth_tag(0),
    "2": the_binds.select_nth_tag(1),
    "3": the_binds.select_nth_tag(2),
    "4": the_binds.select_nth_tag(3),

    "5": the_binds.mod_tag_ratio(-0.05),
    "6": the_binds.mod_tag_ratio(+0.05),
    "7": the_binds.set_tag_ratio_complement(),

    "8": the_binds.mod_col_ratio(-0.05),
    "9": the_binds.mod_col_ratio(+0.05),
    "0": the_binds.set_col_ratio_complement(),

    "q": the_binds.move_win_nth_tag(0),
    "w": the_binds.move_win_nth_tag(1),
    "e": the_binds.move_win_nth_tag(2),
    "r": the_binds.move_win_nth_tag(3),

    "[" : the_binds.select_nth_screen(0),
    "]" : the_binds.select_nth_screen(1),

    "-": the_binds.win_to_nth_screen(0),
    "=": the_binds.win_to_nth_screen(1),

    ".": the_binds.swap_tag_nth_screen(0),
    "/": the_binds.swap_tag_nth_screen(1),

    ";": the_binds.toggle_fullscreen(),

    "'" : the_binds.stack_magic(),
    "\\": the_binds.column_magic(),
}

for key, func in keybinds.iteritems():
    # Normal bind
    # pypixel.bind(key, func)

    # Debug bind
    def debug_func(key=key, func=func):
        func()
        # util.debug("%s: %s" % (key, str(display)))
        util.debug(key)
    pypixel.bind(key, debug_func)

while True:
    the_wm.organize()
    the_wm.set_focii()
    the_wm.draw()
    pypixel.update()
    pypixel.clear()

pypixel.pause()
