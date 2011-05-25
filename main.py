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
    "p": the_binds.add_win,
    "`": the_binds.close_win,

    "a": the_binds.select_next_win,
    "s": the_binds.select_prev_win,

    "d": the_binds.move_win_next,
    "f": the_binds.move_win_prev,

    "y": the_binds.select_stack_next,
    "u": the_binds.select_stack_prev,

    "z": the_binds.move_win_stack_next,
    "x": the_binds.move_win_stack_prev,

    "h": the_binds.select_col_next,
    "j": the_binds.select_col_prev,

    "b": the_binds.move_win_col_next,
    "n": the_binds.move_win_col_next,

    "1": the_binds.select_tag_1,
    "2": the_binds.select_tag_2,
    "3": the_binds.select_tag_3,
    "4": the_binds.select_tag_4,
    # "5": the_binds.select_tag_5,
    # "6": the_binds.select_tag_6,
    # "7": the_binds.select_tag_7,
    # "8": the_binds.select_tag_8,
    # "9": the_binds.select_tag_9,

    "5": the_binds.inc_tag_ratio,
    "6": the_binds.dec_tag_ratio,
    "7": the_binds.set_tag_ratio_complement,

    "8": the_binds.inc_col_ratio,
    "9": the_binds.dec_col_ratio,
    "0": the_binds.set_col_ratio_complement,

    "q": the_binds.move_win_tag_1,
    "w": the_binds.move_win_tag_2,
    "e": the_binds.move_win_tag_3,
    "r": the_binds.move_win_tag_4,
    # ???: the_binds.move_win_tag_5,
    # ???: the_binds.move_win_tag_6,
    # ???: the_binds.move_win_tag_7,
    # ???: the_binds.move_win_tag_8,
    # ???: the_binds.move_win_tag_9,

    "[" : the_binds.select_screen_next,
    "]" : the_binds.select_screen_next,

    "-": the_binds.win_to_screen_next,
    "=": the_binds.win_to_screen_next,

    ".": the_binds.swap_tag_screen_next,
    "/": the_binds.swap_tag_screen_prev,

    ";": the_binds.toggle_fullscreen,

    "'" : the_binds.stack_magic,
    "\\": the_binds.column_magic,
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
