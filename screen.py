from pypixel    import *
from util       import *
from container import Container

class Screen(Container):
    "A screen manages tags"

    @property
    def tags(self):
        return self.items

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.w = WIDTH
        self.h = HEIGHT

    move_win_tag_num = Container.move_win_num

    def select_tag_num(self, number):
        if between2(number, len(self.tags)):
            self.cur = number
        else:
            debug("Tag out of range")
