from pypixel    import *
from util       import *
from container  import Container
from conf       import conf

class Screen(Container):
    "A screen manages tags"

    NAME = "Scr"

    @property
    def tags(self):
        return self.items

    @property
    def dim(self):
        return (self.w, self.h)

    def cur_tag(self):  return self.cur
    def tot_tags(self): return self.n_items()

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        self.w = WIDTH
        self.h = HEIGHT

    move_win_tag_num = Container.move_win_num
    select_tag_num   = Container.select_num

    select_tag_next = Container.select_next
    select_tag_prev = Container.select_prev

    move_win_tag_next = Container.move_win_next
    move_win_tag_prev = Container.move_win_prev
