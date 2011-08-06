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

pypixel.HOOKS["resize"] = wm.set_resolution

bind_funcs = [
    "add_win",
    "close_win",

    "move_win_prev",
    "select_win_prev",
    "select_win_next",
    "move_win_next",

    "select_col_prev",
    "select_stack_next",
    "select_stack_prev",
    "select_col_next",

    "move_win_col_prev",
    "move_win_stack_next",
    "move_win_stack_prev",
    "move_win_col_next",

    "select_tag_1",
    "select_tag_2",
    "select_tag_3",
    "select_tag_4",
    "select_tag_5",
    "select_tag_6",
    "select_tag_7",
    "select_tag_8",
    "select_tag_9",

    "dec_tag_ratio",
    "inc_col_ratio",
    "dec_col_ratio",
    "inc_tag_ratio",

    "tag_master_next",
    "col_master_next",

    "toggle_bar",

    "move_win_tag_1",
    "move_win_tag_2",
    "move_win_tag_3",
    "move_win_tag_4",
    "move_win_tag_5",
    "move_win_tag_6",
    "move_win_tag_7",
    "move_win_tag_8",
    "move_win_tag_9",

    "select_screen_next",
    "select_screen_prev",

    "move_win_screen_next",
    "move_win_screen_prev",

    "swap_tags_next",
    "swap_tags_prev",

    "toggle_fullscreen",

    "column_magic_next",
    "column_magic_prev",
    "stack_magic_next",
    "stack_magic_prev",
]

for func in bind_funcs:
    # Normal bind
    pypixel.bind(getattr(conf, "key_" + func), getattr(binds, func))

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
