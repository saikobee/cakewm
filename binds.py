import util
import itertools
from window import Window
from ratio  import Ratio

class Binds(object):
    "A binds object is used for making keybinds"

    def __init__(self, **kwargs):
        util.debug(kwargs)
        self.display = kwargs["display"]
        self.conf    = kwargs["conf"]

    def screen(self):
        screen = self.display.item()
        return screen

    def tag(self):
        screen = self.screen()
        tag    = screen.item()
        return tag

    def col(self):
        tag = self.tag()
        col = tag.item()
        return col

    def stack(self):
        col   = self.col()
        stack = col.item()
        return stack

    def display_do(func):
        def inner(self, func=func):
            display = self.display
            if display is not None:
                func(display)

        return inner

    def screen_do(func):
        def inner(self, func=func):
            screen = self.screen()
            if screen is not None:
                func(screen)

        return inner

    def tag_do(func):
        def inner(self, func=func):
            tag = self.tag()
            if tag is not None:
                func(tag)

        return inner

    def col_do(func):
        def inner(self, func=func):
            col = self.col()
            if col is not None:
                func(col)

        return inner

    def stack_do(func):
        def inner(self, func=func):
            stack = self.stack()
            if stack is not None:
                func(stack)

        return inner

    # Display binds
    move_win_screen_next = display_do(lambda x: x.move_win_screen_next())
    move_win_screen_prev = display_do(lambda x: x.move_win_screen_prev())
    select_screen_next   = display_do(lambda x: x.select_screen_next())
    select_screen_prev   = display_do(lambda x: x.select_screen_prev())
    swap_tags_next       = display_do(lambda x: x.swap_tags_next())
    swap_tags_prev       = display_do(lambda x: x.swap_tags_prev())

    # Screen binds
    move_win_tag_next = screen_do(lambda x: x.move_win_tag_next())
    move_win_tag_prev = screen_do(lambda x: x.move_win_tag_prev())
    move_win_tag_1    = screen_do(lambda x: x.move_win_tag_num(0))
    move_win_tag_2    = screen_do(lambda x: x.move_win_tag_num(1))
    move_win_tag_3    = screen_do(lambda x: x.move_win_tag_num(2))
    move_win_tag_4    = screen_do(lambda x: x.move_win_tag_num(3))
    move_win_tag_5    = screen_do(lambda x: x.move_win_tag_num(4))
    move_win_tag_6    = screen_do(lambda x: x.move_win_tag_num(5))
    move_win_tag_7    = screen_do(lambda x: x.move_win_tag_num(6))
    move_win_tag_8    = screen_do(lambda x: x.move_win_tag_num(7))
    move_win_tag_9    = screen_do(lambda x: x.move_win_tag_num(8))
    select_tag_next   = screen_do(lambda x: x.select_tag_next())
    select_tag_prev   = screen_do(lambda x: x.select_tag_prev())
    select_tag_1      = screen_do(lambda x: x.select_tag_num(0))
    select_tag_2      = screen_do(lambda x: x.select_tag_num(1))
    select_tag_3      = screen_do(lambda x: x.select_tag_num(2))
    select_tag_4      = screen_do(lambda x: x.select_tag_num(3))
    select_tag_5      = screen_do(lambda x: x.select_tag_num(4))
    select_tag_6      = screen_do(lambda x: x.select_tag_num(5))
    select_tag_7      = screen_do(lambda x: x.select_tag_num(6))
    select_tag_8      = screen_do(lambda x: x.select_tag_num(7))
    select_tag_9      = screen_do(lambda x: x.select_tag_num(8))

    # Tag binds
    column_magic         = tag_do(lambda x: x.column_magic())
    toggle_fullscreen    = tag_do(lambda x: x.toggle_fullscreen())
    move_win_col_next    = tag_do(lambda x: x.move_win_col_next())
    move_win_col_prev    = tag_do(lambda x: x.move_win_col_prev())
    select_col_next      = tag_do(lambda x: x.select_col_next())
    select_col_prev      = tag_do(lambda x: x.select_col_prev())
    inc_tag_ratio        = tag_do(lambda x: x.inc_tag_ratio())
    dec_tag_ratio        = tag_do(lambda x: x.dec_tag_ratio())
    complement_tag_ratio = tag_do(lambda x: x.complement_tag_ratio())

    # Column binds
    stack_magic          = col_do(lambda x: x.stack_magic())
    move_win_stack_next  = col_do(lambda x: x.move_win_stack_next())
    move_win_stack_prev  = col_do(lambda x: x.move_win_stack_prev())
    select_stack_next    = col_do(lambda x: x.select_stack_next())
    select_stack_prev    = col_do(lambda x: x.select_stack_prev())
    inc_col_ratio        = col_do(lambda x: x.inc_col_ratio())
    dec_col_ratio        = col_do(lambda x: x.dec_col_ratio())
    complement_col_ratio = col_do(lambda x: x.complement_col_ratio())

    # Stack binds
    select_win_next = stack_do(lambda x: x.select_win_next())
    select_win_prev = stack_do(lambda x: x.select_win_prev())
    move_win_next   = stack_do(lambda x: x.move_win_next())
    move_win_prev   = stack_do(lambda x: x.move_win_prev())
    add_win         = stack_do(lambda x: x.add_win(Window()))
    close_win       = stack_do(lambda x: x.close_win())
