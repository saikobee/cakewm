#!/usr/bin/python2

import atexit

import pypixel

import util

from binds      import Binds
from cake.wm    import WM

from junk       import display
from conf       import conf

pypixel.title("cakewm test program")
pypixel.show()

wm      = WM(display=display)
binds   = Binds(display=display)

keybinds = {
    "p": binds.add_win,
    "`": binds.close_win,

    "y": binds.move_win_prev,
    "u": binds.select_win_prev,
    "i": binds.select_win_next,
    "o": binds.move_win_next,

    "h": binds.select_col_prev,
    "j": binds.select_stack_next,
    "k": binds.select_stack_prev,
    "l": binds.select_col_next,

    "b": binds.move_win_col_prev,
    "n": binds.move_win_stack_next,
    "m": binds.move_win_stack_prev,
    ",": binds.move_win_col_next,

    "1": binds.select_tag_1,
    "2": binds.select_tag_2,
    "3": binds.select_tag_3,
    "4": binds.select_tag_4,
    # "5": binds.select_tag_5,
    # "6": binds.select_tag_6,
    # "7": binds.select_tag_7,
    # "8": binds.select_tag_8,
    # "9": binds.select_tag_9,

    "a": binds.dec_tag_ratio,
    "s": binds.inc_col_ratio,
    "d": binds.dec_col_ratio,
    "f": binds.inc_tag_ratio,

    "z": binds.tag_master_next,
    "x": binds.col_master_next,
    "c": binds.toggle_bar,

    "q": binds.move_win_tag_1,
    "w": binds.move_win_tag_2,
    "e": binds.move_win_tag_3,
    "r": binds.move_win_tag_4,
    # ???: binds.move_win_tag_5,
    # ???: binds.move_win_tag_6,
    # ???: binds.move_win_tag_7,
    # ???: binds.move_win_tag_8,
    # ???: binds.move_win_tag_9,

    "]" : binds.select_screen_next,
    "[" : binds.select_screen_prev,

    "-": binds.move_win_screen_next,
    "=": binds.move_win_screen_prev,

    "/": binds.swap_tags_next,
    ".": binds.swap_tags_prev,

    "\\": binds.toggle_fullscreen,

    ";": binds.column_magic,
    "'": binds.stack_magic,
}

for key, func in keybinds.iteritems():
    # Normal bind
    pypixel.bind(key, func)

    # Debug bind
    #def debug_func(key=key, func=func):
        #func()
        #util.debug("%s: %s" % (key, str(display)))
        #util.debug(key)
    #pypixel.bind(key, debug_func)

util.debug(conf)

@atexit.register
def goodbye():
    if conf.exit_message:
        util.debug("Thanks for using cakewm!")
        util.debug("Goodbye!")

if conf.welcome_message:
    util.debug("Welcome to cakewm!")

while True:
    wm.organize()
    wm.set_focii()
    wm.draw_wallpaper()
    wm.draw()
    wm.update_top_bar()
    wm.update_bottom_bar()
    wm.draw_bars()
    #wm.debug_bars()
    pypixel.update()
    pypixel.clear()

pypixel.pause()
