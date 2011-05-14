from util import *
from container import Container

class Column(Container):
    "A column manages stacks"

    @property
    def stacks(self):
        return self.items

    move_win_stack_num = Container.move_win_num

    def select_stack_num(self, number):
        if between2(number, len(self.stacks)):
            self.cur = number
        else:
            debug("Column out of range")
