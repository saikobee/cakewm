from util import *

def guard_cur_isnt_none(func):
    @guard(lambda self: self.cur)
    def inner(self, *args, **kwargs):
        return func(*args, **kwargs)

    return inner

class Container(object):
    '''Base class representing containers'''

    def __init__(self, **kwargs):
        self.items = kwargs.get("items", [])
        self.cur   = kwargs.get("cur",   None)

    @guard_cur_isnt_none
    def _go(self, a):
        self.cur += a

    def go_next(self): self._go(+1)
    def go_prev(self): self._go(-1)

    @guard_cur_isnt_none
    def _swap(self, a):
        x = self.cur_col
        y = x + a
        n = len(self.cols)

        if 0 <= y <= n:
            swap(self.cols, x, y)

    def swap_next(self): self._swap(+1)
    def swap_prev(self): self._swap(-1)

    @guard_cur_isnt_none
    def _move_item(self, item, a):
        x = self.cur
        y = x + a
        n = len(self.items)

        if 0 <= y <= n:
            self.stacks[x].add_item(item)

    def move_item_next(self, item): self._move_item(item, +1)
    def move_item_prev(self, item): self._move_item(item, -1)

    @guard_cur_isnt_none
    def _make_new(self, a, item):
        self.items.insert(self.cur + a, item)

    def make_new_next(self, item): self._make_new(1, item)
    def make_new_prev(self, item): self._make_new(0, item)

    doc({
        swap_next: "Swap item with the next one",
        swap_prev: "Swap item with the previous one",

        move_item_next: "Move item to next container",
        move_item_prev: "Move item to previous container",

        make_new_next: "Make a new item before or after the current item",
        make_new_prev: "Make a new item before or after the current item",

        go_next: "Move cur to the next item",
        go_prev: "Move cur to the previous item",
    })
