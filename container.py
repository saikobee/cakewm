from util import *

class Container(object):
    '''Base class representing containers'''

    SHORT_CLASS = "C"

    def __str__(self):
        return "#%s(cur=%i, items=[%s])" % (
            type(self).SHORT_CLASS,
            self.cur,
            ", ".join(map(str, self.items))
        )

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

    def _make_new(self, item, a):
        b = a
        if b == -1:
            b = 0

        self.items.insert(self.cur + b, item)
        self._go(a)

    def make_new_next(self, item): self._make_new(item, +1)
    def make_new_prev(self, item): self._make_new(item, -1)

    def each(self):
        for i, x in enumerate(self.items):
            yield i, x

    def make_new_win(self):
        self.items[self.cur].make_new_win()

    def _get_item(self, a):
        if (self.cur is not None and
            self.items and
            0 <= self.cur + a <= len(self.items) - 1):
            return self.items[self.cur + a]
        else:
            return None

    def get_cur_item(self):  return self._get_item( 0)
    def get_next_item(self): return self._get_item(+1)
    def get_prev_item(self): return self._get_item(-1)

    def remove_at(self, i):
        ret = self.items[i]
        del   self.items[i]

        return ret

    def remove_cur_item(self):
        if self.cur is None:
            return None
        else:
            return self.remove_at(self.cur)

    def is_empty(self):
        return len(self.items) == 0

    def collapse(self):
        for i, item in self.each():
            if item.is_empty():
                self.remove_at(i)
            else:
                item.collapse()

    def move_win_stack_next(self): self.get_cur_item().move_win_stack_next()
    def move_win_stack_prev(self): self.get_cur_item().move_win_stack_prev()

    doc({
        swap_next: "Swap item with the next one",
        swap_prev: "Swap item with the previous one",

        move_item_next: "Move item to next container",
        move_item_prev: "Move item to previous container",

        make_new_next: "Make a new item before or after the current item",
        make_new_prev: "Make a new item before or after the current item",

        go_next: "Move cur to the next item",
        go_prev: "Move cur to the previous item",

        get_cur_item:  "Get the current item, or None if that doesn't make sense",
        get_next_item: "Get the next item, or None if that doesn't make sense",
        get_prev_item: "Get the previous item, or None if that doesn't make sense",

        remove_cur_item: "Remove the current item and return it, or None if that doesn't make sense",
    })
