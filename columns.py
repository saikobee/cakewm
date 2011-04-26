from pypixel import *

import container

from util import *

class Columns(container.Container):
    def organize(self):
        '''Place windows appropriately'''

        for i, stacks in self.each():
            for j, stack in stacks.each():
                for k, window in stack.each():
                    col_w   = WIDTH  / len(self.items)
                    stack_h = HEIGHT / len(stacks.items)

                    window.x = i * col_w
                    window.y = j * stack_h

                    window.w = col_w
                    window.h = stack_h

    def go_stack_next(self): self.items[self.cur].go_next()
    def go_stack_prev(self): self.items[self.cur].go_prev()

    def go_win_next(self): self.items[self.cur].go_win_next()
    def go_win_prev(self): self.items[self.cur].go_win_prev()

    def move_window_col_next(self):
        stacks  = self      .get_cur_item()
        stack   = stacks    .get_cur_item()
        nstacks = self      .get_next_item()
        nstack  = nstacks   .get_cur_item()
        win     = stack     .remove_cur_item()
        nstack.make_new_prev(win)
        stack.go_next()

    def move_window_col_prev(self):
        stacks  = self      .get_cur_item()
        stack   = stacks    .get_cur_item()
        nstacks = self      .get_prev_item()
        nstack  = nstacks   .get_cur_item()
        win     = stack     .remove_cur_item()
        nstack.make_new_prev(win)
        stack.go_prev()
