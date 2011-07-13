from util import *
from container import Container
from stack     import Stack
from ratio     import Ratio
from magic     import Magic
from master    import Master
from conf      import conf

class Column(Container, Ratio, Magic, Master):
    "A column manages stacks"

    @staticmethod
    def get_max():
        return conf.max_stacks

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

    def n_stacks(self):
        return len(self.stacks)

    @property
    def stacks(self):
        return self.items

    def n_wins(self):
        tot = 0
        for stack in self.stacks:
            tot += stack.n_wins()

        return tot

    def organize(self, screen):
        tag = screen.item()
        if self.n_items() == 0:
            pass
        elif self.n_items() == 1:
            self.stacks[0].h = tag.h
            self.stacks[0].y = tag.y_offset
        elif self.n_items() == 2:
            self.stacks[0].h = int(tag.h * self.ratio)
            self.stacks[0].y = tag.y_offset
            self.stacks[1].h = tag.h - self.stacks[0].h
            self.stacks[1].y = tag.y_offset + self.stacks[0].h
        else:
            tot = 0
            for i, stack in enumerate(self.stacks):
                stack.h = tag.h / self.n_items()
                stack.y = tag.y_offset + stack.h * i

                tot += stack.h

            self.stacks[-1].h = tag.h - tot + self.stacks[0].h

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
