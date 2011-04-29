from container  import *
from util       import *
from stack      import *

class Stacks(Container):

    SHORT_CLASS = "Stks"

    def go_win_next(self): self.items[self.cur].go_win_next()
    def go_win_prev(self): self.items[self.cur].go_win_prev()

    def _move_win_stack(self, a):
        stack = self .get_cur_item()
        win   = stack.remove_cur_item()
        stack._go(a)

        nstck = self._get_item(a)

        nstck._make_new(win, -1)
        #nstck._make_new(win, a)

        #self._go(a)
        if a == -1:
            self._go(a)

    def move_win_stack_next(self): self._move_win_stack(+1)
    def move_win_stack_prev(self): self._move_win_stack(-1)

    def _make_win_stack(self, a):
        stack = self .get_cur_item()
        win   = stack.remove_cur_item()
        stack._go(a)

        nstack = Stack(cur=0, items=[win])
        self._make_new(nstack, a)

    def make_win_stack_next(self): self._make_win_stack(+1)
    def make_win_stack_prev(self): self._make_win_stack(-1)
