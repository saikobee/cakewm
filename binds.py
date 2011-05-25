import util
import itertools
from window import Window
from ratio  import Ratio

class Binds(object):
    "A binds object is used for making keybinds"

    def __init__(self, display, **kwargs):
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

    # Display binds
    def win_to_nth_screen(self, number):
        self.display.move_win_screen_num(number)
    def swap_tag_nth_screen(self, number):
        self.display.swap_tags_num(number)
    def select_nth_screen(self, number):
        self.display.select_screen_num(number)

    # Screen binds
    def move_win_nth_tag(self, number):
        screen = self.screen()
        screen.move_win_tag_num(number)
    def select_nth_tag(self, number):
        screen = self.screen()
        screen.select_tag_num(number)

    # Tag binds
    def column_magic(self):
        tag = self.tag()
        tag.item_magic()
    def toggle_fullscreen(self):
        tag = self.tag()
        tag.toggle_fullscreen()
    def move_win_nth_col(self, number):
        tag = self.tag()
        tag.move_win_col_num(number)
    def select_nth_col(self, number):
        tag = self.tag()
        tag.select_col_num(number)
    def mod_tag_ratio(self, number):
        tag = self.tag()
        tag.ratio = util.clamp(
            tag.ratio + number,
            Ratio.MIN,
            Ratio.MAX
        )
    def set_tag_ratio_complement(self):
        tag = self.tag()
        tag.ratio = 1 - tag.ratio

    # Column binds
    def move_win_nth_stack(self, number):
        col = self.col()
        col.move_win_stack_num(number)
    def select_nth_stack(self, number):
        col = self.col()
        col.select_stack_num(number)
    def mod_col_ratio(self, number):
        col = self.col()
        col.ratio = util.clamp(
            col.ratio + number,
            Ratio.MIN,
            Ratio.MAX
        )
    def set_col_ratio_complement(self):
        col = self.col()
        col.ratio = 1 - col.ratio

    # Stack binds
    def select_next_win(self):
        stack = self.stack()
        stack.select_win_next()
    def select_prev_win(self):
        stack = self.stack()
        stack.select_win_prev()
    def move_win_next(self):
        stack = self.stack()
        stack.move_win_next()
    def move_win_prev(self):
        stack = self.stack()
        stack.move_win_prev()
    def add_win(self, win=None):
        stack = self.stack()
        stack.add_win(win or Window())
    def close_win(self):
        stack = self.stack()
        stack.close_win()
