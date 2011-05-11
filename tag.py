from util import *

class Tag(object):
    "A tag manages columns"

    def __init__(self, **kwargs):
        self.cur  = kwargs.get("cur",  None)
        self.cols = kwargs.get("cols", [])

    def move_win_col_num(self, number):
        "Move the current window to the nth column"

        if self.cur is not None:
            try:
                win = self.take_cur_win()
                if win is not None:
                    self.cols[self.cur].add_window(win)
            except IndexError:
                debug("Attempted to move window to non-existent column")

    def set_num_cols(self, number):
        # TODO
        debug("Tag.set_num_cols: PLEASE IMPLEMENT ME")

    def select_col_num(self, number):
        if between2(number, len(self.cols)):
            self.cur = number
        else:
            debug("Column out of range")
