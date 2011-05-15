from util import *
from container import Container

class Tag(Container):
    "A tag manages columns"

    @property
    def cols(self):
        return self.items

    move_win_col_num = Container.move_win_num
    select_col_num   = Container.select_num

    def set_num_cols(self, number):
        # TODO
        debug("Tag.set_num_cols: PLEASE IMPLEMENT ME")
