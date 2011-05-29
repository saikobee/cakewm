import util
from container  import Container
from ratio      import Ratio
from column     import Column
from magic      import Magic
from stack      import Stack

class Tag(Container, Ratio, Magic):
    "A tag manages columns"

    MAX  = 9
    NAME = "Tag"

    def default_item(self):
        return Column(cur=0, items=[Stack(cur=0, items=[])])

    def __init__(self, **kwargs):
        super(Tag, self).__init__(**kwargs)

        self.fullscreen = False

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen

    def item_magic(self):
        super(Tag, self).item_magic()
        if self.cols == []:
            util.debug("HELP!")
            self.cols.append(Column(cur=0, items=[Stack(cur=None, items=[])]))

    complement_tag_ratio = Ratio.complement_ratio
    inc_tag_ratio = Ratio.inc_ratio
    dec_tag_ratio = Ratio.dec_ratio

    @property
    def cols(self):
        return self.items

    move_win_col_num = Container.move_win_num
    select_col_num   = Container.select_num

    select_col_next = Container.select_next
    select_col_prev = Container.select_prev

    move_win_col_next = Container.move_win_next
    move_win_col_prev = Container.move_win_prev

    def draw_fullscreen(self, screen):
        col = self.item()
        stk = col .item()
        win = stk .item()

        win.draw_fullscreen(screen)

    def organize(self, screen):
        if self.n_items() == 1:
            self.cols[0].w = screen.w
            self.cols[0].x = 0
        elif self.n_items() == 2:
            self.cols[0].w = int(screen.w * self.ratio)
            self.cols[0].x = 0

            self.cols[1].w = screen.w - self.cols[0].w
            self.cols[1].x = self.cols[0].w
        else:
            tot = 0
            for i, col in enumerate(self.cols):
                col.w = screen.w / self.n_items()
                col.x = col.w * i

                tot += col.w

            self.cols[-1].w = screen.w - tot + self.cols[0].w

        for col in self.cols:
            col.organize(screen)

Tag.column_magic = Tag.item_magic
