from util import *
from container import Container
from ratio     import Ratio

class Column(Container, Ratio):
    "A column manages stacks"

    @property
    def stacks(self):
        return self.items

    move_win_stack_num = Container.move_win_num
    select_stack_num   = Container.select_num
