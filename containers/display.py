from util import *

from container import Container

class Display(Container):
    "A display manages screens"

    NAME = "Dpy"

    def set_resolution(self, res):
        for screen in self.screens:
            screen.set_resolution(res)

    @property
    def screens(self):
        return self.items

    def cur_screen(self):  return self.cur
    def tot_screens(self): return self.n_items()

    move_win_screen_num = Container.move_win_num
    select_screen_num   = Container.select_num

    select_screen_next = Container.select_next
    select_screen_prev = Container.select_prev

    move_win_screen_next = Container.move_win_next
    move_win_screen_prev = Container.move_win_prev

    swap_tags_next = lambda self: self.swap_tags_num((self.cur or 0) + 1)
    swap_tags_prev = lambda self: self.swap_tags_num((self.cur or 0) - 1)

    def swap_tags_num(self, number):
        "Swap the current tags on the current and nth screen"

        try:
            this_screen = self.screens[self.cur]
            that_screen = self.screens[number  ]

            if (this_screen is not None and
                that_screen is not None):
                this_tag_num = this_screen.cur
                that_tag_num = that_screen.cur
                that_tag     = that_screen.item()
                this_tag     = this_screen.item()

                if (this_tag_num is not None and
                    that_tag_num is not None):
                    this_screen.items[this_tag_num] = that_tag
                    that_screen.items[that_tag_num] = this_tag
        except IndexError:
            debug("Screen out of range")
