from container  import Container
from window     import Window

class Stack(Container):
    def draw(self):
        if self.cur is not None:
            self.items[self.cur].draw()

    def go_win_next(self): self.go_next()
    def go_win_prev(self): self.go_prev()

    def make_new_window(self):
        '''Add a new window to the stack'''
        self.make_new_next(Window())
