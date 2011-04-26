from util import *

class Container(object):
    '''Base class representing containers'''

    def __init__(self, **kwargs):
        self.items = kwargs.get("items", [])
        self.cur   = kwargs.get("cur",   None)

    def __len__(self):
        return len(self.items)

    def _go(self, a):
        self.cur = clamp2(self.cur + a, len(self))

    def go_next(self): self._go(+1)
    def go_prev(self): self._go(-1)

    def _swap(self, a):
        x = self.cur_col
        y = x + a
        n = len(self.cols)

        if 0 <= y <= n:
            swap(self.cols, x, y)

    def swap_next(self): self._swap(+1)
    def swap_prev(self): self._swap(-1)

    def _move_item(self, item, a):
        x = self.cur
        y = x + a
        n = len(self.items)

        if 0 <= y <= n:
            self.items[x].add_item(item)

    def move_item_next(self, item): self._move_item(item, +1)
    def move_item_prev(self, item): self._move_item(item, -1)

    def _make_new(self, a, item):
        self.items.insert(self.cur + a, item)

    def make_new_next(self, item): self._make_new(1, item)
    def make_new_prev(self, item): self._make_new(0, item)

    def each(self):
        for i, x in enumerate(self.items):
            yield i, x

    def make_new_window(self):
        self.items[self.cur].make_new_window()

    def _get_item(self, a):
        if (self.cur is not None and
            self.items and
            0 <= self.cur + a <= len(self.items) + 1):
            return self.items[self.cur + a]
        else:
            return None

    def get_cur_item(self):
        if self.cur is not None and self.items:
            return self.items[self.cur]
        else:
            return None

    def get_next_item(self):
        if (self.cur is not None and
            self.cur + 1 <= len(self.items) - 1):
            return self.items[self.cur + 1]
        else:
            return None

    def get_prev_item(self):
        if (self.cur is not None and
            0 <= self.cur - 1):
            return self.items[self.cur - 1]
        else:
            return None

    def remove_cur_item(self):
        ret = self.get_cur_item()

        if ret is not None:
            del self.items[self.cur]

        return ret

    doc({
        swap_next: "Swap item with the next one",
        swap_prev: "Swap item with the previous one",

        move_item_next: "Move item to next container",
        move_item_prev: "Move item to previous container",

        make_new_next: "Make a new item before or after the current item",
        make_new_prev: "Make a new item before or after the current item",

        go_next: "Move cur to the next item",
        go_prev: "Move cur to the previous item",

        get_cur_item:    "Get the current item, or None if that doesn't make sense",
        remove_cur_item: "Remove the current item and return it, or None if that doesn't make sense",

        get_next_item: "Get the next item, or None if that doesn't make sense",
    })
