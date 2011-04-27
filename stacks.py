import container
from util import *

class Stacks(container.Container):

    SHORT_CLASS = "Stks"

    def go_win_next(self): self.items[self.cur].go_win_next()
    def go_win_prev(self): self.items[self.cur].go_win_prev()

    def _move_win_stack(self, a):
        stack = self .get_cur_item()
        win   = stack.remove_cur_item()

        nstck = self._get_item(a)

        nstck._make_new(win, -1)

        self._go(a)

    def move_win_stack_next(self): self._move_win_stack(+1)
    def move_win_stack_prev(self): self._move_win_stack(-1)
