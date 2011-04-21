from util import *

def _guard(function):
    def inner(self, *args, **kwargs):
        if self.cur_stack is not None:
            return function(*args, **kwargs)

class Stacks(object):
    def __init__(self, stacks=[]):
        self.stacks    = stacks
        self.cur_stack = None

    @_guard
    def _go(self, a):
        self.cur_stack += a

    def go_next(self): self._go(+1)
    def go_prev(self): self._go(-1)

    @_guard
    def _swap(self, a):
        x = self.cur_stack
        y = x + a
        n = len(self.stacks)

        if 0 <= y <= n:
            swap(self.stacks, x, y)

    def swap_above(self): _swap(self, -1)
    def swap_below(self): _swap(self, +1)

    @_guard
    def _move_window(self, window, a):
        x = self.cur_stack
        y = x + a
        n = len(self.stacks)

        if 0 <= y <= n:
            self.stacks[x].add_window(window)

    def move_window_below(self, window): self._move_window(window, +1)
    def move_window_above(self, window): self._move_window(window, -1)


    doc({
        swap_above: "Swap stack with the one above",
        swap_below: "Swap stack with the one below",

        move_window_below: "Move window to stack below",
        move_window_above: "Move window to stack above",

        go_next: "Move to the next stack",
        go_prev: "Move to the previous stack",
    })
