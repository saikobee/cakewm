from util import *

class Column(object):
    "A column manages stacks"

    def __init__(self, **kwargs):
        self.cur    = kwargs.get("cur",    None)
        self.stacks = kwargs.get("stacks", [])

    def move_win_stack_num(self, number):
        "Moves the current window to the nth stack"

        if self.cur is not None:
            try:
                win = self.take_cur_win()
                if win is not None:
                    self.stacks[self.cur].add_window(win)
            except IndexError:
                debug("Attempted to move window to non-existent column")

    def select_stack_num(self, number):
        if between2(number, len(self.stacks)):
            self.cur = number
        else:
            debug("Column out of range")
