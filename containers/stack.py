import util
from util import *
from container      import Container
from window         import Window
from focusable      import Focusable
from floatingrect   import FloatingRect

import pypixel

import const

class Stack(Container, Focusable, FloatingRect):
    "A stack manages windows"

    NAME = "Stk"

    def __init__(self, **kwargs):
        super(Stack, self).__init__(**kwargs)
        FloatingRect.__init__(self)

    @property
    def windows(self):
        return self.items

    n_wins = Container.n_items

    def _select_win(self, direction):
        if self.cur is not None:
            self.cur = util.clamp2(self.cur + direction.num, self.n_items())

    def select_win_next(self): self._select_win(const.NEXT)
    def select_win_prev(self): self._select_win(const.PREV)

    def _move_win(self, direction):
        if self.cur is not None:
            index = util.clamp2(self.cur + direction.num, self.n_items())
            util.swap(self.windows, self.cur, index)
            self.cur = index

    def move_win_next(self): self._move_win(const.NEXT)
    def move_win_prev(self): self._move_win(const.PREV)

    def close_win(self):
        if self.cur is not None:
            try:
                del self.windows[self.cur]
                self.cur = util.clamp2(self.cur - 1, self.n_items())
                if self.windows == []:
                    self.cur = None
            except IndexError:
                util.debug("Bad index removing window from stack")

    def add_win(self, win):
        if self.cur is not None:
            self.windows.insert(self.cur, win)
        elif self.cur is None and self.windows == []:
            self.windows.append(win)
            self.cur = 0
        else:
            util.debug("Cannot add_win: sef.cur is None")

    def take_cur_win(self):
        win = self.item()
        self.close_win()
        return win

    def draw(self):
        color = pypixel.grey(20)
        light = pypixel.grey(30)
        dark  = pypixel.grey(10)
        if self.focused:
            color = pypixel.grey(50)
            light = pypixel.grey(60)
            dark  = pypixel.grey(10)

        x = self.x
        y = self.y
        w = self.w
        h = self.h

        left  = x
        right = x + w - 1
        top   = y
        bot   = y + h - 1

        pypixel.rectangle(color, self.rect)

        # Draw light edge
        pypixel.line(light, (left, top), (right, top))
        pypixel.line(light, (left, top), (left,  bot))

        # Draw dark edge
        pypixel.line(dark, (right, bot), (right, top))
        pypixel.line(dark, (right, bot), (left,  bot))

        item = self.item()
        if item is not None:
            item.draw()

    def focus(self):
        super(Stack, self).focus()

        item = self.item()
        if item is not None:
            item.focus()

    def unfocus(self):
        super(Stack, self).unfocus()

        item = self.item()
        if item is not None:
            item.unfocus()

    def organize(self):
        pad = 6
        for i, win in enumerate(self.windows):
           win.x = self.x + pad
           win.y = self.y + pad

           win.w = self.w - pad - pad
           win.h = self.h - pad - pad
