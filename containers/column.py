from util import *
from container import Container
from stack     import Stack
from ratio     import Ratio
from magic     import Magic

class Column(Container, Ratio, Magic):
    "A column manages stacks"

    max  = the_conf.max_stacks
    NAME = "Col"

    def default_item(self):
        return Stack(cur=0, items=[])

    def __init__(self, **kwargs):
        super(Column, self).__init__(**kwargs)
        self.x = None
        self.w = None

    def item_magic(self):
        super(Column, self).item_magic()
        if self.stacks == []:
            self.stacks.append(Stack(cur=None, items=[]))

    @property
    def stacks(self):
        return self.items

    def n_wins(self):
        tot = 0
        for stack in self.stacks:
            tot += stack.n_wins()

        return tot

    def organize(self, screen):
        if self.n_items() == 0:
            pass
        elif self.n_items() == 1:
            self.stacks[0].h = screen.h
            self.stacks[0].y = 0
        elif self.n_items() == 2:
            self.stacks[0].h = int(screen.h * self.ratio)
            self.stacks[0].y = 0
            self.stacks[1].h = screen.h - self.stacks[0].h
            self.stacks[1].y = self.stacks[0].h
        else:
            tot = 0
            for i, stack in enumerate(self.stacks):
                stack.h = screen.h / self.n_items()
                stack.y = stack.h * i

                tot += stack.h

            self.stacks[-1].h = screen.h - tot + self.stacks[0].h

        for stack in self.stacks:
            stack.w = self.w
            stack.x = self.x
            stack.organize()

    move_win_stack_num = Container.move_win_num
    select_stack_num   = Container.select_num

    select_stack_next = Container.select_next
    select_stack_prev = Container.select_prev

    move_win_stack_next = Container.move_win_next
    move_win_stack_prev = Container.move_win_prev

    complement_col_ratio = Ratio.complement_ratio
    inc_col_ratio = Ratio.inc_ratio
    dec_col_ratio = Ratio.dec_ratio

Column.stack_magic = Column.item_magic
