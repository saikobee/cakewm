from util import *

class Columns(object):
    def __init__(self):
        self.cols       = []
        self.cur_col    = None

    def _go(self, a):
        self.cols += a

    def go_next(self): _go(self, +1)
    def go_prev(self): _go(self, -1)

    def _make_new(self, a):
        self.cols.insert(self.cur_col + a, Column())

    def make_new_right(self): _make_new(self, 1)
    def make_new_left (self): _make_new(self, 0)

    def _swap(self, a):
        x = self.cur_col
        y = self.cur_col + a
        n = len(self.cur_col)

        if 0 <= y <= n:
            swap(self.cols, x, y)

    def swap_right(self): _swap(self, +1)
    def swap_left (self): _swap(self, -1)

    doc({
        go_next: "Focuses the next column",
        go_prev: "Focuses the previous column",

        make_new_right: "Make new column to the right",
        make_new_left:  "Make new column to the right",

        swap_right: "Swap column with the right one",
        swap_left:  "Swap column with the right one",
    })
