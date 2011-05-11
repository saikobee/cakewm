from util import *

import const

class Stack(object):
    "A stack manages windows"

    def __init__(self, **kwargs):
        self.cur  = kwargs.get("cur",     None)
        self.cols = kwargs.get("windows", [])

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
            del self.windows[self.cur]
            self.cur = clamp2(self.cur, len(self.items))

    def add_win(self):
        if self.cur is not None:
            self.windows.insert(self.cur, Window())
