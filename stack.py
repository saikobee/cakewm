from container import Container

class Stack(Container):
    def draw(self):
        self.items[self.cur].draw()

    def go_win_next(self): self.go_next()
    def go_win_prev(self): self.go_prev()
