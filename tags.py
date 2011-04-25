from container import Container

class Tags(Container):
    def organize(self):
        for item in self.items:
            item.organize()

    def go_stack_next(self): self.items[self.cur].go_stack_next()
    def go_stack_prev(self): self.items[self.cur].go_stack_prev()

    def go_win_next(self): self.items[self.cur].go_win_next()
    def go_win_prev(self): self.items[self.cur].go_win_prev()

    def big_looper(self):
        if self.cur is None:
            return

        self.organize()

        cols = self.items[self.cur]
        a    = cols.cur
        for i, stacks in cols.each():
            b = stacks.cur
            for j, stack in stacks.each():
                c = stack.cur
                for k, window in stack.each():
                    window.unfocus()
                    if (a, b, c) == (i, j, k):
                        window.focus()
                stack.draw()
