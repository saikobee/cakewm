from container import Container

class Stack(Container):
    def draw(self):
        self.items[self.cur].draw()
