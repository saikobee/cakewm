from container  import Container
from window     import Window

from util import *

class Stack(Container):

    SHORT_CLASS = "Stk"

    def draw(self):
        if self.cur is not None:
            self.items[self.cur].draw()

    def go_win_next(self): self.go_next()
    def go_win_prev(self): self.go_prev()

    def collapse(self): pass

    def num_cur_wins(self):
        return len(self.items)

    def make_new_win(self):
        '''Add a new window to the stack'''
        self.make_new_next(Window())
