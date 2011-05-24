import util
from container  import Container
from ratio      import Ratio
from column     import Column
from magic      import Magic

class Tag(Container, Ratio, Magic):
    "A tag manages columns"

    MAX = 3

    def default_item(self):
        return Column(cur=0, items=[])

    def __init__(self, **kwargs):
        super(Tag, self).__init__(**kwargs)

        self.fullscreen = False

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen

    @property
    def cols(self):
        return self.items

    move_win_col_num = Container.move_win_num
    select_col_num   = Container.select_num

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
