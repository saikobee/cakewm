import util
from util import *
from container  import Container
from window     import Window

import const

class Stack(Container):
    "A stack manages windows"

    @property
    def windows(self):
        return self.items

    def _select_win(self, direction):
        if self.cur is not None:
            self.cur = clamp2(self.cur + direction.num, len(self.windows))

    def select_win_next(self): self._select_win(const.NEXT)
    def select_win_prev(self): self._select_win(const.PREV)

    def _move_win(self, direction):
        if self.cur is not None:
            index = clamp2(self.cur + direction.num, len(self.windows))
            swap(windows, self.cur, index)

    def move_win_next(self): self._move_win(const.NEXT)
    def move_win_prev(self): self._move_win(const.PREV)

    def close_win(self):
        if self.cur is not None:
            try:
                del self.windows[self.cur]
                self.cur = clamp2(self.cur - 1, len(self.items))
                if self.windows == []:
                    self.cur = None
            except IndexError:
                util.debug("Bad index removing window from stack")

    def add_win(self):
        if self.cur is not None:
            self.windows.insert(self.cur, Window())
        elif self.cur is None and self.windows == []:
            self.windows.append(Window())
            self.cur = 0
        else:
            util.debug("Cannot add_win: sef.cur is None")

    def draw(self):
        if self.cur is not None:
            self.windows[self.cur].draw()
