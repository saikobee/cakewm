from pypixel    import *
from util       import *
from container import Container

class Screen(Container):
    "A screen manages tags"

    NAME = "Scr"

    @property
    def tags(self):
        return self.items

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.w = WIDTH
        self.h = HEIGHT

    move_win_tag_num = Container.move_win_num
    select_tag_num   = Container.select_num
