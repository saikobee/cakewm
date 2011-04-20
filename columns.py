from util import *

def _guard(function):
    def inner(self, *args, **kwargs):
        if self.cur_stack is not None:
            return function(*args, **kwargs)

class Columns(object):
    def __init__(self):
        self.cols       = []
        self.cur_col    = None

    @_guard
    def _go(self, a):
        self.cur_col += a

    def go_next(self): self._go(+1)
    def go_prev(self): self._go(-1)

    @_guard
    def _make_new(self, a, stack):
        self.cols.insert(self.cur_col + a, stack)

    def make_new_right(self, stack): self._make_new(1, Stacks(stack))
    def make_new_left (self, stack): self._make_new(0, Stacks(stack))

    @_guard
    def _swap(self, a):
        x = self.cur_col
        y = x + a
        n = len(self.cols)

        if 0 <= y <= n:
            swap(self.cols, x, y)

    def swap_right(self): self._swap(+1)
    def swap_left (self): self._swap(-1)

    doc({
        go_next: "Focuses the next column",
        go_prev: "Focuses the previous column",

        make_new_right: "Make new column to the right",
        make_new_left:  "Make new column to the right",

        swap_right: "Swap column with the right one",
        swap_left:  "Swap column with the right one",
    })
