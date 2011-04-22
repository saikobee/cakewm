from pypixel import *

import container

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
