import math

import pypixel
import util
from container  import Container
from ratio      import Ratio
from column     import Column
from magic      import Magic
from stack      import Stack
from master     import Master
from conf       import conf

class Tag(Container, Ratio, Magic, Master):
    "A tag manages columns"

    @staticmethod
    def get_max():
        return conf.max_columns

    NAME = "Tag"

    def default_item(self):
        return Column(cur=0, items=[Stack(cur=0, items=[])])

    @property
    def dim(self):
        return (self.w, self.h)

    def __init__(self, **kwargs):
        super(Tag, self).__init__(**kwargs)
        Master.__init__(self)

        self.fullscreen = False

        self.w = pypixel.WIDTH
        self.h = pypixel.HEIGHT - 2 * conf.bar_height

        self.y_offset = conf.bar_height

        self.bar_hidden = False

    def set_resolution(self, res, **kwargs):
        screen = kwargs["screen"]
        self.w, self.h = res
        self.h -= 2 * conf.bar_height
        self.y_offset = conf.bar_height
        self.organize(screen)

    def hide_bar(self):
        self.h         += 2 * conf.bar_height
        self.y_offset   = 0
        self.bar_hidden = True

    def show_bar(self):
        self.h         -= 2 * conf.bar_height
        self.y_offset   =     conf.bar_height
        self.bar_hidden = False

    def toggle_bar(self):
        if self.bar_hidden: self.show_bar()
        else:               self.hide_bar()

    def toggle_fullscreen(self):
        col = self.item()
        stk = col .item()
        win = stk .item()

        if win is not None:
            self.fullscreen = not self.fullscreen

    def _item_magic_post_hook(self):
        self.cols.append(Column(cur=0, items=[Stack(cur=None, items=[])]))

    def column_magic_next(self): self.item_magic_next()
    def column_magic_prev(self): self.item_magic_prev()

    def close_win(self):
        self.fullscreen = False
        col = self.item()
        stk = col .item()
        if stk is not None:
            stk.close_win()

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

        if win is not None:
            win.draw_fullscreen(screen)

    def organize(self, screen):
        n = self.n_items()
        if n == 1:
            self.cols[0].w = screen.w
            self.cols[0].x = 0
        elif n > 1:
            tot  = screen.w
            mw   = int(tot * self.ratio) # master width
            tot -= mw
            q    = tot // (n - 1)
            for i, col in enumerate(self.cols):
                if not i == self.master:
                    col.w = q
                    tot  -= q

            self.items[self.master].w = mw + tot

            tot = 0
            for i, col in enumerate(self.cols):
                col.x = tot
                tot  += col.w

        for col in self.cols:
            col.organize(screen)

Tag.column_magic = Tag.item_magic
